from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
 
from shop.models import Category, Product, Article


# Article Serializers --------------------------------------------------------

class ArticleSerializer(ModelSerializer):
 
    class Meta:
        model = Article
        fields = ['id', 'name', "product" , "date_created", "date_updated", "description", "active", "price"]




# Product Serializers --------------------------------------------------------

class ProductDetailSerializer(ModelSerializer):

    articles = serializers.SerializerMethodField()
 
    class Meta:
        model = Product
        fields = ['id', 'name', "category" , "date_created", "date_updated", "description", "active", "articles"]

    def get_articles(self, instance):

        queryset = instance.articles.filter(active=True)

        serializer = ArticleSerializer(queryset, many=True)

        return serializer.data

class ProductListSerialiser(ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', "date_created", "date_updated"]





# Category Serializers --------------------------------------------------------

class CategoryDetailSerializer(ModelSerializer):

    products = serializers.SerializerMethodField()
 
    class Meta:
        model = Category
        fields = ['id', 'name', "date_created", "date_updated", "description", "active", "products"]
    
    def get_products(self, instance):

        queryset = instance.products.filter(active=True)

        serializer = ProductDetailSerializer(queryset, many=True)

        return serializer.data

class CategoryListSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', "date_created", "date_updated"]

