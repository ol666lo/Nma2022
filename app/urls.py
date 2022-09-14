from django.urls import path
from .views import home  , verclientes , solicitarasesoria
urlpatterns = [
    path('', home, name="home"),
    path('verclientes/', verclientes, name="verclientes"),
    path('solicitarasesoria/', solicitarasesoria, name="solicitarasesoria"),
 
]