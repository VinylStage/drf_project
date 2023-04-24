from django.urls import path
from articles import views

urlpatterns = [
    path('', views.ArticleView.as_view(), name='ArticleView'),
    path('feed/', views.FeedView.as_view(), name='FeedView'),
    path('<int:article_id>/', views.ArticleDetailView.as_view(),
         name='ArticleDetailView'),
    path('<int:article_id>/comment/',
         views.CommentView.as_view(), name='CommentView'),
    path('<int:article_id>/comment/<int:comment_id>/',
         views.CommentDetailView.as_view(), name='CommentDetailView'),
    path('<int:article_id>/like/', views.LikeView.as_view(), name='LikeView'),
]
