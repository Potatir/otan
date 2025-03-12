from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group  # Добавлен импорт Group
from .models import Profile

# Настройка админки для Profile
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    fields = ('phone', 'photo')  # Только телефон и фото
    verbose_name_plural = 'Профиль'

# Настройка админки для User
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'first_name', 'last_name', 'is_superuser', 'days_since_registration')
    list_filter = ('is_superuser',)
    search_fields = ('username', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Личная информация', {'fields': ('first_name', 'last_name')}),
        ('Права', {'fields': ('is_superuser',)}),
    )

    def days_since_registration(self, obj):
        return obj.profile.days_since_registration
    days_since_registration.short_description = 'Дней с регистрации'

# Перерегистрируем User с кастомной админкой
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Удаляем стандартные модели
admin.site.unregister(Group)