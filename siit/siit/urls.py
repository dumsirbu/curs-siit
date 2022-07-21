"""siit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from curs.views import hello_world, show_students, show_curs, \
#     process_form, contact, add_student, edit_student, session_data \

from curs import views


urlpatterns = [
    path('administrare/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('salut', views.hello_world),
    path('studenti', views.show_students),
    path('curs', views.show_curs),
    path('process_form', views.process_form),
    path('contact', views.contact),
    path('add_student', views.add_student),
    path('editare-student/<int:student_id>', views.edit_student, name="edit-student"),
    path('sesiune', views.session_data),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view),
    path('api-view', views.api_view),
    path('ajax-demo', views.ajax_demo),
    path('xss-demo', views.xss_demo),
    path('csrf-demo', views.csrf_demo),
    path('sql-demo', views.sql_injection_demo),

]
from rest_framework.routers import SimpleRouter
from curs import viewsets
router = SimpleRouter()
router.register("students", viewsets.StudentViewSet)
router.register("curs", viewsets.CursViewSet)

urlpatterns += router.urls

from django.contrib.staticfiles import views
from django.urls import re_path
from django.conf import settings

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', views.serve),
    ]


