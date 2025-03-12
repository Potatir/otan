from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    registration_date = models.DateTimeField(default=timezone.now)
    days_since_registration = models.IntegerField(default=0)
    last_update_date = models.DateTimeField(default=timezone.now)

    def update_days(self):
        today = timezone.now().date()
        last_update = self.last_update_date.date()
        days_passed = (today - last_update).days
        if days_passed > 0:
            self.days_since_registration += days_passed
            self.last_update_date = timezone.now()
            self.save()

class LastUpdate(models.Model):
    last_update_date = models.DateTimeField(default=timezone.now)

    @classmethod
    def get_last_update(cls):
        obj, created = cls.objects.get_or_create(id=1, defaults={'last_update_date': timezone.now()})
        return obj

    def save(self, *args, **kwargs):
        self.id = 1  # Всегда одна запись
        super().save(*args, **kwargs)