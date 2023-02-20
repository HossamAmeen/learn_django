from rest_framework.routers import DefaultRouter

from users.api import (AdminViewSet, CAllCenterViewSet, CustomerViewSet,
                       DeliveryViewSet, ManagerViewSet, TraderViewSet)

router = DefaultRouter()
router.register(r'admins', AdminViewSet, basename='admins')
router.register(r'managers', ManagerViewSet, basename='managegrs')
router.register(r'call-centers', CAllCenterViewSet, basename='call-centers')
router.register(r'deliveries', DeliveryViewSet, basename='deliveries')
router.register(r'customers', CustomerViewSet, basename='customers')
router.register(r'traders', TraderViewSet, basename='traders')

urlpatterns = router.urls
