from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
 
from shop.views import CategoryViewset, ProductViewset, ArticleViewset, AdminCategoryViewset, AdminArticleViewset, TokenObtainPairView, TokenRefreshView
 
# Ici nous créons notre routeur
router = routers.SimpleRouter()
# Puis lui déclarons une url basée sur le mot clé ‘category’ et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/category/’
router.register('categories', CategoryViewset, basename='category')
router.register('products', ProductViewset, basename='product')
router.register('articles', ArticleViewset, basename='article')
router.register('admin/categories', AdminCategoryViewset, basename='admin-category')
router.register('admin/articles', AdminArticleViewset, basename='admin-articles')
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),  # Il faut bien penser à ajouter les urls du router dans la liste des urls disponibles.
]