# translation.py

from modeltranslation.translator import translator, TranslationOptions
from .models import Home, About, Category, Skills

class HomeTranslationOptions(TranslationOptions):
    fields = ('name', 'greetings_1', 'greetings_2')

class AboutTranslationOptions(TranslationOptions):
    fields = ('heading', 'career', 'description')

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)  

class SkillsTranslationOptions(TranslationOptions):
    fields = ('skill_name',)  

translator.register(Home, HomeTranslationOptions)
translator.register(About, AboutTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Skills, SkillsTranslationOptions)
