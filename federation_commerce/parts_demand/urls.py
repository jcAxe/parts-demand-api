from django.urls import path
from . import views

urlpatterns = [
    path('demands/', views.PartsDemandList.as_view()),
    path('demands/<int:pk>/', views.PartsDemandDetail.as_view()),
    path('demands/<int:pk>/close/', views.CloseDemand.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
