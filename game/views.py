from django.shortcuts import render

games =[
    { 'name': 'Pac-man', 'price': 4.99, 'stock': 1},
    { 'name': 'man-man', 'price': 3.15, 'stock': 0},
    { 'name': 'man-Pac', 'price': 6.25, 'stock': 3},
    { 'name': 'Pac', 'price': 55.69, 'stock': 1},
    { 'name': 'man', 'price': 12.34, 'stock': 1}
]

# Create your views here.
def index(request):
    return render(request, 'game/index.html', context={
        'games' :games
    })
