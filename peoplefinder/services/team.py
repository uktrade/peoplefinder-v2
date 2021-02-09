from django.db.models import QuerySet

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
