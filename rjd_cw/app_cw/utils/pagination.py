"""
自定义的分页组件，以后如果想要使用分页组件，需要做以下几件事
在视图函数中：
    def pretty_list(request):
        # 1根据自己的情况去筛选自己的数据
        queryset = models.PrettyNum.objects.filter(**data_dict).order_by("-level")
        # 2实例化分页对象
        page_object = Pagination(request, queryset)
        context = {
            'queryset': page_object.page_queryset,  # 分页完数据
            'page_string': page_object.html()  # 生成页码
            }
        return render(request, 'pretty_list.html', context)
在HTML页面中：
    {% for obj in queryset %}
    <tr>
        <th scope="row">{{ obj.id }}</th>
        <td>{{ obj.mobile }}</td>
        <td>{{ obj.price }}</td>
        <td>{{ obj.get_level_display }}</td>
        <td>{{ obj.get_status_display }}</td>

        <td>
            <a class="btn btn-primary btn-xs" href="/pretty/{{ obj.id }}/edit/">编辑</a>
            <a class="btn btn-danger btn-xs" href="/pretty/{{ obj.id }}/delete/">删除</a>
        </td>
    </tr>
    {% endfor %}

    <ul class="pagination">
        {{ page_string }}
    </ul>
"""
from django.utils.safestring import mark_safe


class Pagination(object):

    def __init__(self, request, queryset, page_size=30, page_param="page", plus=5):
        """
        :param request: 请求的对象
        :param queryset: 符合条件的数据（根据这个数据进行分页处理）
        :param page_size: 每页显示多少条数据
        :param page_param: 在URL总传递的获取分页的参数（exp：/pretty/list/?page=12）
        :param plus: 显示当前页的前和后几页
        """
        from django.http.request import QueryDict
        import copy
        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict
        self.page_param = page_param

        page = request.GET.get(page_param, "1")
        if page.isdecimal():
            page = int(page)
        else:
            page = 1
        self.page = page
        self.page_size = page_size

        self.start = (page - 1) * page_size
        self.end = page * page_size

        self.page_queryset = queryset[self.start:self.end]

        # 数据总条数
        total_count = queryset.count()

        # 总页码
        total_page_count, div = divmod(total_count, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.plus = plus

    def html(self):
        # 计算初，显示当前页的前5页、后五页
        if self.total_page_count <= 2 * self.plus + 1:
            # 数据库数据小于11页
            start_page = 1
            end_page = self.total_page_count
        else:
            # 当前页<5时
            if self.page <= self.plus:
                start_page = 1
                end_page = 2 * self.plus + 1
            else:
                # 当前页>5时候
                if (self.page + self.plus) > self.total_page_count:
                    start_page = self.total_page_count - 2 * self.plus
                    end_page = self.total_page_count
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus + 1

        # 页码
        page_str_list = []

        # 首页
        self.query_dict.setlist(self.page_param, [1])
        page_str_list.append('<li><a href="?{}">首页</a></li>'.format(self.query_dict.urlencode()))

        # 上一页
        if self.page > 1:
            self.query_dict.setlist(self.page_param, [self.page - 1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(prev)

        # 页面
        for i in range(start_page, end_page + 1):
            self.query_dict.setlist(self.page_param, [i])
            if i == self.page:
                ele = '<li class="active"><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            else:
                ele = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            page_str_list.append(ele)

        # 下一页
        if self.page < self.total_page_count:
            self.query_dict.setlist(self.page_param, [self.page + 1])
            prev = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [self.total_page_count])
            prev = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(prev)

        # 尾页
        self.query_dict.setlist(self.page_param, [self.total_page_count])
        page_str_list.append('<li><a href="?{}">尾页</a></li>'.format(self.query_dict.urlencode()))

        search_string = """
            <li>
                <form style="float: left; margin-left: -1px" method="get">
                    <div class="input-group" style="width:110px">
                        <input type="text" class="form-control" placeholder="页码" name="page">
                        <span class="input-group-btn">
                            <button class="btn btn-default" type="submit">跳转</button>
                        </span>
                    </div>
                </form>
            </li>
        """
        page_str_list.append(search_string)

        page_string = mark_safe("".join(page_str_list))
        return page_string
