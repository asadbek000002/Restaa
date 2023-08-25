# Generated by Django 4.2.1 on 2023-08-25 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=30)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=30)),
                ('image', models.ImageField(upload_to='')),
                ('recipe', models.TextField(max_length=1000)),
                ('real_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('porsiya', models.CharField(blank=True, choices=[('05_HISSA', '05_HISSA'), ('ODATIY', 'ODATIY')], default='ODATIY', max_length=10, null=True)),
                ('liter', models.CharField(choices=[('0.5 L', '0.5 L'), ('1 L', '1 L'), ('1.5 L', '1.5 L'), ('2 L', '2 L')], default='1 L', max_length=10)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.menu')),
            ],
        ),
    ]
