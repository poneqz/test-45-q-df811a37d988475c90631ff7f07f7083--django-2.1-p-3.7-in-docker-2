# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import IntegrityError
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Leads
from .serializers import LeadsSerializer, MarkLeadSerializer
from rest_framework.decorators import api_view
from .choices import StatusTypeChoices


def index(requests):
    return HttpResponse("Hello, world. You're at Rest.")


@api_view(['POST'])
def leads_post(request):
    try:
        if request.method == 'POST':
            leads_data = JSONParser().parse(request)
            leads_serializer = LeadsSerializer(data=leads_data)
            if leads_serializer.is_valid(raise_exception=True):
                leads_serializer.save()
                return JsonResponse(leads_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse({"status": "failure", "reason": leads_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except IntegrityError as e:
        return JsonResponse({"status": "failure", "reason": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def leads_detail(request, pk):
    try:
        leads = Leads.objects.get(pk=pk)
    except Leads.DoesNotExist:
        return JsonResponse({}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            leads_serializer = LeadsSerializer(leads)
            return JsonResponse(leads_serializer.data)
        except Exception as e:
            return JsonResponse({"status": "failure", "reason": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            leads_data = JSONParser().parse(request)
            leads_serializer = LeadsSerializer(leads, data=leads_data)
            if leads_serializer.is_valid():
                leads_serializer.save()
                return JsonResponse({"status": "success"}, status=status.HTTP_202_ACCEPTED)
            return JsonResponse({"status": "failure", "reason": leads_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({"status": "failure", "reason": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            leads.delete()
            return JsonResponse({'status': 'success'}, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"status": "failure", "reason": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def mark_lead(request, pk):
    try:
        leads = Leads.objects.get(pk=pk)
    except Leads.DoesNotExist:
        return JsonResponse({'message': 'The lead does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        try:
            leads_data = JSONParser().parse(request)
            leads_data['status'] = StatusTypeChoices.Contacted
            mark_lead_serializer = MarkLeadSerializer(leads, data=leads_data)
            if mark_lead_serializer.is_valid(raise_exception=True):
                mark_lead_serializer.save()
                return JsonResponse(mark_lead_serializer.data, status=status.HTTP_202_ACCEPTED)
            return JsonResponse({"status": "failure", "reason": mark_lead_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({"status": "failure", "reason": str(e)}, status=status.HTTP_400_BAD_REQUEST)
