from rest_framework.decorators import api_view
from watchlist_app.models import WatchList, StreamingPlatform
from rest_framework.response import Response
from rest_framework import status
from .serializers import WatchListSerializer, StreamingPlatformSerializer
from rest_framework.views import APIView


class WatchListView(APIView):
    def get(self, request):
        try:
            movies = WatchList.objects.all()
            serializer = WatchListSerializer(movies, many=True)
            return Response(serializer.data)
        except WatchList.DoesNotExist:
            return Response("Not found", status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchListDetailView(APIView):

    def get(self, request, id):
        try:
            try:
                movie = WatchList.objects.get(pk=id)
                serializer = WatchListSerializer(movie)
                return Response(serializer.data)
            except WatchList.DoesNotExist:
                return Response("Not found", status=status.HTTP_404_NOT_FOUND)
        except WatchList.DoesNotExist:
            return Response("Not found", status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            movie = WatchList.objects.get(pk=id)
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except WatchList.DoesNotExist:
            return Response("Not found", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            movie = WatchList.objects.get(pk=id)
        except WatchList.DoesNotExist:
            return Response("Not found", status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StreamingPlatformView(APIView):

    def get(self, request):

        try:
            platforms = StreamingPlatform.objects.all()
            serializer = StreamingPlatformSerializer(
                platforms, many=True,
                # context={'request': request}
                )
            return Response(serializer.data)
        except StreamingPlatform.DoesNotExist:
            return Response("Not found", status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = StreamingPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StreamingPlatformDetailView(APIView):

    def get(self, request, id):
        try:
            try:
                platform = StreamingPlatform.objects.get(pk=id)
                serializer = StreamingPlatformSerializer(platform)
                return Response(serializer.data)
            except StreamingPlatform.DoesNotExist:
                return Response("Not found", status=status.HTTP_404_NOT_FOUND)
        except StreamingPlatform.DoesNotExist:
            return Response("Not found", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):

        try:
            platform = StreamingPlatform.objects.get(pk=id)
        except StreamingPlatform.DoesNotExist:
            return Response("Not found", status=status.HTTP_404_NOT_FOUND)

        serializer = StreamingPlatformSerializer(platform, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            platform = StreamingPlatform.objects.get(pk=id)
            platform.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except StreamingPlatform.DoesNotExist:
            return Response("Not found", status=status.HTTP_404_NOT_FOUND)


# @api_view(['GET', 'POST'])
# def movie_list(request):

#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = WatchListSerializer(movies, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = WatchListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
# def movie_detail(request, id):

#     if request.method == 'GET':

#         try:
#             movie = Movie.objects.get(pk=id)
#             serializer = WatchListSerializer(movie)
#             return Response(serializer.data)
#         except Movie.DoesNotExist:
#             return Response("Not found", status=status.HTTP_404_NOT_FOUND)


#     elif request.method == 'PUT':

#         try:
#             movie = Movie.objects.get(pk=id)
#         except Movie.DoesNotExist:
#             return Response("Not found", status=status.HTTP_404_NOT_FOUND)

#         serializer = WatchListSerializer(movie, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     elif request.method == 'PATCH':
#         pass


#     elif request.method == 'DELETE':

#         try:
#             movie = Movie.objects.get(pk=id)
#             movie.delete()
#             return Response("Movie deleted succesfully", status=status.HTTP_204_NO_CONTENT)
#         except Movie.DoesNotExist:
#             return Response("Not found", status=status.HTTP_404_NOT_FOUND)
