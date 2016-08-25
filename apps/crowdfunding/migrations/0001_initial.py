# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-24 19:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_headline', models.CharField(max_length=300, verbose_name='Campaign headline')),
                ('desc_preview', models.TextField(max_length=400, verbose_name='Short description')),
                ('summ_goal', models.PositiveIntegerField()),
                ('duration', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30)])),
                ('image_main', models.ImageField(blank=True, upload_to='campaigns_images', verbose_name='Campaign image')),
                ('desc_main', models.TextField(verbose_name='Description')),
                ('collected_summ', models.PositiveIntegerField(blank=True, default=0)),
                ('state', models.CharField(default='draft', max_length=50, verbose_name='State')),
                ('funding_type', models.CharField(choices=[('conditional', 'Conditional funding'), ('unconditional', 'Unconditional funding')], default='unconditional', max_length=50, verbose_name='Funding type')),
                ('date_start', models.DateField(null=True, verbose_name='start date')),
                ('date_finish', models.DateField(null=True, verbose_name='finish date')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='creation date')),
                ('views_count', models.PositiveIntegerField(default=0, verbose_name='view count')),
                ('editors', models.ManyToManyField(related_name='campaign_editors', to=settings.AUTH_USER_MODEL, verbose_name='campaign editors')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='campaign owner')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField()),
                ('method', models.CharField(choices=[('METHOD_CARD', 'Bank card'), ('METHOD_TERMINAL', 'Terminal')], default='METHOD_CARD', max_length=40)),
                ('external_id', models.CharField(max_length=150, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('confirmed', models.BooleanField(default=False)),
                ('date_confirmed', models.DateTimeField(null=True)),
                ('is_public', models.BooleanField(default=True)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crowdfunding.Campaign')),
                ('payer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='campaign',
            name='tags',
            field=models.ManyToManyField(blank=True, to='crowdfunding.Tag', verbose_name='Tags'),
        ),
    ]
