from django.urls import path
from plots import views

app_name="plots"
urlpatterns = [
    path('plots/', views.plots, name='plots'),
    path('plots/<int:plot_id>/', views.plot_detail, name='plot_detail'),
    path('plotnumbers/', views.all_plotnumbers, name='plotnumbers'),
    #path('plotnumbers/<int:plotnumber_id>/', views.plotnumber_detail, name='plotnumber_detail')   
]