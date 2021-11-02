from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from watchlist.models import Media, Platform
from .serializers import MediaSerializer, PlatformSerializer
from rest_framework import status

class MediaListAPI(APIView):

    def get(self, request):
        media = Media.objects.all()
        serializer = MediaSerializer(media, many=True)
        return Response(serializer.data)
        

    def post(self, request):   
        serializer = MediaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else: 
            return Response(serializer.errors) 

class MediaDetailAPI(APIView): 
    
    def get(self, request, pk):
        try:
            media = Media.objects.get(id=pk)
        except:
            return Response({'Error': 'Media not found!'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MediaSerializer(media)
        return Response(serializer.data)

    def put(self, request, pk):   
        media = Media.objects.get(id=pk)
        serializer = MediaSerializer(media, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        media = Media.objects.get(id=pk)
        media.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PlatformListAPI(APIView):
    """
    List all code platforms, or create a new platform.
    """
    def get(self, request):
        platforms = Platform.objects.all()
        serializer = PlatformSerializer(platforms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class PlatformDetailsAPI(APIView):

    def get(self, request, pk):

        try:
            platform = Platform.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        selializer = PlatformSerializer(platform)
        return Response(selializer.data)

    def put(self, request, pk):
        platform = Media.objects.get(id=pk)
        serializer = Platformserializer(platform, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        platoform = Platform.get(id = pk)
        platform.delete()
        return Responsse(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def movie_list(request):

#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         else: 
#             return Response(serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, pk):

#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(id=pk)
#         except:
#             return Response({'Error': 'Movie not found!'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         movie = Movie.objects.get(id=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


