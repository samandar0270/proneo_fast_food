from django.db.models.functions import Lower
from rest_framework import serializers
from catalog.models import Category, Product




class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, )
    name = serializers.CharField(max_length=20)
    icon = serializers.CharField(max_length=200)
    sort_order = serializers.IntegerField(required=True, )

    def validate_name(self, value):
        query_set = Category.objects.annotate(name_lower=Lower('name'))
        if query_set.filter(name_lower=value.lower()).exists():
            raise serializers.ValidationError("XATOLIK")
        return value


    def create(self, validated_data):
        return Category.objects.create(**validated_data)


class ProductSerializer2(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, )
    name = serializers.CharField(max_length=20)
    category = CategorySerializer()


    def validate_name(self, value):
        query_set = Category.objects.annotate(name_lower=Lower('name'))
        if query_set.filter(name_lower=value.lower()).exists():
            raise serializers.ValidationError("XATOLIK")
        return value


    def create(self, validated_data):
        return Category.objects.create(**validated_data)


class ProductListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        books = [Product(**item) for item in validated_data]
        return Product.objects.bulk_create(books)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'icon', 'sort_order']

class ProductSerializer(serializers.Serializer):

    class Meta:
        list_serializer_class = ProductListSerializer
