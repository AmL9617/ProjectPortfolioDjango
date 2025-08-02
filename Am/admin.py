from django.contrib import admin
from parler.admin import TranslatableAdmin, TranslatableTabularInline
from django.contrib.admin import TabularInline


# Register your models here.
from .models import Home, About, Profile, Category, Skills, Project


# Home
@admin.register(Home)
class HomeAdmin(TranslatableAdmin):  # ⬅️ Must inherit from TranslatableAdmin
    list_display = ('name', 'updated')

# About
class ProfileInline(TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(TranslatableAdmin):
     inlines = [
        ProfileInline,
    ]

# Skills
class SkillsInline(TranslatableTabularInline):
    model = Skills
    extra = 2


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
     inlines = [
        SkillsInline,
    ]


# Projects
admin.site.register(Project)