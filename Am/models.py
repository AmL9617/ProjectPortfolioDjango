from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

# HOME SECTION

class Home(models.Model):
    name = models.CharField(max_length=20,  verbose_name=_("Name"))
    greetings_1 = models.CharField(max_length=9,  verbose_name=_("Greetings 1"))
    greetings_2 = models.CharField(max_length=9,  verbose_name=_("Greetings 2"))
    picture = models.ImageField(upload_to='picture/')
    
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# ABOUT SECTION

class About(models.Model):
    heading = models.CharField(max_length=50,  verbose_name=_("Heading"))
    career = models.CharField(max_length=20,  verbose_name=_("Career"))
    description = models.TextField(blank=False,  verbose_name=_("Description"))
    profile_img = models.ImageField(upload_to='profile/')    
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career

class Profile(models.Model):
    about = models.ForeignKey(About,
                                on_delete=models.CASCADE)




# SKILLS SECTION

class Category(models.Model):
    name = models.CharField(max_length=20,  verbose_name=_("Name Category"))

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Skill')
        verbose_name_plural = _('Skills')

    def __str__(self):
        return self.name

class Skills(models.Model):
    category = models.ForeignKey(Category,
                                on_delete=models.CASCADE,  verbose_name=_("Category"))
    skill_name = models.CharField(max_length=20,  verbose_name=_("Skill"))

    

# PROJECT SECTION

class Project(models.Model):
    image = models.ImageField(upload_to='project/')
    link = models.URLField(max_length=200)

    def __str__(self):
        return f'Project {self.id}'

class Setting(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	value = models.CharField(max_length=200)

	def __str__(self):
		return self.name