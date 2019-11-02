from django.contrib import admin
from .models import Tutorial, Person
from django.db import models
from tinymce.widgets import TinyMCE
# Register your models here.

class TutorialAdmin(admin.ModelAdmin):
	fieldsets = [
					("Title/date", {"fields": ["tutorial_title", "tutorial_published"]  }),
					("Content", {"fields": ["tutorial_content"]})
			]
#	formfield_overrides = { models.TextField: {"widget": TinyMCE()}}

	
admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(Person)