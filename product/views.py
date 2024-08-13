from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .filtters import ProductFilter
from .serializers import ProductSerializer
# Create your views here.


@api_view(['Get'])
def get_all_product(request):
    filterset=ProductFilter(request.GET,queryset=Product.objects.all().order_by('id'))
    serializer=ProductSerializer(filterset.qs,many=True)
    return Response({'products':serializer.data})


@api_view(['Get'])
def get_by__id_product(request,pk):
    product=get_object_or_404(Product,id=pk)
    serializer=ProductSerializer(product,many=False)
    return Response({'product':serializer.data})