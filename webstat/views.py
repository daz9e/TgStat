from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from webstat.algs import addusers
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
        out = addusers(myfile.name)
        return render(request, 'upload.html', {
            'uploaded_file_url': out
        })
    return render(request, 'upload.html')

def home(request):
    return render(request, 'base.html')