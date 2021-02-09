from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponse

from peoplefinder.services.team import TeamService


def home(request: HttpRequest) -> HttpResponse:
    root_team = TeamService().get_root_team()

    return redirect(f"/teams/{root_team.slug}")
