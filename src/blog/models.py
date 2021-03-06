from datetime import date

from django.db import models
from django.urls import reverse

from organizer.models import Startup, Tag


class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(
        max_length=63, unique_for_month="pub_date", help_text="A label for URL config"
    )
    text = models.TextField()
    pub_date = models.DateField("date published", default=date.today)
    tags = models.ManyToManyField(Tag, related_name="blog_posts")
    startups = models.ManyToManyField(Startup, related_name="blog_posts")

    class Meta:
        get_latest_by = "pub_date"
        ordering = ["-pub_date", "title"]
        verbose_name = "blog post"

    def __str__(self):
        date_string = self.pub_date.strftime("%Y-%m-%d")
        return f"{self.title} on {date_string}"

    def get_absolute_url(self):
        return reverse(
            'post_detail',
            kwargs={
                'year': self.pub_date.year,
                'month': self.pub_date.month,
                'slug': self.slug
            }
        )
