from django.shortcuts import render


def home(request):
    projects = [
        {
            "title": "Project X Dashboard",
            "description": "A clean dashboard concept for tracking tasks, goals, and weekly progress.",
            "tags": ["Django", "JavaScript", "CSS"],
        },
        {
            "title": "Client Launch Page",
            "description": "A responsive web page with service highlights, smooth sections, and contact options.",
            "tags": ["HTML", "CSS", "UX"],
        },
        {
            "title": "Smart Tools Prototype",
            "description": "A small app interface for useful forms, saved searches, and quick data previews.",
            "tags": ["Python", "API", "Frontend"],
        },
    ]

    skills = ["Python", "Django", "HTML", "CSS", "JavaScript", "SQLite"]

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
        },
    )
