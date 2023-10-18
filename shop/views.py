from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
 
from shop.models import Category, Product, Article
from shop.serializers import CategoryDetailSerializer, CategoryListSerializer, ProductDetailSerializer, ProductListSerialiser, ArticleSerializer
 

# |========================================== Les Models Viewset des Clients ================================================

class MultipleSerializerMixin:

    detail_serializer_class = None
    def get_serializer_class(self):
        if self.action == "retrieve" and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()

# Category Viewset -----------------------------------------------

class CategoryViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):

    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer

    def get_queryset(self):
        return Category.objects.all()
    
    # def get_serializer_class(self):
    #     if self.action == "retrieve":
    #         return self.detail_serializer_class
    #     return super().get_serializer_class()
    
    @action(detail=True, methods=["post"])
    def disable(self, request, pk):
        self.get_object().disable()
        return Response()
    
        


# Product Viewset -----------------------------------------------

class ProductViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):

    serializer_class = ProductListSerialiser
    detail_serializer_class = ProductDetailSerializer


    def get_queryset(self):

        queryset = Product.objects.filter(active=True)

        category_id = self.request.GET.get("category_id")
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)

        return queryset
    
    # def get_serializer_class(self):
    #     if self.action == "retrieve":
    #         return self.detail_serializer_class
    #     return super().get_serializer_class()





# Article Viewset -----------------------------------------------

class ArticleViewset(ReadOnlyModelViewSet):

    serializer_class = ArticleSerializer

    def get_queryset(self):

        queryset = Article.objects.filter(active=True)

        product_id = self.request.GET.get("product_id")
        if product_id is not None:
            queryset = queryset.filter(product_id=product_id)

        return queryset
    
# |========================================== Les Models Viewset d'Administrateur ================================================
# |
# |====> Admin Category Viewset

class AdminCategoryViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer

    def get_queryset(self):
        return Category.objects.all()
    
# |
# |====> Admin Article Viewset

class AdminArticleViewset(ModelViewSet):

    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.all()