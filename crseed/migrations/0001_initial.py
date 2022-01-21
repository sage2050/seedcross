# Generated by Django 3.2.8 on 2022-01-21 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessLog',
            fields=[
                ('log_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('live', models.BooleanField(default=False)),
                ('total_in_client', models.IntegerField(default=0)),
                ('flow_limit', models.IntegerField(default=0)),
                ('progress', models.IntegerField(default=0)),
                ('query_count', models.IntegerField(default=0)),
                ('match_count', models.IntegerField(default=0)),
                ('download_count', models.IntegerField(default=0)),
                ('log_message', models.TextField()),
                ('error_abort', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ProcessParam',
            fields=[
                ('process_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('jackett_url', models.CharField(max_length=128)),
                ('jackett_api_key', models.CharField(max_length=255)),
                ('delay', models.IntegerField(default=5)),
                ('trackers', models.CharField(default='', max_length=255, null=True)),
                ('strict_size', models.BooleanField(default=False)),
                ('fc_count', models.IntegerField(default=20)),
                ('fc_interval', models.IntegerField(default=2)),
            ],
            options={
                'db_table': 'crseed_process_param',
            },
        ),
        migrations.CreateModel(
            name='SearchedHistory',
            fields=[
                ('torrent_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('hash', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('size', models.BigIntegerField(default=0)),
                ('location', models.CharField(max_length=255, null=True)),
                ('tracker', models.CharField(max_length=255, null=True)),
                ('root_dir', models.CharField(max_length=255, null=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'crseed_searched_torrent',
            },
        ),
        migrations.CreateModel(
            name='TaskControl',
            fields=[
                ('task_control_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('cancel_task', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TorClientSetting',
            fields=[
                ('client_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('host', models.CharField(max_length=128)),
                ('port', models.IntegerField(default=8091)),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('clienttype', models.CharField(choices=[('qb', 'qbittorrent'), ('tr', 'transmission'), ('de', 'deluge')], default='de', max_length=2)),
                ('inprocess', models.BooleanField(default=False)),
                ('process_param', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crseed.processparam')),
            ],
            options={
                'db_table': 'crseed_torrent_client',
            },
        ),
        migrations.CreateModel(
            name='CrossTorrent',
            fields=[
                ('torrent_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('size', models.BigIntegerField(default=0)),
                ('location', models.CharField(max_length=255, null=True)),
                ('tracker', models.CharField(max_length=255, null=True)),
                ('root_dir', models.CharField(max_length=255, null=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('crossed_with', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crseed.searchedhistory')),
            ],
            options={
                'db_table': 'crseed_cross_torrent',
            },
        ),
    ]