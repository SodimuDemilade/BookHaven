from django.db import models
import uuid
from users.models import User
import authors2

# Create your models here.
class Book(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = True)
    title = models.CharField(max_length=255)
    description = models.TextField(default="A book")
    image = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    price = models.FloatField()
    # content = models.FileField()
    content = models.TextField(default="hi")
    author = models.ForeignKey(authors2.models.Author, on_delete=models.CASCADE, default=0, related_name='book_set')
    contributors = models.CharField(max_length=255)
    contributors_role = models.CharField(max_length=255)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

    # def get_absolute_url(self):
    #     return reverse('books:single',kwargs={'username':self.Author.username,'pk':self.pk})
    #     # we will use primary key as a way to link post back to url


    def __str__(self):
        return self.title


class Review(models.Model):
    rating_choices = (
        ('1', 'One Star'),
        ('2', 'Two Stars'),
        ('3', 'Three Stars'),
        ('4', 'Four Stars'),
        ('5', 'Five Stars'),
    )
    id = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=False)
    comment = models.CharField(max_length=255)
    ratings = models.CharField(choices=rating_choices, max_length=4, default="1")
    date_created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.comment
