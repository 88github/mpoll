from django.contrib import admin
from mysite import models
# Register your models here.

class PollAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'created_at', 'enabled')
    ordering = ('-created_at',)

class PollItemAdmin(admin.ModelAdmin):
    list_display = ('poll', 'name', 'image_url', 'vote')
    ordering = ('poll',)

class VoteCheckAdmin(admin.ModelAdmin):
        list_display = ('userid', 'pollid', 'pollitemid', 'vote_date')
        ordering = ('-vote_date', )

admin.site.register(models.Poll, PollAdmin)
admin.site.register(models.Pollitem, PollItemAdmin)
admin.site.register(models.VoteCheck, VoteCheckAdmin)