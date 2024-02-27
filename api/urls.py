from django.urls import path
from . import views
from .views import DeleteAPIView

urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem),
    path('name-detail/<str:pk>/', views.nameDetail, name="name-detail"),
    path('delete-detail/<int:pk>/', DeleteAPIView.as_view(), name="delete-detail"),
    path('update/<str:pk>/', views.updateItem, name="update"),
]
