from rest_framework import serializers
from sotinyurl.tinyurls.models import TinyUrl

class TinyUrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = TinyUrl
        fields = [
            "tiny_url",
            "redirect_to"
        ]