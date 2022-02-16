# Generated by Django 4.0.2 on 2022-02-16 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='allErrors',
            fields=[
                ('serial_no', models.AutoField(primary_key=True, serialize=False)),
                ('section', models.CharField(choices=[('General', 'General'), ('Django', 'Django'), ('Python', 'Python'), ('Database', 'Database'), ('Api', 'Api'), ('Aws', 'Aws'), ('Frontend', 'Frontend'), ('Extras', 'Extras')], default='General', max_length=10)),
                ('error_type', models.CharField(max_length=150)),
                ('solution', models.TextField(max_length=10000)),
                ('link', models.URLField(blank=True, max_length=10000)),
            ],
        ),
    ]
