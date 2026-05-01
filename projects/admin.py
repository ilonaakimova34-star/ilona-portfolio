from django.contrib import admin
from .models import Project, ProjectImage, Skill, Experience

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill)
admin.site.register(Experience)

from .models import Project, ProjectImage, Skill, Experience, Certification

admin.site.register(Certification)