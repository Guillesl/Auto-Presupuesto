from django.contrib import admin
from .models import Project, Solar_field

# class Solar_fieldInLine(admin.StackedInline):
#     model = Solar_field
#     extra = 3

# class ProjectAdmin(admin.ModelAdmin):
#     fields = ["num_colect", "cost", "real_offer", "pub_date"]
#     inlines = [Solar_fieldInLine]
#     list_display = ("num_colect", "cost", "real_offer", "pub_date")

admin.site.register(Project)
