from django.contrib import admin
from .models import Pizza, Topping

admin_models = [
    Pizza,
    Topping
]

for model in admin_models:
    admin.site.register(model)
