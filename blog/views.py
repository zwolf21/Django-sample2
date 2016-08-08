from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView

from blog.models import Post

# Create your views here.

class PostLV(ListView):
	model = Post
	template_name = 'blog/post_all.html' # 템플릿 파일: 지정하지 않으면 blog/post_list.html 로 됨
	context_object_name ='posts' # 템플릿 파일로 넘겨주는 객체 리스트 컨텍스트변수 : 지정하지 않으면 object_list 로 됨
	paginate_by = 2 # 한페이지에 보여지는 객체 리스트 수


# 객체 리스트에서 slug 키로 객체를 조회 후 객체 상세 정보 출력 
class PostDV(DetailView):
	model = Post


# 날짜 필드를 기준으로 최신 객체를 먼저 출력
class PostAV(ArchiveIndexView):
	model = Post
	date_field = 'modify_date' # 기준이 되는 날짜 필드

# 테이블의 날짜 필드의 연도를 기준으로 객체리스트를 가져와 그 객체들이 속한 월을 리스트로 출력
class PostYAV(YearArchiveView):
	model = Post
	date_field = 'modify_date'
	make_object_list = True # 템플릿으로 객체의 리스트(object_list)를 넘겨줌

# 날짜의 연월을 기준으로 포스트를 검색
class PostMAV(MonthArchiveView):
	model = Post
	date_field = 'modify_date'

# 날짜필드의 연월일 을 기준으로 객체리스트를 가져옴
class PostDAV(DayArchiveView):
	model = Post
	date_field = 'modify_date'

class PostTAV(TodayArchiveView):
	model = Post
	date_field = 'modify_date'
