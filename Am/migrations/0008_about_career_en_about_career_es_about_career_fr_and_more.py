# Generated by Django 5.1.1 on 2024-10-18 15:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Am', '0007_about_profile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='career_en',
            field=models.CharField(max_length=20, null=True, verbose_name='Career'),
        ),
        migrations.AddField(
            model_name='about',
            name='career_es',
            field=models.CharField(max_length=20, null=True, verbose_name='Career'),
        ),
        migrations.AddField(
            model_name='about',
            name='career_fr',
            field=models.CharField(max_length=20, null=True, verbose_name='Career'),
        ),
        migrations.AddField(
            model_name='about',
            name='career_pt',
            field=models.CharField(max_length=20, null=True, verbose_name='Career'),
        ),
        migrations.AddField(
            model_name='about',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='about',
            name='description_es',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='about',
            name='description_fr',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='about',
            name='description_pt',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='about',
            name='heading_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Heading'),
        ),
        migrations.AddField(
            model_name='about',
            name='heading_es',
            field=models.CharField(max_length=50, null=True, verbose_name='Heading'),
        ),
        migrations.AddField(
            model_name='about',
            name='heading_fr',
            field=models.CharField(max_length=50, null=True, verbose_name='Heading'),
        ),
        migrations.AddField(
            model_name='about',
            name='heading_pt',
            field=models.CharField(max_length=50, null=True, verbose_name='Heading'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=20, null=True, verbose_name='Name Category'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_es',
            field=models.CharField(max_length=20, null=True, verbose_name='Name Category'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_fr',
            field=models.CharField(max_length=20, null=True, verbose_name='Name Category'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_pt',
            field=models.CharField(max_length=20, null=True, verbose_name='Name Category'),
        ),
        migrations.AddField(
            model_name='home',
            name='greetings_1_en',
            field=models.CharField(max_length=5, null=True, verbose_name='Greetings 1'),
        ),
        migrations.AddField(
            model_name='home',
            name='greetings_1_es',
            field=models.CharField(max_length=5, null=True, verbose_name='Greetings 1'),
        ),
        migrations.AddField(
            model_name='home',
            name='greetings_1_fr',
            field=models.CharField(max_length=5, null=True, verbose_name='Greetings 1'),
        ),
        migrations.AddField(
            model_name='home',
            name='greetings_1_pt',
            field=models.CharField(max_length=5, null=True, verbose_name='Greetings 1'),
        ),
        migrations.AddField(
            model_name='home',
            name='greetings_2_en',
            field=models.CharField(max_length=5, null=True, verbose_name='Greetings 2'),
        ),
        migrations.AddField(
            model_name='home',
            name='greetings_2_es',
            field=models.CharField(max_length=5, null=True, verbose_name='Greetings 2'),
        ),
        migrations.AddField(
            model_name='home',
            name='greetings_2_fr',
            field=models.CharField(max_length=5, null=True, verbose_name='Greetings 2'),
        ),
        migrations.AddField(
            model_name='home',
            name='greetings_2_pt',
            field=models.CharField(max_length=5, null=True, verbose_name='Greetings 2'),
        ),
        migrations.AddField(
            model_name='home',
            name='name_en',
            field=models.CharField(max_length=20, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='home',
            name='name_es',
            field=models.CharField(max_length=20, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='home',
            name='name_fr',
            field=models.CharField(max_length=20, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='home',
            name='name_pt',
            field=models.CharField(max_length=20, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='skills',
            name='skill_name_en',
            field=models.CharField(max_length=20, null=True, verbose_name='Skill'),
        ),
        migrations.AddField(
            model_name='skills',
            name='skill_name_es',
            field=models.CharField(max_length=20, null=True, verbose_name='Skill'),
        ),
        migrations.AddField(
            model_name='skills',
            name='skill_name_fr',
            field=models.CharField(max_length=20, null=True, verbose_name='Skill'),
        ),
        migrations.AddField(
            model_name='skills',
            name='skill_name_pt',
            field=models.CharField(max_length=20, null=True, verbose_name='Skill'),
        ),
        migrations.AlterField(
            model_name='about',
            name='career',
            field=models.CharField(max_length=20, verbose_name='Career'),
        ),
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='about',
            name='heading',
            field=models.CharField(max_length=50, verbose_name='Heading'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Name Category'),
        ),
        migrations.AlterField(
            model_name='home',
            name='greetings_1',
            field=models.CharField(max_length=5, verbose_name='Greetings 1'),
        ),
        migrations.AlterField(
            model_name='home',
            name='greetings_2',
            field=models.CharField(max_length=5, verbose_name='Greetings 2'),
        ),
        migrations.AlterField(
            model_name='home',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Am.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='skill_name',
            field=models.CharField(max_length=20, verbose_name='Skill'),
        ),
    ]
