from django.urls import path, include
from .import views 

app_name = 'store'

urlpatterns = [  
    path('', views.all_products, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
    #path('submit_review/<int:product_id>', views.submit_review, name='submit_review'),
    #path('addcomment/<int:id>', views.addcomment, name="addcomment"),
    # Auth
    #path('signup/', views.signupuser, name="signupuser"),
    #path('login/', views.loginuser, name="loginuser"),
    #path('logout/', views.logoutuser, name="logoutuser"),

]