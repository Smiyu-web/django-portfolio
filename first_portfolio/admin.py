from django.contrib import admin
from .models import Work
from .models import Blog

admin.site.site_header = "Portfolio"
# Register your models here.
admin.site.register(Work)
admin.site.register(Blog)

