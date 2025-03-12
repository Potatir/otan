import os
import sys

# Настройка окружения Django
project_path = r'C:\Users\sanya\Desktop\otan2\autoshkola'
sys.path.append(project_path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autoshkola.settings')

# Инициализация Django
import django
django.setup()

# Теперь импортируем модели после настройки
from django.contrib.auth.models import User
from django.utils import timezone
from accounts.models import Profile
from datetime import timedelta

def create_test_user(username, email, password, days_since_registration):
    try:
        # Проверяем, существует ли пользователь
        if User.objects.filter(username=username).exists():
            print(f"Пользователь с именем {username} уже существует.")
            return
        
        # Создаём нового пользователя
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        print(f"Создан пользователь: {user.username} (email: {user.email})")

        # Вычисляем дату регистрации (сегодня минус days_since_registration)
        registration_date = timezone.now() - timedelta(days=days_since_registration)

        # Создаём профиль с нужным количеством дней
        profile = Profile.objects.create(
            user=user,
            phone="1234567890",
            registration_date=registration_date,
            days_since_registration=days_since_registration,
            last_update_date=timezone.now()
        )
        print(f"Создан профиль для {user.username}: "
              f"Дата регистрации = {profile.registration_date}, "
              f"Дней с регистрации = {profile.days_since_registration}, "
              f"Последнее обновление = {profile.last_update_date}")

    except Exception as e:
        print(f"Ошибка при создании пользователя: {e}")

if __name__ == "__main__":
    # Параметры для тестового пользователя
    test_username = "testuser100"
    test_email = "test100@example.com"
    test_password = "testpassword123"
    test_days_since_registration = 100  # > 76 дней

    # Вызов функции
    create_test_user(test_username, test_email, test_password, test_days_since_registration)