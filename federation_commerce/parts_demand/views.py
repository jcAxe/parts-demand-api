from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import PartsDemand
from .serializers import PartsDemandSerializer

# Create your views here.
@csrf_exempt
def demand_list(request):

    if request.method == 'GET':
        demands = PartsDemand.objects.all()
        serializer = PartsDemandSerializer(demands, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PartsDemandSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def demand_detail(request, pk):

    try:
        demand = PartsDemand.objects.get(pk=pk)
    except PartsDemand.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PartsDemandSerializer(demand)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PartsDemandSerializer(demand, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        demand.delete()
        return HttpResponse(status=204)