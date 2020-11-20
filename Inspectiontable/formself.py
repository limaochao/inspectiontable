# -*- coding: utf-8 -*-
"""
@Author : hejian
@File   : formself.py
@Project: django3test
@Time   : 2020-11-02 13:23:43
@Desc   : The file is ...
@Version: v1.0
"""


from django.forms import Form, ModelForm
from Inspectiontable import models


class TestForm(ModelForm):
    class Meta:
        model = models.Airconditioning
        fields = '__all__'

    def __init__(self,*args,**kwargs):
        super(TestForm,self).__init__(*args,**kwargs)

        for field_name in self.base_fields:
            field = self.base_fields(field_name)
            field.widget.attrs.update({'class': 'form-control'})