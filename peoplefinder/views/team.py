from django.db.models import Q
from django.views.generic.detail import DetailView

from peoplefinder.models import Team, User
from peoplefinder.services.team import TeamService


# TODO: Potential to refactor for the common parts.


class TeamDetailView(DetailView):
    model = Team
    context_object_name = "team"
    template_name = "peoplefinder/team.html"

    def get_context_data(self, **kwargs: dict) -> dict:
        context = super().get_context_data(**kwargs)

        team = context["team"]
        team_service = TeamService()

        context["parent_teams"] = team_service.get_all_parent_teams(team)
        context["sub_teams"] = team_service.get_immediate_child_teams(team)

        # Must be a leaf team.
        if not context["sub_teams"]:
            context["people"] = User.objects.filter(teams=team)

        return context


class TeamTreeView(DetailView):
    model = Team
    context_object_name = "team"
    template_name = "peoplefinder/team-tree.html"

    def get_context_data(self, **kwargs: dict) -> dict:
        context = super().get_context_data(**kwargs)

        team = context["team"]
        team_service = TeamService()

        context["parent_teams"] = team_service.get_all_parent_teams(team)

        return context


class TeamPeopleView(DetailView):
    model = Team
    context_object_name = "team"
    template_name = "peoplefinder/team-people.html"

    def get_context_data(self, **kwargs: dict) -> dict:
        context = super().get_context_data(**kwargs)

        team = context["team"]
        team_service = TeamService()

        context["parent_teams"] = team_service.get_all_parent_teams(team)
        context["sub_teams"] = team_service.get_all_child_teams(team)
        context["people"] = User.objects.filter(
            Q(teams=team) | Q(teams__in=context["sub_teams"])
        )

        return context
