from django.db.models import Subquery, QuerySet

from peoplefinder.models import Team, TeamTree


class TeamService:
    def add_team(self, team: Team, parent: Team) -> None:
        """Add a team into the hierarchy.

        Args:
            team (Team): The team to be added.
            parent (Team): The parent team.
        """
        TeamTree.objects.bulk_create(
            [
                # reference to itself
                TeamTree(parent=team, child=team, depth=0),
                # all required tree connections
                *(
                    TeamTree(parent=tt.parent, child=team, depth=tt.depth + 1)
                    for tt in TeamTree.objects.filter(child=parent)
                ),
            ]
        )

    def get_all_child_teams(self, parent: Team) -> QuerySet:
        """Return all child teams of the given parent team.

        Args:
            parent (Team): The given parent team.

        Returns:
            QuerySet: A queryset of teams.
        """
        return Team.objects.filter(children__parent=parent).exclude(
            children__child=parent
        )

    def get_immediate_child_teams(self, parent: Team) -> QuerySet:
        """Return all immediate child teams of the given parent team.

        Args:
            parent (Team): The given parent team.

        Returns:
            QuerySet: A queryset of teams.
        """
        return Team.objects.filter(children__parent=parent, children__depth=1)

    def get_all_parent_teams(self, child: Team) -> QuerySet:
        """Return all parent teams for the given child team.

        Args:
            child (Team): The given child team.

        Returns:
            QuerySet: A query of teams.
        """
        return (
            Team.objects.filter(parents__child=child).exclude(parents__parent=child)
            # TODO: Not sure if we should order here or at the call sites.
            .order_by("-parents__depth")
        )

    def get_root_team(self) -> Team:
        """Return the root team.

        Returns:
            Team: The root team.
        """
        teams_with_parents = TeamTree.objects.filter(depth__gt=0)

        return Team.objects.exclude(
            id__in=Subquery(teams_with_parents.values("child"))
        ).get()
