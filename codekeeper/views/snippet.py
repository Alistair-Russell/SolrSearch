from rest_framework import generics
from rest_framework import renderers
from codekeeper.models.snippet import Snippet
from codekeeper.serializers.snippet import SnippetSerializer
from codekeeper.renderers.custom_html_renderer import CustomHTMLRenderer


class SnippetList(generics.ListCreateAPIView):
    # ListCreate details what HTTP commands we are extended
    # so there are implicitly defined get and post methods
    # you can simply go into the django rest framework and look at this class to see this!!!!
    template_name = "snippet/snippet_list.html"
    renderer_classes = (CustomHTMLRenderer,
                        renderers.JSONRenderer,
                        renderers.BrowsableAPIRenderer)
    model = Snippet
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    template_name = "snippet/snippet_detail.html"
    renderer_classes = (CustomHTMLRenderer,
                        renderers.JSONRenderer,
                        renderers.BrowsableAPIRenderer)
    model = Snippet
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()
