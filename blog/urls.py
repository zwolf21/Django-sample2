from django.conf.urls import url
from blog.views import *

# blog 의 이름 공간에 있는 url패턴들
# 패턴 접근시 blog:index, blog:post_month_archive 등 blog:로 blog라는 이름 공간 명시


urlpatterns = [
	# Example: /
	url(r'^$', PostLV.as_view(), name='index'),
	
	# Example: /post/ , PostLV 는 /, /post/ 두가지 요청을 처리
	url(r'^post/$', PostLV.as_view(), name='post_list'), 
	
	# Example: /post/django-example/
	url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail')

	# Example: /archive/
	url(r'^archive/$', PostAV.as_view(), name='post_archive'),

	# Example: /2012/
	url(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),

	# Example: /2012/nov/
	url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_month_archive'),

	# Example: /2012/nov/10/
	url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),

	# Example: /today/
	url(r'^today/$', PostTAV.as_view(), name='post_today_archive')
]