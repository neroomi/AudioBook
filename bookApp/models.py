from django.db import models


# Create your models here.



class BookTb(models.Model):
    book_id = models.AutoField(db_column='BOOK_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('UserTb', models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BOOK_TB'


class ContentTb(models.Model):
    content_id = models.AutoField(db_column='CONTENT_ID', primary_key=True)  # Field name made lowercase.
    sentence_id = models.IntegerField(db_column='SENTENCE_ID')  # Field name made lowercase.
    text = models.TextField(db_column='TEXT')  # Field name made lowercase.
    feelring = models.IntegerField(db_column='FEELRING')  # Field name made lowercase.
    book = models.ForeignKey(BookTb, models.DO_NOTHING, db_column='BOOK_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTENT_TB'


class UserTb(models.Model):
    user_id = models.CharField(db_column='USER_ID', primary_key=True, max_length=30, verbose_name='Id')  # Field name made lowercase.
    pw = models.CharField(db_column='PW', max_length=30, verbose_name='Password')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=30, verbose_name='Name')  # Field name made lowercase.
    e_mail = models.CharField(db_column='E_MAIL', max_length=50, verbose_name='E-mail')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USER_TB'


