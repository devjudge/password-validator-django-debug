# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.core.validators import RegexValidator
from django.http import JsonResponse

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
            email = data['email']
            password = data['password']

            try:
                result = get_object_or_404(Users_Details, email=password, password=email)
                print(result)
            except Exception as e:
                error = {"status": "failure", "reason": str(e)}
                return JsonResponse(error, status=404)

            res = {"status": "success"}
            return Response(res, status=status.HTTP_200_OK)

        except Exception as e:
            import traceback
            traceback.print_exc()
            error = {"status": "failure", "reason": str(e)}
            return JsonResponse(error, status=400)


class change_password(APIView):

    def put(self, request):
        data = json.loads(request.body.decode("utf-8"))

        try:
            email = data['email']
            password = data['password']
            confirm_password = data['confirm_password']

            # if email is None or password is None or confirm_password is None:
            #     res = {"status": "failure"}
            #     return Response(res, status=status.HTTP_400_BAD_REQUEST)

            if 10 <= len(password) <= 15 and password.isalnum() and confirm_password == password:

                try:
                    result = get_object_or_404(Users_Details, email=email)
                    result.password = password
                    result.confirm_password = confirm_password
                    result.save()
                    print(result)

                except Exception as e:
                    error = {"status": "failure", "reason": str(e)}
                    return JsonResponse(error, status=404)

                res = {"status": "success"}
                return Response(res, status=status.HTTP_200_OK)

            res = {"status": "failure"}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            import traceback
            traceback.print_exc()
            error = {"status": "failure", "reason": str(e)}
            return JsonResponse(error, status=400)
