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
# admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)