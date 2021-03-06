import json

from django.http import HttpResponse, HttpResponseNotFound
from geo.views import geo_as_json, get_geos_by_bounds_and_type, get_censustract_geos
from geo.models import Geo
from censusdata.views import race_summary_as_json, minority_aggregation_as_json
from hmda.views import loan_originations_as_json
from respondents.views import branch_locations_as_json
from geo.utils import check_bounds

def all(request):
    """This endpoint allows multiple statistical queries to be made in a
    single HTTP request"""
    hmda = loan_originations_as_json(request)
    minority = race_summary_as_json(request)
    responses = {'minority' : minority, 'loanVolume': hmda}
    return HttpResponse(json.dumps(responses), content_type='application/json')

def tables(request):
    table_data = minority_aggregation_as_json(request)
    return HttpResponse(json.dumps(table_data), content_type='application/json')

def msas(request):
    """return a list of MSA ids visible by bounding coordinates"""
    try:
        northEastLat = request.GET.get('neLat')
        northEastLon = request.GET.get('neLon')
        southWestLat = request.GET.get('swLat')
        southWestLon = request.GET.get('swLon')
        bounds = check_bounds(northEastLat, northEastLon, southWestLat, southWestLon)
        if bounds:
            pass
            #maxlat, minlon, minlat, maxlon = bounds[0], bounds[1], bounds[2], bounds[3]
        msas = get_geos_by_bounds_and_type(*bounds, metro=True)
        msa_list = [metro.geoid for metro in msas]
        return HttpResponse(json.dumps(msa_list), content_type='application/json')
    except:
        return HttpResponseNotFound("Invalid lat/lon bounding coordinates")

def hmda(request):
    """This endpoint returns hmda data using params from the request"""
    return HttpResponse(json.dumps(loan_originations_as_json(request)), content_type='application/json')

def census(request):
    """This endpoint returns census data used for circle coloring over tracts"""
    return HttpResponse(json.dumps(race_summary_as_json(request)), content_type='application/json')

def tractCentroids(request):
    """This endpoint returns census tract centroids used to determine circle position on map"""
    geos = get_censustract_geos(request)
    if geos is None:
        return HttpResponseNotFound("Missing one of lat/lon bounds or metro")
    tracts_geo_json = geo_as_json(geos)
    return HttpResponse(json.dumps(tracts_geo_json), content_type='application/json')
    
def branch_locations(request):
    return HttpResponse(json.dumps(branch_locations_as_json(request)), content_type='application/json')
