from rest_framework import serializers
from watchlist.models import Media, Platform, Review

class ReviewSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = '__all__'
        # exclude = ['media']

class MediaSerializer(serializers.ModelSerializer):

    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Media
        fields = '__all__'
        # fields = ['id', 'name', 'description', 'reviews']
        # exclude = ['description'] 
        
class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    
    media = MediaSerializer(many=True, read_only=True)

    class Meta:
        model = Platform
        fields = '__all__' 
        # fields = ['name', 'about', 'website', 'media'] 
    

# class MovieSerializer(serializers.Serializer):
#     id = serializers.CharField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     rating = serializers.IntegerField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data): 
#         instance.name = validated_data.get('name')
#         instance.description = validated_data.get('description')
#         instance.rating = validated_data.get('rating')
#         return instance 
    
    # def validate_name(self, value):

    #     if len(value) < 2:
    #         raise serializers.ValidationError('Name is too short!')
        
    #     return value
    
    
        
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError('Name and description must not be same!')
        
    #     return data