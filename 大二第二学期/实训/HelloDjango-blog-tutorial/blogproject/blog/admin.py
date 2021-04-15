from django.contrib import admin

from django.contrib import admin
from .models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):  # 将此 Modeladmin 关联注册的 model 实例保存到数据库。
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    # 标题 创建时间 修改时间 分类 作者
    fields = ['title', 'body', 'excerpt', 'category', 'tags']
    # 标题 正文 摘要 分类 标签

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)
        # 这里调用父类的save_model()


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
# Register your models here.
