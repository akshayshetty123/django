from django.conf.urls import patterns, include, url
from polls.views import *
from django.contrib import admin
from django.conf import settings




urlpatterns = patterns('',
                       url(r'^$', 'openshift.views.home', name='home'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$',signinmethod),
                       url(r'^homePage/', signInB),
                       url(r'^forgetPasswordHtmlKey/', forgetPasswordPageShow),
                       url(r'^signup/',signUp),
                       url(r'^homePage1/',Check),
                       url(r'^homePage2/',Check2),
                       url(r'^submit/', submit),
		       url(r'^loginpage/', signinmethod),
                       url(r'^option/',option1),
                       url(r'^link/',redirect),
                       url(r'^emailsend/',emailsend1),
                       url(r'^forget/',forget1),
                       url(r'^forgetmethod/',forgetmethod),
                      
                       
                
                       
                       )
