from enum import Enum

from pony.orm import Optional, PrimaryKey, Required, Set

from .base import database


class PROVIDERS(Enum):
    LOCAL = "local"
    GOOGLE = "google"
    ICLOUD = "icloud"


class User(database.Entity):
    """Пользователи"""

    id = PrimaryKey(int, auto=True)
    provider = Required(str, default=PROVIDERS.LOCAL.value)
    provider_id = Required(str)  # Уникальный идентификатор пользователя от провайдера
    email = Required(str, unique=True)  # Email пользователя (уникальный)
    first_name = Required(str)
    last_name = Required(str)
    middle_name = Optional(str)
    avatar_url = Optional(
        str
    )  # Ссылка на аватар пользователя (если предоставляется провайдером)
    is_active = Required(bool, default=True)  # Активен ли пользователь
    incomes = Set("Income")  # Связь с доходами
    expenses = Set("Expense")  # Связь с расходами
    savings_goals = Set("SavingsGoal")  # Связь с целями
    budget_plans = Set("BudgetPlan")  # Связь с планами бюджета
    debts = Set("Debt")  # Связь с долгами
    notifications = Set("Notification")  # Связь с уведомлениями
    tokens = Set("OAuthToken")  # Связь с токенами OAuth2

    def get_full_name(self) -> str:
        if self.middle_name:
            return f"{self.last_name} {self.first_name} {self.middle_name}"
        return f"{self.last_name} {self.first_name}"


class OAuthToken(database.Entity):
    """OAuthToken"""

    id = PrimaryKey(int, auto=True)
    user = Required(User)  # Связь с пользователем
    access_token = Required(str)  # Токен доступа
    refresh_token = Optional(str)  # Токен обновления (если предоставляется провайдером)
    token_type = Optional(str)  # Тип токена (например, "Bearer")
    expires_at = Optional(int)  # Время истечения токена (timestamp)
    scope = Optional(str)  # Области доступа (scope), предоставленные провайдером
    provider = Required(
        str, default=PROVIDERS.LOCAL.value
    )  # Название провайдера OAuth2 (например, "google", "github")


class Notification(database.Entity):
    """Модель для хранения уведомлений пользователя"""

    id = PrimaryKey(int, auto=True)
    message = Required(str)  # Текст уведомления
    is_read = Required(bool, default=False)  # Прочитано ли уведомление
    user = Required(User)  # Связь с пользователем
