from rest_framework.routers import DefaultRouter
from .views import TaskViewset

router = DefaultRouter()
router.register(r'^tasks',TaskViewset)
urlpatterns = router.urls