from rest_framework import serializers
from products import models
from users.models import User
from users.serializers import UserDetailSerializer

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=models.Category.objects.all(), write_only=True, source='category')
    user = UserDetailSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, source='user')
    class Meta:
        model = models.Product
        fields = '__all__'