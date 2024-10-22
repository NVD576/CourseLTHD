from django.db import models

# Create your models here.

class ModelBase(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='courses/%Y/%m/', null=True)
    class Meta:
        abstract = True
        ordering = ['-id'] # sắp giảm theo id
    

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Course(models.Model):
    subject = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,  on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    class Meta:
        unique_together = ('subject', 'category')
    def __str__(self):
        return self.subject