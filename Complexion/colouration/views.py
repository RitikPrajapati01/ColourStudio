from django.shortcuts import render
# from .forms import ImageForm
from .forms import ColourForm
from .models import ImageData
import cv2
import numpy as np
from django.views.decorators.csrf import csrf_exempt
import base64
# Create your views here.


@csrf_exempt
def image_colour(request):
    if request.method == 'POST':
        forms = ColourForm(request.POST, request.FILES) 
        if forms.is_valid():
            image = request.FILES['images']
            choice = request.POST['colours']
            nparr = np.fromstring(image.read(), np.uint8)
            opencv_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            if choice == 'hsv':
                hsv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2HSV)
            elif choice == 'rgb':
                hsv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
            elif choice =='gray':    
                hsv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)
            elif choice =='hls':    
                hsv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2HLS)
            elif choice == 'neg':
                gray = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)
                hsv_image = 255 - gray
            else:
                return render(request, 'ImagePaint/colour.html', {'forms':forms})    
            _, buffer = cv2.imencode('.jpg', hsv_image)
            converted_images = base64.b64encode(buffer).decode('utf-8')
            imaging = request.FILES['images']
            i = ImageData(image=imaging)
            i.save()
            _images  = ImageData.objects.last()
            return render(request, 'ImagePaint/colour.html', {'forms':forms, 'converted_images':converted_images, 'r_images':_images})
            
    else:    
        forms = ColourForm()    
        return render(request, 'ImagePaint/colour.html', {'forms':forms})
    return render(request, 'ImagePaint/colour.html', {'forms':forms})

def index(request):
    return render(request, 'ImagePaint/index.html')
