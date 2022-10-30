from django.urls import path,include
from .views import course_list,course_detail,CourseAPIView,CourseDetails,GenericAPIView,CourseViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('course',CourseViewSet,basename='course')
urlpatterns = [
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>/',include(router.urls)),
    #path('course/',course_list),
    path('course/',CourseAPIView.as_view()),

    #path('detail/<int:pk>/',course_detail),
    path('detail/<int:id>/',CourseDetails.as_view()),

    path('generic/course/<int:id>/',GenericAPIView.as_view())

]


