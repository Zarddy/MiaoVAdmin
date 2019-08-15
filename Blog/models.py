from django.db import models

# Create your models here.


class Category(models.Model):
    """
    分类
    """
    uid = models.TextField()                    # 唯一id
    parent_id = models.IntegerField(default=0)  # 父级分类id
    title = models.TextField()                  # 标题
    cover = models.TextField()                  # 封面图
    source = models.TextField(default='')       # 源数据链接
    type = models.IntegerField(default=0)       # 文章类型，默认0：普通文章，1：视频下载，2：相册文章（纯图片）
    sort = models.IntegerField(default=9)       # 排序
    comment = models.TextField(default='')      # 备注

    def __str__(self):
        return self.title


class Article(models.Model):
    """
    文章
    """
    uid = models.TextField()                    # 唯一id
    title = models.TextField()                  # 标题
    cover = models.TextField()                  # 封面图
    content = models.TextField(default='')      # 详细内容
    http_download_link = models.TextField()     # http 下载链接
    xunlei_download_link = models.TextField()   # 迅雷下载链接
    source = models.TextField(default='')       # 来源
    published_time = models.DateTimeField(auto_now=True)    # 发布时间
    state = models.IntegerField(default=1)      # 状态，是否显示
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
