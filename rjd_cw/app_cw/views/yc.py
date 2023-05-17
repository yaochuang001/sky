from django.shortcuts import redirect
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from sky import models

@csrf_exempt
def yc_test(request):
    src = request.body
    print('**************')
    print(src.decode('utf-8'))
    a = eval(src.decode('utf-8'))
    print(type(a))
    row_object = models.LhWorkStatus.objects.first()
    print(row_object)
    return HttpResponse('nidaye')

def yc_admin(request):
    if request.session['info']['name'] == "Admin":

        return redirect('/rjd/account/pub/list/')
    else:
        return redirect('/sky/dg/chart/')