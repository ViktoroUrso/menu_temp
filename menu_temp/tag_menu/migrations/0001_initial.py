# Generated by Django 4.1.13 on 2024-02-25 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TagMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Menu item', max_length=255, unique=True)),
                ('url', models.CharField(default='menu/', max_length=255)),
                ('left', models.IntegerField(blank=True, null=True)),
                ('right', models.IntegerField(blank=True, null=True)),
                ('level', models.IntegerField(blank=True, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='tag_menu.tagmenu')),
                ('root', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='head', to='tag_menu.tagmenu')),
            ],
        ),
    ]
