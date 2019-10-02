from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('', include('parts_demand.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]