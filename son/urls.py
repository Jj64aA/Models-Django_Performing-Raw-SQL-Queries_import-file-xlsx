from django.urls import path ,include
from . import views


#---------------------------------------
urlpatterns = [
    path('',views.home,name='home'),
    path('import_xlsx',views.import_xlsx,name='import_xlsx'),
    path('show_creance',views.show_creance,name='show_creance'),
    path('function1',views.function_1,name='function_1') ,
    path('function2',views.function_2,name='function_2') ,
    path('function3',views.function_3,name='function_3') ,
    path("/", views.del_data , name="del_data")
]