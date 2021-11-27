from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('share', models.BooleanField(default=False)),
                ('description', models.TextField(null=True)),
                ('cover_img', models.ImageField(
                    null=True, upload_to='board/covers')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('board', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='board.board')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField(null=True)),
                ('ckeck_list', models.JSONField(null=True)),
                ('board', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='board.board')),
            ],
        ),
        migrations.CreateModel(
            name='Collaborator',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('is_super', models.BooleanField(default=False)),
                ('can_invite', models.BooleanField(default=False)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='board',
            name='collaborators',
            field=models.ManyToManyField(to='board.Collaborator'),
        ),
        migrations.AddField(
            model_name='board',
            name='owner',
            field=[models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ('description', models.TextField(blank=True, null=True)),
                ('cover_img', models.ImageField(
                    blank=True, null=True, upload_to='board/covers')),
            ],
        ),
        migrations.CreateModel(
            name='Collaborator',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                 primary_key=True, serialize=False, to='account.userprofile')),
                ('is_super', models.BooleanField(default=False)),
                ('can_invite', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('board', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='board.board')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField(null=True)),
                ('ckeck_list', models.JSONField(null=True)),
                ('board', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='board.board')),
            ],
        ),
        migrations.AddField(
            model_name='board',
            name='collaborators',
            field=models.ManyToManyField(
                blank=True, to='board.Collaborator'),
        ),
        migrations.AddField(
            model_name='board',
            name='owner',
            field=[models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ('description', models.TextField(default='', null=True)),
                ('cover_img', models.ImageField(upload_to='board_covers')),
            ],
        ),
    ]
