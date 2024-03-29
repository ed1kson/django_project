# Generated by Django 5.0.1 on 2024-02-07 18:23

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=40)),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='students', to='myapp.class')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.IntegerField(validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)])),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='notes', to='myapp.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='notes', to='myapp.subject')),
            ],
        ),
        migrations.CreateModel(
            name='DailySchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fifth_lesson', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='fifths', to='myapp.subject')),
                ('first_lesson', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='firsts', to='myapp.subject')),
                ('fourth_lesson', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='fourths', to='myapp.subject')),
                ('second_lesson', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='seconds', to='myapp.subject')),
                ('seventh_lesson', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sevenths', to='myapp.subject')),
                ('sixth_lesson', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sixths', to='myapp.subject')),
                ('third_lesson', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='thirds', to='myapp.subject')),
            ],
        ),
        migrations.AddField(
            model_name='subject',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='subjects', to='myapp.teacher'),
        ),
        migrations.CreateModel(
            name='WeeklySchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friday', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='fridays', to='myapp.dailyschedule')),
                ('monday', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mondays', to='myapp.dailyschedule')),
                ('thursday', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='thursdays', to='myapp.dailyschedule')),
                ('tuesday', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tuesdays', to='myapp.dailyschedule')),
                ('wednesday', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='wednesdays', to='myapp.dailyschedule')),
            ],
        ),
        migrations.AddField(
            model_name='teacher',
            name='schedule',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='trelation', to='myapp.weeklyschedule'),
        ),
        migrations.AddField(
            model_name='class',
            name='schedule',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='relation', to='myapp.weeklyschedule'),
        ),
    ]
