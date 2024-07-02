from django.shortcuts import render
from datetime import datetime,timedelta
from django.http import HttpResponse
# Create your views here.

def Home(request):
    response=render(request,'home.html')
    response.set_cookie('name','Noyon',expires=datetime.utcnow()+timedelta(days=7))
    return response

def get_cookie(request):
    name=request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request,'get_cookie.html',{'name':name})


def delete_cookies(request):
    response=render(request,'del.html')
    response.delete_cookie('name')
    return response

    
def set_session(request):
    data={
        'name': 'Noyon',
        'ages':22,

    }

    request.session.update(data)
    return render(request,'set_session.html')


def get_session(request):
    if 'name' in request.session:
        name=request.session.get('name')
        age=request.session.get('ages')
        request.session.modified=True
        return render(request,'get_session.html',{'name': name,'age':age})
    else:
        return HttpResponse('Your session has been expired')

def delete_session(request):
    request.session.flush()
    return render(request,'del.html')