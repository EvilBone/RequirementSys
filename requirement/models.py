from django.db import models

# Create your models here.
class Requirement(models.Model):
    req_uccode = models.CharField(max_length=100,verbose_name='用例编号',unique=True)
    req_summary = models.CharField(max_length=500,verbose_name='需求概要')
    req_des = models.CharField(max_length=1000,verbose_name='需求描述')
    req_raise_date = models.DateField(verbose_name='提出时间')
    req_raise_user = models.CharField(verbose_name='提出人',max_length=100)
    req_raise_dep = models.CharField(verbose_name='提出部门',max_length=100)
    req_doc_finish_date = models.DateField(verbose_name='文档完成时间',null=True,blank=True)
    req_status = models.CharField(verbose_name='当前状态',max_length=100)
    req_developer = models.CharField(verbose_name='开发人员',null=True,blank=True,max_length=100)
    req_doc_link =  models.CharField(verbose_name='文档链接',null=True,blank=True,max_length=300)
    req_priority = models.CharField(verbose_name='优先级',max_length=100,default='中')
    req_expect_date = models.DateField(verbose_name='期望完成日期',default='2000-01-01')

    def __unicode__(self):
        return self.req_summary

    class Meta:
        verbose_name = "需求"
        verbose_name_plural = "需求管理"

    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))