from django.shortcuts import render

# Create your views here.

def home(request):
    dict={'Name' : 'Mahedi', 'age': 22, 'courses':[
        {
          'id':1,
          'Name':'Python',
          'fee':3000

        },
        {
            'id':2,
            'Name':'Django',
            'fee' : 2500
        }
      ]
    }
    return render(request,'index.html',dict)