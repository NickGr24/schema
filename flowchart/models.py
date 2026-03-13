from django.db import models
from django.utils.translation import gettext_lazy as _


class ProcedureCategory(models.Model):
    """
    Categorii pentru gruparea etapelor procedurale.
    Exemplu: "Urmărirea penală", "Judecata", "Căile de atac"
    """
    name = models.CharField(_("Denumire"), max_length=200)
    name_ru = models.CharField(_("Denumire (RU)"), max_length=200, blank=True)
    slug = models.SlugField(unique=True)
    order = models.PositiveIntegerField(_("Ordine"), default=0)
    color = models.CharField(
        _("Culoare"),
        max_length=7,
        default="#3b82f6",
        help_text="Cod HEX pentru culoarea nodurilor din această categorie"
    )

    class Meta:
        verbose_name = _("Categorie procedură")
        verbose_name_plural = _("Categorii proceduri")
        ordering = ['order']

    def __str__(self):
        return self.name


class LegalArticle(models.Model):
    """
    Articole din Codul de Procedură Penală al Republicii Moldova.
    """
    article_number = models.CharField(_("Numărul articolului"), max_length=20)
    title = models.CharField(_("Titlu"), max_length=500)
    content = models.TextField(_("Conținut"))
    content_ru = models.TextField(_("Conținut (RU)"), blank=True)
    chapter = models.CharField(_("Capitol"), max_length=200, blank=True)
    external_url = models.URLField(
        _("Link extern"),
        blank=True,
        help_text="Link către versiunea oficială a articolului (legis.md)"
    )

    class Meta:
        verbose_name = _("Articol CPP")
        verbose_name_plural = _("Articole CPP")
        ordering = ['article_number']

    def __str__(self):
        return f"Art. {self.article_number} - {self.title[:50]}"


class ProcedureStage(models.Model):
    """
    Noduri individuale în diagramă reprezentând etapele procedurii penale.
    """
    NODE_TYPES = [
        ('start', _('Start')),
        ('end', _('Sfârșit')),
        ('process', _('Proces')),
        ('decision', _('Decizie')),
        ('document', _('Document')),
        ('subprocess', _('Subproces')),
    ]

    # Informații de bază
    title = models.CharField(_("Titlu"), max_length=300)
    title_ru = models.CharField(_("Titlu (RU)"), max_length=300, blank=True)
    short_title = models.CharField(
        _("Titlu scurt"),
        max_length=100,
        help_text="Afișat pe nodurile mici"
    )
    description = models.TextField(_("Descriere"), blank=True)
    description_ru = models.TextField(_("Descriere (RU)"), blank=True)

    # Ierarhie
    category = models.ForeignKey(
        ProcedureCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Categorie"),
        related_name='stages'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Etapa părinte"),
        related_name='children',
        help_text="Pentru noduri imbricate (expand/collapse)"
    )

    # Aspectul nodului
    node_type = models.CharField(
        _("Tip nod"),
        max_length=20,
        choices=NODE_TYPES,
        default='process'
    )

    # Poziție (calculată automat, dar poate fi ajustată manual)
    position_x = models.IntegerField(_("Poziția X"), default=0)
    position_y = models.IntegerField(_("Poziția Y"), default=0)

    # Referințe legale
    articles = models.ManyToManyField(
        LegalArticle,
        blank=True,
        verbose_name=_("Articole CPP"),
        related_name='stages'
    )

    # Termene și deadline-uri
    deadline_days = models.PositiveIntegerField(
        _("Termen (zile)"),
        null=True,
        blank=True,
        help_text="Termenul legal în zile"
    )
    deadline_note = models.CharField(
        _("Notă termen"),
        max_length=200,
        blank=True,
        help_text="Ex: '15 zile de la comunicare'"
    )

    # Metadate
    order = models.PositiveIntegerField(_("Ordine"), default=0)
    is_active = models.BooleanField(_("Activ"), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Optimizare căutare
    search_keywords = models.TextField(
        _("Cuvinte cheie"),
        blank=True,
        help_text="Cuvinte cheie pentru căutare, separate prin virgulă"
    )

    class Meta:
        verbose_name = _("Etapă procedură")
        verbose_name_plural = _("Etape procedură")
        ordering = ['category__order', 'order']

    def __str__(self):
        return f"{self.short_title} ({self.get_node_type_display()})"

    @property
    def has_children(self):
        return self.children.filter(is_active=True).exists()


class StageConnection(models.Model):
    """
    Muchii care conectează etapele procedurale.
    """
    EDGE_TYPES = [
        ('default', _('Implicit')),
        ('success', _('Succes')),
        ('failure', _('Eșec')),
        ('conditional', _('Condiționat')),
        ('optional', _('Opțional')),
    ]

    source = models.ForeignKey(
        ProcedureStage,
        on_delete=models.CASCADE,
        related_name='outgoing_connections',
        verbose_name=_("De la")
    )
    target = models.ForeignKey(
        ProcedureStage,
        on_delete=models.CASCADE,
        related_name='incoming_connections',
        verbose_name=_("Către")
    )

    label = models.CharField(_("Etichetă"), max_length=100, blank=True)
    edge_type = models.CharField(
        _("Tip conexiune"),
        max_length=20,
        choices=EDGE_TYPES,
        default='default'
    )

    # Pentru nodurile de decizie - textul condiției
    condition = models.CharField(
        _("Condiție"),
        max_length=200,
        blank=True,
        help_text="Ex: 'Da', 'Nu', 'În termen'"
    )

    animated = models.BooleanField(_("Animat"), default=False)
    order = models.PositiveIntegerField(_("Ordine"), default=0)

    class Meta:
        verbose_name = _("Conexiune")
        verbose_name_plural = _("Conexiuni")
        ordering = ['order']
        unique_together = ['source', 'target']

    def __str__(self):
        label = f" ({self.label})" if self.label else ""
        return f"{self.source.short_title} → {self.target.short_title}{label}"


class FlowchartSettings(models.Model):
    """
    Model singleton pentru setările globale ale diagramei.
    """
    title = models.CharField(
        _("Titlu"),
        max_length=200,
        default="Codul de Procedură Penală al Republicii Moldova"
    )
    subtitle = models.CharField(_("Subtitlu"), max_length=300, blank=True)
    default_zoom = models.FloatField(_("Zoom implicit"), default=1.5)
    min_zoom = models.FloatField(_("Zoom minim"), default=0.1)
    max_zoom = models.FloatField(_("Zoom maxim"), default=2.0)

    # Stilizare
    background_color = models.CharField(
        _("Culoare fundal"),
        max_length=7,
        default="#f8fafc"
    )
    node_border_radius = models.PositiveIntegerField(
        _("Rotunjire noduri (px)"),
        default=8
    )

    # Setări export
    export_watermark = models.CharField(
        _("Watermark export"),
        max_length=200,
        default="penitadreptului.md"
    )

    class Meta:
        verbose_name = _("Setări diagramă")
        verbose_name_plural = _("Setări diagramă")

    def save(self, *args, **kwargs):
        # Asigură că există doar o singură instanță
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_settings(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return "Setări diagramă"
