from django.db import models
from users.models import User

# django-ckeditor
from ckeditor.fields import RichTextField

class Tipo(models.Model):
    """Tipo model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tipo')
    title = models.CharField(max_length=255)
    description = RichTextField(null=True)


    def __str__(self):
        """Return extra academic education and first_name and last_name."""
        return f'{self.user.first_name} {self.user.last_name} | {self.title}'