

from django.http import HttpResponse

def Home(resqust):
    return HttpResponse("this Home pages")

def contact(resqust):
    return HttpResponse("This is contact pages")



