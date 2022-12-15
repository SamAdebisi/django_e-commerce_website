from django.urls import path
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from main.views import ContactUsView, ProductListView
from main.models import Product

urlpatterns = [
    path("product/<slug:slug>/", DetailView.as_view(model=Product), name="product"),
    path("products/<slug:tag>/", ProductListView.as_view(), name="products"),
    path("contact-us/", ContactUsView.as_view(), name="contact_us"),
    path('about-us/', TemplateView.as_view(template_name='about_us.html'), name='about_us'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
