from django.shortcuts import render
from django.utils import timezone

# Номер дня (0 = понеділок) -> назва, css-клас фону, емодзі
DAYS = [
    ('Понеділок', 'monday', '☕'),
    ('Вівторок', 'tuesday', '📚'),
    ('Середа', 'wednesday', '🐫'),
    ('Четвер', 'thursday', '🚀'),
    ('П\'ятниця', 'friday', '🎉'),
    ('Субота', 'saturday', '🏖'),
    ('Неділя', 'sunday', '😴'),
]


def index(request):
    day_number = timezone.localdate().weekday()
    # Для перевірки інших днів: /?day=1 ... /?day=7
    day_param = request.GET.get('day')
    if day_param and day_param.isdigit() and 1 <= int(day_param) <= 7:
        day_number = int(day_param) - 1

    name, css_class, emoji = DAYS[day_number]
    context = {
        'day_name': name,
        'css_class': css_class,
        'emoji': emoji,
        'date': timezone.localdate(),
        'days': [(i + 1, d[0]) for i, d in enumerate(DAYS)],
    }
    return render(request, 'weekday/index.html', context)
