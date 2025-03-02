# core/models.py
from django.db import models

class QRCode(models.Model):
    OPERATOR_CHOICES = (
        ('mixx', 'MixxByYas'),
        ('moov', 'Moov Money Flooz'),
    )
    
    operator = models.CharField(max_length=10, choices=OPERATOR_CHOICES)
    qr_image = models.ImageField(upload_to='qrcodes/')
    created_at = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()  # Stocke les données encodées dans le QR code
    
    def __str__(self):
        return f"{self.operator} QR Code - {self.created_at}"