from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views


app_name = 'news'
urlpatterns = [
    path('', PostListView.as_view(), name='home-page'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts-page'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail-page'),
    path('post/new/', PostCreateView.as_view(), name='post-create-page'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update-page'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete-page'),
    path('post/<int:pk>/comment/', views.comment, name='comment-page'),
    path('about/', views.about, name='about-page'),
]
