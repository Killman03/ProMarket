from django.urls import path
from .views import HomeView, AboutView, ContactView, ServiceView, CatalogView, ReservationView, TestimonialView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('service/', ServiceView.as_view(), name='service'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('reservation/', ReservationView.as_view(), name='reservation'),
    path('testimonial/', TestimonialView.as_view(), name='testimonial'),
    # other paths...
]