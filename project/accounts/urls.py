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

    path('home/', views.home, name="home"),

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


	path('checkout/get',views.get,name="checkout/get"),
	path('checkout/post',views.post,name="checkout/post"),

	path('success/', views.success, name="success"),

	path('seller',views.seller,name="seller"),

    path('profile',views.profile,name='profile'),
	path('profile2/<str:username>/',views.profile2,name='profile2'),

	path('uploadedphotos',views.uploadedphotos,name='uploadedphotos'),
	path('uploadedphotos2/<str:username>/',views.uploadedphotos2,name='uploadedphotos2'),

	path('follow/<str:username>',views.follow,name='follow'),
	path('unfollow',views.unfollow,name='unfollow'),
	path('following',views.following,name='following'),




   path('favorite_photo/<int:id>/',views.favorite_photo,name='favorite_photo'),
   path('photo_favorite_list',views.photo_favorite_list,name='photo_favorite_list'),

   path('search', views.search, name='search'),
     

]
