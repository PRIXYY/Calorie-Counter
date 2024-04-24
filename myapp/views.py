from django.shortcuts import render, get_object_or_404
from .models import Food, Consume
from django.utils.datastructures import MultiValueDictKeyError
def index(request):
    if request.method == "POST":
        try:
            food_consumed = request.POST['food_consumed']
        except MultiValueDictKeyError:
            food_consumed = False
        try:
            food = Food.objects.get(name=food_consumed)
        except Food.DoesNotExist:
            # Handle the case where the Food object does not exist
            return render(request, 'myapp/error.html', {'message': 'The food consumed does not exist.'})
        consume = Consume(user=request.user, food_consumed=food)
        consume.save()
        foods = Food.objects.all()

    else:
        
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)
    return render(request, 'myapp/index.html', {'foods': foods,'consumed_food':consumed_food})
