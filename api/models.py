from django.db import models


class Task(models.Model):
    task = models.CharField(max_length=255)
    done = models.BooleanField(null=False, default=False)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.task
