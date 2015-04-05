from bottle import get, post, request, run, static_file, route
from panda_network import PandaSocialNetwork, Panda




panda_ntw = PandaSocialNetwork()
@post('/pandas')
def test():
    global  panda_ntw
    panda_ntw.load_from('dada1.json')
    lst_pandas = panda_ntw.pandas_details()
    return [panda+'<br>' for panda in lst_pandas]

@route('/<filename>')
def server_static(filename):
    return static_file(filename, root='/home/kaloyan/Documents/Hack_Bulgaria/week3')

@get('/get_friends')
def g_fr():
    fle = open('get_friends.html')
    otpt = fle.read()
    fle.close()
    return otpt

@post('/return_panda_friends')
def ret_fr():
    try:
        name = request.forms.get("panda_name")
        mail = request.forms.get("panda_mail")
        gender = request.forms.get("panda_gender")
        out = panda_ntw.friends_of(Panda(str(name), str(mail), str(gender)))
    except AttributeError:
        return '<br>Wrong info given..<br>'

    if out == False:
        return '''<h1> This panda isn't in the network and therefore has no friends... <h1>
            <img src="http://192.168.12.67:8083/ForeverAlone.png" style="display:block; margin-left:auto; margin-right:auto">
    '''
    elif out == []:
        return "<h1>This panda has no friends<h1>"
        
    return [panda + "<br>" for panda in out]

@post('/connection_level')
def con_lvl():
    return '42'
@post('/curr_pandas')
def ret_curr():
    global panda_ntw
    lst_pandas = panda_ntw.pandas_details()
    if lst_pandas == []:
        return 'No pandas yet'
    return [panda + '<br>' for panda in lst_pandas]

@post('/make_friends')
def mk_fr():
    return '42'

@get('/')
def ret():
    fle = open('test.html')
    a = fle.read()
    fle.close()
    return a

@post('/add_panda')
def add_pan():
    fle = open('add_panda.html')
    a = fle.read()
    fle.close()
    return a

@post('/final_add_panda')
def fin_add():
    global panda_ntw
    name = request.forms.get('panda_name')
    mail = request.forms.get('panda_mail')
    gender = request.forms.get('panda_gender')
    panda_ntw.add_panda(Panda(str(name), str(mail), str(gender)))
    return '<h1>Panda added! <h1>'


@get('/login')
def ret():
    name1 = request.forms.get('panda_name')
    email1 = request.forms.get('panda_mail')
    gender1 = request.forms.get('panda_gender')
    global panda_ntw
    panda_ntw.add_panda(Panda(str(name1), str(email1), str(gender1)))
    return '''Panda added successfully!
        <form action = '/curr_pandas' methond = 'get'>
         <input value='Back' type='submit' />
    ''' 
@get('/logout')
def ret():
    fle = open('test.html')
    a = fle.read()
    return a
run(host = '192.168.12.67', port = 8083, debug=True)
