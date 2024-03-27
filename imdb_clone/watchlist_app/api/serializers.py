from rest_framework import serializers
from watchlist_app.models import WatchList, StreamingPlatform, Reviews


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['id', 'rating', 'description', 'created', 'watchlist', 'active', 'updated']
        read_only_fields = ['id', 'created']


class WatchListSerializer(serializers.ModelSerializer):

    # len_title = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = ['id', 'title', 'storyline', 'active', 'created', 'platform', 'reviews']
        read_only_fields = ['id', 'created']

    # def get_len_title(self, obj):
    #     len_title = len(obj.title)
    #     return len_title

    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Name must be at least 2 characters long.')
        else:
            return value

    def validate(self, data):
        if data['title'] == data['storyline']:
            raise serializers.ValidationError('Title and storyline cannot be the same.')
        else:
            return data


class StreamingPlatformSerializer(serializers.ModelSerializer):

    watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist = serializers.StringRelatedField(many=True, read_only=True)
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True, read_only=True, view_name="watch_list_detail_view", lookup_field='id'
    #     )
    # watchlist = serializers.HyperlinkedIdentityField()

    class Meta:
        model = StreamingPlatform
        fields = ['id', 'name', 'about', 'website', 'created', 'watchlist']
        read_only_fields = ['id', 'created']


# URL instead of ID (HyperlinkedModelSerializer)
# class StreamingPlatformSerializer(serializers.HyperlinkedModelSerializer):

#     watchlist = WatchListSerializer(many=True, read_only=True)
#     # watchlist = serializers.StringRelatedField(many=True, read_only=True)
#     # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     # watchlist = serializers.HyperlinkedRelatedField(
#     #     many=True, read_only=True, view_name="watch_list_detail_view", lookup_field='id'
#     #     )
#     # watchlist = serializers.HyperlinkedIdentityField()

#     class Meta:
#         model = StreamingPlatform
#         fields = ['url', 'id', 'name', 'about', 'website', 'created', 'watchlist']
#         read_only_fields = ['id', 'created']

#         extra_kwargs = {
#             'url': {'view_name': 'watch_list_detail_view', 'lookup_field': 'id'}
#         }


# def title_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('Name must be at least 2 characters long.')
#     return value
    # title = serializers.CharField(validators=[title_length])


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         instance = Movie.objects.create(**validated_data)
#         return instance

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()

#         return instance

#     # Field level validation
#     def validate_title(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError('Name must be at least 2 characters long.')
#         else:
#             return value

#     def validate(self, data):
#         if data['title'] == data['description']:
#             raise serializers.ValidationError('Title and description cannot be the same.')
#         else:
#             return data