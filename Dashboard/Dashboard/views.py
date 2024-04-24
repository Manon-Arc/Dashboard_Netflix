"""
Views for the dashboard app.
"""

from csv import DictReader
from django.shortcuts import render
from . import func


def index(request):
    """
    Index page view
    :param request:
    :return:
    """
    with open("netflix_coord.csv", newline="", encoding="utf-8") as csvfile:
        reader = DictReader(csvfile)
        data = list(reader)
    if request.method == "POST":
        filt = request.POST.get("filter")
        if not filt:
            filt = "title"
        sorted_data = sorted(data, key=lambda x: x[filt])
    else:
        sorted_data = sorted(data, key=lambda x: x["title"])

    pie_chart_sorted_html = func.generate_pie_chart(sorted_data)
    heatmap_html = func.generate_choropleth_map(sorted_data)
    duration_map = func.generate_choropleth_map_duration(sorted_data)
    bar_chart_html = func.generate_director_bar_chart(data)
    pie_chart_html = func.generate_pie_chart(data)

    return render(
        request,
        "html/test.html",
        {
            "pie_chart_sorted_html": pie_chart_sorted_html,
            "heatmap_html": heatmap_html,
            "duration_map": duration_map,
            "bar_chart_html": bar_chart_html,
            "pie_chart_html": pie_chart_html,
        },
    )


def movies_page(request):
    """
    View to display movies page.
    """
    with open("netflix_coord.csv", newline="", encoding="utf-8") as csvfile:
        reader = DictReader(csvfile)
        data = list(reader)

    bar_chart_html = func.generate_cast_bar_chart(data)
    bar_chart_html2 = func.generate_cast_duration_bar_chart(data)
    circular_chart_html = func.generate_listed_in_circular_chart(data)
    line_chart_release_html = func.generate_release_year_line_chart(data)
    line_chart_duration_html = func.generate_duration_line_chart(data)

    context = filtre(request, "Movie")
    context["bar_chart_html"] = bar_chart_html
    context["bar_chart_html2"] = bar_chart_html2
    context["circular_chart_html"] = circular_chart_html
    context["line_chart_html"] = line_chart_release_html
    context["line_chart_html1"] = line_chart_duration_html

    return render(request, "html/movies.html", context)


def tv_shows_page(request):
    """
    View to display movies page.
    """
    with open("netflix_coord.csv", newline="", encoding="utf-8") as csvfile:
        reader = DictReader(csvfile)
        data = list(reader)

    bar_chart_html1 = func.generate_cast_bar_chart(data, typ="TV Show")
    bar_chart_html3 = func.generate_cast_duration_bar_chart(data, typ="TV Show")
    line_chart_html1 = func.generate_release_year_line_chart(data, typ="TV Show")
    line_chart_duration_html1 = func.generate_duration_line_chart(data, typ="TV Show")

    context = filtre(request, "TV Show")
    context["bar_chart_html1"] = bar_chart_html1
    context["bar_chart_html3"] = (bar_chart_html3,)
    context["line_chart_html1"] = line_chart_html1
    context["line_chart_duration_html1"] = line_chart_duration_html1

    return render(request, "html/TV_shows.html", context)


def filtre(request, type):
    """"
    View to display filtres page.
    """

    release_year = set()
    date_added = set()
    country = set()
    director = set()
    cast = set()
    category = set()

    selected_release_year = request.GET.get("release_year", "")
    selected_add_date = request.GET.get("date_add", "")
    selected_country = request.GET.get("country", "")
    selected_director = request.GET.get("director", "")
    selected_cast = request.GET.get("cast", "")
    selected_category = request.GET.get("category", "")

    with open("netflix_coord.csv", newline="", encoding="utf-8") as csvfile:
        reader = DictReader(csvfile)
        data = list(reader)

        for row in data:
            if row["type"] == type:
                release_year.add(row["release_year"])
                date_added.add(row["date_added"])

                countries = row["country"].split(",")
                for c in countries:
                    country.add(c.strip())

                directors = row["director"].split(",")
                for d in directors:
                    director.add(d.strip())

                casts = row["cast"].split(",")
                for c in casts:
                    cast.add(c.strip())

                categories = row["listed_in"].split(",")
                for c in categories:
                    category.add(c.strip())

    filtered_data = [x["title"] for x in data]

    if (
        selected_release_year
        or selected_add_date
        or selected_country
        or selected_director
        or selected_cast
        or selected_category
    ):
        filtered_data = []
        for row in data:
            if (
                (
                    not selected_release_year
                    or row["release_year"].strip() == selected_release_year.strip()
                )
                and (
                    not selected_add_date
                    or row["date_added"].strip() == selected_add_date.strip()
                )
                and (
                    not selected_country
                    or selected_country.strip()
                    in [x.strip() for x in row["country"].split(",")]
                )
                and (
                    not selected_director
                    or selected_director.strip()
                    in [x.strip() for x in row["director"].split(",")]
                )
                and (
                    not selected_cast
                    or selected_cast.strip()
                    in [x.strip() for x in row["cast"].split(",")]
                )
                and (
                    not selected_category
                    or selected_category.strip()
                    in [x.strip() for x in row["listed_in"].split(",")]
                )
            ):
                filtered_data.append(row["title"])

    return {
        "selected_release_year": selected_release_year,
        "selected_add_date": selected_add_date,
        "selected_country": selected_country,
        "selected_director": selected_director,
        "selected_cast": selected_cast,
        "selected_category": selected_category,
        "release_year_list": sorted(release_year),
        "date_add_list": sorted(date_added),
        "country_list": sorted(country),
        "director_list": sorted(director),
        "cast_list": sorted(cast),
        "category_list": sorted(category),
        "result": filtered_data,
    }
