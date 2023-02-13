from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from . import models

# Create your views here.


def index_template(request):
    data = {}
    return render(request, "home.html", data)


def curriculums(request, id=False) -> (HttpResponse | JsonResponse | None):
    obj_curriculums = models.curriculums
    if request.method == 'GET':
        data = {
            "curriculums": obj_curriculums.objects.values()
        }
        return render(request, "curriculum.html", data)
    elif request.method == 'POST':
        body = json.loads(request.body)
        name = body['txtName']
        obj_result = obj_curriculums.objects.get_or_create(
            name=name
        )
        if obj_result[1]:
            msg = "Curriculum Created"
            icon = "success"
            color_text = "text-success"
        else:
            msg = "Curriculum already exists"
            icon = "info"
            color_text = "text-info"
        data = {
            "state": "Ok",
            "msg": msg,
            "icon": icon,
            "color_text": color_text
        }
        return JsonResponse(data)
    elif request.method == 'DELETE':
        obj_curriculums.objects.get(id=id).delete()
        data = {
            "state": "Ok",
            "msg": "Delete curriculum succesfully"
        }
        return JsonResponse(data)
    elif request.method == 'PUT':
        body = json.loads(request.body)
        name = body['name']
        curriculum = obj_curriculums.objects.get(id=id)
        curriculum.name = str(name).title()
        curriculum.save()
        data = {
            "state": "Ok",
            "msg": "It was updated correctly",
            "name":name
        }
        return JsonResponse(data)


def curriculum_information(request, id):
    curriculum = models.curriculums.objects.get(id=id)
    data = {
        "id": id,
        "curriculum": curriculum
    }
    return render(request, "curriculum_information.html", data)