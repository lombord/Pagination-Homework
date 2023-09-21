from django.db import models
from django.urls import reverse


class Language(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


STATUSES = [
    ('junior', 'Junior'),
    ('middle', 'Middle'),
    ('senior', 'Senior'),
]


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    languages = models.ManyToManyField(Language, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=255, choices=STATUSES, default='junior')
    description = models.TextField(blank=True, null=True)
    salary = models.DecimalField(max_digits=15, decimal_places=0)

    class Meta:
        ordering = "-id",

    def get_absolute_url(self):
        return reverse("vacancy", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.title}-{self.salary}$"
