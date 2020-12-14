from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from .models import Teacher, SchoolName, Book, Classes, Teaching, Student


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','name','sex','image','oneYearContract','oneYearContract','collegeContract','masterContract','graduateCollege')


class SchoolNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'schoolName', 'image')


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')


class ClassesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


class TeachingAdmin(admin.ModelAdmin):
    list_display = ('id','get_teacher_name','get_school_name', 'get_class_name', 'get_book_name')

    def get_teacher_name(self, obj):
        return obj.teacherName.name

    def get_school_name(self, obj):
        return obj.schoolName.schoolName

    def get_class_name(self, obj):
        return obj.className.name

    def get_book_name(self, obj):
        return obj.bookName.name


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'nameInKhmer',
                    'nameInEnglish',
                    'sex',
                    'dateOfBirth',
                    'enrollDate',
                    'phoneNumber',
                    'email',
                    'familySituation',
                    'graduted',
                    'get_teacher_name',
                    'get_school_name',
                    'get_class_name',
                    'get_book_name')

    def get_teacher_name(self, obj):
        return obj.teacherName.name

    def get_school_name(self, obj):
        return obj.schoolName.schoolName

    def get_class_name(self, obj):
        return obj.className.name

    def get_book_name(self, obj):
        return obj.bookName.name

    search_fields = ('nameInKhmer', 'nameInEnglish', 'email')
    list_filter = ('schoolName',)
    
    list_filter = (

        # for related fields
        ('schoolName', RelatedDropdownFilter),
    )
    filter_horizontal = ()

    fieldsets = ()


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(SchoolName, SchoolNameAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Classes, ClassesAdmin)
admin.site.register(Teaching, TeachingAdmin)
admin.site.register(Student, StudentAdmin)
