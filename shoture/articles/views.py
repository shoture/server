from .models import Article
from .serializers import ArticleSerializer

from support.json_response import JSONResponse

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def article_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return JSONResponse(serializer.data)