from django.db import models
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, db_index=True)
    desc = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=158.6)
    image = models.ImageField(upload_to= "products/%y/%m/%d", blank=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("product:product_detail", args=[self.id,self.slug])





