from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
 
from shop.models import Category, Product, Article


# Article Serializers --------------------------------------------------------

class ArticleSerializer(ModelSerializer):
 
    class Meta:
        model = Article
        fields = ['id', 'name', "product" , "date_created", "date_updated", "description", "price"]

    def validate_price(self, value):
        if value<1 :
            raise serializers.ValidationError('Price must be highter than 1 $')
        return value
    
    def validate_product(self, value):
      if value.active is False:
            raise serializers.ValidationError('Inactive product')
      return value



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
    ecoscore = serializers.ReadOnlyField(source='category.ecoscore')
    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name', 'category', 'ecoscore']
    





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
        fields = ['id', 'name', "date_created", "date_updated", "description"]
    
    def validate_name(self, value):
        # Nous vérifions que la catégorie existe
        if Category.objects.filter(name=value).exists():
        # En cas d'erreur, DRF nous met à disposition l'exception ValidationError
            raise serializers.ValidationError('Category already exists')
        return value
    
    def validate(self, data):
        # vériffier l'existance de nom dans la déscription
        if data['name'] not in data['description']:
            raise serializers.ValidationError('Name must be in description')
        return data

