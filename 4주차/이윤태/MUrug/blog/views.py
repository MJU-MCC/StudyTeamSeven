from django.shortcuts import render, redirect
from blog.models import Post, Comment

def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts" : posts,
    }
    return render(request, "post_list.html", context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        comment_content = request.POST["comment"]
        Comment.objects.create(
            post = post,
            content = comment_content,
        )
    context = {
        "post" : post,
    }
    return render(request, "post_detail.html", context)

def post_add(request):
    if request.method == "POST":
        title = request.POST["title"]
        singer = request.POST["singer"]
        content = request.POST["content"]
        lyrics = request.POST["lyrics"]
        thumbnail = request.FILES.get("thumbnail")
        post = Post.objects.create(
            title = title,
            singer = singer,
            content = content,
            lyrics = lyrics,
            thumbnail = thumbnail,
        )
        return redirect(f"/post/{post.id}") # 새로 생성된 post 링크로 이동
    return render(request, "post_add.html")
# Create your views here.
