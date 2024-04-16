from django.urls import path
from . import views
from django.conf.urls import url
from ..bot import StartView, AuthorCommandView

urlpatterns = [
    path('', views.index, name='index'),
    path('admins/', views.admins, name='admins'),
    path('admins/delete/<int:admin_id>/', views.admins_delete,
         name='admins_delete'),
    path('admins/edit/<int:admin_id>/', views.admins_edit, name='admins_edit'),
    path('toggle_a_access/<int:admin_id>/', views.toggle_a_access, name='toggle_a_access'),
    path('orders/', views.orders, name='orders'),
    path('orders/delete/<int:order_id>/', views.orders_delete,
         name='orders_delete'),
    path('orders/edit/<int:order_id>/', views.orders_edit,
         name = 'orders_edit'),
    path('toggle_o_status/<int:order_id>/', views.toggle_o_status, name='toggle_o_status'),
    path('defects/', views.defects, name='defects'),
    path('defects/delete/<int:defect_id>/', views.defects_delete,
         name = 'defects_delete'),
    path('defects/edit/<int:defect_id>/', views.defects_edit,
         name = 'defects_edit'),
    path('toggle_d_status/<int:defect_id>/', views.toggle_d_status, name='toggle_d_status'),
    path('users/', views.users, name='users'),
    path('users/delete/<int:user_id>/', views.users_delete,
         name='users_delete'),
    path('users/edit/<int:user_id>/', views.users_edit, name = 'users_edit'),
    path('toggle_u_access/<int:user_id>/', views.toggle_u_access, name='toggle_u_access'),
    path('set_webhook/', views.set_webhook, name='set_webhook'),
    url(r'^start/$', StartView.as_command_view(), name = 'start'),
    url(r'^author/$', AuthorCommandView.as_command_view(), name = 'author'),
]
