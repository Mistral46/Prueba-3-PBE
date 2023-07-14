from django.urls import path,include
from rest_framework import routers
from paises import views

router = routers.DefaultRouter()
router.register(r'pais',views.PaisViewSet)

urlpatterns = [
    path('', include(router.urls))
]