# Generated by Django 3.1.7 on 2021-10-10 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('actions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='follower',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='follower',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='follower',
            name='to_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rel_to', to='main.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='follower',
            name='subscriber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_from', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='follower',
            unique_together={('subscriber', 'to_user')},
        ),
        migrations.RemoveField(
            model_name='follower',
            name='user',
        ),
    ]