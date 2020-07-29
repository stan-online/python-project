from django.views.decorators.csrf import csrf_exempt
import logging
from django.forms.models import model_to_dict
from django.http import JsonResponse
from goods.models import Product
import json

logger = logging.getLogger(__name__)


@csrf_exempt
def products(request):
    # curl http://127.0.0.1:8000/api/v1/products/
    if request.method == "GET":
        products_list = {"products": []}
        for item in Product.objects.all():
            products_list["products"].append(
                model_to_dict(item, fields=["id",
                                            "name",
                                            "description",
                                            "unit",
                                            "photo_url"
                                            ]))
        return JsonResponse(products_list, content_type='application/json')
    if request.method == "POST":
        # curl -X POST \
        #  --header "Content-Type: application/json" \
        # --data '{"name": "test 1"}' \
        # http://127.0.0.1:8000/api/v1/products/
        try:
            data = json.loads(request.body)
            product = Product()
            product.name = data["name"] if "name" in data else ""
            product.description = data["description"] if "description" in data else ""
            product.unit = data["unit"] if "unit" in data else ""
            product.photo_url = data["photo_url"] if "photo_url" in data else ""
            res = product.save()
            logger.debug(res)
        except Exception as e:
            return JsonResponse(
                {
                    "status": "Product is not created",
                    "error": e
                },
                status=500)
        return JsonResponse({"status": "SUCCESS"})


@csrf_exempt
def product_details(request, pk):
    if request.method == "GET":
        # curl http://127.0.0.1:8000/api/v1/products/3/
        g = Product.objects.get(pk=pk)
        return JsonResponse(model_to_dict(g, fields=["id",
                                                     "name",
                                                     "description",
                                                     "unit",
                                                     "photo_url"
                                                     ]))
    elif request.method == "POST":
        # curl --header "Content-Type: application/json" \
        # --request POST --data '{"name":"xyz"}' \
        # http://127.0.0.1:8000/api/v1/products/3/
        try:
            data = json.loads(request.body)
            g = Product.objects.get(pk=pk)
            g.name = data.get("name", None)
            g.save()
        except goods.models.Product.DoesNotExist:
            return JsonResponse({"status": "Items does not exists"}, status=500)
        return JsonResponse({"status": "SUCCESS"})
    elif request.method == "DELETE":
        # curl --request DELETE http://127.0.0.1:8000/api/v1/products/3/
        try:
            Product.objects.get(pk=pk).delete()
        except goods.models.Product.DoesNotExist:
            return JsonResponse({"status": "Items does not exists"}, status=500)
        return JsonResponse({"status": "SUCCESS"})
