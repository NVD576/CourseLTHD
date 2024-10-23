from django.db import models
from ckeditor.fields import RichTextField

# from django.contrib.auth.models import AbstractUser
# class User(AbstractUser):
#     pass

class ModelBase(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='courses/%Y/%m/')

    class Meta:
        abstract = True
        ordering = ['-id'] # sắp giảm theo id
    

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Course(ModelBase):
    subject = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=255)

    category = models.ForeignKey(Category,  on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('subject', 'category')

    
    def __str__(self):
        return self.subject
    

# class Lesson(ModelBase):
#     subject = models.CharField(max_length=255, null=False)
#     content = RichTextField(null=False)
#     image = models.ImageField(upload_to="lessons/%Y/%m/")
#     course = models.ForeignKey(Course, on_delete=models.RESTRICT)

#     def __str__(self):
#         return self.subject

class Lesson(ModelBase):
    class Meta:
        unique_together = ('subject', 'course')
    subject = models.CharField(max_length=255)
    content = models.TextField()
    course = models.ForeignKey (
        Course, on_delete=models.CASCADE ,
        related_name='lessons',
        related_query_name='my_lession'
    )
    def __str__(self):
        return self.subject