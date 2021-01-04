from django.shortcuts import render, get_object_or_404
from .models import Post

def all_blogs(request):
	title = 'blog main page'

	# posts = Post.objects.all()
	posts = Post.objects.order_by('-date_posted')  	#[:5]
	return render(request, 'blog/all_blogs.html', {'title': title, 'posts': posts})

def detail(request, blog_id):
	post = get_object_or_404(Post, pk=blog_id)
	return render(request, 'blog/detail.html', {'post':post})
