from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
import json
from .models import Zipcode
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from operator import itemgetter
from itertools import groupby

def zipRangeFinder(zips):
    first = last = zips[0]
    for n in zips[1:]:
        if n - 1 == last:  # Part of the group, bump the end
            last = n
        else:  # Not part of the group, yield current group and start a new
            yield first, last
            first = last = n
    yield first, last

@method_decorator(csrf_exempt, name='dispatch')
def display(request):
    if not Zipcode.objects.all():
        return HttpResponse("No Zip Codes inserted!")
    zipcodes = Zipcode.objects.all()

    zipcodesValues = set()
    for zipcode in zipcodes:
        zipcodesValues.add(zipcode.zipcode)
    zipcodesValues = list(zipcodesValues)

    zipcodesValues.sort()

    zipCodeRanges = [i if i[0] != i[1] else [i[0]] for i in zipRangeFinder(zipcodesValues)]

    formattedZipcodes = ""
    for zipcodeRange in zipCodeRanges:
        if len(zipcodeRange) > 1:
            formattedZipcodes += str(zipcodeRange[0]) + "-" + str(zipcodeRange[1]) + ", "
        else:
            formattedZipcodes += str(zipcodeRange[0]) + ", "
    formattedZipcodes = formattedZipcodes[:len(formattedZipcodes)-2]


    return HttpResponse(formattedZipcodes)

@method_decorator(csrf_exempt, name='dispatch')
def delete(request, zipcode):
    if not (Zipcode.objects.get(zipcode=zipcode)):
        return HttpResponse(str(zipcode)+" Not Found!")
    zipcodeObject = Zipcode.objects.filter(zipcode=zipcode)[0]
    zipcodeObject.delete()

    return HttpResponse("Zip Code "+str(zipcode)+" deleted.")

@method_decorator(csrf_exempt, name='dispatch')
def insert(request,zipcode):

    zipcodeObject= {
        'zipcode': int(zipcode),
    }
    try:
        zipcodeEntry = Zipcode.objects.create(**zipcodeObject)
    except:
        return HttpResponse("Zipcode " + str(zipcode) + " already inserted.")

    return HttpResponse("Zipcode "+str(zipcodeEntry.zipcode)+" inserted.")

@method_decorator(csrf_exempt, name='dispatch')
def has(request,zipcode):
    try:
        if (Zipcode.objects.get(zipcode=zipcode)):
            return HttpResponse("true")
    except:
        return HttpResponse("false")