from django.shortcuts import render, redirect
from rjd.form.form import *
from app_cw.utils.pagination import Pagination
import datetime
from openpyxl import load_workbook

def account_pub_list(request):
    """对公已付表"""
    now_time = datetime.datetime.now()
    data_dict = {}
    # 数据收集
    search_data = request.GET.get('q', "")
    search_date = request.GET.get('d', '')
    search_date2 = request.GET.get('d2', '')
    if search_date:
        start_date = datetime.date(*map(int, search_date.split('-')))
    else:
        start_date = ''
    if search_date2:
        end_date = datetime.date(*map(int, search_date2.split('-')))
    else:
        end_date = ''
    if search_data:
        data_dict["supplier__supplier_name__contains"] = search_data
    if start_date and end_date:
        queryset = models.PublicAccount.objects.filter(**data_dict,
                                                        create_time__range=(start_date, end_date)).order_by('-id')
    else:
        queryset = models.PublicAccount.objects.filter(**data_dict,create_time__year=now_time.year,
                                                        create_time__month=now_time.month).order_by('-id')

    page_object = Pagination(request, queryset)
    context = {
        'queryset': page_object.page_queryset,
        'search_data': search_data,
        'page_string': page_object.html(),
        'search_date': search_date,
        'search_date2': search_date2,
    }
    return render(request,'account_pub_list.html',context)


def account_pub_add(request):
    """添加已付账户"""
    if request.method == "GET":
        form = AccountPubModelForm()
        context = {
            'form':form,
            'title':'添加对公付款'
        }
        return render(request,'rjd_add.html',context)
    form = AccountPubModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/rjd/account/pub/list/')
    context = {
        'form':form,
        'title':"添加对公付款",
    }
    return render(request,'rjd_add.html',context)


def account_pub_edit(request,nid):
    """编辑已付账单"""
    row_object = models.PublicAccount.objects.filter(id=nid).first()

    if request.method == "GET":
        form = AccountPubModelForm(instance=row_object)
        context = {
            'form':form,
            'title':'编辑对公已付',
        }
        return render(request,'rjd_add.html',context)
    form = AccountPubModelForm(data=request.POST,instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/rjd/account/pub/list/')
    context = {
        'form':form,
        'title':'编辑对公已付',
    }
    return render(request,'rjd_add.html',context)


def account_pub_delete(request,nid):
    """删除单行账目"""
    models.PublicAccount.objects.filter(id=nid).delete()
    return redirect('/rjd/account/pub/list/')

def account_pub_multi(request):
    """批量上传对公账户"""
    # 1、获取用户上传的文件对象
    file_object = request.FILES.get("exc")
    print(type(file_object))

    # 2、对象传递给openpyxl，由openpyxl读取文件的内容
    wb = load_workbook(file_object)
    sheet = wb.worksheets[0]
    for row in sheet.iter_rows(min_row=8):
        for value in row:
            print(value.value)
    return redirect('/rjd/account/pub/list/')
