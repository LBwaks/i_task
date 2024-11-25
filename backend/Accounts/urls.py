from .views import UserViewSet
from django.urls import path
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'users', UserViewSet)
urlpatterns = router.urls
