from django.db import models
from djrichtextfield.models import RichTextField

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    """ Game review model """
    user = models.ForeignKey(
        User, related_name="review_user", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=250, null=False, blank=False)
    game_name = models.CharField(max_length=150, null=False, blank=False)
    content = RichTextField(max_length=10000, null=False, blank=False)
    image = models.ImageField(upload_to="reviews/", null=False, blank=False)
    review_date = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(
        default=1, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    class Meta:
        ordering = ["-review_date"]

    def __str__(self):
        return str(self.title)
