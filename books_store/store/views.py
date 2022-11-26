import json
import django.http as Http
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Product

@csrf_exempt
def calculate_discount(request: Http.HttpRequest):
    try:
        if request.method == "PATCH":
            body = json.loads(request.body)
            calculated_price = body["price"] * (1- body["discount"]/100) 
            return Http.JsonResponse({"calculated_price": calculated_price})
    except Exception as e:
        return Http.HttpResponseServerError(json.dumps({"error": e.args}))

    return Http.HttpResponseNotFound()

def all_products(request: Http.HttpRequest):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


    