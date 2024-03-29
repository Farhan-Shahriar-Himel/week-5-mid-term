from django.shortcuts import render, redirect
from carbrands.models import Brand, Car, Comment
from carbrands.forms import CommentForm
from boughtcar.models import BoughtCar

def home(request, id=None):
    data = Brand.objects.all()
    cars = Car.objects.all()

    if id is not None:
        brand = Brand.objects.filter(id=id)
        cars = Car.objects.filter(brand=brand[0])

    return render(request, 'home.html', {'data': data, 'cars': cars})


def view_more(request, id):
    cars = Car.objects.filter(id = id)
    comments = Comment.objects.filter(post = cars[0])

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = cars[0]
            new_comment.save()

    form = CommentForm()
    return render(request, 'details_view.html', {'cars': cars, 'comments': comments, 'form': form})


def buy_now(request, id):
    data = Car.objects.filter(id = id)[0]
    data.quantity -= 1
    data.save()
    owner = request.user
    new_buy = BoughtCar(car=data, owner=owner)
    new_buy.save()
    return redirect('view_more', data.id)