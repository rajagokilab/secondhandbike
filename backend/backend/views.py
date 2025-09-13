from django.views.generic import View
from django.http import HttpResponse
from pathlib import Path

class FrontendAppView(View):
    def get(self, request, *args, **kwargs):
        # Adjust this path to match your project structure
        build_index = Path(__file__).resolve().parent.parent.parent / "frontend" / "dist" / "index.html"
        
        # DEBUG: print the path Django is trying to use
        print("Looking for React build at:", build_index)
        
        if build_index.exists():
            with open(build_index, encoding="utf-8") as f:
                return HttpResponse(f.read())
        return HttpResponse("React build not found", status=501)
