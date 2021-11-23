from django.contrib import admin
from .models import Pin,PinCategory,Note,Section

# Register your models here.
admin.site.register(Pin)
admin.site.register(PinCategory)
admin.site.register(Note)
admin.site.register(Section)
