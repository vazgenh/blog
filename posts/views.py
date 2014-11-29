from django.shortcuts import render, render_to_response
from django.template import RequestContext
from authors.models import Author
from posts.models import Post
# Create your views here.



def home_blog(request):
	first_author = Author.objects.all()[0]
	first_posts = Post.objects.filter(post_author=first_author).all()
	return render_to_response('index.html',
                          {'gago':first_posts},
                          context_instance=RequestContext(request))

def author_posts(request):

	return render_to_response('author_posts.html',
                          {},
                          context_instance=RequestContext(request))

def post(request):

	return render_to_response('post.html',
                          {},
                          context_instance=RequestContext(request))
