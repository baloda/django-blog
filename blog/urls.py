from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    # path('', views.home, name = 'home'),
    path('', views.PostListView.as_view(), name = 'home'),
    path('user/<str:username>', views.UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='post-detail'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    # path('post/<int:pk>/', views.PostDetailView.as_view(), name = 'blogpost'),
    # path('post/add/', views.PostCreateView.as_view(), name = 'add'),
    path('about/', views.about, name = 'about')
]