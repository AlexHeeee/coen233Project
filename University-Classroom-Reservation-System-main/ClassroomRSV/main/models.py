#coding:utf-8
from django.db import models

from .model import BaseModel

from datetime import datetime

class xuesheng(BaseModel):
    __doc__ = u'''xuesheng'''
    __tablename__ = 'xuesheng'

    __loginUser__='yonghuzhanghao'


    __authTables__={}
    __authPeople__='yes'
    __loginUserColumn__='yonghuzhanghao'
    __sfsh__='no'
    __authSeparate__='no'
    __thumbsUp__='no'
    __intelRecom__='no'
    __browseClick__='no'
    __foreEndListAuth__='no'
    __foreEndList__='no'
    __isAdmin__='no'
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'create time')
    yonghuzhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='user account' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='name' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='gender' )
    mima=models.CharField ( max_length=255, null=True, unique=False, verbose_name='password' )
    '''
    yonghuzhanghao=VARCHAR
    xingming=VARCHAR
    xingbie=VARCHAR
    mima=VARCHAR
    '''
    class Meta:
        db_table = 'xuesheng'
        verbose_name = verbose_name_plural = 'student'
class jiaoshixinxi(BaseModel):
    __doc__ = u'''jiaoshixinxi'''
    __tablename__ = 'jiaoshixinxi'



    __authTables__={}
    __authPeople__='no'
    __sfsh__='no'
    __authSeparate__='no'
    __thumbsUp__='no'
    __intelRecom__='no'
    __browseClick__='no'
    __foreEndListAuth__='no'
    __foreEndList__='no'
    __isAdmin__='no'
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'create time')
    jiaoshibianhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='classroom id' )
    jiaoshishebei=models.TextField   (  null=True, unique=False, verbose_name='classroom equipment' )
    rongnarenshu=models.IntegerField  (  null=True, unique=False, verbose_name='Capacity' )
    jiaoshizhuangtai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='status' )
    '''
    jiaoshibianhao=VARCHAR
    jiaoshishebei=Text
    rongnarenshu=Integer
    jiaoshizhuangtai=VARCHAR
    '''
    class Meta:
        db_table = 'jiaoshixinxi'
        verbose_name = verbose_name_plural = 'classroom information'
class xueshengshenqing(BaseModel):
    __doc__ = u'''xueshengshenqing'''
    __tablename__ = 'xueshengshenqing'



    __authTables__={'yonghuzhanghao':'xuesheng',}
    __authPeople__='no'
    __sfsh__='yes'
    __authSeparate__='no'
    __thumbsUp__='no'
    __intelRecom__='no'
    __browseClick__='no'
    __foreEndListAuth__='no'
    __foreEndList__='no'
    __isAdmin__='no'
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'addition date')
    yonghuzhanghao=models.CharField ( max_length=255,null=False, unique=False, verbose_name='user account' )
    xingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='name' )
    jiaoshibianhao=models.CharField ( max_length=255,null=False, unique=False, verbose_name='classroom number' )
    zhanyongkeshi=models.IntegerField  ( null=False, unique=False, verbose_name='class schedule' )
    riqi=models.DateField   ( null=False, unique=False, verbose_name='date' )
    shenqingliyou=models.TextField   ( null=False, unique=False, verbose_name='application reason' )
    shenqingshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='application date' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='No', verbose_name='check or not' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='feedback' )
    '''
    yonghuzhanghao=VARCHAR
    xingming=VARCHAR
    jiaoshibianhao=VARCHAR
    zhanyongkeshi=Integer
    riqi=Date
    shenqingliyou=Text
    fudaoyuanqianming=VARCHAR
    shenqingshijian=DateTime
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'xueshengshenqing'
        verbose_name = verbose_name_plural = 'student application'

class xueshengquxiaoyuyue(BaseModel):
    __doc__ = u'''xueshengquxiaoyuyue'''
    __tablename__ = 'xueshengquxiaoyuyue'



    __authTables__={'yonghuzhanghao':'xuesheng',}
    __authPeople__='no'
    __sfsh__='no'
    __authSeparate__='no'
    __thumbsUp__='no'
    __intelRecom__='no'
    __browseClick__='no'
    __foreEndListAuth__='no'
    __foreEndList__='no'
    __isAdmin__='no'
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'create time')
    yonghuzhanghao=models.CharField ( max_length=255,null=False, unique=False, verbose_name='user account' )
    xingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='name' )
    jiaoshibianhao=models.CharField ( max_length=255,null=False, unique=False, verbose_name='classroom id' )
    zhanyongkeshi=models.CharField ( max_length=255,null=False, unique=False, verbose_name='class time' )
    yudingshijian=models.DateField   ( null=False, unique=False, verbose_name='reserve time' )
    quxiaoliyou=models.TextField   (  null=True, unique=False, verbose_name='cancel reason' )
    shenqingshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='application time' )
    '''
    yonghuzhanghao=VARCHAR
    xingming=VARCHAR
    jiaoshibianhao=VARCHAR
    zhanyongkeshi=VARCHAR
    yudingshijian=Date
    quxiaoliyou=Text
    shenqingshijian=DateTime
    '''
    class Meta:
        db_table = 'xueshengquxiaoyuyue'
        verbose_name = verbose_name_plural = 'cancel application'
