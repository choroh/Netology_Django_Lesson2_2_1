from django.contrib import admin

from .models import Student, Teacher, StudentPosition


# Создаем инлайн модель для улучшенной адинпанели
class StudentPositioninline(admin.TabularInline):
    model = StudentPosition
    # выстраиваем модель для StudentPosition
    extra = 0
    # необязательный параметр. Количество позиций товаров в таблице отображения в заказе


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group']
    inlines = [StudentPositioninline, ]
    # Чтобы добавлять преподавателям студентов


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
    inlines = [StudentPositioninline,]
    # Чтобы добавлять студентам преподавателей.


