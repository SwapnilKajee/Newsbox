from turtle import home
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from datetime import *
from django.utils import timezone
from django.urls import reverse_lazy
from news_portal.models import Category, News
from django.views.generic import View, ListView, CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from news_portal.forms import NewsForm, RegisterForm, Contact, Newsletter, Comment
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

PAGINATE_BY = 6 

class Register(SuccessMessageMixin, CreateView):
    template_name = "registration/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    success_message  = "User have been successfully REGISTERED. Please login with your username and password !"
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Please enter the details correctly.")
        return redirect('register')

class LoginView(SuccessMessageMixin, LoginView):
    success_url = reverse_lazy('home')
    success_message = "You are successfully LOGGED IN. Welcome to the NewsBox !"
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Username or password is incorrect. Please enter the correct details !")
        return redirect('login')

class LogoutView(SuccessMessageMixin, LogoutView):
    success_url = reverse_lazy('home')
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, 'You have successfully LOGGED OUT !')
        return response

class HomePageView(ListView):
    model = "News"
    template_name = "index.html"
    context_object_name = "news"
    queryset = News.objects.filter(status="published").order_by("-published_at")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['most_viewed'] = (News.objects.filter(status="published").order_by("-views_count").first())
        context['recent_news'] = News.objects.filter(status="published").order_by("-created_at")
        context['top_categories'] = Category.objects.all()
        return context

class NewsDetailView(DetailView):
    model = News
    template_name = "main/news_detail.html"
    context_object_name = "news"
    def get_context_data(self, **kwargs):
        obj = self.get_object()
        obj.views_count += 1
        obj.save()
        context = super().get_context_data(**kwargs)
        return context

class NewsCategory(ListView):
    model = News
    template_name = "main/categories.html"
    context_object_name = "news"
    paginate_by = PAGINATE_BY
    def get_queryset(self):
        super().get_queryset()
        queryset = News.objects.filter(status = "published", category=self.kwargs["cat_name"]).order_by("-published_at")
        return queryset

class NewsTag(ListView):
    model = News
    template_name = "main/categories.html"
    context_object_name = "news"
    paginate_by = PAGINATE_BY
    def get_queryset(self):
        super().get_queryset()
        queryset = News.objects.filter(status = "published", tag=self.kwargs["tag_id"]).order_by("-published_at")
        return queryset

class AddNewsView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = News
    form_class = NewsForm
    template_name = "main/add_news.html"
    success_url = reverse_lazy("home")  
    success_message  = "Your news has been successfully PUBLISHED."
    def form_valid(self, form):
        news = form.save(commit=False)
        form.instance.author = self.request.user
        news.status = "published"
        news.published_at = timezone.now()
        news.save()
        form.save_m2m()
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Please enter the details properly.")
        return redirect('register')

class MyNewsView(LoginRequiredMixin, ListView):
    model = News
    template_name = "main/my_news.html"
    context_object_name = "news"
    paginate_by = PAGINATE_BY
    def get_queryset(self):
        super().get_queryset()
        queryset = News.objects.filter(author__id=self.request.user.id).order_by("-published_at")
        return queryset

class UpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = News
    form_class = NewsForm
    template_name = "main/add_news.html"
    success_url = reverse_lazy("home")
    success_message  = "Your news has been successfully UPDATED."
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Please enter the details properly.")
        return redirect('register')

class DeleteView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        news = get_object_or_404(News, pk=pk)
        news.delete()
        return redirect("home")

class Contact(View):
    template_name = "contact.html"
    form_class = Contact
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    def post(self, request, *args, **kwargs):
        is_ajax = request.headers.get("x-requested-with")
        if is_ajax == "XMLHttpRequest":   
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({"success": True}, status=200)
        return JsonResponse({"success": False}, status=400)

class Newsletter(View):
    form_class = Newsletter
    def post(self, request, *args, **kwargs):
        is_ajax = request.headers.get("x-requested-with")
        if is_ajax == "XMLHttpRequest":   
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({"success": True}, status=200)
        return JsonResponse({"success": False}, status=400)

class CommentView(View):
    form_class = Comment
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        post_id = request.POST["post"]
        if form.is_valid():
            form.save()
        return redirect("news-detail", post_id)

class NewsSearchView(View):
    template_name = 'main/news_search.html'
    paginate_by = PAGINATE_BY
    def get(self, request, *args, **kwargs):
        query = request.GET["query"]
        news_list = News.objects.filter( (Q(title__icontains=query) | Q(content__icontains=query) | Q(author__username__icontains=query)) & Q(status="published")).order_by("-published_at")
        page = request.GET.get("page", 1)
        paginator = Paginator(news_list, PAGINATE_BY)
        try:
            news = paginator.page(page)
        except PageNotAnInteger:
            news = paginator.page(1)
        except EmptyPage:
            news = paginator.page(paginator.num_pages)
        return render(request, self.template_name, {"page_obj":news, "query":query})
    
 