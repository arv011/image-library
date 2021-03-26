from django.urls import path
from imgupload.views import Imageuploader
app_name = 'imgupload'
urlpatterns = [
    path('',Imageuploader, name='image-upload')

]