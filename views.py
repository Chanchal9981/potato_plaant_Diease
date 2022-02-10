from django.shortcuts import render,redirect

# Create your views here.

from django.core.files.storage import FileSystemStorage
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import os
from PIL import Image
import  numpy as np
model=load_model("potato_diease_plant.h5")
def Agriculture_crop(plant):
    img=load_img(plant,target_size=(224,224))
    img=img_to_array(img)/255
    img=np.expand_dims(img,axis=0)
    img=model.predict(img).round(3)
    print(img)
    img=np.argmax(img)
    if img == 0:
        return "Bacterial_spot",'Bacterial_spot.html'
    elif img == 1:
        return "healthy",'healthy.html'
    elif img == 2:
        return "Early_blight",'Early_blight.html'
    elif img == 3:
        return "Late_blight",'Late_blight.html'
    elif img == 4:
        return "healthy",'healthy.html'
    elif img == 5:
        return "Bacterial",'Tomato_Bacterial.html'
    elif img == 6:
        return "leaf_spot",'Tomato_leaf_spot.html'
    elif img ==7:
        return "septoria_leaf_spot",'Tomato_septoria_leaf_spot.html'
    elif img == 8:
        return "spider_mites",'Tomato_spider_mites.html'
    elif img == 9:
        return "target_spot",'Tomato_target_spot.html'
    elif img == 10:
        return "curl_virus",'Yellow_leaf_curl_virus.html'
    else:
        return "mosaic_virus",'tomato_mosaic_virus.html'

def Home(request):
    return render(request,'Home.html')
def result(request):
    if request.method=="POST":
        image=request.FILES["image"]
        fs=FileSystemStorage()
        imgg=fs.save(image.name,image)
        imgg=fs.url(imgg)
        test_img='.'+imgg
        pred,use_tem=Agriculture_crop(plant=test_img)
        return render(request,use_tem,{"pred":pred,"user_img":imgg})
    return render(request,'result.html')


