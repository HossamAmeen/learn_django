from rest_framework.routers import DefaultRouter
from users.views import AdminViewSet

router = DefaultRouter()
router.register(r'admins', AdminViewSet, basename='users')

urlpatterns = router.urls
