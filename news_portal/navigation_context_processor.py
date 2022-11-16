from news_portal.models import News, Category, Tag
def navigation(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    latest_news = News.objects.filter(status="published").order_by("-created_at")[:5]
    trending_news = News.objects.filter(status="published").order_by("-views_count")
    return {"categories":categories, "tags":tags, "latest_news":latest_news, "trending_news":trending_news}
