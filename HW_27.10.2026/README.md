# Домашнє завдання 27.10.2026 — моделі Tag, Profile та Django Admin

Копія проєкту блогу (`New Project/website`), в якій виконано завдання. Оригінальний проєкт не змінювався.

## Запуск

```bash
python manage.py migrate
python manage.py seed_blog      # тестові дані: 5 публікацій, 3 категорії, 5 тегів, 2 профілі
python manage.py runserver
```

Адмінка: http://127.0.0.1:8000/admin/ — тестовий суперкористувач створюється командою `seed_blog`
(логін і пароль — у `blog/management/commands/seed_blog.py`).

## #1 Модель Tag

- `Tag.name` — `CharField(max_length=30, unique=True)`, є `__str__`, `verbose_name`, `verbose_name_plural`.
- `Post.tags` — `ManyToManyField(Tag, blank=True, related_name='posts')`.
- Міграція: `blog/migrations/0003_...py`. Tag зареєстровано в адмінці.

Перевірка (`python manage.py shell`):

```text
Теги поста «Вихідні у Львові»: ['кава', 'львів', 'поради']        <- один пост має кілька тегів
Пости з тегом python: ['Django Admin: швидкий старт', '10 порад для чистого коду на Python', 'Перші кроки в Django']
                                                                   <- один тег використовується в кількох постах
Створення тегу 'python' ще раз: UNIQUE constraint failed: blog_tag.name
```

## #2 Модель Profile

- `Profile.user` — `OneToOneField(User, on_delete=models.CASCADE)`.
- `bio`, `city`, `birth_date` — `blank=True` (дата ще й `null=True`), тому їх можна не заповнювати.
- Є `__str__`, модель зареєстрована в адмінці, створено профілі для `olena` і `ivan`.

Перевірка: спроба створити другий профіль для `olena`:

```text
IntegrityError: UNIQUE constraint failed: blog_profile.user_id
```

**Чому Django не дозволяє:** `OneToOneField` — це зв'язок «один до одного». Django створює в таблиці
`blog_profile` колонку `user_id` з обмеженням `UNIQUE`, тобто один користувач може мати тільки один профіль.
База даних відхиляє другий запис з тим самим `user_id`, а в адмінці Django ще до збереження показує помилку
«Профіль з таким Користувач вже існує».

## #3 PostAdmin

```python
list_display = ['title', 'category', 'user', 'published_date', 'content_length']
list_filter = ['category', 'published_date']
search_fields = ['title', 'content']
filter_horizontal = ['tags']
```

Перевірка на 5 тестових публікаціях:

```text
Пошук «кав»                 -> Як обрати каву для дому, Вихідні у Львові   (знайдено і в заголовку, і в тексті)
Фільтр «Програмування»      -> 3 публікації
Фільтр за датою «Сьогодні»  -> 5 публікацій
На сторінці редагування поста теги обираються через віджет із двома списками (filter_horizontal).
```
