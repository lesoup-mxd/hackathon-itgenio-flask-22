from app import app
from flask import make_response, request, render_template, url_for, session


@app.route('/cookie/')
def cookie():
    if not request.cookies.get('foo'):
        res = make_response("Setting a cookie")
        res.set_cookie('foo', 'bar', max_age=60*60*24*365*2)
    else:
        res = make_response(
            "Value of cookie foo is {}".format(request.cookies.get('foo'))
            )
    return res

@app.route('/delete-cookie/')
def delete_cookie():
    res = make_response("Cookie Removed")
    res.set_cookie('foo', 'bar', max_age=0)
    return res

@app.route('/article/', methods=['POST',  'GET'])
def article():
    if request.method == 'POST':
        print(request.form)
        res = make_response("")
        res.set_cookie("font", request.form.get('font'), 60*60*24*15)
        res.headers['location'] = url_for('article')
        return res, 302

    return render_template('cookies/article.html')

@app.route('/visits-counter/')
def visits():
    session.permanent = True
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1
    return "Всего посещений: {}".format(session.get('visits'))

@app.route('/session/')
def updating_session():
    res = str(session.items())

    cart_item = {'pineapples': '10', 'apples': '20', 'mangoes': '30'}

    if 'cart_item' in session:
        session['cart_item']['pineapples'] = 100
        session.modified = False
    else:
        session['cart_item'] = cart_item

    return res

@app.route('/delete-visits/')
def delete_visits():
    session.pop('visits', None)
    session.pop('cart_item', None)
    return 'Посещения очищенны'
