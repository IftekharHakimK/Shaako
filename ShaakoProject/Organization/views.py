from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView


# Create your views here.

# Organization
class OrganizationList(ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializers


class OrganizationCreate(CreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializers


class OrganizationDestroy(DestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializers


# Organization Admin
class OrganizationAdminList(ListAPIView):
    queryset = OrganizationAdmin.objects.all()
    serializer_class = OrganizationAdminSerializers


class OrganizationAdminCreate(CreateAPIView):
    queryset = OrganizationAdmin.objects.all()
    serializer_class = OrganizationAdminSerializers


class OrganizationAdminDestroy(DestroyAPIView):
    queryset = OrganizationAdmin.objects.all()
    serializer_class = OrganizationAdminSerializers


# Location
class LocationList(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializers


class LocationCreate(CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializers


class LocationDestroy(DestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializers


# Notification
class NotificationList(ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializers


class NotificationCreate(CreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializers


class NotificationDestroy(DestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializers


# Supervisor
class SupervisorList(ListAPIView):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializers


class SupervisorCreate(CreateAPIView):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializers


class SupervisorDestroy(DestroyAPIView):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializers


# Campaign
class CampaignList(ListAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializers


class CampaignCreate(CreateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializers


class CampaignDestroy(DestroyAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializers


# Location_Campaign
class Location_CampaignList(ListAPIView):
    queryset = Location_Campaign.objects.all()
    serializer_class = Location_CampaignSerializers


class Location_CampaignCreate(CreateAPIView):
    queryset = Location_Campaign.objects.all()
    serializer_class = Location_CampaignSerializers


class Location_CampaignDestroy(DestroyAPIView):
    queryset = Location_Campaign.objects.all()
    serializer_class = Location_CampaignSerializers


# Supervisor_Campaign
class Supervisor_CampaignList(ListAPIView):
    queryset = Supervisor_Campaign.objects.all()
    serializer_class = Supervisor_CampaignSerializers


class Supervisor_CampaignCreate(CreateAPIView):
    queryset = Supervisor_Campaign.objects.all()
    serializer_class = Supervisor_CampaignSerializers


class Supervisor_CampaignDestroy(DestroyAPIView):
    queryset = Supervisor_Campaign.objects.all()
    serializer_class = Supervisor_CampaignSerializers


# CHW
class CHWList(ListAPIView):
    queryset = CHW.objects.all()
    serializer_class = CHWSerializers


class CHWCreate(CreateAPIView):
    queryset = CHW.objects.all()
    serializer_class = CHWSerializers


class CHWDestroy(DestroyAPIView):
    queryset = CHW.objects.all()
    serializer_class = CHWSerializers


# Patient
class PatientList(ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers


class PatientCreate(CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers


class PatientDestroy(DestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers


# PatientCampaign
class PatientCampaignList(ListAPIView):
    queryset = PatientCampaign.objects.all()
    serializer_class = PatientCampaignSerializers


class PatientCampaignCreate(CreateAPIView):
    queryset = PatientCampaign.objects.all()
    serializer_class = PatientCampaignSerializers


class PatientCampaignDestroy(DestroyAPIView):
    queryset = PatientCampaign.objects.all()
    serializer_class = PatientCampaignSerializers


# VisitForm
class VisitFormList(ListAPIView):
    queryset = VisitForm.objects.all()
    serializer_class = VisitFormSerializers


class VisitFormCreate(CreateAPIView):
    queryset = VisitForm.objects.all()
    serializer_class = VisitFormSerializers


class VisitFormDestroy(DestroyAPIView):
    queryset = VisitForm.objects.all()
    serializer_class = VisitFormSerializers


# Lesson
class LessonList(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers


class LessonCreate(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers


class LessonDestroy(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers


# Quiz
class QuizList(ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializers


class QuizCreate(CreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializers


class QuizDestroy(DestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializers


# QuizItem
class QuizItemList(ListAPIView):
    queryset = QuizItem.objects.all()
    serializer_class = QuizItemSerializers


class QuizItemCreate(CreateAPIView):
    queryset = QuizItem.objects.all()
    serializer_class = QuizItemSerializers


class QuizItemDestroy(DestroyAPIView):
    queryset = QuizItem.objects.all()
    serializer_class = QuizItemSerializers


# Lesson_CHW
class Lesson_CHWList(ListAPIView):
    queryset = Lesson_CHW.objects.all()
    serializer_class = Lesson_CHWSerializers


class Lesson_CHWCreate(CreateAPIView):
    queryset = Lesson_CHW.objects.all()
    serializer_class = Lesson_CHWSerializers


class Lesson_CHWDestroy(DestroyAPIView):
    queryset = Lesson_CHW.objects.all()
    serializer_class = Lesson_CHWSerializers


# QuizSubmission
class QuizSubmissionList(ListAPIView):
    queryset = QuizSubmission.objects.all()
    serializer_class = QuizSubmissionSerializers


class QuizSubmissionCreate(CreateAPIView):
    queryset = QuizSubmission.objects.all()
    serializer_class = QuizSubmissionSerializers


class QuizSubmissionDestroy(DestroyAPIView):
    queryset = QuizSubmission.objects.all()
    serializer_class = QuizSubmissionSerializers


# SubmissionItem
class SubmissionItemList(ListAPIView):
    queryset = SubmissionItem.objects.all()
    serializer_class = SubmissionItemSerializers


class SubmissionItemCreate(CreateAPIView):
    queryset = SubmissionItem.objects.all()
    serializer_class = SubmissionItemSerializers


class SubmissionItemDestroy(DestroyAPIView):
    queryset = SubmissionItem.objects.all()
    serializer_class = SubmissionItemSerializers