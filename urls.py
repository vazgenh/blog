from django.conf.urls import patterns, include, url
from django.contrib import admin

from posts.views import home_blog, author_posts, post

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'home/', home_blog),
	url(r'author_posts/<profile_id>', author_posts),
	url(r'posts/<post_id>', post),

)
