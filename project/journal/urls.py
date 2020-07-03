from django.conf.urls import url
from . import views
from .models import user_profile


urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^login/$',views.user_login,name='user_login'),
    url(r'^login/dashboard/(?P<pk>\d+)$',views.dashboard.as_view(),name='dashboard'),
    url(r'^logout/$',views.user_logout,name='user_logout'),
    url(r'^diary/list/(?P<pk>\d+)$',views.diary_list.as_view(),name='diary_list'),
    url(r'^create/(?P<pk>\d+)$',views.create_diary_view,name='create_diary'),
    url(r'^diary/detail/(?P<pk>\d+)$',views.diary_detail.as_view(),name='diary_detail'),
    url(r'^diary/detail/update/(?P<pk>\d+)$',views.diary_update.as_view(),name='diary_update'),
    url(r'^diary/update/success',views.update_success,name='update_success'),
    url(r'^diary/delete/(?P<pk>\d+)$',views.diary_delete.as_view(),name='diary_delete'),
    url(r'^diary/search$',views.search,name='search'),
    
]

# #form loading images
# from project import  settings
# from django.contrib.staticfiles.urls import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
 
# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# p=user_profile.objects.get(pk=4)
# print("p=",p,p.pk,p.id)