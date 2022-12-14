# Generated by Django 4.0.6 on 2022-08-18 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('head0', models.CharField(default='', max_length=450)),
                ('head1', models.CharField(default='', max_length=550)),
                ('head2', models.CharField(default='', max_length=650)),
                ('thumbnail', models.ImageField(default='', upload_to='blog/images')),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
