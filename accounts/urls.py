from rest_framework import routers
from .api import UserViewSet

router = routers.DefaultRouter()
router.register('api/accounts', UserViewSet, 'accounts')

urlpatterns = router.urls