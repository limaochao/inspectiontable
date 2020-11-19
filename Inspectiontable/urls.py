# -*- coding: utf-8 -*-
"""
@Author : hejian
@File   : urls.py
@Project: django3test
@Time   : 2020-10-20 16:28:54
@Desc   : The file is ...
@Version: v1.0
"""

from django.urls import path
from .views import *

urlpatterns = [
    path('', Inspection_table,name = 'Inspection_table'),
]