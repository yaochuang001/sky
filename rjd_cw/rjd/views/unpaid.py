from django.shortcuts import render, redirect
from rjd.form.form import *
from app_cw.utils.pagination import Pagination
import datetime


def unpaid_list(request):
    """未付表单"""
    now_time = datetime.datetime.now()
    data_dict = {}
    # 数据收集
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["supplier__contains"] = search_data
    queryset = models.Unpaid.objects.filter(**data_dict).order_by('-id')

    page_object = Pagination(request, queryset)
    context = {
        'queryset': page_object.page_queryset,
        'search_data': search_data,
        'page_string': page_object.html(),
    }
    return render(request, 'unpaid_list.html', context)


def unpaid_add(request):
    """添加未付款项目"""
    if request.method == "GET":
        form = UnpaidModelForm()
        context = {
            'form': form,
            'title': '添加未付款'
        }
        return render(request, 'rjd_add.html', context)
    form = UnpaidModelForm(data=request.POST)
    if form.is_valid():
        form.instance.final_payment = form.instance.total_price - form.instance.paid
        form.save()
        return redirect('/rjd/unpaid/list/')
    context = {
        'form': form,
        'title': "添加未付款",
    }
    return render(request, 'rjd_add.html', context)


def unpaid_edit(request, nid):
    """编辑未付账单"""
    row_object = models.Unpaid.objects.filter(id=nid).first()

    if request.method == "GET":
        form = UnpaidModelForm(instance=row_object)
        context = {
            'form': form,
            'title': '编辑未付款',
        }
        return render(request, 'rjd_add.html', context)
    form = UnpaidModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.instance.final_payment = form.instance.total_price - form.instance.paid
        form.save()
        return redirect('/rjd/unpaid/list/')
    context = {
        'form': form,
        'title': '编辑未付款',
    }
    return render(request, 'rjd_add.html', context)


def unpaid_delete(request, nid):
    """删除未付账目"""
    models.Unpaid.objects.filter(id=nid).delete()
    return redirect('/rjd/unpaid/list/')
