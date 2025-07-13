from django.db import models
from django.contrib.auth.models import User

# ----------------------------------------
# Product Model
# ----------------------------------------
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return round(sum([r.rating for r in reviews]) / reviews.count(), 2)
        return 0

    def __str__(self):
        return self.name

# ----------------------------------------
# Review Model
# ----------------------------------------
class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField()
    feedback = models.TextField()

    class Meta:
        unique_together = ('product', 'user')  # One review per user per product

    def __str__(self):
        return f"{self.user.username} → {self.product.name}"
