from django.views.generic.detail import DetailView

from peoplefinder.models import User
from peoplefinder.services.team import TeamService


class ProfileDetailView(DetailView):
    model = User
    context_object_name = "user"
    template_name = "peoplefinder/profile.html"

    def get_context_data(self, **kwargs: dict) -> dict:
        context = super().get_context_data(**kwargs)

        user = context["user"]
        # TODO: What if a user is in multiple teams?
        team = user.teams.first()

        context["team"] = team
        # TODO: `parent_teams` is common to all views. Perhaps we should
        # refactor this into a common base view or mixin?
        context["parent_teams"] = TeamService().get_all_parent_teams(team)

        return context
