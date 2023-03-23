from django.shortcuts import render, redirect
from app_cw.utils.pagination import Pagination
from app_cw.form.form import *


def pretty_list(request):
    """靓号列表"""
    # for i in range(300):
    #     models.PrettyNum.objects.create(mobile="13713642364", price=1888, level=1, status=1, )
    # # 条件筛选
    # data_dict = {"mobile":"19999999991", "id":123}
    # models.PrettyNum.objects.filter(**data_dict)
    #
    # # 等于12
    # models.PrettyNum.objects.filter(id=12)
    # # 大于12
    # models.PrettyNum.objects.filter(id__gt=12)
    # # 大于等于12
    # models.PrettyNum.objects.filter(id__gte=12)
    # # 小于12
    # models.PrettyNum.objects.filter(id__lt=12)
    # # 小于等于12
    # models.PrettyNum.objects.filter(id__lte=12)
    #
    # # 等于
    # models.PrettyNum.objects.filter(mobile="999")
    # # 筛选出以1999开头
    # models.PrettyNum.objects.filter(mobile__startswith="1999")
    # # 筛选出以999结尾
    # models.PrettyNum.objects.filter(mobile__endswith="999")
    # # 筛选包含999
    # models.PrettyNum.objects.filter(mobile__contains="999")
    data_dict = {}
    # 收据搜索
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["mobile__contains"] = search_data
    queryset = models.PrettyNum.objects.filter(**data_dict).order_by("-level")

    page_object = Pagination(request, queryset)
    context = {
        'queryset': page_object.page_queryset,  # 分页数据
        'search_data': search_data,
        'page_string': page_object.html()  # 分页信息
    }

    return render(request, 'pretty_list.html', context)


def pretty_add(request):
    """添加靓号"""
    if request.method == "GET":
        form = PrettyModelForm()
        return render(request, 'pretty_add.html', {'form': form})
    form = PrettyModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/pretty/list/')
    return render(request, 'pretty_add.html', {'form': form})


def pretty_edit(request, nid):
    """编辑靓号"""
    row_object = models.PrettyNum.objects.filter(id=nid).first()

    if request.method == "GET":
        form = PrettyEditModelForm(instance=row_object)
        return render(request, 'pretty_edit.html', {"form": form})

    form = PrettyEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/pretty/list/')

    return render(request, 'pretty_edit.html', {"form": form})


def pretty_delete(request, nid):
    """删除靓号"""
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect('/pretty/list/')