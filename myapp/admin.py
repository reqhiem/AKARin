from django.contrib import admin
from .models import Documento
# Register your models here.

class DocumentoAdmin(admin.ModelAdmin):
    readonly_fields = ('loaded',)

admin.site.register(Documento, DocumentoAdmin)