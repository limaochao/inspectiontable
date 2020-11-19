# -*- coding: utf-8 -*-
"""
@Author : hejian
@File   : forms.py
@Project: django3test
@Time   : 2020-10-20 15:07:21
@Desc   : The file is ...
@Version: v1.0
"""
from django import forms
from .models import *

class Inspection_form(forms.ModelForm):

    class Meta:
        model = Tableheadmodels
        exclude = ['Order_number','Personnel']

class Ordinaryequipment_form(forms.ModelForm):

    class Meta:
        model = Airconditioning
        fields = '__all__'
        exclude = ['Airconditioning_list']