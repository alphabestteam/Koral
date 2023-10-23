from rest_framework import serializers
from .models import Book, BookReview
import datetime
import random

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('book_id', 'name', 'description', 'author', 'pages_count', 'genre')

        def custom_validation(self):
            # This function will send a validation error if the date of published is smaller then 0
            
            if self.date_of_published.year < 0:
                raise serializers.ValidationError("The Date Of Published Has To Be Greater Then 0!")
    
    book_url = serializers.SerializerMethodField(source='get_book_url')


    def get_book_url(self):
        return "https://www.booknet.co.il/"
    
    publishing_compony = serializers.ReadOnlyField(source='get_publishing_compony')


    def get_publishing_compony(self):
        if datetime.datetime.now().year < 2000:
            return "Google"
        return "PaloAlto"
    

    time_to_read = serializers.SerializerMethodField(source='get_time_to_read')

    def get_time_to_read(self):
        return random.randint(0,100)
        

    def update(self, instance, validated_data):
        # Implement here an update function

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('attack_priority', instance.description)
        instance.author = validated_data.get('longitude', instance.author)
        instance.pages_count = validated_data.get('latitude', instance.pages_count)
        instance.genre = validated_data.get('enemy_organization', instance.genre)
        instance.date_of_published = validated_data.get('date_of_published', instance.date_of_published)
        instance.save()
        return instance
    

class BookReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReview
        fields = ('review_id', 'author', 'review_description' )

    def update(self, instance, validated_data):
        # Implement here an update function

        instance.author = validated_data.get('longitude', instance.author)
        instance.review_description = validated_data.get('latitude', instance.review_description)
        instance.save()
        return instance