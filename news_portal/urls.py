from django.contrib import admin
from django.urls import path
from news_portal import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("accounts/registration/", views.Register.as_view(), name="register"),
    path("accounts/login/", views.LoginView.as_view(), name="login"),
    path("accounts/logout/", views.LogoutView.as_view(), name="logout"),
    path("news-detail/<int:pk>/", views.NewsDetailView.as_view(), name="news-detail"),
    path("news-category/<int:cat_name>/", views.NewsCategory.as_view(), name="news-category"),
    path("add-news/", views.AddNewsView.as_view(), name="add-news"),
    path("my-news/", views.MyNewsView.as_view(), name="my-news"),
    path("update-news/<int:pk>/", views.UpdateView.as_view(), name="update-news"),
    path("delete-news/<int:pk>/", views.DeleteView.as_view(), name="delete-news"),
    path("contact/", views.Contact.as_view(), name="contact"),
    path("newsletter", views.Newsletter.as_view(), name="newsletter"),
    path("comment/", views.CommentView.as_view(), name="comment"),
    path("news-search/", views.NewsSearchView.as_view(), name="news-search"),
]
  