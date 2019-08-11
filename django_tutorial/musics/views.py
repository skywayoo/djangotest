# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import musics.countpy


# Create your views here.
def hello_view(request):
    a = musics.countpy.shownum(3)
    try:
        if request.method == 'POST':
            if  request.POST.get('excel_path') and request.POST.get('edf_path') :
                excel_path= request.POST.get('excel_path')
                edf_path= request.POST.get('edf_path')
        
                return render(request, 'index.html', {
                'data': "Hello Django WORKing!!!! ",
                'number_pkg':str(a),
                'EXCEL_PATH':excel_path,
                'EDF_PATH':edf_path,
                })
            else:
                 return render(request, 'index.html', {
                    'data': "Hello Django NOT WORK request = True ",
                    'number_pkg':str(a),
                    })
        else:
            return render(request, 'index.html', {
                    'data': "Hello Django NOT WORK ",
                    'number_pkg':str(a),
            })
    except:
        return render(request, 'index.html', {
        'data': "Hello Django NOT WORK ",
        'number_pkg':str(a),
            })

    