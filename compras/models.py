from django.db import models
from users.models import User

# django-ckeditor
from ckeditor.fields import RichTextField

class Marca(models.Model):
    """Marca model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Marca')
    title = models.CharField(max_length=255)
    description = RichTextField(null=True)


    def __str__(self):
        """Return Marca academic education and first_name and last_name."""
        return f'{self.user.first_name} {self.user.last_name} | {self.title}'