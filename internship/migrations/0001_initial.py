# Generated by Django 4.1.3 on 2024-01-16 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InternshipRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(choices=[('UI/UX', 'UI/UX'), ('Backend Development using Django', 'Backend Development using Django'), ('Devops', 'Devops'), ('Frontend Development', 'Frontend Development'), ('Mobile application Development in Flutter', 'Mobile application Development in Flutter')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='InternshipRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('is_accepted', models.BooleanField(default=False)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internship.internshiprole')),
            ],
        ),
    ]