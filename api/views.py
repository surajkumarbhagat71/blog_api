from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated




class CategoryView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self,request):
        try:
            cat = Category.objects.all()
            serializer = CategorySerilizer(cat,many=True)
            return Response(serializer.data)
        except:
            return Response({'data not avalable'})



class Home(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self,request):
        try:
            blog = Blog.objects.all()
            serializer = BlogSerilizer(blog,many=True,context={'request': request})
            return Response(serializer.data)
        except:
            return Response({'data not avalable'})
     
    # def post(self,request):
    #     blog_list = []
    #
    #     blog = Blog.objects.all()
    #     for x in blog:
    #
    #         data = {
    #             'title':x.title,
    #             'dis':x.description,
    #             'image':request.build_absolute_uri(x.image.url)
    #         }
    #
    #         blog_list.append(data)
    #     return Response(blog_list)



class AddBlog(APIView):
    def post(self,request):
        data = request.data

        blog = Blog()
        blog.title = data['title']
        blog.description = data['description']
        blog.category = data['categorty_id']
        blog.image = data['image']
        blog.save()
        return Response({'Blog add successfully'})



