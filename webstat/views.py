from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from webstat.algs import uploaddb
from webstat.algs import get_longest_message
from webstat.algs import get_top_words
from webstat.algs import get_top_active_users,top_media
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
        get_top_active_users(myfile.name,top_n=5)
        top_media(myfile.name,top_n=5)
        os.remove(os.path.join(path, filename))
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url
        })

    return render(request, 'upload.html')

def home(request):
    return render(request, 'base.html')