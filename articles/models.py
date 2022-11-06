from django.db import models


class Article(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.text[:15]