
from django.db import models

class Certificate(models.Model):
    recipient_name = models.CharField(max_length=100)
    certificate_id = models.CharField(max_length=8, unique=True)

    class Meta:
        permissions = [
            ('can_generate_certificate', 'Can generate certificate'),  # Permission for generating certificate
            ('can_view_generated_certificate', 'Can view generated certificate'),  # Permission for viewing generated certificate
        ]

    def __str__(self):
        return f'{self.recipient_name} - Certificate ID: {self.certificate_id}'
