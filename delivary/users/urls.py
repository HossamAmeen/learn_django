from rest_framework.routers import DefaultRouter

from users.api import (AdminViewSet, CallCenterViewSet, ClientViewSet,
                       DeliveryViewSet, ManagerViewSet, TraderViewSet,
                       VacationViewSet)

router = DefaultRouter()
router.register(r'admins', AdminViewSet, basename='admins')
router.register(r'managers', ManagerViewSet, basename='managegrs')
router.register(r'call-centers', CallCenterViewSet, basename='call-centers')
router.register(r'deliveries', DeliveryViewSet, basename='deliveries')
router.register(r'clients', ClientViewSet, basename='clients')
router.register(r'traders', TraderViewSet, basename='traders')

router.register(r'vacations', VacationViewSet, basename='vactions')
urlpatterns = router.urls
