from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from users.models import User
from articles.serializers import ArticleListSerializer


class UserProflieSerializer(serializers.ModelSerializer):
    followers = serializers.StringRelatedField(many=True)
    followings = serializers.StringRelatedField(many=True)
    followings_count = serializers.SerializerMethodField()
    article_set = ArticleListSerializer(many=True)
    like_articles = ArticleListSerializer(many=True)

    def get_followings_count(self, obj):
        return obj.followings.count()

    class Meta:
        model = User
        fields = ("id", "email", "followings", "followers",
                  "followings_count", "article_set", "like_articles")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user

    def update(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token
