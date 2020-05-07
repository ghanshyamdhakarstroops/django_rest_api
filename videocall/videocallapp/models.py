from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class PdfData(models.Model):
	count=models.IntegerField(default=0)
	text=models.TextField(blank=True)

class Hero(models.Model):
	owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
	name=models.CharField(max_length=30)
	alise=models.CharField(max_length=50)

	def __str__(self):
		return self.name

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_token(sender, instance=None, created=False, **kwargs):
	if created:
		token=Token.objects.create(user=instance)
		print(token.key)
# Create your models here.
