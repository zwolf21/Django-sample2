from django.contrib import admin
from blog.models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    '''
        Admin View for Post
    '''
    list_display = ('title','modify_date') # 포스트 객체를 보여줄 때 title과 modify_date를 화면에 출력 하라고 지정
    list_filter = ('modify_date',) # modify_date 컬럼을 사용하는 필터 사이드바를 보여주도록 지정
    search_fields = ('title','content') # 검색박스 설치 
    prepopulated_fields = {'slug':('title',)} # slug 필드는 title 필드를 이용해 미리 채워 지도록 설정

admin.site.register(Post, PostAdmin)