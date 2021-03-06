# Generated by Django 3.1.1 on 2020-11-03 08:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Airconditioning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AirconditioningListname', models.CharField(max_length=100, verbose_name='空调列表')),
                ('Airconditioning_temperature', models.IntegerField(default=21, null=True, verbose_name='空调温度')),
                ('Open_state', models.BooleanField(default=True, null=True, verbose_name='开启状态')),
                ('Abnormal_noise', models.BooleanField(default=False, null=True, verbose_name='异常噪音')),
                ('Airconditioning_Remarks', models.TextField(null=True, verbose_name='空调备注')),
                ('Airconditioning_Create_Data', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cabinet_list', models.CharField(max_length=100, verbose_name='机柜列表')),
                ('Operating_status', models.BooleanField(default=True, verbose_name='机柜状态')),
                ('Voltage', models.IntegerField(default=220, verbose_name='机柜电压')),
                ('Current', models.IntegerField(default=10, verbose_name='机柜电流')),
                ('Cabinet_Remarks', models.TextField(verbose_name='机柜备注')),
            ],
        ),
        migrations.CreateModel(
            name='Devicelist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Devicename', models.CharField(max_length=100, verbose_name='设备名称')),
            ],
        ),
        migrations.CreateModel(
            name='Ordinaryequipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Equipment_name', models.CharField(max_length=100, verbose_name='设备名称')),
                ('Operating_status', models.BooleanField(default=True, verbose_name='设备运行状态')),
                ('Ordinaryequipment_Remarks', models.TextField(verbose_name='机房环境备注')),
            ],
        ),
        migrations.CreateModel(
            name='Tableheadmodels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order_number', models.IntegerField(verbose_name='表单编号')),
                ('Createdate', models.DateTimeField(auto_now_add=True)),
                ('Personnel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
