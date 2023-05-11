from django.urls import path
from rjd.views import supplier, custom, account_pub, account_pri, unpaid, accounts_receivable

urlpatterns = [
    # 供应商表
    path('supplier/list/', supplier.supplier_list),
    path('supplier/add/', supplier.supplier_add),
    path('supplier/<int:nid>/edit/', supplier.supplier_edit),
    path('supplier/<int:nid>/delete/', supplier.supplier_delete),

    # 客户列表
    path('custom/list/', custom.custom_list),
    path('custom/add/', custom.custom_add),
    path('custom/<int:nid>/edit/', custom.custom_edit),
    path('custom/<int:nid>/delete/', custom.custom_delete),

    # 对公账目表
    path('account/pub/list/', account_pub.account_pub_list),
    path('account/pub/add/', account_pub.account_pub_add),
    path('account/pub/<int:nid>/edit/', account_pub.account_pub_edit),
    path('account/pub/<int:nid>/delete/', account_pub.account_pub_delete),
    path('account_pub/multi/', account_pub.account_pub_multi),

    # 对私账目表
    path('account/pri/list/', account_pri.account_pri_list),
    path('account/pri/add/', account_pri.account_pri_add),
    path('account/pri/<int:nid>/edit/', account_pri.account_pri_edit),
    path('account/pri/<int:nid>/delete/', account_pri.account_pri_delete),
    path('account_pri/multi/', account_pri.account_pri_multi),

    # 未付款账目表
    path('unpaid/list/', unpaid.unpaid_list),
    path('unpaid/add/', unpaid.unpaid_add),
    path('unpaid/<int:nid>/edit/', unpaid.unpaid_edit),
    path('unpaid/<int:nid>/delete/', unpaid.unpaid_delete),

    # 未付款账目表
    path('account/receivable/list/', accounts_receivable.account_receivable_list),
    path('account/receivable/add/', accounts_receivable.account_receivable_add),
    path('account/receivable/<int:nid>/edit/', accounts_receivable.account_receivable_edit),
    path('account/receivable/<int:nid>/delete/', accounts_receivable.account_receivable_delete),
]
