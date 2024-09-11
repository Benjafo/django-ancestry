from django.contrib import admin

# Register your models here.
from .models import Event, Source, Tree, Person

admin.site.register(Event)
admin.site.register(Source)
admin.site.register(Tree)
admin.site.register(Person)