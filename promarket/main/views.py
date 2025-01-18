from django.views.generic import TemplateView, ListView

from .models import Product, Testimonial, Service


class HomeView(TemplateView):
    model = Product
    template_name = 'main/index.html'
    context_object_name = 'product'
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testimonials'] = Testimonial.objects.all()
        context['services'] = Service.objects.all()
        context['product'] = Product.objects.all()
        return context

    def get_queryset(self):
        return Product.objects.filter(available=True)


class AboutView(TemplateView):
    template_name = 'main/about.html'

class ContactView(TemplateView):
    template_name = 'main/contact.html'

class ServiceView(TemplateView):
    template_name = 'main/service.html'

class CatalogView(ListView):
    model = Product
    template_name = 'main/catalog.html'
    context_object_name = 'product'

class ReservationView(TemplateView):
    template_name = 'main/reservation.html'

class TestimonialView(TemplateView):
    template_name = 'main/testimonial.html'