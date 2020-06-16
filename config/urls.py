"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from Api.views import *
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.urls import include, path

urlpatterns = [
path('admin/', admin.site.urls),

url(r'^api/megapod/$', MegpapodListView.as_view()),
url(r'^api/megapod/(?P<pk>\d+)/$', MegapodView.as_view()),
url(r'^api/megapod/list/$', Megpapod_Detail_ListView.as_view()),
url(r'^api/megapod/list/(?P<pk>\d+)/$', Megpapod_Detail_View.as_view()),

url(r'^api/hvac1/$', ServerPodListView_1.as_view()),
url(r'^api/hvac1/(?P<pk>\d+)/$', ServerPodView_1.as_view()),

url(r'^api/hvac2/$', ServerPodListView_2.as_view()),
url(r'^api/hvac2/(?P<pk>\d+)/$', ServerPodView_2.as_view()),

url(r'^api/hvac3/$', ServerPodListView_3.as_view()),
url(r'^api/hvac3/(?P<pk>\d+)/$', ServerPodView_3.as_view()),

url(r'^api/hvac4/$', ServerPodListView_4.as_view()),
url(r'^api/hvac4/(?P<pk>\d+)/$', ServerPodView_4.as_view()),

url(r'^api/hvac5/$', ServerPodListView_5.as_view()),
url(r'^api/hvac5/(?P<pk>\d+)/$', ServerPodView_5.as_view()),


]