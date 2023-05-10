from django.shortcuts import render, redirect
from rjd.form.form import *
from app_cw.utils.pagination import Pagination
import datetime

def account_receivable_list(request):
    """应收款项表"""
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
        data_dict["custom__company_name__contains"] = search_data
    if start_date and end_date:
        queryset = models.AccountsReceivable.objects.filter(**data_dict,
                                                        create_time__range=(start_date, end_date)).order_by('-id')
    else:
        queryset = models.AccountsReceivable.objects.filter(**data_dict, create_time__year=now_time.year,
                                                        create_time__month=now_time.month).order_by('-id')

    page_object = Pagination(request, queryset)
    context = {
        'queryset': page_object.page_queryset,
        'search_data': search_data,
        'page_string': page_object.html(),
        'search_date': search_date,
        'search_date2': search_date2,
    }
    return render(request,'account_receivable_list.html',context)


def account_receivable_add(request):
    """添加应收款项"""
    if request.method == "GET":
        form = AccountsReceivableModelForm()
        context = {
            'form':form,
            'title':'添加应收款'
        }
        return render(request,'rjd_add.html',context)
    form = AccountsReceivableModelForm(data=request.POST)
    if form.is_valid():
        form.instance.final_payment = form.instance.total_price - form.instance.paid
        form.save()
        return redirect('/rjd/account/receivable/list/')
    context = {
        'form':form,
        'title':"添加应收款项",
    }
    return render(request,'rjd_add.html',context)


def account_receivable_edit(request,nid):
    """编辑已付账单"""
    row_object = models.AccountsReceivable.objects.filter(id=nid).first()

    if request.method == "GET":
        form = AccountsReceivableModelForm(instance=row_object)
        context = {
            'form':form,
            'title':'编辑应收款',
        }
        return render(request,'rjd_add.html',context)
    form = AccountsReceivableModelForm(data=request.POST,instance=row_object)
    if form.is_valid():
        form.instance.final_payment = form.instance.total_price-form.instance.paid
        form.save()
        return redirect('/rjd/account/receivable/list/')
    context = {
        'form':form,
        'title':'编辑应收款',
    }
    return render(request,'rjd_add.html',context)


def account_receivable_delete(request,nid):
    """删除应收款"""
    models.AccountsReceivable.objects.filter(id=nid).delete()
    return redirect('/rjd/account/receivable/list/')
