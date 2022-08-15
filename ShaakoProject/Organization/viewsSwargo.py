from __future__ import division

import datetime
from io import BytesIO
from os.path import exists

from argon2 import PasswordHasher as ph
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from PIL import Image
from pyparsing import Or
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ShaakoProject.settings import BASE_DIR

from .models import *
from .serializers import *


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getProfile(request):
    if request.method == 'POST':
        print("line 25")
        organizationAdminID = request.data
        print(organizationAdminID)

        # get all information of the organizationAdmin
        organizationAdmin = OrganizationAdmin.objects.values('name', 'password', 'email', 'contactNo',
                                                             'presentAddress').filter(id=organizationAdminID)
        # create dictionary with all information
        print(organizationAdmin)
        ret = {'name': organizationAdmin[0]['name'], 'password': organizationAdmin[0]['password'],
               'email': organizationAdmin[0].get('email', None),
               'contactNo': organizationAdmin[0].get('contactNo', None),
               'presentAddress': organizationAdmin[0].get('presentAddress', None)}

        print(ret)
        return Response(ret)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def updateProfile(request):
    if request.method == 'POST':
        data = request.data
        id = data['id']
        name = data['name']
        password = data['password']
        password2 = data['password2']
        passwordOld = data['passwordOld']
        passwordOld2 = data['passwordOld2']
        email = data['email']
        contactNo = data['contact']
        presentAddress = data['address']

        if len(password) == 0 or len(password2) == 0:
            OrganizationAdmin.objects.filter(id=id).update(name=name, email=email, contactNo=contactNo,
                                                           presentAddress=presentAddress)
            return Response({"success": "True"})
        if password == password2:
            # match argon2 hash of passwordOld2 with passwordOld with try/except
            try:
                ph().verify(passwordOld, passwordOld2)
                # update OrganizationAdmin with name, password, email, contactNo, presentAddress
                passwordHash = ph().hash(password)
                OrganizationAdmin.objects.filter(id=id).update(name=name, password=passwordHash,
                                                               email=email, contactNo=contactNo,
                                                               presentAddress=presentAddress)
                return Response({"success": "True"})

            except:
                return Response({"success": "False"})
