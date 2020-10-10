from django.views.generic import ListView

from articles.models import Article


class ArticleListView(ListView):
    template_name = 'articles/news.html'
    model = Article
    ordering = '-published_at'

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        for article in context['object_list']:
            article.sorted_scopes = article.scopes.all().order_by('name')
        return context

