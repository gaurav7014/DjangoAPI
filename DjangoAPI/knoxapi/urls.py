from pyrsistent import inc
from accounts.views import LoginAPI, RegisterAPI
from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include("rest_framework.urls")), 
    path('accounts',include('accounts.urls')),
    path('',include('products.urls')),
    path('user/',include('cart.urls'))



]