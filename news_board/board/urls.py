from django.urls import path

from . import views

urlpatterns = [
    path('post/', views.PostListView.as_view()),
    path('post/<int:pk>/', views.PostView.as_view()),
    path('comment/', views.CommentsListView.as_view()),
    path('comment/<int:pk>/', views.CommentView.as_view()),
]

