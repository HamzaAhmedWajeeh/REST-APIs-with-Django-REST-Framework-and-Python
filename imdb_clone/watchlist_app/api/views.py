from rest_framework.decorators import api_view
from watchlist_app.models import Movie
from rest_framework.response import Response
from rest_framework import status
from .serializers import MovieSerializer

@api_view(['GET', 'POST'])
def movie_list(request):

    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def movie_detail(request, id):

    if request.method == 'GET':

        try:
            movie = Movie.objects.get(pk=id)
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        except Movie.DoesNotExist:
            return Response("Movie not found", status=status.HTTP_404_NOT_FOUND)


    elif request.method == 'PUT':

        try:
            movie = Movie.objects.get(pk=id)
        except Movie.DoesNotExist:
            return Response("Movie not found", status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'PATCH':
        pass


    elif request.method == 'DELETE':

        try:
            movie = Movie.objects.get(pk=id)
            movie.delete()
            return Response("Movie deleted succesfully", status=status.HTTP_204_NO_CONTENT)
        except Movie.DoesNotExist:
            return Response("Movie not found", status=status.HTTP_404_NOT_FOUND)
