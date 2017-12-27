from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import Player
from .serializers import PlayerSerializer
from django.shortcuts import render, get_object_or_404


class PlayerList(APIView):

    def get(self, request):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)


def index(request):
    player_list = Player.objects.order_by()
    context = {'player_list': player_list}
    return render(request, 'players/index.html', context)


def detail(request, player_id):
        player = get_object_or_404(Player, pk=player_id)
        return render(request, 'players/detail.html', {'player': player})




