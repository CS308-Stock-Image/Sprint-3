from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from bson.decimal128 import Decimal128, create_decimal128_context
import decimal
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.
from .models import *
from .forms import  *


def home(request):
    user=request.user
    userid=user.id
    photos =Photo.objects.all()
    context={'photos':photos,'userid':userid}
    return render(request, 'accounts/main.html',context)
    


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        context = {'form':form}
        return render(request, 'accounts/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')
    
			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def gallery(request):
    user = request.user
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.filter(category__user=user)
    else:
        photos = Photo.objects.filter(
            category__name=category, category__user=user)

    categories = Category.objects.filter(user=user)
    context = {'categories': categories, 'photos': photos}
    return render(request,  'accounts/photos/gallery.html', context)


@login_required(login_url='login')
def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'accounts/photos/photo.html', {'photo': photo})


@login_required(login_url='login')
def addPhoto(request):
    user = request.user

    categories = user.category_set.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                user=user,
                name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                category_name=category,
                description=data['description'],
                image=image,
                price=data['price'],
                uploaded_by=user
            )

        return redirect('home')

    context = {'categories': categories}
    return render(request, 'accounts/photos/add.html', context)

def deletePhoto(request, id):
    user=request.user
    photo=Photo.objects.get(id=id)
    photo.delete()
    return redirect('/home')


########            SORTING             ##########

def sortByCategory(request):
   photos =Photo.objects.all().order_by('category_name')
   context={'photos':photos}
   return render(request, 'accounts/main.html',context)

def sortByIncreasingPrice(request):
   photos =Photo.objects.all().order_by('price')
   context={'photos':photos}
   return render(request, 'accounts/main.html',context)

def sortByDecreasingPrice(request):
   photos =Photo.objects.all().order_by('-price')
   context={'photos':photos}
   return render(request, 'accounts/main.html',context)



########            SHOPPING CART           #########

def shopcart(request):
    image=ShopCart.objects.filter()
    sum=0
    for product in image:
       
        sum+= product.price.to_decimal()
        

    
    context= {"image":image,'sum':sum}
    
    return render(request,"accounts/cart.html",context)
    

def addtoshopcart(request,id):

    current_user=request.user
    data=ShopCart(id=id)

    if data.quantity==0:
        data.user_id =current_user.id
        data.product_id =id
        data.product= Photo(id=id)
        data.quantity=1
        data.save()
        image=ShopCart.objects.filter()
        context= {"image":image}
        return render(request,"accounts/cart.html",context)
   
    return redirect('home')

def deletecart(request,id):
    cart = ShopCart(id)
    cart.delete()
    return redirect('shopcart')


def seller(request):
    user=request.user
    user.is_staff=True
    user.save()
    photo = Photo.objects.all()
    return render(request,"accounts/main.html",{'user1':user,'photos':photo})

def profile(request):
    user=request.user
    photo= Photo.objects.all()
    return render(request,"accounts/profile.html",{'photos':photo,'user':user})

def uploadedphotos(request):
    user=request.user
    userid=user.id

    photo=Photo.objects.filter(uploaded_by_id=userid)
    return render(request,"accounts/photos/uploadedphotos.html",{'photos':photo})

def uploadedphotos2(request,username):
    user= User.objects.get(username=username)
    userid=user.id
    photo=Photo.objects.filter(uploaded_by_id=userid)
   
    return render(request,"accounts/photos/uploadedphotos2.html",{'photos':photo,'user2':user})

def profile2(request,username): 
    user1=request.user
    user = User.objects.get(username=username)
    return render(request,"accounts/profile2.html",{'user2':user,'user':user1})

    

def favorite_photo(request,id):
    photo= get_object_or_404(Photo,id=id)
    if photo.favorite.filter(id=request.user.id).exists():
        pass
    else:
        photo.favorite.add(request.user)
    return HttpResponseRedirect('/home')

def favorite2(request,username):
    user=User.objects.get(username=username)
    favorite_photos=user.favorite.all()
    context={'favorite_photos':favorite_photos,'user2':user}
    return render(request,'accounts/favorites2.html',context)





def photo_favorite_list(request):
    user=request.user
    favorite_photos=user.favorite.all()
    context={'favorite_photos':favorite_photos,'user':user}
    return render(request,'accounts/favorites.html',context)

def follow(request,username):
    user1=request.user
    user=User.objects.get(username=username)
    follow=Follow()
    follow.username=user
    follow.username_id=user.id
    follow.id=user1.id
    follow.follows.add(user.id)
    follow.save()
    following=Follow.objects.filter(id=user1.id)
    return render(request,"accounts/follow.html",{'user1':following})



def unfollow(request,username):
    user1=request.user
    user=User.objects.get(username=username)
    
    follow=Follow(user1.id)
    follow.follows.remove(user1.id)
    follow.save()
    following=Follow.objects.filter(id=user1.id) 
    return render(request,"accounts/follow.html",{'user1':following})



def following(request):
    user=request.user
    following=Follow.objects.filter(id=user.id)
    
    return render(request, "accounts/follow.html",{'user1':following})

def follow2(request,username):
    user1=request.user
    user = User.objects.get(username=username)
    user2=Follow.objects.filter(id=user.id)
    
    return render(request, "accounts/follow2.html",{'user1':user2,'user2':user})


def search(request):
    if request.method == 'POST': # check post
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query'] # get form input data
            
            products=Photo.objects.filter(category_name=query) 
            
            
            if products not in Photo.objects.filter(category_name=query) :
               users=User.objects.filter(username=query)  

               context = {'photos': products, 'query':query,'users':users}
            else:
              context = {'photos': products, 'query':query}
            return render(request, 'accounts/search_photos.html', context)

    return HttpResponseRedirect('/home')


    





#######         CHECKOUT            ########

def success(request):
    return render(request,"accounts/success.html")


def get(request):
    image=ShopCart.objects.filter()
    sum=0
    for product in image:
        sum+= product.price.to_decimal()
    form = CheckoutForm()
    context = { 'form': form,'sum':sum}
    return render(request, 'accounts/checkout.html', context)

def purchasedphotos(request):
    order = ShopCart.objects.filter(user=request.user)
    for order1 in order:
      if order1.ordered==True :
          return render(request,"accounts/purchasedphotos.html",{'photos':order})

    return render(request,"accounts/purchasedphotos.html")


