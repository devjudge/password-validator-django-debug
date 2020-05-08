# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import uuid
from django.core.validators import RegexValidator
from django.http import HttpResponse, JsonResponse, Http404

# Create your views here.
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from restapi.models import Users_Details

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')


class User_login(APIView):

    def put(self, request):
        data = json.loads(request.body.decode("utf-8"))

        try:
            email = data.get('email', None)
            password = data.get('password', None)

            if password and email:

                try:
                    result = get_object_or_404(Users_Details, email=email, password=password)
                    Users_Details.objects.filter(email=result.email, password=result.password).update(is_logged_in=1, auth_token=uuid.uuid4().hex)

                    field_name = 'auth_token'
                    obj = Users_Details.objects.first()
                    field_object = Users_Details._meta.get_field(field_name)
                    field_value = getattr(obj, field_object.attname)

                    res = {"status": "success", "auth_token": field_value}
                    return Response(res, status=status.HTTP_200_OK)

                except Http404 as e:
                    error = {"status": "failure", "reason": str(e)}
                    return JsonResponse(error, status=status.HTTP_404_NOT_FOUND)

            res = {"status": "failure"}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            error = {"status": "failure", "reason": str(e)}
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class change_password(APIView):

    def put(self, request):
        data = json.loads(request.body.decode("utf-8"))

        try:
            auth_token = request.META['HTTP_AUTH_TOKEN']
            password = data.get('password', None)
            confirm_password = data.get('confirm_password', None)

            if password and confirm_password and confirm_password == password:

                try:
                    result = Users_Details.objects.get(auth_token=auth_token)
                    result.password = password
                    result.save()

                except Users_Details.DoesNotExist as e:
                    error = {"status": "failure", "reason": str(e)}
                    return Response(error, status=status.HTTP_401_UNAUTHORIZED)

                res = {"status": "success"}
                return Response(res, status=status.HTTP_200_OK)

            res = {"status": "failure"}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            error = {"status": "failure", "reason": str(e)}
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

