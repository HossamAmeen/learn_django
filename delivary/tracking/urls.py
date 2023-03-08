from rest_framework.routers import DefaultRouter

from .api import TrackingViewSet


router = DefaultRouter()
router.register('order-tracking', TrackingViewSet, basename="order-trackings")

urlpatterns = router.urls
