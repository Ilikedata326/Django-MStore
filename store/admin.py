
from django.contrib import admin
from .models import Carousel, Category, Product, ProductImage, Video, RealImage


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date'] 
    
    model = Carousel


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ProductImageAdmin(admin.StackedInline):
    list_display = ['product', 'added_date']

    model = ProductImage


class RealImageAdmin(admin.StackedInline):
    list_display = ['product', 'added_date']

    model = RealImage


class VideoAdmin(admin.StackedInline):
    list_display = ('product', 'caption', 'added_date',)

    model = Video


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price', 'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}

    inlines = [ProductImageAdmin, VideoAdmin, RealImageAdmin]

    class Meta:
        model = Product 