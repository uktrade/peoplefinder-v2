from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from peoplefinder.models import User
from peoplefinder.services.team import TeamService


class ProfileDetailView(DetailView):
    model = User
    context_object_name = "profile"
    template_name = "peoplefinder/profile.html"

    def get_context_data(self, **kwargs: dict) -> dict:
        context = super().get_context_data(**kwargs)

        profile = context["profile"]
        # TODO: What if a user is in multiple teams?
        team = profile.teams.first()

        context["team"] = team
        # TODO: `parent_teams` is common to all views. Perhaps we should
        # refactor this into a common base view or mixin?
        context["parent_teams"] = TeamService().get_all_parent_teams(team)

        return context


class ProfileEditView(UserPassesTestMixin, UpdateView):
    model = User
    template_name = "peoplefinder/profile-edit.html"
    fields = ["email", "manager", "do_not_work_for_dit"]

    def test_func(self) -> bool:
        # The profile must be that of the logged in user.
        return self.get_object() == self.request.user
