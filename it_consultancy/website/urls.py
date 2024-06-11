from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TestimonialViewSet,
    TeamMemberViewSet,
    ServiceViewSet,
    CaseStudyViewSet,
    BlogPostViewSet,
    JobOpeningViewSet,
    CompanyInfoViewSet
)
from . import views

router = DefaultRouter()
router.register(r'testimonials', TestimonialViewSet)
router.register(r'team-members', TeamMemberViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'case-studies', CaseStudyViewSet)
router.register(r'blog-posts', BlogPostViewSet)
router.register(r'job-openings', JobOpeningViewSet)
router.register(r'company-info', CompanyInfoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', views.signup, name='signup'),
]
