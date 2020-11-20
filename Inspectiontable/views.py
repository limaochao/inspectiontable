'''
Description: 
Author: limaochao
Date: 2020-11-20 19:19:34
LastEditTime: 2020-11-20 20:11:12
'''
from django.shortcuts import render, reverse, redirect
from .forms import Ordinaryequipment_form
from .models import AirconditioningList
# from .formself import *
import time
# Create your views here.


# 订单号生成
def grantOrderNumber():
    struct_time = time.localtime(time.time())
    number = time.strftime('%Y%m%d', struct_time)
    return number


def Inspection_table(request):
    if request.method == 'GET':
        order_detrail = AirconditioningList.objects.all()
        Insp = Ordinaryequipment_form()
        devicelist = AirconditioningList.objects.all()
        return render(request, 'Inspectiontable/index.html', locals())
    else:
        Insp = Ordinaryequipment_form(request.POST)
        print(Insp)
        print('-----------------')
        print(request.POST)
        if Insp.is_valid():
            recove = Insp.save(commit=False)
            # recove.Airconditioning_list = 
            recove.save()

        else:
            # print(Insp)
            print('Error')
        return redirect(reverse('Inspection_table'))
