from dataclasses import field, fields
from typing import ItemsView
from django.contrib import admin
from .models import Event, Item

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display  = ('id', 'slug', 'author','created')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id','description')

