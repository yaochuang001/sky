from django.shortcuts import render, redirect
from rjd.form.form import *
from app_cw.utils.pagination import Pagination


def custom_list(request):
    """客户列表"""
    data_dict = {}
    # 数据收集
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["company_name__contains"] = search_data
    queryset = models.CustomInfo.objects.filter(**data_dict).order_by("-id")

    page_object = Pagination(request, queryset)
    context = {
        'queryset': page_object.page_queryset,  # 分页数据
        'search_data': search_data,
        'page_string': page_object.html(),  # 分页信息
    }
    return render(request, 'custom_list.html', context)


def custom_add(request):
    """添加客户"""
    if request.method == "GET":
        form = CustomModelForm()
        context = {
            'form': form,
            'title': '新建客户',
        }
        return render(request, 'rjd_add.html', context)
    form = CustomModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/rjd/custom/list/')
    context = {
        'form': form,
        'title': '新建客户',
    }
    return render(request, 'rjd_add.html', context)


def custom_edit(request, nid):
    """编辑客户信息"""
    row_object = models.CustomInfo.objects.filter(id=nid).first()

    if request.method == "GET":
        form = CustomModelForm(instance=row_object)
        context = {
            'form': form,
            'title': '编辑客户'
        }
        return render(request, 'rjd_add.html', context)
    form = CustomModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/rjd/custom/list/')
    context = {
        'form': form,
        'title': '编辑客户',
    }
    return render(request, 'rjd_add.html', context)


def custom_delete(request,nid):
    """删除客户"""
    models.CustomInfo.objects.filter(id=nid).delete()
    return redirect('/rjd/custom/list/')
