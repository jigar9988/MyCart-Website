from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="ShopHome"),
    path("about", views.about, name="ShopAbout"),
    path("contact", views.contact, name="ShopContact"),
    path("tracker", views.tracker, name="ShopTracker"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
]
