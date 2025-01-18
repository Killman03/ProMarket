from django.utils import timezone
from django.db import models
from django.urls import reverse


# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    machine_model = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/')
    feedback = models.TextField()

    def __str__(self):
        return self.client_name


class Product(models.Model):
    """Товар."""

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField(upload_to="images/%Y/%m/%d/")
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def get_absolute_url(self):
        return reverse("Product", kwargs={"product_slug": self.slug})

    def __str__(self):
        return self.title