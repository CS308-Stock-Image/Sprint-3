from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),

	path('', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),
	path('deletePhoto/<int:pk>/',views.deletePhoto, name='deletePhoto'),

	path('sortByCategory',views.sortByCategory,name='sortByCategory'),
    path('sortByIncreasingPrice',views.sortByIncreasingPrice,name='sortByIncreasingPrice'),
	path('sortByDecreasingPrice',views.sortByDecreasingPrice,name='sortByDecreasingPrice'),

	path('addtoshopcart/<int:id>/',views.addtoshopcart,name='addtoshopcart'),
	path('shopcart',views.shopcart,name='shopcart'),
	path('deletecart/<int:id>',views.deletecart, name='deletecart'),
	path('checkout',views.checkout,name="checkout"),

	path('seller',views.seller,name="seller"),
    path('profile',views.profile,name='profile'),
     

]
