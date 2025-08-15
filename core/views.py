from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Issue

def home(request):
    return render(request, "home.html", {
        "issues": Issue.objects.order_by("-created_at")
    })

@login_required
def create_issue(request):
    if request.method == "POST":
        Issue.objects.create(
            title=request.POST["title"],
            description=request.POST["description"],
            created_by=request.user
        )
        return redirect("home")
    return render(request, "create_issue.html")
