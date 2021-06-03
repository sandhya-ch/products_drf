from products import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'category', views.CategoryViewSet, basename='category'),
router.register(r'product', views.ProductViewSet, basename='product')

urlpatterns = router.urls