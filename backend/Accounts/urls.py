from .views import UserViewSet,AssigneeViewSet
from django.urls import path,include
from rest_framework.routers import SimpleRouter,DefaultRouter

router = SimpleRouter()
router.register(r'users', UserViewSet,basename='user')
router.register(r'assignees',AssigneeViewSet,basename='assignees')

urlpatterns = [
    path ('', include(router.urls))
          ]
