from rest_framework import routers
from .api import KekeriderViewSet

router = routers.DefaultRouter()
router.register('api/kekeriders', KekeriderViewSet, 'kekerider')

urlpatterns = router.urls 