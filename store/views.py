from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from .models import Carousel, Category, Product, ProductImage, Video, RealImage
from django.core.paginator import Paginator  
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from django.db import IntegrityError
from django.db.models import Q 
 
from django.http import HttpResponseRedirect, HttpResponse

def aboutus(request):
    return render(request, 'store/aboutus.html')


def categories(request): 
    return {
        'categories' : Category.objects.all()
    }

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context = {'category': category, 'products': products}
    return render(request, 'store/category.html', context)


def all_products(request):
    products = Product.objects.all()   
    carousels = Carousel.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != "" and item_name is not None:
        products = Product.objects.filter(title__icontains=item_name) 
    
    # pagination
    paginator = Paginator(products, 3) # 5 is the number of product to display
    page = request.GET.get('page')
    products = paginator.get_page(page) 
    
    # Search for products
    item_name = request.GET.get("item-name")
    if item_name != "" and item_name is not None:
        products = Product.objects.filter(description__icontains=item_name)
        
    context = {'products': products, 'carousels':carousels}
    return render(request, 'store/home.html', context)


def product_detail(request, slug):
    products = Product.objects.all() 
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    images = ProductImage.objects.filter(product=product)
    videos = Video.objects.filter(product=product)
    real_images = RealImage.objects.filter(product=product)
    
   
    # Add reviews
    #review = ReviewRating.objects.filter(product=product)
    """
    if request.method == 'POST' and request.user.is_authenticated:
        stars = request.POST.get('stars', 3)
        review = request.POST.get('review', '')
        user = request.user 

        reviews = ProductReview.objects.create(user=user, product=product, review=review, stars=stars).save()
    
        return redirect('store:product_detail', slug=slug)

    """
    return render(request, 'store/detail.html', {'product': product, 
                                                 'images':images, 
                                                 'videos': videos, 
                                                 'real_images':real_images, 
                                                 'products': products})

#  Account models
"""
def review_rate(request):
    if request.method == "GET":
        prod_id = request.GET.get('prod_id')
        product = Product.objects.get(id=prod_id)
        review = request.GET.get('review')
        stars = request.GET.get('stars')
        user = request.user
        ProductReview(user=user, product=product, review=review, stars=stars).save()
        return redirect('detail', id=prod_id)
"""

"""
def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=reviews)
            #form.save()
            messages.success(request, "Thank you! Your review has been update")
            return redirect(url)
        
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid(): 
                
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.comment = form.cleaned_data['comment']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save() 
                messages.success(request, "Thankyou! Your review has been submitted.")
                return redirect(url)


def addcomment(request, id):
    url = request.META.get('HTTP_REFERER')
    return HttpResponse(url)
    if request.method == 'POST':
        form = CommentForm(request.POS)
        if form.is_valid(T):
            data = Comment() # create relation with model
            data.name = form.cleaned_data['name']
            data.subject = form.cleaned_data['subject']
            data.rating = form.cleaned_data['rating']
            data.comment = form.cleaned_data['comment']
            data.ip = request.META.get('REMOTE_ADDR')
            data.product_id = id 
            #current_user = user
            data.user_id = request.user.id
            data.save() 
            messages.success(request, "Thankyou! Your review has been submitted.")
            return HttpResponseRedirect(url)
        
    return HttpResponseRedirect(url)# render(request, 'store/addcomment.html')

 """
 

 