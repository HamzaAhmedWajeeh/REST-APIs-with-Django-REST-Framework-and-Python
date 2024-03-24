from rest_framework.decorators import api_view
from watchlist_app.models import Movie
from rest_framework.response import Response
from .serializers import MovieSerializer

@api_view(['GET'])
def movie_list(request):

    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, id):

    movie = Movie.objects.get(pk=id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)