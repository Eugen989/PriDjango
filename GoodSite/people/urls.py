from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('about/', about, name="about"),
    path('pri/', pri, name="pri"),
    path('pri/<int:number_student>/', pri_id, name="spisok_pri"),
    path('pri/<slug:cat>/', categories),
    path("year/<int:year_number>/", year_handler, name="year"),
    path('post/', post_detail),

    path("split_line", split_line),

    path("get_data_type/", get_data_type),
    path("get_data_type/<int:numer>/", get_data_for_number)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
