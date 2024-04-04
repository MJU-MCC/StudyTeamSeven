from django.db import models

# Create your models here.

class Post(models.Model):   #포스트(글) 작성
    title = models.CharField("포스트 제목", max_length = 100)   #포스트의 제목 글자크기 설정 
    content = models.TextField("포스트 내용")   #포스트의 내용물 (CharField는 글자 수가 상수, TextField는 변할 수 있음)
    thumbnail = models.ImageField("썸네일 이미지", upload_to="post", blank=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):    #댓글 작성
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    content = models.TextField("댓글 내용")

    def __str__(self):
        return f"{self.post.title}의 댓글 (ID: {self.id})"