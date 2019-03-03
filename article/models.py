from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE, verbose_name = "Kullanıcı")
    #başka tablo ile eşleştirdik, kullanıcı silinirse makale de silinecek
    title = models.CharField(max_length = 50, verbose_name = "Başlık")
    #CK editor gelince bunu sildik
    #content = models.TextField(verbose_name="İçerik")
    content = RichTextField(verbose_name = "İçerik")
    #kayıt zamanı otomatik olarak eklenecek
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    #Bu alanı sonradan ekledik. Makale resimleri için. Gerekli updatelerin yapılması için compile yapılmalı. makemigrations +migrate
    image = models.FileField(blank = True, null = True, verbose_name="Makaleye Foto Ekle", upload_to='documents/')
    def __str__(self):
        return self.title
    #bkz Django model ordering
    #sonradan ekledik. 
    class Meta:
        ordering = ['-created_date'] #- ile son girilen makalenin ilk gösterilmesi sağlanıyor


#makalelere yorum eklemek için koyduk
#admin sayfasına eklenmesi lazım, bkz admin
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE, verbose_name = "Makale", related_name="comments")
    comment_author = models.CharField(max_length = 50, verbose_name = "İsim")
    comment_content = models.CharField(max_length = 200, verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.comment_content
    #bkz Django model ordering
    #sonradan ekledik. 
    class Meta:
        ordering = ['-comment_date'] #- ile son girilen makalenin ilk gösterilmesi sağlanıyor
