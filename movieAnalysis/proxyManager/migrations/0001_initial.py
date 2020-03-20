# Generated by Django 2.2 on 2020-03-16 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proxy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protocol', models.SmallIntegerField(choices=[(0, '未知'), (1, 'http'), (2, 'https'), (3, 'http + https')], default=0, verbose_name='代理类型')),
                ('anonymity', models.SmallIntegerField(choices=[(0, '未知'), (1, '高匿'), (2, '普匿'), (3, '透明')], default=0, verbose_name='匿名程度')),
                ('ip', models.CharField(max_length=16, null=True, unique=True, verbose_name='ip')),
                ('port', models.CharField(max_length=12, null=True, verbose_name='端口号')),
                ('speed', models.CharField(max_length=12, null=True, verbose_name='响应速度')),
                ('area', models.CharField(max_length=64, null=True, verbose_name='ip地址')),
                ('verify_time', models.DateTimeField(default=None, verbose_name='最后验证时间')),
                ('source', models.CharField(max_length=20, verbose_name='来源')),
            ],
        ),
    ]
