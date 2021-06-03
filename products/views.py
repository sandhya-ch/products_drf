from rest_framework import viewsets
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product
from rest_framework.permissions import IsAuthenticated
from django.core.mail import EmailMultiAlternatives
from users.models import User
from rest_framework.response import Response
from rest_framework.decorators import action

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def create(self, request):
        data = request.data
        print(data)
        user = User.objects.get(id=data['user_id'])
        category = Category.objects.get(id=data['category_id'])
        print("category")
        res_data = Product.objects.create(user=user, category=category, name = data['name'])
        users = User.objects.filter(is_superuser=True).values('email')
        if users:
            to = []
            for i in users:
                to.append(i['email'])
            subject, from_email, to = 'Updation', 'qcaredocs.test@gmail.com', to
            msg = EmailMultiAlternatives(subject, 'Hello {0}, {1} created successfully'.format(res_data.user.first_name,res_data.name), from_email, to)
            msg.send()
        return Response({"message":"Data Created Successfully","status":201})