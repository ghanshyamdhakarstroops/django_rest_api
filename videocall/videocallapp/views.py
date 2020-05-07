from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Hero
from .serializers import HeroSerialize, UserSerializer
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

# class HeroList(generics.ListCreateAPIView):
# 	queryset=Hero.objects.all()
# 	serializer_class=HeroSerialize
# 	permission_classes = [permissions.IsAuthenticated]

# 	def perform_create(self, serializer):
# 		serializer.save(owner=self.request.user)

# class HeroDetail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset=Hero.objects.all()
# 	serializer_class=HeroSerialize
# 	permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

from rest_framework.status import(
	HTTP_400_BAD_REQUEST,
	HTTP_404_NOT_FOUND,
	HTTP_200_OK
	)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
	username=request.data.get('username')
	password=request.data.get('password')
	if username is None or password is None:
		return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
	user = authenticate(username=username, password=password)
	if not user:
		return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
	token,_= Token.objects.get_or_create(user=user)
	return Response({'token': token.key}, status=HTTP_200_OK)



class HeroViewSet(viewsets.ModelViewSet):
	"""
	This viewset automatically provides `list`, `create`, `retrieve`,
	`update` and `destroy` actions.

	Additionally we also provide an extra `highlight` action.
	"""
	queryset = Hero.objects.all()
	serializer_class = HeroSerialize
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


# class UserList(generics.ListAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	This viewset automatically provides `list` and `detail` actions.
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer

@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'users': reverse('user-list', request=request, format=format),
		'hero': reverse('hero-list', request=request, format=format)
	})
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated] 

# class HeroView(viewsets.ModelViewSet):
# 	query=Hero.objects.all().order_by('name')
# 	serializer_cls=HeroSerialize


# import requests
# import json
# from django.core.files.storage import FileSystemStorage
# from django.http import HttpResponse, HttpResponseNotFound
# from django.http import FileResponse, Http404
# import PyPDF2
# from .models import *
# import collections
# import sys, fitz
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.converter import HTMLConverter
# from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure, LTImage
# from pdfminer.pdfpage import PDFPage
# from io import BytesIO

# import os
# import sys
# import time


# def home(request):
# 	pass


	# doc=fitz.open('/home/ghanshyam/Desktop/NEWS.pdf')
	# for page in doc:
	# 	html_text=page.getText('html')
	# 	print(html_text)
	# filename='/var/www/html/pdfconverted.html'
	# print(filename)
	# print('Aceess time: ', time.ctime(os.path.getatime(filename)))
	# print('modified time: ', time.ctime(os.path.getmtime(filename)))
	# print('change time: ', time.ctime(os.path.getctime(filename)))
	# print('size: ',os.path.getsize(filename))
	# rsrcmgr = PDFResourceManager()
	# retstr = BytesIO()
	# # codec = 'utf-8'
	# laparams = LAParams(all_texts=True)
	# device = HTMLConverter(rsrcmgr, retstr, laparams=laparams)
	# interpreter = PDFPageInterpreter(rsrcmgr, device)
	# fp = open('/home/ghanshyam/Desktop/NEWS.pdf', 'rb')
	# password = ""
	# maxpages = 0 #is for all
	# caching = True
	# pagenos=set()
	# for i, page in enumerate(PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True)):
	# 	interpreter.process_page(page)
	# text = retstr.getvalue()
	# fp.close()
	# device.close()
	# retstr.close()
	# print(text)
	# pdf=PdfData.objects.create(count=maxpages, text=text)
	# return render(request, 'home.html', {'pdf':pdf})

# test = home('/home/ghanshyam/Desktop/sample.pdf')
# print(test)

# def home(request):
	# pdfFileObj = open('/home/ghanshyam/Desktop/sample.pdf', 'rb')
	# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	# num_pages = pdfReader.numPages
	# count = 0
	# text = ""
	# while count < num_pages:
	# 	pageObj = pdfReader.getPage(count)
	# 	count +=1
	# 	text += pageObj.extractText()
	# # if text != "":
	# #    text = text
	# # else:
	# #    text = textract.process(fileurl, method='tesseract', language='eng')
	# print(text)
	# pdf=PdfData.objects.create(count=num_pages, text=text)
	# return render(request, 'home.html', {'pdf':pdf})









	# fs=FileSystemStorage()
	# filename='Haltermanpythonbook.pdf'
	# if fs.exists(filename):
	# 	with fs.open(filename) as pdf:
	# 		response=HttpResponse(pdf, content_type='application/pdf')
	# 		response['Content-Disposition']='inline; filename="Haltermanpythonbook.pdf"'
	# 		return response

	# with open('/home/ghanshyam/Desktop/Haltermanpythonbook.pdf', 'rb') as pdf:
	# 	response=HttpResponse(pdf.read(), content_type='application/pdf')
	# 	response['Content-Disposition']='inline; filename="/home/ghanshyam/Desktop/Haltermanpythonbook.pdf"'
	# 	return response
	# pdf.closed


# import urllib
# params = urllib.urlencode({ 'username': 'dhakar1988@gmail.com', 'password': 'laserJet1300', 'recipient': 'anotherperson@contoso.com', 'message': 'Hello World!' })
# f = urllib.urlopen("https://localhost/home.html", params)
# print(f)


# # def home(request):
# # 	head={'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOm51bGwsImlzcyI6IkpCakJkaHVlUWctUTFSc0JhZWFjaWciLCJleHAiOjE1ODg4NjA2OTEsImlhdCI6MTU4ODI1NTg5MX0.C8Swg_arX3G3Hmbc-s9ZvBK6SD9GIYPZ0L3jJIiKMg8'}
# # 	userdata=requests.get('https://api.zoom.us/v2/users/', headers=head)
# # 	userdjsn=userdata.json()
# # 	# dslice=userdjsn.slice()
# # 	usersd=userdjsn['users']
# # 	# print(usersd)
# # 	# if request.method == 'POST':
# # 	metdata= {
# # 				"topic": "corona virus",
# # 				"type": 2,
# # 				"start_time": "2020-04-30T15:35:01",
# # 				"duration": 60,
# # 				"timezone": "Asia/Calcutta",
# # 				"password": "password",
# # 				"agenda": "Agenda",
# # 				"recurrence": {
# # 					"type": 1,
# # 					"repeat_interval": 1,
# # 					"weekly_days": "1,2,3,4,5,6",
# # 					"end_times": 50
# # 				},
# # 				"settings": {
# # 					"host_video": True,
# # 					"participant_video": True,
# # 					"cn_meeting": True,
# # 					"in_meeting": False,
# # 					"join_before_host": True,
# # 					"mute_upon_entry": False,
# # 					"watermark": False,
# # 					"use_pmi": False,
# # 					"approval_type": 2,
# # 					"registration_type": 3,
# # 					"audio": "both",
# # 					"auto_recording": "cloud",
# # 					"enforce_login": False,
# # 					"alternative_hosts": ""
# # 				}
# # 			}
# # 	print(metdata)
# # 	metingcrte=requests.post('https://api.zoom.us/v2/users/TTTip9fvSm6rLomtCjbNIA/meetings', headers=head, data=json.dumps(metdata))
# # 	print(metingcrte.text)
# # 	return render(request, 'home.html')

# # # Create your views here.
