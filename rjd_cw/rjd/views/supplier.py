from django.shortcuts import render, redirect
from rjd.form.form import *
from app_cw.utils.pagination import Pagination


def supplier_list(request):
    """供应商列表"""
    data_dict = {}
    # 数据收集
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["supplier_name__contains"] = search_data
    queryset = models.Supplier.objects.filter(**data_dict).order_by("-id")

    page_object = Pagination(request, queryset)
    context = {
        'queryset': page_object.page_queryset,
        'search_data': search_data,
        'page_string': page_object.html(),
    }
    return render(request, 'supplier_list.html', context)


def supplier_add(request):
    """添加供应商"""
    if request.method == "GET":
        form = SupplierModelForm()
        context = {
            'form': form,
            'title': '新建供应商',
        }
        return render(request, 'rjd_add.html', context)
    form = SupplierModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/rjd/supplier/list/')
    context = {
        'form': form,
        'title': '新建供应商',
    }
    return render(request, 'rjd_add.html', context)


def supplier_edit(request, nid):
    """编辑供应商信息"""
    row_object = models.Supplier.objects.filter(id=nid).first()

    if request.method == "GET":
        form = SupplierModelForm(instance=row_object)
        context = {
            'form': form,
            'title': '编辑供应商',
        }
        return render(request, 'rjd_add.html', context)
    form = SupplierModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/rjd/supplier/list/')
    context = {
        'form': form,
        'title': '编辑供应商',
    }
    return render(request, 'rjd_add.html', context)


def supplier_delete(request,nid):
    """删除供应商"""
    models.Supplier.objects.filter(id=nid).delete()
    return redirect('/rjd/supplier/list/')
