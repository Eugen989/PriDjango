from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render, redirect

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

year_animal = {
    1 : "козы",
    2 : "обезьяны",
    3 : "петуха",
    4 : "собаки",
    5 : "свиньи",
    6 : "крысы",
    7 : "быка",
    8 : "тигра",
    9 : "кролика",
    10 : "дракона",
    11 : "змея",
}

class new_year():
    def __init__(self, year):
        self.year = int(year)

    def print(self):
        if int(self.year) >= 2015 and int(self.year) <= 2025:
            return f"Год {year_animal[self.year - 2014]}"
        else:
            return redirect(f"/home", permanent=True)

class year_interpreter():
    def __init__(self, year):
        self.year = int(year)
    @property
    def print(self):
        if int(self.year) >= 2015 and int(self.year) <= 2025:
            return "Всё хорошо"
            return f"Год {year_animal[self.year - 2014]}"
        else:
            #raise PermissionDenied()
            return redirect(f"/home", permanent=True)

menu = [{'title': 'Главная', 'url_n': 'home'}, {'title': 'О сайте', 'url_n': 'about'}, {'title': 'О студентах', 'url_n': 'pri'}]

data_db = [
    {
        "id": 1,
        "title": "Илон Маск",
        "content": "Биография Илона Маска",
        "is_public": True
     },

    {
        "id": 2,
        "title": "Жириновский",
        "content": "Биография Жириновскорого",
        "is_public": True
     },

    {
        "id": 3,
        "title": "Баба Яга",
        "content": "Биография бабы яги",
        "is_public": False
     }

]
float = 3.7

# Create your views here.
def index(request):
    #get = request.GET
    #get_1 = dict(get)
    #print(get_1[name])
    #return HttpResponse(f"Пусто")

    data = {'title': "Главная страница",
        'menu': menu,
        'float': 3.8,
        'posts': data_db
        }
    return render(request, "women/index.html", data)


def about(request):
    # return redirect("spisok_pri", '12')

    data = {'title': "О программе", 'menu': menu}

    return render(request, 'women/about.html', data)
    return HttpResponse('<h1> БГИТУ </h1>')


def pri(request):
    data_pri = {}
    # for i in pri_data:
    #     data_pri[f"pri_{i}"] = pri_data[f'{i}'][0]

    data = {'title': "Списки студентов", 'menu': menu, "pri_data": pri_data}
    print(pri_data)

    return render(request, 'women/student.html', data)

def pri_group(request):
    conclusion = '<h1> ПрИ-201 </h1> <p>'
    for number, mas_of_info in pri_data.items():
        conclusion += number + '.'
        conclusion += mas_of_info[0]
        conclusion += '</p>'

    return HttpResponse(conclusion)


def pri_id(request, number_student):

    if str(number_student) in pri_data:
        conclusion = ''
        group_mas = pri_data[str(number_student)]
        conclusion += f'{group_mas[0]} {group_mas[1]}'

        data = {'title': "ПрИ-201", 'menu': menu, "conclusion": conclusion, "number": number_student}
        return render(request, "women/one_student.html", data)
        #return HttpResponse(conclusion)
    else:
        return HttpResponse('<h1> Ошибка </h1> <h3> Такого студента не существует </h3>')


def categories(request, cat):
    return HttpResponse('<h1> Ошибка </h1> <h3> Такого студента не существует </h3>')

def year_handler(request, year_number):

    if year_number >= 2015 and year_number <= 2025:
        y_i = year_interpreter(year_number)
        return HttpResponse(f"<h1> {y_i.print} </h1>")
    else:
        return redirect("about")


def post_detail(request):
    get = request.GET
    if(get):
        get = dict(get)
        str_get = ""
        for i, j in get.items():
            str_get += i
            str_get += '='
            str_get += j[0]
            str_get += "|"
        #str_get += get[0]
        str_get = str_get[:len(str_get) - 1]
        return HttpResponse(f"<h1> {str_get} </h1>")
    else:
        return HttpResponse(f"<h1> Get is empty </h1>")


def get_data_type(requenst):
    year = new_year(2016)
    return HttpResponse(f"<h1> {year.print()} </h1> <br><br> <h1> {data_db} </h1>")

def get_data_for_number(request, number):
    return HttpResponse(f"<h1> Всё хорошо </h1>")


def split_line(request):
    line = "Hello, my, \"world or, not\" ku, ku , \",,\" ,   "
    sep = ","
    parse_line = line
    list = []
    i = 0
    zap_i = 0
    last_i = 0
    sep_symbol = False
    first_symb = False

    while(i < len(line)):
        if i == len(parse_line) - 1:
            if (parse_line[zap_i:i] == len(parse_line[zap_i:i]) * ' '):
                list.append('')
                break

        if parse_line[i] == "\"":
            sep_symbol = not sep_symbol

        # if not first_symb and parse_line[i] == ' ':
        #     zap_i += 1
        #     print("Увелечение zap_i")
        #
        # elif not first_symb and parse_line[i] != " ":
        #     first_symb = True

        if parse_line[i] == sep and not sep_symbol:
            if(parse_line[zap_i:i] == len(parse_line[zap_i:i])*' '):
                list.append('')
            elif(zap_i != 0):
                list.append(parse_line[zap_i:i])
            else:
                list.append(parse_line[zap_i:i])
            i = i + 1
            zap_i = i
            no_sep = False
            # first_symb = False
        i += 1
    if no_sep:
        list.append(line)

    n = 0
    sep_symbol = False

    # for j in range(len(list)):
    # if "\"" in list[j]:
    # for k in range(len(list[j])):
    # if list[j][k] == "\"":
    # list[j] = list[j][k+1:list[j].find("\"")]



    dict = {}
    dict['str'] = list
    print(dict)
    return render(request, 'women/second.html', dict)
    #return HttpResponse(f'<h1> {list} </h1>')



def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1> +Страница не найдена проверьте адресс. </h1>")

def page_bad_request_400(request, exception):
    return HttpResponseBadRequest("<h1> Плохой запрос </h1>")

def page_forbiden_403(request, exception):
    return HttpResponseNotFound('<h1> Такого года нету </h1>')

def page_not_found_404(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена. Проверьте адрес! </h1>')

def page_server_error_500(exception):
    return HttpResponseServerError('<h1> Ошибка cтраницы </h1>')