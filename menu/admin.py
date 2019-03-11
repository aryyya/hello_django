from . import models
from django.contrib import admin

admin_models = [
    models.Category,
    models.TeaItem,
    models.FoodItem,
    models.Grower,
    models.Origin
]

for model in admin_models:
    admin.site.register(model)
