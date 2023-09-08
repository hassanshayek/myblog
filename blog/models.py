from django.db import models
from accounts.models import CustomUser 

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  

    def __str__(self):
        return self.title

class BlogReview(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    blog_post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(7)])
    review_text = models.TextField()

    def __str__(self):
        return f"Review by {self.user.username} on {self.blog_post.title}"


class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    blog_post = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s favorite: {self.blog_post.title}"
