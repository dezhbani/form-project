import random
import string
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# Create your models here.
class User(AbstractUser):
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    birth_date=models.DateField(null=True)


class OtpRequest(models.Model):
    request_id = models.UUIDField(default=uuid.uuid4,editable=False)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=5,null=True)
    valid_from = models.DateTimeField(default=timezone.now)
    valid_until= models.DateTimeField(default=timezone.now()+timezone.timedelta(minutes=2))
    receipt_id = models.CharField(max_length=255,null=True)


    def generate_password(self):
        self.password = self._random_password()

    def _random_password(self):
        rand = random.SystemRandom()
        digits = rand.choices(string.digits,k=4)
        digits = "".join(digits)
        return digits

    class Meta:
        verbose_name=_("one time password")
        verbose_name_plural=_("one time passwords")


    def __str__(self) -> str:
        return f"{self.request_id}"