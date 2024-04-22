from django.shortcuts import render,get_object_or_404
from .models import Food,Consume
# Create your views here.
def index(request):
    
    if request.method == "POST":
        food_consumed = request.POST.get('food_consumed', None)
        consume = get_object_or_404(Food, name=food_consumed)
        user = request.user
        consume = Consume(user=user,food_consumed=consume)
        consume.save()
        foods = Food.objects.all()

    else:
        foods = Food.objects.all()


    return render(request,'myapp/index.html',{'foods':foods})
