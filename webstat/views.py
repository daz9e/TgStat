from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from webstat.algs import uploaddb
from webstat.algs import get_longest_message
from webstat.algs import get_top_words
from webstat.algs import get_top_active_users,  get_chatid,get_chatname
import re


def upload_file(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        folder_name = 'files'
        path = os.path.join(settings.BASE_DIR, folder_name)
        if not os.path.exists(path):
            os.mkdir(path)
        fs = FileSystemStorage(location=path)
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        uploaddb(myfile.name)
        get_longest_message(myfile.name)
        get_top_words(myfile.name,top_n=25)
        active = get_top_active_users(myfile.name,top_n=5)
        chatid = get_chatid(myfile.name)
        chatname = get_chatname(myfile.name)
        os.remove(os.path.join(path, filename))
        return render(request, 'funcs.html', {
            "chatid": chatid,
        })

    return render(request, 'test.html')

def home(request):
    return render(request, 'upload.html')

def home(request):
    return render(request, 'upload.html')