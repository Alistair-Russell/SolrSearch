from rest_framework import views
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.reverse import reverse
from codekeeper.renderers.custom_html_renderer import CustomHTMLRenderer


class HomePageView(views.APIView):
    template_name = "index.html"
    renderer_classes = (CustomHTMLRenderer,
                        renderers.JSONRenderer,
                        renderers.BrowsableAPIRenderer)

    def get(self, request, *args, **kwargs):
        response = Response({
            # using the reverse function we can look up the urls given these names
            # this is useful if the url changes or someone else wants to run this on their localhost
            'snippets': reverse('snippet-list', request=request),
            'tags': reverse('tag-list', request=request),
            'people': reverse('person-list', request=request)
        })
        return response