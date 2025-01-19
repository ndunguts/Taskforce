from django.urls import path
from. import views
urlpatterns = [
    
    path('',views.home,name="home"),
    path('Budget/',views.make_budget,name="budget"),
    path('income/',views.incomes,name="income"),
    path('outcome/',views.outcomes,name="outcome"),
    path('save/',views.save,name="save"),
    path('saveincome',views.saveincome,name="saveincome"),
    path('saveoutcome',views.saveoutcome,name='saveoutcome'),
    path('deletbudget/',views.deletbudget,name='deletbudget'),
    path('check/',views.checkbudget,name='check'),
    path("success/",views.success, name="success"),
    path("lostbudget/",views.lost_budget,name="lostbudget"),
    path("chart/",views.chart_total_saved, name="chart"),
    path("highi",views.highest_income,name="highi"),
    path("higho", views.highest_outcome,name="higho"),
    path('report/',views.report,name="report"),
    path('deletebudget/',views.deletebudget,name="deletebudget")
    

    
    
    
]  