from django.urls import path
from .models import *
from .views import *
app_name = 'blog'


urlpatterns = [
    path('',IndexView.as_view(),name="index"),
    path('/<str:cat_slug>',CategoryView.as_view(),name="cat_slug"),
    path('products',ProductView.as_view(),name="products"),
    path('service',ServiceView.as_view(),name="service"),
    path('menu',MenuView.as_view(),name="menu"),
    path('about',AboutUs.as_view(),name='about'),
    path('contact',ContactView.as_view(),name="contact"),
    # path("search_product",search_product,name="search_product")
]