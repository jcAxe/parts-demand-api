from django.urls import path
from . import views

urlpatterns = [
    path('demands/', views.demand_list),
    path('demands/<int:pk>/', views.demand_detail),
]
