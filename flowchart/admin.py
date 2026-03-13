from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from .models import (
    ProcedureCategory, LegalArticle, ProcedureStage,
    StageConnection, FlowchartSettings
)


@admin.register(ProcedureCategory)
class ProcedureCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'color_preview', 'order', 'stage_count']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'name_ru']
    ordering = ['order']

    def color_preview(self, obj):
        return format_html(
            '<span style="background-color: {}; padding: 5px 15px; '
            'border-radius: 3px; color: white;">{}</span>',
            obj.color, obj.color
        )
    color_preview.short_description = _("Culoare")

    def stage_count(self, obj):
        return obj.stages.count()
    stage_count.short_description = _("Nr. etape")


@admin.register(LegalArticle)
class LegalArticleAdmin(admin.ModelAdmin):
    list_display = ['article_number', 'title', 'chapter', 'usage_count']
    list_filter = ['chapter']
    search_fields = ['article_number', 'title', 'content']
    ordering = ['article_number']

    fieldsets = (
        (None, {
            'fields': ('article_number', 'title', 'chapter')
        }),
        (_('Conținut'), {
            'fields': ('content', 'content_ru')
        }),
        (_('Link extern'), {
            'fields': ('external_url',),
            'classes': ('collapse',)
        }),
    )

    def usage_count(self, obj):
        count = obj.stages.count()
        if count > 0:
            url = reverse('admin:flowchart_procedurestage_changelist')
            return format_html(
                '<a href="{}?articles__id__exact={}">{} etape</a>',
                url, obj.id, count
            )
        return "0 etape"
    usage_count.short_description = _("Utilizat în")


class StageConnectionInline(admin.TabularInline):
    """Inline pentru conexiunile de ieșire dintr-o etapă."""
    model = StageConnection
    fk_name = 'source'
    extra = 1
    autocomplete_fields = ['target']
    fields = ['target', 'label', 'edge_type', 'condition', 'animated', 'order']


class ChildStageInline(admin.TabularInline):
    """Inline pentru etapele copil (pentru ierarhia expand/collapse)."""
    model = ProcedureStage
    fk_name = 'parent'
    extra = 0
    fields = ['short_title', 'node_type', 'order', 'is_active']
    readonly_fields = ['short_title']
    show_change_link = True
    verbose_name = _("Etapă copil")
    verbose_name_plural = _("Etape copil")


@admin.register(ProcedureStage)
class ProcedureStageAdmin(admin.ModelAdmin):
    list_display = [
        'short_title', 'category', 'node_type_badge', 'parent',
        'has_children_badge', 'article_list', 'order', 'is_active'
    ]
    list_filter = ['category', 'node_type', 'is_active', 'parent']
    list_editable = ['order', 'is_active']
    search_fields = ['title', 'short_title', 'description', 'search_keywords']
    autocomplete_fields = ['parent', 'category', 'articles']
    filter_horizontal = ['articles']
    inlines = [StageConnectionInline, ChildStageInline]

    fieldsets = (
        (_('Informații de bază'), {
            'fields': ('title', 'short_title', 'description')
        }),
        (_('Traduceri (RU)'), {
            'fields': ('title_ru', 'description_ru'),
            'classes': ('collapse',)
        }),
        (_('Organizare'), {
            'fields': ('category', 'parent', 'node_type', 'order', 'is_active')
        }),
        (_('Poziționare'), {
            'fields': ('position_x', 'position_y'),
            'classes': ('collapse',),
            'description': _('Poziția pe diagramă (poate fi ajustată automat)')
        }),
        (_('Referințe legale'), {
            'fields': ('articles', 'deadline_days', 'deadline_note')
        }),
        (_('Căutare'), {
            'fields': ('search_keywords',),
            'classes': ('collapse',)
        }),
    )

    def node_type_badge(self, obj):
        colors = {
            'start': '#22c55e',
            'end': '#ef4444',
            'process': '#3b82f6',
            'decision': '#f59e0b',
            'document': '#8b5cf6',
            'subprocess': '#06b6d4',
        }
        color = colors.get(obj.node_type, '#6b7280')
        return format_html(
            '<span style="background-color: {}; padding: 3px 8px; '
            'border-radius: 3px; color: white; font-size: 11px;">{}</span>',
            color, obj.get_node_type_display()
        )
    node_type_badge.short_description = _("Tip")

    def has_children_badge(self, obj):
        if obj.has_children:
            count = obj.children.filter(is_active=True).count()
            return format_html(
                '<span style="background-color: #6366f1; padding: 2px 6px; '
                'border-radius: 3px; color: white;">+ {}</span>',
                count
            )
        return "-"
    has_children_badge.short_description = _("Copii")

    def article_list(self, obj):
        articles = obj.articles.all()[:3]
        if articles:
            return ", ".join([f"Art.{a.article_number}" for a in articles])
        return "-"
    article_list.short_description = _("Articole")


@admin.register(StageConnection)
class StageConnectionAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'edge_type', 'label', 'condition', 'animated']
    list_filter = ['edge_type', 'animated']
    autocomplete_fields = ['source', 'target']
    search_fields = ['source__title', 'target__title', 'label']


@admin.register(FlowchartSettings)
class FlowchartSettingsAdmin(admin.ModelAdmin):
    """Singleton admin - doar un singur obiect de setări permis."""

    fieldsets = (
        (_('General'), {
            'fields': ('title', 'subtitle')
        }),
        (_('Zoom'), {
            'fields': ('default_zoom', 'min_zoom', 'max_zoom')
        }),
        (_('Aspect'), {
            'fields': ('background_color', 'node_border_radius')
        }),
        (_('Export'), {
            'fields': ('export_watermark',)
        }),
    )

    def has_add_permission(self, request):
        return not FlowchartSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
