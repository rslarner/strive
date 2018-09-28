from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserTestView.as_view(), name='tests'),
    path('questions/', views.UserQuestionView.as_view(), name='questions'),
]