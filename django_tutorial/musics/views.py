# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import musics.countpy


# Create your views here.
def hello_view(request):
    a = musics.countpy.shownum(3)
    
    return render(request, 'index.html', {
            'data': "Hello Django ",
            'number_pkg':str(a),
    })
    
