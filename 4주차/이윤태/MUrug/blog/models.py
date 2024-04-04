from django.db import models

class Post(models.Model):
    title = models.CharField("곡 제목", max_length=100)
    singer = models.CharField("가수 이름", max_length=20, default="")
    content = models.TextField("곡 소개")
    lyrics = models.TextField("가사", default="")
    thumbnail = models.ImageField("썸네일 이미지", upload_to="post", blank=True, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField("댓글 내용")

    def __str__(self):
        return f"{self.post.title}의 댓글 (ID: {self.id})"