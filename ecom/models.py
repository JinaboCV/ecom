from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    title = models.CharField( max_length=200)    
    price = models.FloatField()
    description = models.TextField()
    image = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title



