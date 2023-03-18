from django.contrib import admin

from .models import myModel
from .models import Phone

admin.site.register(myModel)

admin.site.register(Phone)


# Register your models here.
