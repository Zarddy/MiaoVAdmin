from django.db import models

# Create your models here.


class Category(models.Model):
    """
    分类
    """
    parent_id = models.IntegerField(default=0) # 父级分类id
    title = models.CharField(max_length=100) # 标题
    cover = models.CharField(max_length=200) # 封面图
    source_url = models.CharField(max_length=200) # 源数据链接
    type = models.IntegerField(default=0) # 文章类型，默认0：普通文章，1：视频下载，2：相册文章（纯图片）
    sort = models.IntegerField(default=9) # 排序
    comment = models.CharField(max_length=200) # 备注

    def __str__(self):
        return self.title


class Article(models.Model):
    """
    文章
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100) # 标题
    cover = models.CharField(max_length=200) # 封面图
    content = models.CharField(max_length=500) # 详细内容
    http_download_link = models.CharField(max_length=200) # http 下载链接
    xunlei_download_link = models.CharField(max_length=200) # 迅雷下载链接
    update_time = models.DateTimeField('date published') # 更新时间

    def __str__(self):
        return self.title
