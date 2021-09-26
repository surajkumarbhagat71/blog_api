from rest_framework import serializers
from .models import *


class CategorySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title','dis']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class BlogSerilizer(serializers.ModelSerializer):
    category_title = serializers.ReadOnlyField(source='category.title')
    category_dis = serializers.ReadOnlyField(source='category.dis')
    image = serializers.SerializerMethodField('get_image_url')

    like = LikeSerializer(many=True,read_only=True)
    comment = CommentSerializer(many=True,read_only=True)


    def get_image_url(self,obj):
        request = self.context.get('request')
        photo_url = obj.image.url
        return request.build_absolute_uri(photo_url)


    class Meta:
        model = Blog
        fields = ['title','description','image','category_title','category_dis','like','comment']

