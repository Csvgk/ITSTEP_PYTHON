from django.shortcuts import render


def index(request):
    brands = [
        ('cars:toyota', 'Toyota', 'Японія', 'Надійність і гібридні технології.'),
        ('cars:honda', 'Honda', 'Японія', 'Двигуни, мотоцикли та спортивний характер.'),
        ('cars:renault', 'Renault', 'Франція', 'Європейський стиль і практичність.'),
    ]
    return render(request, 'cars/index.html', {'brands': brands})


def toyota(request):
    context = {
        'brand': 'Тойота',
        'founded': 1937,
        'country': 'Японія',
        'about': 'Один з найбільших автовиробників світу. Toyota Prius став першим серійним гібридним автомобілем.',
        'models': ['Corolla', 'Camry', 'RAV4', 'Land Cruiser', 'Prius'],
        'theme': 'toyota',
    }
    return render(request, 'cars/brand.html', context)


def honda(request):
    context = {
        'brand': 'Хонда',
        'founded': 1948,
        'country': 'Японія',
        'about': 'Компанія виробляє автомобілі, мотоцикли та двигуни і є одним з найбільших виробників двигунів у світі.',
        'models': ['Civic', 'Accord', 'CR-V', 'Jazz'],
        'theme': 'honda',
    }
    return render(request, 'cars/brand.html', context)


def renault(request):
    context = {
        'brand': 'Рено',
        'founded': 1899,
        'country': 'Франція',
        'about': 'Французький автовиробник, відомий компактними міськими авто та електромобілями.',
        'models': ['Clio', 'Megane', 'Captur', 'Duster', 'Zoe'],
        'theme': 'renault',
    }
    return render(request, 'cars/brand.html', context)
