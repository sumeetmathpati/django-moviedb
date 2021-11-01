from rest_framework import serializers
from watchlist.models import Movie

def name_length(value): 
    
    if len(value) < 2:
         raise serializers.ValidationError('Name is too short!')

class MovieSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    rating = serializers.IntegerField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data): 
        instance.name = validated_data.get('name')
        instance.description = validated_data.get('description')
        instance.rating = validated_data.get('rating')
        return instance 
    
    # def validate_name(self, value):

    #     if len(value) < 2:
    #         raise serializers.ValidationError('Name is too short!')
        
    #     return value
    
    
        
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and description must not be same!')
        
        return data