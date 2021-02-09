from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Team(models.Model):
    people = models.ManyToManyField("User", through="TeamMember")

    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class TeamMember(models.Model):
    person = models.ForeignKey("User", models.CASCADE)
    team = models.ForeignKey("Team", models.CASCADE)

    def __str__(self) -> str:
        return f"{self.team} - {self.person}"


class TeamTree(models.Model):
    class Meta:
        unique_together = [["parent", "child"]]

    parent = models.ForeignKey("Team", models.CASCADE, related_name="parents")
    child = models.ForeignKey("Team", models.CASCADE, related_name="children")

    depth = models.SmallIntegerField()

    def __str__(self) -> str:
        return f"{self.parent} - {self.child} ({self.depth})"
