from django.urls import path
from . import views

app_name = 'flowchart'

urlpatterns = [
    # Pagina principală a diagramei
    path('', views.FlowchartPageView.as_view(), name='flowchart'),

    # API endpoints
    path('api/flowchart/', views.FlowchartAPIView.as_view(), name='api-flowchart'),
    path('api/flowchart/stages/<int:pk>/children/',
         views.StageChildrenAPIView.as_view(), name='api-stage-children'),
    path('api/flowchart/search/', views.SearchAPIView.as_view(), name='api-search'),
    path('api/flowchart/articles/<int:pk>/',
         views.ArticleDetailAPIView.as_view(), name='api-article-detail'),
]
