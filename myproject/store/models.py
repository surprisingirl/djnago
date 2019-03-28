from django.db import  models

class Category(models.Model):
    title = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.title


class Recipe(models.Model):
    title =models.CharField(max_length=30, unique=True) 
    ingredients=models.TextField(max_length=290)
    description=models.TextField(max_length=10000)
    category = models.ForeignKey(Category, null=True,related_name='category',on_delete=models.CASCADE)
    def __str__(self):
        return self.title

