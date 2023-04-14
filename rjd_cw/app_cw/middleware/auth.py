from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class M1(MiddlewareMixin):
    """中间件1"""

    def process_request(self, request):
        # 如果方法中没有返回值（返回None)，继续往后走
        # 如果有返回值 HttpResponse render redirect
        print("1进来了")

    def process_response(self, request, response):
        print("1出去了")
        return response


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 0.排除那些不需要登陆就能访问的页面
        # request.path_info 获取当前用户请求的url
        if request.path_info in ["/login/", "/image/code/","/admin/add/","/yc/test/"]:
            return

        # 1.读取当前访问的用户的session信息，如果能读到，说明已登陆，就可以继续
        info_dict = request.session.get("info")
        if info_dict:
            return

        # 2.没有登陆，重新回到登陆页面
        return redirect('/login/')
