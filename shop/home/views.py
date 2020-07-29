from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.http import JsonResponse
from datetime import datetime
import requests

# from django.contrib.auth.decorators import login_required, permission_required
# from django.http import HttpResponsePermanentRedirect


# @login_required()
def index(request):
    return render(request, 'index.html', {})


def api(request):
    currency = requests.get(url="https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
    return JsonResponse({"currency": currency.json(), "date": datetime.now()})

# class IndexView(generic.ListView):
#     template_name = 'index.html'
#
#     def get_queryset(self):
#         """
#         Return the last five published questions (not including those set to be
#         published in the future).
#         """
#         return ""


class ContactsView(generic.ListView):
    template_name = 'index.html'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return ""
