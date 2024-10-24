import requests
from django.db.models import Avg
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from django.http import Http404
from .models import Post, Comment, Postviewed, Category
from .models import Rating

"""
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

"""


class PostList(APIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, format=None):
        
        posts = Post.objects.all()
        return Response(self.serializer_class(posts, many=True).data)


class CreatePostView(generics.CreateAPIView):
    parser_classes = [JSONParser, MultiPartParser, FormParser]
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    # def post(self, request):

    #     # if email is already in use
    #     serializer = self.serializer_class(data=request.data)

    #     if serializer.is_valid():
            
    #         new_post = serializer.save()
    #         # post_info = {
    #         #     "id":new_user.id,
    #         #     "email": new_user.email
    #         # }
    #         return Response(post_info, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailView(APIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        post = self.get_object(pk)
        if post.owner != request.user:
            raise Http404
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class LikesAPIView(APIView):
    pass

class DislikesAPIView(APIView):
    pass
    
# class PostCountByOwnerView(generics.RetrieveAPIView):
#     serializer_class = serializers.PostSerializer

#     def retrieve(self, request, *args, **kwargs):
#         owner_name= self.kwargs['owner_name']
#         post_count = Post.objects.filter(owner=owner_name).count()
#         return Response({'owner_name': owner_name, 'post_count': post_count})





# class CommentList(generics.ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = serializers.CommentSerializer


# class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = serializers.CommentSerializer

#     def patch(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.likes += 1
#         instance.save()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def patch(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.dislikes += 1
#         instance.save()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     # views.py





# class CategoryList(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = serializers.CategorySerializer


# class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = serializers.PostSerializer



# class RatingList(generics.ListCreateAPIView):
#     queryset = Rating.objects.all()
#     serializer_class = serializers.RatingSerializer



# class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Rating.objects.all()
#     serializer_class = serializers.RatingSerializer





# class PostTotalRating(APIView):
#     def get(self, request, post_id):
#         total_rating = Rating.objects.filter(post=post_id).aggregate(Avg('ratings'))['ratings__avg']
#         return Response({'total_rating': total_rating})
# class PostviewedList(generics.ListCreateAPIView):
#     queryset = Postviewed.objects.all()
#     serializer_class = serializers.PostviewedSerializer
# class PostviewedDetail(generics.RetrieveDestroyAPIView):
#     queryset = Postviewed.objects.all()
#     serializer_class = serializers.PostviewedSerializer

#     def retrieve(self, request,pk= Post.id, *args, **kwargs):
#         instance = self.get_object()
#         #instance.content_views += 1
#         instance.pk += 1
#         instance.save()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)



# def nodejs_view(request):
#     response = requests.get('http://localhost:3000')

#     if response.status_code== 200:
#         data =response.json()
#         return data
#     else:
#         return None

