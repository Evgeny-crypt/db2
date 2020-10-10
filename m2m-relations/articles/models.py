from django.db import models


class Scope(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'РАЗДЕЛ'
        verbose_name_plural = 'РАЗДЕЛЫ'

    def __str__(self):
        return self.name


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    scopes = models.ManyToManyField(Scope, through='ArticleScope')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class ArticleScope(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE)
    base_scope = models.BooleanField(verbose_name='ОСНОВНОЙ')

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематики статьи'

    def __str__(self):
        return f'{self.article}_{self.scope}'

