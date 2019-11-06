from django.contrib import admin
from .models import Question

# Register your models here.
# Para que el administrador considere este modelo 
admin.site.register(Question)