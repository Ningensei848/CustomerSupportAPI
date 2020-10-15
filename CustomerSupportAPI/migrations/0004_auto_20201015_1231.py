# Generated by Django 3.1.2 on 2020-10-15 03:31

import CustomerSupportAPI.models.matter
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerSupportAPI', '0003_auto_20201014_1609'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mattermodel',
            old_name='calling',
            new_name='caller',
        ),
        migrations.AlterField(
            model_name='mattermodel',
            name='title',
            field=models.CharField(default=CustomerSupportAPI.models.matter.title_default, help_text='If you had one keyword to tell your colleagues about this telephone, it would be ...', max_length=255, verbose_name='要件'),
        ),
    ]
