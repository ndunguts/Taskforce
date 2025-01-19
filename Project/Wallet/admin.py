from django.contrib import admin
from .models import Budget,income,outcome,accounts


# Register your models here.
admin.site.register(Budget)
admin.site.register(income)
admin.site.register(outcome)
admin.site.register(accounts)