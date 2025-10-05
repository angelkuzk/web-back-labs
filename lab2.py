from flask import Blueprint, url_for, request, redirect, render_template, abort
lab2 = Blueprint('lab2', __name__)


@lab2.route('/lab2/a')
def a():
    return 'без слэша'

@lab2.route('/lab2/a/')
def a2():
     return 'со слэшем'

flower_list = [
    {'name': 'роза', 'price': 300},
    {'name': 'тюльпан', 'price': 310},
    {'name': 'незабудка', 'price': 320},
    {'name': 'ромашка', 'price': 330},
    {'name': 'георгин', 'price': 300},
    {'name': 'гладиолус', 'price': 310}
]


@lab2.route('/lab2/flowers/')
def flowers_list():
    return render_template('flowers.html', flowers=flower_list)

@lab2.route('/lab2/del_flower/<int:flower_id>')
def del_flower(flower_id):  
    if flower_id >= len(flower_list):
        abort(404)
    flower_list.pop(flower_id)
    return redirect(url_for('flowers_list'))

@lab2.route('/lab2/add_flower/', methods=['GET', 'POST'])
def add_flower():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        if name:
            # есть ли такой цветок
            for flower in flower_list:
                if flower['name'] == name:
                    flower['price'] += 10
                    break
            else:
                flower_list.append({'name': name, 'price': 300})
        return redirect(url_for('flowers_list'))
    return redirect(url_for('flowers_list'))


@lab2.route('/lab2/flowers/all')
def all_flowers():
    return f'''
<!doctype html>
<html>
    <body>
        <h1>Все цветы</h1>
        <p>Количество цветов: {len(flower_list)}</p>
        <p>Полный список: {flower_list}</p>
        <a href="/lab2/flowers/clear">Очистить список</a>
    </body>
</html>
'''

@lab2.route('/lab2/flowers/clear')
def clear_flowers():
    flower_list.clear()
    return redirect(url_for('flowers_list'))

@lab2.route('/lab2/example')
def example():
    name = 'Ангелина Кузнецова'
    group = 'ФБИ-33'
    course = '3 курс'
    number = '2'
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321},
    ]
    return render_template('example.html', 
                           name=name, number=number, group=group, 

                           course=course, fruits=fruits)

@lab2.route('/lab2/')
def lab22():
    return render_template('lab2.html')

@lab2.route('/lab2/')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase = phrase)

@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    return f'''
<!doctype html>
<html>
<body>
    <h1>Расчёт с параметрами:</h1>
    <div class="result">
        {a} + {b} = {a + b}<br>
        {a} - {b} = {a - b}<br>
        {a} × {b} = {a * b}<br>
        {a} / {b} = {a / b if b != 0 else 'на ноль делить нельзя'}<br>
        {a}<sup>{b}</sup> = {a ** b}
    </div>
    <p><a href="/lab2/calc/">Попробовать с другими числами</a></p>
</body>
</html>
'''

@lab2.route('/lab2/calc/')
def calc_default():
    return redirect('/lab2/calc/1/1')

@lab2.route('/lab2/calc/<int:a>')
def calc_single(a):
    return redirect(f'/lab2/calc/{a}/1')

books = [
    {'author': 'Джоан Роулинг', 'title': 'Гарри Поттер и философский камень', 'genre': 'Фэнтези', 'pages': 432},
    {'author': 'Джордж Оруэлл', 'title': '1984', 'genre': 'Антиутопия', 'pages': 328},
    {'author': 'Рэй Брэдбери', 'title': '451° по Фаренгейту', 'genre': 'Научная фантастика', 'pages': 256},
    {'author': 'Агата Кристи', 'title': 'Убийство в Восточном экспрессе', 'genre': 'Детектив', 'pages': 320},
    {'author': 'Джон Толкин', 'title': 'Властелин Колец', 'genre': 'Фэнтези', 'pages': 1128},
    {'author': 'Эрнест Хемингуэй', 'title': 'Старик и море', 'genre': 'Художественная проза', 'pages': 128},
    {'author': 'Фрэнсис Фицджеральд', 'title': 'Великий Гэтсби', 'genre': 'Роман', 'pages': 218},
    {'author': 'Габриэль Маркес', 'title': 'Сто лет одиночества', 'genre': 'Магический реализм', 'pages': 416},
    {'author': 'Артур Конан Дойл', 'title': 'Шерлок Холмс', 'genre': 'Детектив', 'pages': 307},
    {'author': 'Джейн Остин', 'title': 'Гордость и предубеждение', 'genre': 'Роман', 'pages': 432},
]

@lab2.route('/lab2/books/')
def books_list():
    return render_template('books.html', books=books)
dogs = [
    {
        'name': 'Лабрадор-ретривер',
        'image': 'labrador.jpg',
        'description': 'Дружелюбная и энергичная порода, отличный компаньон для семьи'
    },
    {
        'name': 'Немецкая овчарка',
        'image': 'german_shepherd.jpg',
        'description': 'Умная и универсальная порода, часто используется в полиции и армии'
    },
    {
        'name': 'Золотистый ретривер',
        'image': 'golden_retriever.jpg',
        'description': 'Добродушная и интеллигентная порода с золотистой шерстью'
    },
    {
        'name': 'Французский бульдог',
        'image': 'french_bulldog.jpg',
        'description': 'Компактная порода с большими ушами и дружелюбным характером'
    },
    {
        'name': 'Бульдог',
        'image': 'bulldog.jpg',
        'description': 'Спокойная порода с морщинистой мордой и коренастым телом'
    },
    {
        'name': 'Бигль',
        'image': 'beagle.jpg',
        'description': 'Охотничья порода с острым нюхом и дружелюбным нравом'
    },
    {
        'name': 'Пудель',
        'image': 'poodle.jpg',
        'description': 'Умная порода с кудрявой шерстью, известная своей гипоаллергенностью'
    },
    {
        'name': 'Ротвейлер',
        'image': 'rottweiler.jpg',
        'description': 'Сильная и преданная порода с выразительной внешностью'
    },
    {
        'name': 'Сибирский хаски',
        'image': 'siberian_husky.jpg',
        'description': 'Энергичная порода с густой шерстью и голубыми глазами'
    },
    {
        'name': 'Такса',
        'image': 'dachshund.jpg',
        'description': 'Небольшая порода с длинным телом и короткими лапами'
    },
    {
        'name': 'Доберман',
        'image': 'doberman.jpg',
        'description': 'Элегантная и athletic порода с репутацией отличного защитника'
    },
    {
        'name': 'Боксер',
        'image': 'boxer.jpg',
        'description': 'Энергичная и игривая порода с выразительной мордой'
    },
    {
        'name': 'Ши-тцу',
        'image': 'shih_tzu.jpg',
        'description': 'Декоративная порода с длинной шелковистой шерстью'
    },
    {
        'name': 'Австралийская овчарка',
        'image': 'australian_shepherd.jpg',
        'description': 'Умная и активная порода, отличный пастух'
    },
    {
        'name': 'Вельш-корги',
        'image': 'corgi.jpg',
        'description': 'Небольшая пастушья порода с короткими лапами и очаровательной внешностью'
    },
    {
        'name': 'Джек-рассел-терьер',
        'image': 'jack_russell.jpg',
        'description': 'Энергичная и бесстрашная небольшая порода'
    },
    {
        'name': 'Чихуахуа',
        'image': 'chihuahua.jpg',
        'description': 'Самая маленькая порода собак с большим характером'
    },
    {
        'name': 'Мопс',
        'image': 'pug.jpg',
        'description': 'Компактная порода с морщинистой мордой и веселым нравом'
    },
    {
        'name': 'Бернский зенненхунд',
        'image': 'bernese_mountain.jpg',
        'description': 'Крупная порода с трехцветным окрасом и спокойным характером'
    },
    {
        'name': 'Померанский шпиц',
        'image': 'pomeranian.jpg',
        'description': 'Маленькая пушистая порода с лисьей мордочкой'
    }
]

@lab2.route('/lab2/dogs/')
def dogs_list():
    return render_template('dogs.html', dogs=dogs)