from django.contrib import admin
from django.db import models

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 1

class QuestionAdmin(admin.ModelAdmin):
  fieldsets = [(None, {'fields': ['question_text']}),
  ('Date published', {'fields': ['pub_date'], 'classes': ['collapse']}),]
  inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

# admin.site.register(Question)
# admin.site.register(Choice)