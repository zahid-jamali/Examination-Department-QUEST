from django.contrib import admin
from .models import msgs, news, faq, circular, photos, messages, faculty, Category, Apply_for, Registeration, downloads, examination_system
# Register your models here.
admin.site.register(msgs)
admin.site.register(news)
admin.site.register(circular)
admin.site.register(photos)
admin.site.register(messages)
admin.site.register(faculty)
admin.site.register(Category)
admin.site.register(Apply_for)
admin.site.register(Registeration)
admin.site.register(downloads)
admin.site.register(examination_system)
admin.site.register(faq)