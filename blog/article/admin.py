from django.contrib import admin

# Register your models here.
from .models import User, Article


# 建立admin管理器
class UserAdmin(admin.ModelAdmin):
    # 配置展示列表，在User板块下的列表进行一个展示
    list_display = ['username', 'email']
    # 配置过滤查询字段，在User板块下右侧进行一个显示
    list_filter = ['username', 'email']
    # 配置搜索字段，在User板块下右侧进行一个搜索
    search_fields = (['username', 'email'])


class ArticleAdmin(admin.ModelAdmin):
    """
    创建UserAdmin类，继承于admin.ModelAdmin，并重写list_display,list_filter,search_fields方法，
    """

    # 配置展示列表，在User板块下的列表进行一个展示
    list_display = ['id', 'title', 'content', 'pub_time']
    # 显示字符段 自增属性无法使用此方法显示
    fields = ('title', 'content', 'pub_time')
    # 配置过滤查询字段，在User板块下右侧进行一个显示
    list_filter = ['title',]
    # 配置搜索字段，在User板块下右侧进行一个搜索
    search_fields = ['title',]



# 绑定User模型到 Useradmin管理后台

admin.site.register(User, UserAdmin)

# 绑定Article模型到 Articleadmin管理后台
admin.site.register(Article, ArticleAdmin)