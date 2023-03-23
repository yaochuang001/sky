from django.shortcuts import render, redirect
from app_cw import models
from app_cw.utils.bootstrap import BootStrapModelForm


def city_list(request):
    """城市列表"""
    queryset = models.City.objects.all()
    return render(request, 'city_list.html', {'queryset': queryset})


class UpModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ['img']

    class Meta:
        model = models.City
        fields = "__all__"


def city_add(request):
    """新建城市"""
    title = "新建城市"

    if request.method == "GET":
        form = UpModelForm()
        return render(request, 'upload_form.html', {'form': form, 'title': title})

    form = UpModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/city/list/')

    return render(request, 'upload_form.html', {'form': form, 'title': title})
