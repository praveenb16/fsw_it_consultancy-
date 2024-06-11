from django.shortcuts import render
from rest_framework import viewsets
from .models import Testimonial, TeamMember, Service, CaseStudy, BlogPost, JobOpening, CompanyInfo
from .serializers import (
    TestimonialSerializer,
    TeamMemberSerializer,
    ServiceSerializer,
    CaseStudySerializer,
    BlogPostSerializer,
    JobOpeningSerializer,
    CompanyInfoSerializer
)

class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class CaseStudyViewSet(viewsets.ModelViewSet):
    queryset = CaseStudy.objects.all()
    serializer_class = CaseStudySerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class JobOpeningViewSet(viewsets.ModelViewSet):
    queryset = JobOpening.objects.all()
    serializer_class = JobOpeningSerializer

class CompanyInfoViewSet(viewsets.ModelViewSet):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer

def signup(request):
    return render(request, 'signup.html')

