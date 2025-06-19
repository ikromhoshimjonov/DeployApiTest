from rest_framework import routers

from apps.views import ProductViewSet, CategoryViewSet

router = routers.SimpleRouter()
router.register(r'users', ProductViewSet)
router.register(r'accounts', CategoryViewSet)
urlpatterns = router.urls