from django.db import models

from django.urls import reverse


class Post(models.Model):
    user = models.ForeignKey(
    "auth.User",
    on_delete=models.CASCADE,
    )
    question = models.CharField(max_length=200)
    answer = models.TextField()
    created_at = models.DateField()
    update_at = models.DateField()
    def __str__(self):
        return self.question
    def get_absolute_url(self):
        return reverse("post_jokes", kwargs={"pk": self.pk})
