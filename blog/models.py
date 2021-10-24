from django.db import models




class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name



class Product(models.Model):
    category = models.ForeignKey(Category,related_name="products",on_delete=models.CASCADE,verbose_name='katalog')
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='image')
    short_text = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name