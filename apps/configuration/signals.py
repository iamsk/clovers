from django.conf import settings
from django.db.models.signals import post_save
import json
import acm

from .models import Configuration


def sync(sender, instance, **kwargs):
    content = json.dumps(instance.data)
    c.publish(data_id=str(instance.id), group=settings.ALIYUN_ACM['GROUP'], content=content)


if settings.ALIYUN_ACM:
    c = acm.ACMClient(settings.ALIYUN_ACM['ENDPOINT'], settings.ALIYUN_ACM['NAMESPACE'], settings.ALIYUN_ACM['AK'],
                      settings.ALIYUN_ACM['SK'])
    post_save.connect(sync, sender=Configuration)
