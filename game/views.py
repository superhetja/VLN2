from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from game.forms.game_form import GameCreateForm
from game.models import Game, GameImage


# Create your views here.
def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        games = [ {
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'image': x.gameimage_set.first().image
        }for x in Game.objects.filter(name__icontains=search_filter) ]
        return JsonResponse({'data': games})
    context = {'games': Game.objects.all().order_by('name')}
    return render(request, 'game/index.html', context)

# /games/{:id}
def get_game_by_id(request, id):
    return render(request, 'game/game_details.html', {
        'game': get_object_or_404(Game, pk=id)
    })

def create_game(request):
    if request.method == 'POST':
        form = GameCreateForm(data=request.POST)
        if form.is_valid():
            game = form.save()
            game_image = GameImage(image=request.POST['image'], game=game)
            game_image.save()
            return redirect('game-index')
    else:
        form = GameCreateForm()
    return render(request, 'game/create_game.html',  {
        'form': form
    })

def delete_game(request, id):
    game = get_object_or_404(game, pk=id)
    game.delete()
    return redirect('game-index')
