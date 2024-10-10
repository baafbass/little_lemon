from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

