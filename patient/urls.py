from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientView

router = DefaultRouter()
router.register(r'patient', PatientView)

urlpatterns = [
    path('', include(router.urls)),
]