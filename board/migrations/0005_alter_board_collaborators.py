# Generated by Django 3.2.9 on 2021-11-25 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_alter_board_collaborators'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='collaborators',
            field=models.ManyToManyField(blank=True, to='board.Collaborator'),
        ),
    ]
