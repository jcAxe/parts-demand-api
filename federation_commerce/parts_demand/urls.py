from django.urls import path
from . import views

urlpatterns = [
    path('demands/', views.PartsDemandList.as_view()),
    path('demands/<int:pk>/', views.PartsDemandDetail.as_view()),
]
