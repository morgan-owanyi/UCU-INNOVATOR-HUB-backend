from django.db import models
from projects.models import Project

class Analytics(models.Model):
    # Optional: Precomputed metrics
    faculty = models.CharField(max_length=100)
    total_projects = models.IntegerField(default=0)
    approved_projects = models.IntegerField(default=0)
    pending_projects = models.IntegerField(default=0)
    rejected_projects = models.IntegerField(default=0)
    trending_technologies = models.TextField(blank=True, null=True)  # Could store JSON

    def __str__(self):
        return f"Analytics for {self.faculty}"
