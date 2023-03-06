from rest_framework import serializers
from sotinyurl.tinyurls.models import TinyUrl

class TinyUrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = TinyUrl
        fields = [
            "id",
            "tiny_url",
            "redirect_to"
        ]

class TinyUrlDetailSerializer(TinyUrlSerializer):
    class Meta(TinyUrlSerializer.Meta):
        fields = TinyUrlSerializer.Meta.fields + [
            "valid_to",
            "owner",
            "created_at",
            "updated_at"
        ]
