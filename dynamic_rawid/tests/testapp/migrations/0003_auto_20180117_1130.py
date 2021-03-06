# Generated by Django 2.0.1 on 2018-01-17 11:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20171206_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directprimarykeymodel',
            name='num',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Number'),
        ),
        migrations.AlterField(
            model_name='dynamic_rawidtest',
            name='rawid_fk_limited',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rawid_fk_limited', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='dynamic_rawidtest',
            name='dynamic_rawid_fk_limited',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dynamic_rawid_fk_limited', to=settings.AUTH_USER_MODEL),
        ),
    ]
