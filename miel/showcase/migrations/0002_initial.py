# Generated by Django 5.1.4 on 2024-12-15 10:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('showcase', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='superviser',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='ФИО руководителя'),
        ),
        migrations.AddField(
            model_name='invitations',
            name='office',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showcase.office', verbose_name='Офис'),
        ),
        migrations.AddField(
            model_name='candidatecard',
            name='personal_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showcase.personalinfo', verbose_name='Персональная информация'),
        ),
        migrations.AddField(
            model_name='quota',
            name='office',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotas', to='showcase.office', verbose_name='Офис'),
        ),
        migrations.AddField(
            model_name='candidateskill',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showcase.skill'),
        ),
        migrations.AddField(
            model_name='invitations',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showcase.status', verbose_name='Статус'),
        ),
    ]