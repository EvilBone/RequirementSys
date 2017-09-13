#encoding:utf-8
import datetime
import decimal
import json

import simplejson as simplejson
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Requirement

# Create your views here.

#借用自：http://blog.csdn.net/hong201/article/details/3888588
def safe_new_datetime(d):
    kw = [d.year, d.month, d.day]
    if isinstance(d, datetime.datetime):
        kw.extend([d.hour, d.minute, d.second, d.microsecond, d.tzinfo])
    return datetime.datetime(*kw)


def safe_new_date(d):
    return datetime.date(d.year, d.month, d.day)


class DatetimeJSONEncoder(simplejson.JSONEncoder):
    """可以序列化时间的JSON"""

    DATE_FORMAT = "%Y-%m-%d"
    TIME_FORMAT = "%H:%M:%S"

    def default(self, o):
        if isinstance(o, datetime.datetime):
            d = safe_new_datetime(o)
            return d.strftime("%s %s" % (self.DATE_FORMAT, self.TIME_FORMAT))
        elif isinstance(o, datetime.date):
            d = safe_new_date(o)
            return d.strftime(self.DATE_FORMAT)
        elif isinstance(o, datetime.time):
            return o.strftime(self.TIME_FORMAT)
        elif isinstance(o, decimal.Decimal):
            return str(o)
        else:
            return super(DatetimeJSONEncoder, self).default(o)
#-------------------------------以上代码摘自网络——————————————————

def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]

def home(request):
    reqs = Requirement.objects.all()
    return render(request, 'home.html',{'reqs':reqs})

def allreqs(request):
    reqs = Requirement.objects.values()
    data_dict = ValuesQuerySetToDict(reqs)
    jsondata = simplejson.dumps(data_dict,cls=DatetimeJSONEncoder,ensure_ascii = False)
    return HttpResponse(jsondata)

def reqdocs(request,doc_name):
    print("doc_name:"+doc_name)
    return  render(request,doc_name+'.html')