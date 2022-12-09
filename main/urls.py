from django.urls import path
from django.views.generic import TemplateView
from main.views import ContactUsView

urlpatterns = [
    path("contact-us/", ContactUsView.as_view(), name="contact_us"),
    path('about-us/', TemplateView.as_view(template_name='about_us.html'), name='about_us'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
