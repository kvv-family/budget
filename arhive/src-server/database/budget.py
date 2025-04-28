from datetime import date, datetime

from pony.orm import Optional, PrimaryKey, Required, Set

from .base import database


class Debt(database.Entity):
    """Модель для хранения долгов и кредитов"""

    id = PrimaryKey(int, auto=True)
    description = Required(str)  # Описание долга
    amount = Required(float)  # Сумма долга
    date = Required(date)  # Дата (в формате "YYYY-MM-DD")
    is_credit = Required(bool)  # True — мне должны, False — я должен
    closed = Required(bool, default=False)
    user = Required("User")  # Связь с пользователем


class Category(database.Entity):
    """Модель для хранения категорий доходов и расходов"""

    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)  # Название категории
    icon = Required(str)
    is_income = Required(bool)  # True — категория для доходов, False — для расходов
    incomes = Set("Income")  # Связь с доходами
    expenses = Set("Expense")  # Связь с расходами
    budget_plans = Set("BudgetPlan")  # Связь с планами бюджета


class BudgetPlan(database.Entity):
    """Модель для хранения планов бюджета пользователя"""

    id = PrimaryKey(int, auto=True)
    month = Required(str)  # Месяц планирования (в формате "YYYY-MM")
    limit = Required(float)  # Лимит на категорию
    user = Required("User")  # Связь с пользователем
    category = Required(Category)  # Связь с категорией


class SavingsGoal(database.Entity):
    """Модель для хранения финансовых целей пользователя"""

    id = PrimaryKey(int, auto=True)
    name = Required(str)  # Название цели
    target_amount = Required(float)  # Целевая сумма
    current_amount = Required(float)  # Текущая сумма в начале создания цели
    calculate_amount = Required(float)  # Рассчитанная сумма
    deadline = Required(date)  # Дедлайн (в формате "YYYY-MM-DD")
    user = Required("User")  # Связь с пользователем
    incomes = Set("IncomeSaving")


class IncomeSaving(database.Entity):
    "Модель для хранения информации пополнения финансовых целей"

    id = PrimaryKey(int, auto=True)
    amount = Required(float)
    status = Required(bool, default=False)
    create_at = Required(datetime, default=datetime.now())
    execution_at = Optional(datetime)
    goal = Required(SavingsGoal)


class Expense(database.Entity):
    """Модель для хранения расходов пользователя"""

    id = PrimaryKey(int, auto=True)
    amount = Required(float)  # Сумма расхода
    description = Optional(str)  # Описание расхода
    date = Required(str)  # Дата расхода (в формате "YYYY-MM-DD")
    user = Required("User")  # Связь с пользователем
    category = Optional(Category)  # Связь с категорией


class Income(database.Entity):
    """Модель для хранения доходов пользователя"""

    id = PrimaryKey(int, auto=True)
    amount = Required(float)  # Сумма дохода
    description = Optional(str)  # Описание дохода
    date = Required(date)  # Дата дохода (в формате "YYYY-MM-DD")
    user = Required("User")  # Связь с пользователем
    category = Optional(Category)  # Связь с категорией
