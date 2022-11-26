import json
import django.http as Http
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def CalculateDiscount(request: Http.HttpRequest):
    try:
        if request.method == "PATCH":
            body = json.loads(request.body)
            calculated_price = body["price"] * (1- body["discount"]/100) 
            return Http.JsonResponse({"calculated_price": calculated_price})
    except Exception as e:
        return Http.HttpResponseServerError(json.dumps({"error": e.args}))

    return Http.HttpResponseNotFound()
    