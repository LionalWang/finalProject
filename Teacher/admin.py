from django.contrib import admin
from .models import Class
# Register your models here.


class ClassAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'teacher', 'time', 'point1', 'point2',
                    'point3', 'point4', 'point5')

    def get_queryset(self, request):
        qs = super(ClassAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(teacher=request.user)


class MyModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(MyModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(author=request.user)

admin.site.register(Class, ClassAdmin)
