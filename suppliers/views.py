from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from . models import Supplier, Machine, Product, Video

# Create your views here.
