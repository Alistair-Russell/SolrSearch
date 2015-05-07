from codekeeper.models.snippet import Snippet
from codekeeper.models.tag import Tag
from codekeeper.models.person import Person
from rest_framework import serializers
# from codekeeper.serializers.person import PersonSerializer
# this would be a bad idea because in PersonSerializer you will need to import SnippetSerializer


class PersonSnippetSerializer(serializers.HyperlinkedModelSerializer):
    # CreatorSnippetSerializer(serializers.HyperlinkedModelSerializer):
    # full_name = serializers.ReadOnlyField()
    class Meta:
        model = Person
        fields = ("first_name", "last_name", "full_name", "url")
        #fields = ('url', 'full_name')


class TagSnippetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ("name", "url")


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSnippetSerializer(many=True)

    creator = PersonSnippetSerializer()
    # creator = CreatorSnippetSerializer()

    class Meta:
        model = Snippet