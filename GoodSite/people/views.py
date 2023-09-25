from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

pri_data = {
        '1' : ['Абрамов Александр Альбертович', '2004'],
        '2' : ['Близнюк Илья Сергеевич', '2005'],
        '3' : ['Зверев Андрей Александрович', '2000'],
        '4' : ['Карагузин Максим Игоревич', '2002'],
        '5' : ['Круглик Евгений Дмитриевич', '2003'],
        '6' : ['Лысков Влас Евгеньевич', '2003'],
        '7' : ['Маклюсов Роман Романович', '1999'],
        '8' : ['Манешин Антон Сергеевич', '2001'],
        '9' : ['Петрачков Александр Викторович', '2003'],
        '10' : ['Сафонов Глеб Александрович', '2006'],
        '11' : ['Терешин Роман Павлович', '2004'],
        '12' : ['Чертков Федор Андреевич', '2001'],
    }

# Create your views here.
def index(request):
    get = request.GET
    get_1 = dict(get)
    get_2 = get_1['name'][0]
    print(get_2)
    return HttpResponse(f"{get_2}")


def about(request):
    return HttpResponse('<h1> БГИТУ </h1>')


def pri_group(request):
    conclusion = '<h1> ПрИ-201 </h1> <p>'
    for number, mas_of_info in pri_data.items():
        conclusion += number + '.'
        conclusion += mas_of_info[0]
        conclusion += '</p>'

    return HttpResponse(out)


def pri_id(request, number_student):

    if str(number_student) in pri_data:
        conclusion = '<h1> ПрИ-201 </h1> <p>'
        group_mas = pri_data[str(number_student)]
        conclusion += f'{group_mas[0]} {group_mas[1]}'
        conclusion += '</p>'
        return HttpResponse(conclusion)
    else:
        return HttpResponse('<h1> Ошибка </h1> <h3> Такого студента не существует </h3>')


def categories(request, cat):
    return HttpResponse('<h1> Ошибка </h1> <h3> Такого студента не существует </h3>')

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1> Страница не найдена проверьте адресс. </h1>")