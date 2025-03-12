from django.utils import timezone
from accounts.models import Profile, LastUpdate

class UpdateDaysMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Проверяем, нужно ли обновить дни для всех пользователей
        self.update_all_days_if_needed()

        # Выполняем запрос
        response = self.get_response(request)
        return response

    def update_all_days_if_needed(self):
        # Получаем или создаём запись последнего обновления
        last_update_obj = LastUpdate.get_last_update()
        today = timezone.now().date()
        last_update_date = last_update_obj.last_update_date.date()

        # Если прошёл хотя бы один день с последнего обновления
        if (today - last_update_date).days >= 1:
            # Обновляем дни для всех пользователей, кроме суперпользователей
            profiles = Profile.objects.filter(user__is_superuser=False)
            for profile in profiles:
                profile.update_days()

            # Обновляем дату последнего глобального обновления
            last_update_obj.last_update_date = timezone.now()
            last_update_obj.save()