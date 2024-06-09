from django.shortcuts import render
from .models import Myfile
import uuid
# Create your views here.
def home(request):
      if userfile:
        id=uuid.uuid4()
        file=Myfile(id=id,file=userfile)
        file.save()
        link="http://127.0.0.1:8000/"+str(id)+"/"
        print(link)
        return render(request,"index.html",{"link":link})
        return render(request,"index.html")
      def downloadFile(request,id):
          print(id)
          get_file=Myfile.objects.get(id=id)