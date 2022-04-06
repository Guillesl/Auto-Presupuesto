from django.contrib import admin
from presupuesto.models import Project

# class ProjectAdmin(admin.ModelAdmin):
#     fields = ["pub_date", "question_text"]
#     inlines = [ChoiceInLine]
#     list_display = ("question_text", "pub_date", "was_published_recently")
#     list_filter = ["pub_date"]
#     search_fields = ["question_text"]

admin.site.register(Project)
