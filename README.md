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
    from django.db import models
    class Category(models.Model):
        name = models.CharField(max_length=100, unique=True)

        def __str__(self):
            return self.name
    
    class Course(models.Model):
        subject = models.CharField(max_length=100, unique=True)
        description = models.CharField(max_length=255)
        created_date = models.DateTimeField(auto_now_add=True)
        updated_date = models.DateTimeField(auto_now=True)
        category = models.ForeignKey(Category,  on_delete=models.CASCADE)
        active = models.BooleanField(default=True)

            class Meta:
                unique_together = ('subject', 'category')

            def __str__(self):
                return self.subject


    class ModelBase(models.Model):
        created_date = models.DateTimeField(auto_now_add=True)
        updated_date = models.DateTimeField(auto_now=True)
        active = models.BooleanField(default=True)
        image = models.ImageField(upload_to='courses/%Y/%m/', null=True)

        class Meta:
            abstract = True
            ordering = ['-id'] # sắp giảm theo id


# vô admin.py
    from django.contrib import admin
    from .models import models,Category,Course

    # Register your models here.

    admin.site.register(Category)
    admin.site.register(Course)




\\Viết lệnh
#   pip install mysqlclient // phải mở MySQL và đăng nhập vô trước

#   python manage.py makemigrations courses

#   python manage.py sqlmigrate courses 0001

#   python manage.py migrate

muốn thêm sửa j trong database thì đọc file addUser.txt


# Để lưu danh sách các gói Python đã cài đặt vào file requirements.txt
    Chạy lệnh pip freeze và lưu vào file:  \\pip freeze > requirements.txt
    Nếu bạn cần cài đặt lại các gói từ file requirements.txt:   \\pip install -r requirements.txt

