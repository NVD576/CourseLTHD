# tạo thư mục ví dụ : courseApp
# tạo môi trường ảo
    python -m venv venv
    vô venv\Scripts\activate để kích hoạt
# cài django
    pip install django
# tạo project 
    django-admin startproject <name>
# tạo app courses
    django-admin startapp <name>
# chạy thử
    python manage.py runserver
# Tạo courses/urls.py 
    from django.urls import path
    from . import views
    urlpatterns = [
        path('', views.index, name="index")
    ]

#  Chỉnh sửa courseApp/urls.py 
    from django.contrib import admin
    from django.urls import path, include
    urlpatterns = [
        path('', include('courses.urls')),
        path('admin/', admin.site.urls),
    ]

# vô setting sửa
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'coursedb',
        'USER': 'root',
        'PASSWORD': '12345678',
        'HOST': '' # mặc định localhost
        }
    }

    thêm MEDIA_ROOT = '%s/courses/static/' % BASE_DIR     //tạo thêm 1 folder static trong courses
    Trong phần INSTALLED_APP thêm
        'courses.apps.CoursesConfig',


# vô models.py viết code
    from django.contrib.auth.models import AbstractUser
    from ckeditor.fields import RichTextField
    from django.db import models

    class User(AbstractUser):
        pass

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


    class Lesson(ModelBase):
        subject = models.CharField(max_length=255)
        content = models.TextField()
        course = models.ForeignKey (
            Course, on_delete=models.CASCADE ,
            related_name='lessons',
            related_query_name='my_lession'
        )

        class Meta:
            unique_together = ('subject', 'course')
        def __str__(self):
            return self.subject
    

# vô admin.py
    from django.contrib import admin
    from .models import models,Category,Course,Lesson
    from django.utils.html import mark_safe
    from django import forms
    from ckeditor_uploader.widgets import CKEditorUploadingWidget

    # Register your models here.
    class LessonAdmin(admin.ModelAdmin):
        list_display = ['id', 'subject', 'active', 'created_date','avatar', ]
        search_fields = ['subject', 'content']
        list_filter = ['id', 'subject', 'created_date']
        list_editable = ['subject']
        readonly_fields = ['avatar']

        def avatar(self, lesson):
            return mark_safe(f"<img src='/static/{lesson.image.name}' width='200' />")

    class CourseAdmin(admin.ModelAdmin):
        list_display = ('id','image_tag', 'subject', 'active', 'created_date',)
        readonly_fields = ('image_tag',)

        def image_tag(self, obj):
            if obj.image:
                return mark_safe(f'<img src="/static/{obj.image.name}" width="150" height="150" />')
            return "No Image"

    admin.site.register(Course, CourseAdmin)

    admin.site.register(Category)

    admin.site.register(Lesson, LessonAdmin)

\\Viết lệnh
#   pip install mysqlclient // phải mở MySQL và đăng nhập vô trước

#   python manage.py makemigrations courses

#   python manage.py sqlmigrate courses 0001

#   python manage.py migrate

#   python manage.py runserver

muốn thêm sửa j trong database thì đọc file addUser.txt


# Để lưu danh sách các gói Python đã cài đặt vào file requirements.txt
    Chạy lệnh pip freeze và lưu vào file:  \\pip freeze > requirements.txt
    Nếu bạn cần cài đặt lại các gói từ file requirements.txt:   \\pip install -r requirements.txt

