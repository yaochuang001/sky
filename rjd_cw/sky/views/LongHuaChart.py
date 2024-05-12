from django.shortcuts import render, HttpResponse, redirect
from sky import models
from app_cw.utils.pagination import Pagination

def lh_chart(request):
    """龙华实时数据"""

    # 获取所有的数据表
    queryset = models.LhData.objects.all()

    page_object = Pagination(request, queryset, page_size=15)
    chanliang = models.LhData.objects.values('equipment_name',"equipment_status",'current_output','total_output','work_cycle')
    name = []
    current_op = []
    total_op = []
    work_cycle = []
    for item in chanliang:
        name.append(item['equipment_name'])
        current_op.append(item['current_output'])
        total_op.append(item['total_output'])
        work_cycle.append(item['work_cycle'])
    print(name)
    print(work_cycle)

    """

    for obj in queryset:
        print(obj.id,obj.name,obj.account,obj.create_time.strftime("%Y-%m-%d"),obj.gender,obj.get_gender_display(),obj.depart_id,obj.depart.title)

    """
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
        "time":'2022-10-11',
    }
    return render(request, 'lh_chart.html', context)


from app_cw.utils.bootstrap import BootStrapModelForm
class LhDataModelForm(BootStrapModelForm):

    class Meta:
        model = models.LhData
        fields = "__all__"


def lh_data_add(request):
    # 根据ID去数据库获取要编辑的那一行数据（对象）
    row_object = models.UserInfo.objects.filter().first()
    if request.method == "GET":
        form = LhDataModelForm(instance=row_object)
        return render(request, "user_edit.html", {'form': form})

    form = LhDataModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request, 'user_edit.html', {'form': form})
