from datetime import date

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from blog.models import Category, Comment, Post, Profile, Tag

ADMIN = ('admin', 'admin12345')
USERS = [
    ('olena', 'olena12345', {'bio': 'Пишу про подорожі та каву.', 'city': 'Львів', 'birth_date': date(2001, 5, 14)}),
    ('ivan', 'ivan12345', {'bio': 'Розробник на Python.', 'city': 'Київ', 'birth_date': None}),
]

CATEGORIES = ['Подорожі', 'Програмування', 'Їжа']
TAGS = ['python', 'django', 'кава', 'львів', 'поради']

POSTS = [
    ('Вихідні у Львові', 'Подорожі', 'olena', ['львів', 'кава', 'поради'],
     'Львів восени — це запах кави, бруківка і затишні дворики. Розповідаю, куди піти за два дні, '
     'де поснідати і яку каву обов\'язково спробувати. Маршрут підійде навіть для першої поїздки.'),
    ('Перші кроки в Django', 'Програмування', 'ivan', ['python', 'django'],
     'Django — це фреймворк, який дозволяє швидко створити вебзастосунок на Python. У статті розберемо '
     'структуру проєкту, моделі, міграції та адмінку, а також створимо першу сторінку.'),
    ('Як обрати каву для дому', 'Їжа', 'olena', ['кава', 'поради'],
     'Арабіка чи робуста, світле чи темне обсмаження, зерно чи мелена — пояснюю простими словами, '
     'на що звернути увагу, щоб удома кава була не гіршою, ніж у кав\'ярні.'),
    ('10 порад для чистого коду на Python', 'Програмування', 'ivan', ['python', 'поради'],
     'Зрозумілі назви змінних, короткі функції, PEP 8 і тести. Збираю десять простих звичок, які роблять '
     'код читабельним для вас і ваших колег.'),
    ('Django Admin: швидкий старт', 'Програмування', 'ivan', ['django', 'python'],
     'Адмінка Django дозволяє керувати даними без жодного рядка HTML. Налаштовуємо list_display, '
     'search_fields, list_filter і filter_horizontal для зручної роботи з публікаціями.'),
]


class Command(BaseCommand):
    help = 'Заповнює базу тестовими даними для перевірки ДЗ'

    def handle(self, *args, **options):
        if not User.objects.filter(username=ADMIN[0]).exists():
            User.objects.create_superuser(ADMIN[0], '', ADMIN[1])

        users = {}
        for username, password, profile_data in USERS:
            user, created = User.objects.get_or_create(username=username)
            if created:
                user.set_password(password)
                user.save()
            Profile.objects.update_or_create(user=user, defaults=profile_data)
            users[username] = user

        categories = {name: Category.objects.get_or_create(name=name)[0] for name in CATEGORIES}
        tags = {name: Tag.objects.get_or_create(name=name)[0] for name in TAGS}

        for title, category, author, post_tags, content in POSTS:
            post, _ = Post.objects.get_or_create(
                title=title,
                defaults={'content': content, 'category': categories[category], 'user': users[author]},
            )
            post.tags.set([tags[t] for t in post_tags])

        comments = [
            ('Вихідні у Львові', 'ivan', 'Дякую за маршрут, поїду наступного місяця!'),
            ('Вихідні у Львові', 'admin', 'Чудові фото і поради.'),
            ('Перші кроки в Django', 'olena', 'Нарешті зрозуміла, що таке міграції :)'),
        ]
        for title, username, text in comments:
            Comment.objects.get_or_create(
                post=Post.objects.get(title=title),
                author=User.objects.get(username=username),
                text=text,
            )

        self.stdout.write(self.style.SUCCESS(
            f'Готово: {User.objects.count()} користувачі, {Category.objects.count()} категорії, '
            f'{Tag.objects.count()} тегів, {Post.objects.count()} публікацій, {Profile.objects.count()} профілі, {Comment.objects.count()} коментарі'
        ))
