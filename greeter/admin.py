from django.contrib import admin
from .models import Pizza, Topping, Musician, Member, Band

admin_models = [
    Pizza,
    Topping,
    Musician,
    Member,
    Band
]

for model in admin_models:
    admin.site.register(model)
