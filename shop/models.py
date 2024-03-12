from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length = 100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_b_category', kwargs={'category_slug':self.slug})

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE,related_name='products' )
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    date_created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, max_length=1000)
    image_product = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price= models.DecimalField(decimal_places=2, max_digits=10)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('-date_created',)
        index_together= (('id','slug'),)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_detail', kwargs={'pk':self.pk, 'slug':self.slug})



