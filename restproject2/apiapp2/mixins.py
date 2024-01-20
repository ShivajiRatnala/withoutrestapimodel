import json
from django.http import HttpResponse
from django.core.serializers import serialize
class Mixins(object):
    def serilize(self,qs):
        # json_data = serialize('json', qs)
        # pdict = json.loads(json_data)
        # json_data = json.dumps(pdict)
        return HttpResponse(qs,content_type='application/json')