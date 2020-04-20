from django.views.generic import TemplateView, ListView
from .models import Product


class Home(TemplateView):
    template_name = 'mamazon/home.html'


class ProductListView(ListView):
    model = Product
    template_name = 'mamazon/list.html'

    def get_queryset(self):
        # 全ての商品をまず入れる
        queryset = Product.objects.all()
        # もしクエリが検索バーのゲットに入っていたら
        if 'query' in self.request.GET:
            # qs<- 自分の検索したワード
            qs = self.request.GET['query']
            # querysetにフィルターをかけてやる
            queryset = queryset.filter(name__contains=qs)
        return queryset
