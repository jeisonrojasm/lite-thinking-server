from django.shortcuts import render
from django.views import View
from .models import Enterprise
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
class EnterpriseView(View):

    @method_decorator(csrf_exempt)
    # Método que se ejecuta cada vez que hacemos una petición
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, nit=0):
        if (nit > 0):
            enterprises = list(Enterprise.objects.filter(nit=nit).values())
            if len(enterprises) > 0:
                enterprise = enterprises[0]
                data = {'message': 'Success', 'enterprise': enterprise}
            else:
                data = {'message': 'Error... Empresa no encontrada'}
            return JsonResponse(data)
        else:
            enterprises = list(Enterprise.objects.values())
            if len(enterprises) > 0:
                data = {'message': 'Success', 'enterprises': enterprises}
            else:
                data = {'message': 'Error... Empresas no encontradas'}
            return JsonResponse(data)

    def post(self, request):
        jsonData = json.loads(request.body)
        Enterprise.objects.create(
            name=jsonData['name'], address=jsonData['address'], nit=jsonData['nit'], tel=jsonData['tel'])
        data = {'message': 'Success'}
        return JsonResponse(data)

    def put(self, request, nit):
        jsonData = json.loads(request.body)
        enterprises = list(Enterprise.objects.filter(nit=nit).values())
        if len(enterprises) > 0:
            enterprise = Enterprise.objects.get(nit=nit)
            enterprise.name = jsonData['name']
            enterprise.address = jsonData['address']
            enterprise.tel = jsonData['tel']
            enterprise.save()
            data = {'message': 'Success'}
        else:
            data = {'message': 'Error... Empresa no encontrada'}
        return JsonResponse(data)

    def delete(self, request, nit):
        enterprises = list(Enterprise.objects.filter(nit=nit).values())
        if len(enterprises) > 0:
            Enterprise.objects.filter(nit=nit).delete()
            data = {'message': 'Success'}
        else:
            data = {'message': 'Error... Empresa no encontrada'}
        return JsonResponse(data)
