# Register your models here.

from django.contrib import admin

from .models import Choice, Question #,Animal


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
'''    
class AnimalInline(admin.TabularInline):
        fieldsets = [
        (None,               {'fields': ['symptom']}),
        ('Date information', {'fields': ['name','first_day_sickness','owner'], 'classes': ['collapse']}),
        ]
        inlines = [ChoiceInline]
        list_display = ('name', 'first_day_sickness', 'owner')
        list_filter = ['first_day_sickness']
        search_fields = ['symptom']
'''

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    
admin.site.register(Question, QuestionAdmin)
'''
admin.site.register(Animal, AnimalInline)
'''
