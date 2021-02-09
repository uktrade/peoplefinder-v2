from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from peoplefinder.models import User, Team, TeamMember, TeamTree


admin.site.register(User, UserAdmin)
admin.site.register(Team, admin.ModelAdmin)
admin.site.register(TeamMember, admin.ModelAdmin)
admin.site.register(TeamTree, admin.ModelAdmin)
