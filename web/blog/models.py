from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from rest_framework.reverse import reverse_lazy
from taggit.models import TaggedItemBase, TagBase
from taggit.managers import TaggableManager
from .choices import ArticleStatus

User = get_user_model()


class ArticleTag(TagBase):
    objects = models.Manager()

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class TaggedArticle(TaggedItemBase):
    content_object = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='tagged_article')
    tag = models.ForeignKey(ArticleTag, related_name='tagged_article', on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ('-id',)

    def save(self, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        return super().save(**kwargs)


class Article(models.Model):

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='article_set')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, allow_unicode=True, unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='article_set')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.PositiveSmallIntegerField(choices=ArticleStatus.choices, default=ArticleStatus.INACTIVE)
    image = models.ImageField(upload_to='articles/', blank=True, default='no-image-available.jpg')

    tags = TaggableManager(through=TaggedArticle, related_name='article_tags', blank=True)

    objects = models.Manager()

    @property
    def short_title(self) -> str:
        return self.title[:30]

    def __str__(self) -> str:
        return '{title} - {author}'.format(title=self.short_title, author=self.author)

    @staticmethod
    def get_slug(title: str) -> str:
        return slugify(title, allow_unicode=True)

    def save(self, **kwargs):
        self.slug = self.get_slug(self.title)
        return super().save(**kwargs)

    def get_absolute_url(self):
        return reverse_lazy('blog:post-detail', kwargs={'slug': self.slug})

    # def likes(self) -> int:
    #     return self.votes.likes().count()
    #
    # def dislikes(self) -> int:
    #     return self.votes.dislikes().count()

    def tag_list(self) -> str:
        return u", ".join(o.name for o in self.tags.all())

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
        ordering = ('-updated', '-created', 'id')


class Comment(models.Model):
    author = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment_set', blank=True)
    content = models.TextField(max_length=200)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment_set')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='parent_set', blank=True, null=True)
    objects = models.Manager()

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
        ordering = ('-id',)

    def __str__(self):
        return '{author}: {article}'.format(author=self.author, article=self.article.title)
