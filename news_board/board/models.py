from django.db import models


class Post(models.Model):
    title = models.CharField('Title', max_length=60)
    link = models.CharField('Link', max_length=200)  # todo replace with url field
    creation_date = models.DateTimeField('Creation date', auto_now_add=True)
    amount_of_upvotes = models.PositiveIntegerField('Amount of upvotes', default=0)
    author_name = models.CharField('Author name', max_length=120)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Comment(models.Model):
    post = models.ForeignKey(Post, verbose_name='post', on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField('Author name', max_length=120)
    content = models.CharField('Content', max_length=400)
    creation_date = models.DateTimeField('Creation date', auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
