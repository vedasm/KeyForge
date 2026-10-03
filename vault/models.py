from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
from django.conf import settings

class Vault(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vaults')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class APIKeyEntry(models.Model):
    vault = models.ForeignKey(Vault, on_delete=models.CASCADE, related_name='keys')
    name = models.CharField(max_length=100)
    provider = models.CharField(max_length=50, blank=True)
    encrypted_value = models.BinaryField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    
    def set_value(self, raw_value: str):
        f = Fernet(settings.FERNET_KEY)
        self.encrypted_value = f.encrypt(raw_value.encode())

    def get_value(self) -> str:
        f = Fernet(settings.FERNET_KEY)
        return f.decrypt(bytes(self.encrypted_value)).decode()

    def __str__(self):
        return f"{self.name} ({self.provider})"
