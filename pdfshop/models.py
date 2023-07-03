from django.db import models

class RevisionPDF(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # Add more fields as per your requirements
