# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import render
from django.views import View
import copy_fun as cff
import time
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse

# Create your views here.

def show_progress(request):
    LOG = {
            'LOG_INFO': '\n'.join(cff.LOG_ALL), 
            'LOG_NUM': cff.LOG_NUM,
            'num_progress': cff.num_progress,
            'CELL_NUM': input_info['CELL_NUM'],
            'DIE_NUM': input_info['DIE_NUM'],
            'GND_NUM': str(input_info['GND_NUM'])+'/'+str(input_info['GND_GROUP']),
            'NC_NUM': str(input_info['NC_NUM'])+'/'+str(input_info['NC_GROUP']),
            'PKG_NUM': input_info['PKG_NUM']
            }
#    print '--show_progress----------'+str(cff.num_progress)+'...lognum'+str(LOG_NUM)+str(LOG_INFO)
    return JsonResponse(LOG, safe=False)


class show_html(View):
    
    def __init__(self):
        global LOG_INFO, LOG_NUM,log_str, input_info ,download_disable
        LOG_NUM = 0
        LOG_INFO = ""
        download_disable="disabled"
        input_info = {"CELL_NUM":0,
                "DIE_NUM":0,
                "GND_NUM":0,
                "GND_GROUP":0,
                "NC_NUM":0,
                "NC_GROUP":0,
                "PKG_NUM":0,
                "download_disable":download_disable
                }
        
        
    def get(self,request):
        return render(request, 'index.html', {
                'bar_num':0,
                'CELL_NUM': 0,
                'DIE_NUM': 0,
                'GND_NUM': 0,
                'GND_GROUP': 0,
                'NC_NUM': 0,
                'NC_GROUP': 0,
                'PKG_NUM': 0,
                'LOG_NUM': 0,
                'LOG_INFO':"",
                'download_disable' : 'disabled',
            })
    
    def post(self,request):
        global LOG_INFO, LOG_NUM,log_str,input_info,download_disable
        
        if request.method == 'POST':
            if  request.FILES['excel_path'] and request.FILES['edf_path'] :
                            
                #load file
                excel_file = request.FILES['excel_path']
                edf_file = request.FILES['edf_path']
                            
                fs = FileSystemStorage()
                excel_filename = fs.save(excel_file.name, excel_file)
                edf_filename = fs.save(edf_file.name, edf_file)
    
                excel_uploaded_file_url = fs.url(excel_filename)
                edf_uploaded_file_url = fs.url(edf_filename)
                
                path="D:/django_tutorial/"
                excel_path = path+excel_uploaded_file_url
                edf_path = path+edf_uploaded_file_url
    #            
    #            excel_path= request.POST.get('excel_path')
    #            edf_path= request.POST.get('edf_path')
#    #            
#                path="K:/10_Algorithm/ALGDEV/171101/100/"
#                excel_path = path+"(1)TMLP16X12_TFM-V1~~D01_ST-Design_V1.xlsx"
#                edf_path = path+"LIBRARY1M.EDF"
                

                self.res = cff.copy_die_fun(excel_path, edf_path)
                
                input_info = self.res.input_info()

#    
                #run copy
                output_path = path+"media/"
                self.res.run_copy(output_path)
            
                download_disable = ''

                return render(request, 'index.html', {
                    'excel_uploaded_file_url':excel_uploaded_file_url,
                    'edf_uploaded_file_url':edf_uploaded_file_url,
                    'bar_num':100,
                    'CELL_NUM': input_info['CELL_NUM'],
                    'DIE_NUM': input_info['DIE_NUM'],
                    'GND_NUM': input_info['GND_NUM'],
                    'GND_GROUP': input_info['GND_GROUP'],
                    'NC_NUM': input_info['NC_NUM'],
                    'NC_GROUP': input_info['NC_GROUP'],
                    'PKG_NUM': input_info['PKG_NUM'],
                    'LOG_NUM': cff.LOG_NUM,
                    'LOG_INFO':'\n'.join(cff.LOG_ALL),
                    })
            else:
                log_type = 'ERROR : '
                log_time = time.strftime("%H:%M:%S", time.localtime())
                LOG_NUM = LOG_NUM + 1
                log_str = log_time + '-' + log_type +"[{}] Fail in request file.".format(LOG_NUM)
                LOG_INFO.append(log_str)
                
                return render(request, 'index.html', {
                    'bar_num':0,
                    'CELL_NUM': 0,
                    'DIE_NUM': 0,
                    'GND_NUM': 0,
                    'GND_GROUP': 0,
                    'NC_NUM': 0,
                    'NC_GROUP': 0,
                    'PKG_NUM': 0,
                    'LOG_NUM': LOG_NUM,
                    'LOG_INFO':"",
                    'download_disable' : 'disabled',
                    })
        else:   
                
            return render(request, 'index.html', {
                'bar_num':0,
                'CELL_NUM': 0,
                'DIE_NUM': 0,
                'GND_NUM': 0,
                'GND_GROUP': 0,
                'NC_NUM': 0,
                'NC_GROUP': 0,
                'PKG_NUM': 0,
                'LOG_NUM': LOG_NUM,
                'LOG_INFO':"",
                'download_disable' : 'disabled',
            })
#
#def show_html(request):
#    LOG_NUM = 0
#    LOG_INFO = []
#    if request.method == 'POST':
#        if  request.FILES['excel_path'] and request.FILES['edf_path'] :
#        
#            log_type = 'INFO : '
#            log_time = time.strftime("%H:%M:%S", time.localtime())
#            log_str = log_time + '-' + log_type +"Uploading files"
#            LOG_INFO.append(log_str)
#            LOG_NUM = LOG_NUM + 1
#            #load file
#            excel_file = request.FILES['excel_path']
#            edf_file = request.FILES['edf_path']
#                        
#            fs = FileSystemStorage()
#            excel_filename = fs.save(excel_file.name, excel_file)
#            edf_filename = fs.save(edf_file.name, edf_file)
#
#            excel_uploaded_file_url = fs.url(excel_filename)
#            edf_uploaded_file_url = fs.url(edf_filename)
#            
#
#            path="D:/django_tutorial/"
#            excel_path = path+excel_uploaded_file_url
#            edf_path = path+edf_uploaded_file_url
##            
##            excel_path= request.POST.get('excel_path')
##            edf_path= request.POST.get('edf_path')
##            
#            path="K:/10_Algorithm/ALGDEV/171101/100/"
#            excel_path = path+"(1)TMLP16X12_TFM-V1~~D01_ST-Design_V1.xlsx"
#            edf_path = path+"LIBRARY1M.EDF"
#            
#            log_type = 'INFO : '
#            log_time = time.strftime("%H:%M:%S", time.localtime())
#            log_str = log_time + '-' + log_type +"Loading {} files".format(excel_uploaded_file_url)
#            LOG_INFO.append(log_str)
#            log_str = log_time + '-' + log_type +"Loading {} files".format(edf_uploaded_file_url)
#            LOG_INFO.append(log_str)
#            LOG_NUM = LOG_NUM + 2
#            
#            res = cff.copy_die_fun(excel_path, edf_path)
#            input_info = res.input_info()
#            
#            log_type = 'INFO : '
#            log_time = time.strftime("%H:%M:%S", time.localtime())
#            log_str = log_time + '-' + log_type +"Show info"
#            LOG_INFO.append(log_str)
#            LOG_NUM = LOG_NUM + 1
#            LOG_INFO = '\n'.join(LOG_INFO)
#
#            
#            return render(request, 'index.html', {
#                'CELL_NUM': input_info['CELL_NUM'],
#                'DIE_NUM': input_info['DIE_NUM'],
#                'GND_NUM': input_info['GND_NUM'],
#                'GND_GROUP': input_info['GND_GROUP'],
#                'NC_NUM': input_info['NC_NUM'],
#                'NC_GROUP': input_info['NC_GROUP'],
#                'PKG_NUM': input_info['PKG_NUM'],
#                'LOG_NUM': LOG_NUM,
#                'LOG_INFO':LOG_INFO,
#                'EXCEL_PATH':str(excel_path),
#                'EDF_PATH':str(edf_path),
#                'excel_uploaded_file_url':excel_uploaded_file_url,
#                'edf_uploaded_file_url':edf_uploaded_file_url,
#                
#            })
#        else:
#            log_type = 'ERROR : '
#            log_time = time.strftime("%H:%M:%S", time.localtime())
#            log_str = log_time + '-' + log_type +"Fail in request file."
#            LOG_INFO.append(log_str)
#            LOG_NUM = LOG_NUM + 1
#            
#            return render(request, 'index.html', {
#                'CELL_NUM': 0,
#                'DIE_NUM': 0,
#                'GND_NUM': 0,
#                'GND_GROUP': 0,
#                'NC_NUM': 0,
#                'NC_GROUP': 0,
#                'PKG_NUM': 0,
#                'LOG_NUM': LOG_NUM,
#                'LOG_INFO':LOG_INFO,
#                'download_disable' : 'disabled'
#                })
#    else:   
#            
#        return render(request, 'index.html', {
#            'CELL_NUM': 0,
#            'DIE_NUM': 0,
#            'GND_NUM': 0,
#            'GND_GROUP': 0,
#            'NC_NUM': 0,
#            'NC_GROUP': 0,
#            'PKG_NUM': 0,
#            'LOG_NUM': LOG_NUM,
#            'LOG_INFO':LOG_INFO,
#            'download_disable' : 'disabled'
#
#        })