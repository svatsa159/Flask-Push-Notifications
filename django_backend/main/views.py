from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
import os
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
import requests
from main import notifs
from django.shortcuts import redirect
import time
from .threads import ProcessThread,deleteThread
import simplejson as json
import base64
# fl = "1.jpeg"
@csrf_exempt
def get_change_data_view(request):
    if request.method == 'GET':
        global fl
        # print('valid form')
        # myfile = request.FILES['myfile']
        # print(os.getcwd())
        # fs = FileSystemStorage()
        # filename = fs.save("res.jpeg", myfile)
        if(fl=="1.jpeg"):
            fl="2.jpeg"
        else:
            fl="1.jpeg"
        # notifs.notify_users("Data has been Changed")
        return JsonResponse({"success":1})
        # ProcessThread().start()
        # return redirect("http://35.224.209.131:8080/")
@csrf_exempt
def post_send_all(request):
    if request.method == "POST":
        body = json.loads(request.body)
        # print(body["fre"])
        notifs.notify_users(9999,body["message"])
    return JsonResponse({"yes":"1"})

@csrf_exempt
def post_login_alert(request):
    if request.method == "POST":
        body = json.loads(request.body)
        # print(body)
        notifs.notify_users("admin",str(body["logged_in"])+" has logged in")
    return JsonResponse({"success":"1"})

@csrf_exempt
def post_user_process(request):
    if request.method == "POST":
        body=json.loads(request.body)
        print(body)
        notifs.notify_users(400,str(body["logged_in"])+" has completed a process")
        notifs.notify_users(402,str(body["logged_in"])+" has completed a process")
    return JsonResponse({"success":"1"})