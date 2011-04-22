from django.contrib import admin
from django.contrib.auth.models import Group
from django.forms import ModelForm
from django.forms import ModelMultipleChoiceField
from django.contrib.admin.widgets import FilteredSelectMultiple

from courses.models import Course, Semester

class CourseAdminForm(ModelForm):
    faculty = ModelMultipleChoiceField(queryset = Group.objects.get(name = 'Faculty').user_set.all(),
                                       required = False,
                                       widget = FilteredSelectMultiple("Faculty", False) )
    class Meta:
        model = Course

class CourseAdmin(admin.ModelAdmin):
     list_filter = ('semester',)
     filter_horizontal = ('faculty',)
     form = CourseAdminForm

admin.site.register(Course, CourseAdmin)
admin.site.register(Semester)
