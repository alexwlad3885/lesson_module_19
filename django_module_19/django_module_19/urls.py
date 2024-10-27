from django.contrib import admin
from django.urls import path
from task1.views import func_index, func_index_1, func_index_2, sign_up_by_django


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sign_up_by_django),
    path('main/', func_index),
    path('page_1/', func_index_1),
    path('page_2/', func_index_2),
]
