# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class Post(models.Model):
	title = models.CharField('TITLE', max_length=50) 
		# 레이블 : TITLE
	slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias') 
		# slug 필드 : 페이지나 포스트를 설명하는 핵심단어집합,  unique 옵션주어 기본키 및 url에 사용, 형식:django-sample
		# unique: 포스트 검색시 기본키로 사용 
		# allow_unicode: 한글사용 가능하게 하기 
	description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text')
		# blank: 빈칸가능
	content = models.TextField('CONTENT')
		# TextField : 여러줄 입력 가능 
	create_date = models.DateTimeField('Creat Date', auto_now_add=True)
		# auto_now_add : 개체가 생성될 때의 시간을 자동으로 기록
	modify_date = models.DateTimeField('Modify Date', auto_now=True)
		# auto_now : 객체가 변경 될 때의 시간을 기록

	class Meta:
	# Meta : 필드 속성 외에 필요한 파라미터 설정
	    verbose_name = "post"
	    # 테이블의 단수 별칭
	    verbose_name_plural = "posts"
	    # 테이블의 복수 별칭
	    db_table = 'my_post'
	    # 데이터베이스에 실제 저장되는 테이블의 이름, 이항목을 생략하면 기본값으로 blog_post 가됨
	    ordering = ('-modify_date',)
	    # 모델객체의 리스트 출력시 modify_date 컬럼 기준으로 내림차순 정렬

	def __str__(self):
	    return self.title # 객체대표 문자열

	def get_absolute_url(self): 
		return reverse('blog:post_detail', args=(self.slug,))
		# 객체를 지칭하는 url 을 반환

	def get_previous_post(self):
		return self.get_previous_by_modify_date()
		# modify_date 컬럼을 기준으로 이전 포스트를 반환 

	def get_next_post(self):
		return self.get_next_by_modify_date()
