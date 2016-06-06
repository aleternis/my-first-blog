# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-06 01:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('exam_list', 'Can see exam list'), ('exam_detail', 'Can see exam detail')),
            },
        ),
        migrations.CreateModel(
            name='ExamTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('questions', models.IntegerField()),
                ('answers', models.IntegerField()),
            ],
            options={
                'permissions': (('exam_template_list', 'Can see template list'), ('exam_template_detail', 'Can see template detail')),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', tinymce.models.HTMLField()),
                ('alternativeA', tinymce.models.HTMLField()),
                ('alternativeB', tinymce.models.HTMLField()),
                ('alternativeC', tinymce.models.HTMLField()),
                ('alternativeD', tinymce.models.HTMLField()),
                ('alternativeE', tinymce.models.HTMLField()),
                ('exam', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Exam')),
            ],
            options={
                'permissions': (('question_list', 'Can see question list'), ('question_detail', 'Can see question detail')),
            },
        ),
        migrations.AddField(
            model_name='exam',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.ExamTemplate'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post'),
        ),
    ]