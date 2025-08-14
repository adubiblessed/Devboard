from django.db import models
from django.conf import settings
from datetime import date, timedelta
from django.utils import timezone

class Streak(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="streak"
    )
    streak_count = models.PositiveIntegerField(default=0)
    last_activity = models.DateField(null=True, blank=True, default=timezone.now)
    start_date = models.DateField(default=timezone.now)

    def update_streak(self):
        today = date.today()

        # First-time streak
        if not self.last_activity:
            self.streak_count = 1
            self.last_activity = today

        else:
            delta = today - self.last_activity

            if delta.days == 1:
                # Consecutive day → increment streak
                self.streak_count += 1
                self.last_activity = today

            elif delta.days > 1:
                # Missed at least one day → reset streak
                self.streak_count = 1
                self.last_activity = today
            else:
                # Same day → do nothing
                pass

        self.save()

    def __str__(self):
        return f"{self.user.username} — {self.streak_count} days"
