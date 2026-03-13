from rest_framework import serializers
from .models import (
    ProcedureCategory, LegalArticle, ProcedureStage,
    StageConnection, FlowchartSettings
)


class LegalArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalArticle
        fields = ['id', 'article_number', 'title', 'content', 'chapter', 'external_url']


class LegalArticleBriefSerializer(serializers.ModelSerializer):
    """Informații minimale despre articol pentru afișarea pe noduri."""
    class Meta:
        model = LegalArticle
        fields = ['id', 'article_number', 'title']


class ProcedureCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcedureCategory
        fields = ['id', 'name', 'slug', 'color', 'order']


class ProcedureStageSerializer(serializers.ModelSerializer):
    """Serializator pentru nodurile diagramei."""
    articles = LegalArticleBriefSerializer(many=True, read_only=True)
    category_color = serializers.CharField(source='category.color', read_only=True, default='#6b7280')
    category_name = serializers.CharField(source='category.name', read_only=True, default='')
    children_count = serializers.SerializerMethodField()

    class Meta:
        model = ProcedureStage
        fields = [
            'id', 'title', 'short_title', 'description',
            'node_type', 'position_x', 'position_y',
            'category', 'category_name', 'category_color',
            'parent', 'children_count',
            'articles', 'deadline_days', 'deadline_note',
            'order', 'search_keywords'
        ]

    def get_children_count(self, obj):
        return obj.children.filter(is_active=True).count()


class StageConnectionSerializer(serializers.ModelSerializer):
    """Serializator pentru muchiile diagramei."""
    class Meta:
        model = StageConnection
        fields = [
            'id', 'source', 'target', 'label',
            'edge_type', 'condition', 'animated'
        ]


class FlowchartDataSerializer(serializers.Serializer):
    """Serializator combinat pentru datele complete ale diagramei."""
    nodes = ProcedureStageSerializer(many=True)
    edges = StageConnectionSerializer(many=True)
    categories = ProcedureCategorySerializer(many=True)
    settings = serializers.SerializerMethodField()

    def get_settings(self, obj):
        settings = FlowchartSettings.get_settings()
        return {
            'title': settings.title,
            'subtitle': settings.subtitle,
            'defaultZoom': settings.default_zoom,
            'minZoom': settings.min_zoom,
            'maxZoom': settings.max_zoom,
            'backgroundColor': settings.background_color,
            'nodeBorderRadius': settings.node_border_radius,
            'exportWatermark': settings.export_watermark,
        }
