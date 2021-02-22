from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    manager = models.ForeignKey(
        "User", models.SET_NULL, null=True, blank=True, related_name="+"
    )

    do_not_work_for_dit = models.BooleanField(default=False)

    def get_absolute_url(self) -> str:
        return reverse("profile-view", kwargs={"pk": self.pk})


class Team(models.Model):
    people = models.ManyToManyField("User", through="TeamMember", related_name="teams")

    name = models.CharField(max_length=255, unique=True)
    abbreviation = models.CharField(max_length=10, null=True, blank=True)
    slug = models.SlugField(max_length=100)

    def __str__(self) -> str:
        return self.short_name

    @property
    def short_name(self) -> str:
        """Return a short name for the team.

        Returns:
            str: The team's short name.
        """
        return self.abbreviation or self.name


class TeamMember(models.Model):
    person = models.ForeignKey("User", models.CASCADE)
    team = models.ForeignKey("Team", models.CASCADE)

    job_title = models.CharField(max_length=100)
    head_of_team = models.BooleanField(default=False)

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
