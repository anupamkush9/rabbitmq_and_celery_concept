from django.http import HttpResponse
from .tasks import add

def Indexview(request):
    print("--------------------------------------")
    # print(add(45, 56).delay())  //Incorrect way of Adding task to celery.
    total_sum = add.delay(45,89)
    print("++++++++brfore call add method++++++++++++=",type(total_sum))
    print("++++++++brfore call add method++++++++++++=",total_sum)
    return HttpResponse("<h1>Hello world</h1>")

