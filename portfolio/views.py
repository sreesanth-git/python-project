from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render


def home(request):
    projects = [
        {
            "title": "Project X Dashboard",
            "description": "A focused operations dashboard for tracking tasks, goals, and weekly progress with a calm interface.",
            "tags": ["Django", "JavaScript", "CSS"],
        },
        {
            "title": "Client Launch Page",
            "description": "A polished responsive launch page with service highlights, smooth sections, and direct contact routes.",
            "tags": ["HTML", "CSS", "UX"],
        },
        {
            "title": "Smart Tools Prototype",
            "description": "A practical app interface for forms, saved searches, quick previews, and clean frontend interactions.",
            "tags": ["Python", "API", "Frontend"],
        },
    ]

    skills = ["Python", "Django", "HTML", "CSS", "JavaScript", "SQLite"]
    services = [
        {
            "title": "Django Websites",
            "description": "Fast, structured websites with clean templates, reusable views, and database-ready foundations.",
        },
        {
            "title": "Authentication Systems",
            "description": "Login, signup, logout, session handling, user profile states, and secure Django auth flows.",
        },
        {
            "title": "Frontend Polish",
            "description": "Responsive layouts, refined typography, smooth transitions, and professional interaction details.",
        },
    ]
    process = [
        {"step": "01", "title": "Plan", "description": "Shape the goal, content, pages, and database needs."},
        {"step": "02", "title": "Build", "description": "Create Django views, templates, styling, and connected features."},
        {"step": "03", "title": "Refine", "description": "Test the flow, tune responsive design, and polish the experience."},
    ]
    metrics = [
        {"value": "3", "label": "Theme modes"},
        {"value": "100%", "label": "Responsive layout"},
        {"value": "MySQL", "label": "WAMP connected"},
    ]

    return render(
        request,
        "portfolio/home.html",
        {
            "name": "Project X",
            "role": "Django Web Studio",
            "email": "hello@projectx.dev",
            "github": "github.com/project-x-dev",
            "projects": projects,
            "skills": skills,
            "services": services,
            "process": process,
            "metrics": metrics,
        },
    )


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        messages.success(request, f"Welcome back, {form.get_user().username}.")
        return redirect("home")

    return render(request, "portfolio/login.html", {"form": form})


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, f"Welcome, {user.username}. Your profile is ready.")
        return redirect("home")

    return render(request, "portfolio/signup.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("home")
