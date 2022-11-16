from django.db import models

class Time(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True

class Category(Time):
    name = models.CharField(max_length=20) 
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Tag(Time):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name 

class News(Time):
    title = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    tag = models.ManyToManyField(Tag)
    content = models.TextField()
    image = models.ImageField(upload_to="news_images/%Y/&m/%d", blank=False)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    published_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[("published","published"),("unpublished","unpublished")], default="unpublished")
    views_count = models.PositiveBigIntegerField(default=0)
    def __str__(self):
        return self.title
    class Meta():
        verbose_name = "News"
        verbose_name_plural = "News"
    
    @property
    def new_comments(self):
        comments = Comment.objects.filter(post=self).order_by("-created_at")
        return comments

class Contact(Time):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length= 100)
    message = models.TextField()
    def __str__(self):
        return self.subject
    
class Newsletter(Time):
    email = models.EmailField()
    def __str__(self):
        return self.email

class Comment(Time):
    post = models.ForeignKey('News', on_delete=models.CASCADE, related_name="comments")
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.message