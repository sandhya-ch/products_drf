from django.contrib import admin
from django.urls import path,include
import users.urls, products.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(users.urls)),
    path('api/products/', include(products.urls))
]
