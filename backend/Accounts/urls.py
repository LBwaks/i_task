from .views import UserViewSet
from django.urls import path,include
from rest_framework.routers import SimpleRouter,DefaultRouter

router = SimpleRouter()
router.register(r'users', UserViewSet,basename='user')

urlpatterns = [
    path ('', include(router.urls))
          ]
