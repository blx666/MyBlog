from django.core.serializers import json
from dajaxice.decorators import dajaxice_register
from dajaxice.core import dajaxice_functions

@dajaxice_register
def sayhello(request):
    return json.dumps({'message': 'Hello World'})


dajaxice_functions.register(sayhello)