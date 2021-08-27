# Generated by Django 3.2.5 on 2021-08-27 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_employee_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Астрахань', max_length=40)),
                ('days_delivery', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Города, доступные для доставки',
                'db_table': 'city',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='accounts.city'),
        ),
    ]