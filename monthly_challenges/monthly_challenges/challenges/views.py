from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january":"Don't eat meat for the entire month!",
    "february":"Walk for a least 20 minutes every day!",
    "march":"Learn Django for at least 20 minutes every day!",
    "april":"Walk for a least 20 minutes every day!",
    "may":"Learn Django for at least 20 minutes every day!",
    "june":"Don't eat meat for the entire month!",
    "july":"Walk for a least 20 minutes every day!",
    "august": "Learn Django for at least 20 minutes every day!",
    "september":"Don't eat meat for the entire month!",
    "october":"Learn Django for at least 20 minutes every day!",
    "november":"Walk for a least 20 minutes every day!",
    "december":None
}

# Create your views here.

def index(request):
    list_items=""
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args = [month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    #varianta lunga unde trebuie adaugate toate lunile
    # response_data = """
    #     <ul>
    #         <li><a href=""/challenges/january>January</a></li>
    #     </ul>
    # """

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month>len(months):
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args = [redirect_month])

    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html", {
            "text":challenge_text,
            "month_name": month.capitalize()
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        raise Http404()
