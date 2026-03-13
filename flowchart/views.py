from rest_framework import views, status
from rest_framework.response import Response
from django.db.models import Q
from django.views.generic import TemplateView
from .models import (
    ProcedureCategory, LegalArticle, ProcedureStage,
    StageConnection, FlowchartSettings
)
from .serializers import (
    ProcedureCategorySerializer, LegalArticleSerializer,
    ProcedureStageSerializer, StageConnectionSerializer,
    FlowchartDataSerializer
)


class FlowchartAPIView(views.APIView):
    """
    Endpoint principal API care returnează datele complete ale diagramei.
    GET /api/flowchart/
    """

    def get(self, request):
        # Parametru pentru a afișa toate nodurile sau doar cele de nivel superior
        show_all = request.query_params.get('all', 'false').lower() == 'true'

        if show_all:
            stages = ProcedureStage.objects.filter(is_active=True)
        else:
            # Doar nodurile fără părinte (nivel superior)
            stages = ProcedureStage.objects.filter(
                is_active=True,
                parent__isnull=True
            )

        stages = stages.select_related('category').prefetch_related('articles')

        # Obține conexiunile doar între nodurile vizibile
        stage_ids = list(stages.values_list('id', flat=True))
        connections = StageConnection.objects.filter(
            source_id__in=stage_ids,
            target_id__in=stage_ids
        )

        categories = ProcedureCategory.objects.all()

        data = {
            'nodes': stages,
            'edges': connections,
            'categories': categories,
        }

        serializer = FlowchartDataSerializer(data)
        return Response(serializer.data)


class StageChildrenAPIView(views.APIView):
    """
    Obține copiii unei etape specifice pentru expand/collapse.
    GET /api/flowchart/stages/{id}/children/
    """

    def get(self, request, pk):
        try:
            parent = ProcedureStage.objects.get(pk=pk, is_active=True)
        except ProcedureStage.DoesNotExist:
            return Response(
                {'error': 'Etapa nu a fost găsită'},
                status=status.HTTP_404_NOT_FOUND
            )

        children = parent.children.filter(is_active=True).select_related(
            'category'
        ).prefetch_related('articles')

        # Obține conexiunile între copii și părinte
        child_ids = list(children.values_list('id', flat=True))
        child_ids.append(pk)

        connections = StageConnection.objects.filter(
            source_id__in=child_ids,
            target_id__in=child_ids
        )

        return Response({
            'parent_id': pk,
            'nodes': ProcedureStageSerializer(children, many=True).data,
            'edges': StageConnectionSerializer(connections, many=True).data,
        })


class SearchAPIView(views.APIView):
    """
    Căutare etape și articole.
    GET /api/flowchart/search/?q=query
    """

    def get(self, request):
        query = request.query_params.get('q', '').strip()

        if len(query) < 2:
            return Response({
                'stages': [],
                'articles': [],
                'message': 'Introduceți cel puțin 2 caractere'
            })

        # Căutare în etape
        stages = ProcedureStage.objects.filter(
            is_active=True
        ).filter(
            Q(title__icontains=query) |
            Q(short_title__icontains=query) |
            Q(description__icontains=query) |
            Q(search_keywords__icontains=query) |
            Q(articles__article_number__icontains=query) |
            Q(articles__title__icontains=query)
        ).distinct().select_related('category').prefetch_related('articles')[:20]

        # Căutare în articole
        articles = LegalArticle.objects.filter(
            Q(article_number__icontains=query) |
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )[:10]

        return Response({
            'stages': ProcedureStageSerializer(stages, many=True).data,
            'articles': LegalArticleSerializer(articles, many=True).data,
        })


class ArticleDetailAPIView(views.APIView):
    """
    Obține conținutul complet al articolului pentru afișare modală.
    GET /api/flowchart/articles/{id}/
    """

    def get(self, request, pk):
        try:
            article = LegalArticle.objects.get(pk=pk)
        except LegalArticle.DoesNotExist:
            return Response(
                {'error': 'Articolul nu a fost găsit'},
                status=status.HTTP_404_NOT_FOUND
            )

        # Etapele care referențiază acest articol
        related_stages = article.stages.filter(is_active=True)[:5]

        return Response({
            'article': LegalArticleSerializer(article).data,
            'related_stages': ProcedureStageSerializer(
                related_stages, many=True
            ).data
        })


class FlowchartPageView(TemplateView):
    """View pentru pagina principală a diagramei."""
    template_name = 'flowchart/flowchart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings'] = FlowchartSettings.get_settings()
        return context
