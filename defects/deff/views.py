from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Admin, Defect, Order, User
def index(request):
    return render(request, 'index.html')

def admins(request):
    data = Admin.objects.all()
    return render(request, 'admins.html', {'data': data})

def admins_delete(request, admin_id):
     admin = get_object_or_404(Admin, id_admin=admin_id)

     if request.method == 'POST':
         admin.delete()
         return redirect('admins')
     return redirect('admins')
def admins_edit(request):
    return render(request, 'admins-edit.html')

def admins_edit(request, admin_id):
    admin = get_object_or_404(Admin, id_admin=admin_id)
    if request.method == 'POST':
        admin.a_username = request.POST.get('a_username')
        admin.a_name = request.POST.get('a_name')
        admin.a_access = request.POST.get('a_access') == 'on'
        admin.save()
        return redirect('admins')
    return render(request, 'admins-edit.html', {'admin': admin})

def toggle_a_access(request, admin_id):
    admin = get_object_or_404(Admin, id_admin=admin_id)
    if admin.a_access != True:
       admin.a_access = True
    admin.save()
    return redirect('admins')

def orders(request):
    data = Order.objects.all()
    return render(request, 'orders.html', {'data': data})

def orders_delete(request, order_id):
    order = get_object_or_404(Order, id_order = order_id)

    if request.method == 'POST':
        order.delete()
        return redirect('orders')

    return redirect('orders')

def orders_edit(request, order_id):
    order = get_object_or_404(Order, id_order=order_id)
    if request.method == 'POST':
        order.o_guest_name = request.POST.get('o_guest_name')
        order.o_item_ordered = request.POST.get('o_item_ordered')
        order.o_room_number = request.POST.get('o_room_number')
        order.o_quantity = request.POST.get('o_quantity')
        order.o_status = request.POST.get('o_status')
        order.save()
        return redirect('orders')
    return render(request, 'orders-edit.html', {'order': order})

def toggle_o_status(request, order_id):
    order = get_object_or_404(Order, id_order=order_id)
    if order.o_status != 'Виконано':
       order.o_status = 'Виконано'
    order.save()
    return redirect('orders')

def defects(request):
    data = Defect.objects.all()
    return render(request, 'defects.html', {'data': data})

def defects_delete(request, defect_id):
    defect = get_object_or_404(Defect, id_defect = defect_id)

    if request.method == 'POST':
        defect.delete()
        return redirect('defects')

    return redirect('defects')

def defects_edit(request, defect_id):
    defect = Defect.objects.get(id_defect = defect_id)
    users = User.objects.all()

    if request.method == 'POST':
        defect.d_room_number = request.POST.get('d_room_number')
        defect.d_defect_type = request.POST.get('d_defect_type')
        defect.d_description = request.POST.get('d_description')
        defect.d_status = request.POST.get('d_status')

        # Змінюємо тільки користувача, який повідомив про дефект, якщо він не null
        reported_by_id = request.POST.get('d_reported_by')
        if reported_by_id:
            defect.d_reported_by_id = reported_by_id

        defect.save()
        return redirect('defects')

    return render(request, 'defects-edit.html',
                  {'defect': defect, 'users': users})

def toggle_d_status(request, defect_id):
    defect = get_object_or_404(Defect, id_defect=defect_id)
    if defect.d_status != 'Виконано':
        defect.d_status = 'Виконано'
    defect.save()
    return redirect('defects')

def users(request):
    data = User.objects.all()
    return render(request, 'users.html', {'data': data})


def users_delete(request, user_id):
    user = get_object_or_404(User, id_user = user_id)

    if request.method == 'POST':
        user.delete()
        return redirect('users')

    return redirect('users')

def users_edit(request, user_id):
    user = get_object_or_404(User, id_user=user_id)
    if request.method == 'POST':
        user.u_username = request.POST.get('u_username')
        user.u_name = request.POST.get('u_name')
        user.u_role = request.POST.get('u_role')
        user.u_access = request.POST.get('u_access') == 'on' 
        user.save()
        return redirect('users')
    return render(request, 'users-edit.html', {'user': user})

def toggle_u_access(request, user_id):
    user = get_object_or_404(User, id_user=user_id)
    if user.u_access != True:
       user.u_access = True
    user.save()
    return redirect('users')

# Telegram

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from telegrambot.models import TelegramBot

@csrf_exempt
@require_POST
def set_webhook(request):
    bot = TelegramBot.objects.get(pk=1)  # встановіть відповідний pk
    if bot.enabled:
        bot.set_webhook()  # Реалізуйте метод встановлення вебхука у вашій моделі
        return JsonResponse({'message': 'Webhook set successfully'})
    else:
        return JsonResponse({'message': 'Bot is not enabled, please enable it first'})

