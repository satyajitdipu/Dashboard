from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from dashboard.views import DataViewSet

# Create a router and register the DataViewSet with it
router = DefaultRouter()
router.register(r'data', DataViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Include the router's generated URLs
]