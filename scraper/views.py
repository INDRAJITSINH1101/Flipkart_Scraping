from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
import subprocess
import os

def dashboard(request):
    return render(request, 'scraper/dashboard.html')

def run_scraper(request):
    if request.method == 'POST':
        scraper = request.POST.get('scraper')

        if scraper == "flipkart":
            script_path = os.path.abspath("flip.py")
        elif scraper == "linkedin":
            script_path = os.path.abspath("linkedin.py")
        else:
            return HttpResponse("Invalid option.")

        result = subprocess.run(["python", script_path], capture_output=True, text=True)

        if result.returncode == 0:
            return render(request, 'scraper/dashboard.html', {
                'message': f"{scraper.capitalize()} scraping completed successfully!"
            })
        else:
            return render(request, 'scraper/dashboard.html', {
                'message': f"Error running {scraper}: {result.stderr}"
            })
