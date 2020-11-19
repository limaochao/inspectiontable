from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#表单头
class Tableheadmodels(models.Model):
    Order_number = models.IntegerField(verbose_name='表单编号')
    Personnel = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    Createdate = models.DateTimeField(auto_now_add=True)

#设备列表
class Devicelist(models.Model):
    Devicename = models.CharField('设备名称',max_length=100)


#机房环境普通设备
class Ordinaryequipment(models.Model):
    Equipment_name = models.CharField('设备名称',max_length=100)
    Operating_status = models.BooleanField('设备运行状态',default=True)
    Ordinaryequipment_Remarks = models.TextField('机房环境备注')


#空调列表
class AirconditioningList(models.Model):
    AirconditioningListname = models.CharField('空调列表', max_length=100)



#机房空调状态
class Airconditioning(models.Model):
    Airconditioning_list = models.ForeignKey(AirconditioningList,on_delete=models.DO_NOTHING)
    # AirconditioningListname = models.CharField('空调列表', max_length=100)
    Airconditioning_temperature = models.IntegerField('空调温度',default=21,null=True)
    Open_state = models.BooleanField('开启状态',default=True,null=True)
    Abnormal_noise = models.BooleanField('异常噪音',default=False,null=True)
    Airconditioning_Remarks = models.TextField('空调备注',null=True)
    Airconditioning_Create_Data = models.DateTimeField(auto_now_add=True,null=True)

#机房强电机柜
class Cabinet(models.Model):
    Cabinet_list = models.CharField('机柜列表',max_length=100)
    Operating_status = models.BooleanField('机柜状态',default=True)
    Voltage = models.IntegerField('机柜电压',default=220)
    Current = models.IntegerField('机柜电流',default=10)
    Cabinet_Remarks = models.TextField('机柜备注')