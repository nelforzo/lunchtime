from django.db import models

class Lunch(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)      # Automatically set on update
    deleted_at = models.DateTimeField(null=True, blank=True)  # Nullable for soft deletion

    class Meta:
        db_table = 'lunches'