from django.shortcuts import render
from .forms import CourseForm, CampusForm, BrForm
from django.http import JsonResponse, HttpResponse
import json
from .models import navbartext
from django.utils import timezone
# Create your views here.
def index(request):
    if request.is_ajax():
        print("hello")
    if 'code' in request.GET:
        code_search_main = CourseForm(request.GET)
        campus = CampusForm(request.GET)
        br = BrForm(request.GET)
        rest = {}
        if code_search_main.is_valid() and campus.is_valid() and br.is_valid():
            I_search = code_search_main.search()
            camp = campus.search()
            br_s = br.search()
            result = CourseForm.main_search(I_search, camp, br_s)
        else:
            result = CourseForm()
            camp = CampusForm()
            br_s = br.search()



    else:
        code_search_main = CourseForm()
        result = CourseForm()
        campus = CampusForm()
        br = BrForm()
    return render(request, 'thepath/pathway.html', {"B": code_search_main, "rest": result, "campus":campus, "Br":br})

def checkagain(request):
    if 'code' in request.GET:
        code_search_sec = CourseForm(request.GET)
        campus2 = CampusForm(request.GET)
        br2 = BrForm(request.GET)
        res2 = {}
        if code_search_sec.is_valid() and campus2.is_valid() and br2.is_valid():
            tt_search = code_search_sec.search()
            camp = campus2.search()
            br_s2 = br2.search()
            res2 = CourseForm.main_search(tt_search, camp, br_s2)
        else:
            res2 = CourseForm()
            camp = CampusForm()
            br_s2 = br2.search()
    else:
        code_search_sec = CourseForm()
        res2 = CourseForm()
        campus2 = CampusForm()
        br2 = BrForm()
    return JsonResponse(res2)

def navbartext_list(request):
    navbartex = navbartext.objects.all()
    return render(request, 'thepath/pathway.html', {'navbartex': navbartex})
