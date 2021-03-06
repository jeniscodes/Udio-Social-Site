# Generated by Django 3.0.8 on 2020-07-30 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tweeter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likedtweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='network.Tweet')),
                ('liker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listlikes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('commentedtweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='network.Tweet')),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listcomments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
