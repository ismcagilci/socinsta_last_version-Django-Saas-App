# Generated by Django 2.2 on 2020-10-04 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0008_auto_20201004_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socinstaproxy',
            name='ip_adress',
            field=models.CharField(max_length=200, null=True, verbose_name='Proxy IP Adress'),
        ),
    ]