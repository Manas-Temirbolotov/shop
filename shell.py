import json
import io
from datetime import datetime
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class Comment:
    def __init__(self,name, code):
        self.name = name
        self.code = code
        self.create = datetime.now()


class CommentSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=20)
    code = serializers.IntegerField()
