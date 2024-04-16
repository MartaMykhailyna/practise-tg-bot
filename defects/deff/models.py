from django.db import models
from enum import Enum

class Status(Enum):
    accepted = 'Прийнято'
    completed = 'Виконано'
    in_progress = 'В обробці'
    rejected = 'Відхилено'

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    u_username = models.CharField(max_length=45, unique=True)
    u_name = models.CharField(max_length=45)
    u_role = models.CharField(max_length=45)
    u_access = models.BooleanField(default = False)

    class Meta:
        db_table = 'users'
        managed = False

class Admin(models.Model):
    id_admin = models.AutoField(primary_key=True, default=1)
    a_username = models.CharField(max_length=45, unique=True)
    a_name = models.CharField(max_length=45)
    a_access = models.BooleanField(default = False)

    class Meta:
        db_table = 'admins'  # Вказати ім'я таблиці в базі даних

class Defect(models.Model):
    id_defect = models.AutoField(primary_key=True)
    d_room_number = models.IntegerField()
    d_defect_type = models.CharField(max_length=45)
    d_description = models.CharField(max_length=245, null=True, blank=True)
    d_date_reported = models.DateTimeField(auto_now_add=True)
    d_status = models.CharField(max_length=45, choices=[(status.value, status.name) for status in Status], null = True)
    d_reported_by = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, db_column='d_reported_by')
    def __str__(self):
        return f"{self.d_defect_type} - {self.d_status}"
    class Meta:
        db_table = 'defects'  # Вказати ім'я таблиці в базі даних

class Order(models.Model):
    id_order = models.AutoField(primary_key=True, default=1)
    o_room_number = models.IntegerField()
    o_guest_name = models.CharField(max_length=45)
    o_item_ordered = models.CharField(max_length=45)
    o_quantity = models.IntegerField()
    o_order_date = models.DateTimeField(auto_now_add=True)
    o_status = models.CharField(max_length=45, choices=[(status.value, status.name) for status in Status])

    class Meta:
        db_table = 'orders'  # Вказати ім'я таблиці в базі даних

# Telegram

from django.db import models

class TelegramBot(models.Model):
    token = models.CharField(max_length=100)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.token
