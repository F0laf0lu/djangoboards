from django.shortcuts import get_object_or_404, render
from django.http import  HttpResponse
from django.shortcuts import render

from boards.models import Board
# Create your views here.


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board':board})
