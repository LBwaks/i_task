from rest_framework.routers import DefaultRouter
from Task.views import TaskList

router = DefaultRouter()
router.register(r'tasks', TaskList, basename='task')
urlpatterns = router.urls