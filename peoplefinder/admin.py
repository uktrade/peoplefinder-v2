from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from peoplefinder.forms import TeamModelForm
from peoplefinder.models import Team, TeamMember, User
from peoplefinder.services.team import TeamService


class TeamModelAdmin(admin.ModelAdmin):
    """Admin page for the Team model."""

    form = TeamModelForm

    def save_model(self, request, obj, form, change):  # type: ignore
        """Save the model and update the team hierarchy."""
        super().save_model(request, obj, form, change)

        team_service = TeamService()

        current_parent_team = team_service.get_immediate_parent_team(obj)
        new_parent_team = form.cleaned_data["parent_team"]

        if current_parent_team != new_parent_team:
            if change:
                team_service.update_team_parent(obj, new_parent_team)
            else:
                team_service.add_team(obj, new_parent_team)


admin.site.register(User, UserAdmin)
admin.site.register(Team, TeamModelAdmin)
admin.site.register(TeamMember, admin.ModelAdmin)
