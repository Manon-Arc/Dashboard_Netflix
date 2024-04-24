"""
URL configuration for Dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("movies/", views.movies_page, name="movies"),
    path("TV_shows/", views.tv_shows_page, name="TV_shows"),
    path("admin/", admin.site.urls),
    # path("duration_pie_chart/", views.duration_pie_chart, name="duration_pie_chart"),
    # path("director_bar_chart/", views.director_bar_chart, name="director_bar_chart"),
    # path("cast_bar_chart/", views.cast_bar_chart, name="cast_bar_chart"),
    # path("cast_line_chart/", views.cast_line_chart, name="cast_line_chart"),
    # path("cast_circular_chart/", views.cast_circular_chart, name="cast_circular_chart"),
    # path("duration_line_chart/", views.duration_line_chart, name="duration_line_chart"),
]
