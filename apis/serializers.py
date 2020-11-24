from rest_framework import serializers
from trvaelblogs import models


class TravelBlogsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'place_name',
            'district_name',
            'country_name',
            'about',
            'description',
            'image',
            'video_url',
            'post_date'
        )
        model = models.TravelBlog



class TravelPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'place_name',
            'district_name',
            'country_name',
            'image',
            'post_date'
        )
        model = models.TravelPlace

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'food_name',
            'famous_in_city',
            'famous_in_country',
            'about',
            'description',
            'image',
            'post_date'
        )
        model = models.Food

class DramaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'drama_name',
            'famous_in_country',
            'about',
            'description',
            'image',
            'video_url',
            'post_date'
        )
        model = models.Drama


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'app_name',
            'about_us',
            'privacy_policy',
            'image',
            'facebook',
            'instagram',
            'youtube',
        )
        model = models.About