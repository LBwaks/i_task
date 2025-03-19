from rest_framework.routers import SimpleRouter
from Task.views import TaskViewSet, SectorViewSet, SourceViewSet, IssueViewSet, StatusViewSet, PriorityViewSet,SupportViewSet
from django.urls import path, include

router = SimpleRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'sector', SectorViewSet, basename='sector')
router.register(r'source', SourceViewSet, basename='source')
router.register(r'issue', IssueViewSet, basename='issue')
router.register(r'status', StatusViewSet, basename='status')
router.register(r'priority', PriorityViewSet, basename='priority')
router.register(r'support', SupportViewSet, basename='support')


urlpatterns = [
    path('', include(router.urls)),

    #path('task-detail', TaskDetailView.as_view(), name='task-detail')
]