from django.http import JsonResponse
from django.shortcuts import render
import re

# Function to extract YouTube video ID from the URL
def extract_video_id(youtube_url):
    """Extracts the video ID from a YouTube URL"""
    regex = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(regex, youtube_url)
    return match.group(1) if match else None

def fetch_video_clip(request):
    """API to fetch video clip status (simulated for now)"""
    url = request.GET.get("url", "")
    video_id = extract_video_id(url)

    if not video_id:
        return JsonResponse({"error": "Invalid YouTube URL"}, status=400)

    # For the sake of simulation, we are assuming the video clipping process here
    try:
        # Simulating the video clipping process (replace with your clipping logic)
        # Here you could integrate actual video clipping logic
        clipped_video_url = f"https://www.youtube.com/watch?v={video_id}"
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"

        return JsonResponse({
            "video_id": video_id,
            "clipped_video_url": clipped_video_url,
            "thumbnail": thumbnail_url
        })
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def home(request):
    """Renders the homepage"""
    return render(request, "index.html")  # This should be your main home page template

def process_clip(request):
    """Renders the clip processing page with the video URL"""
    video_url = request.GET.get("url", "")
    return render(request, "process_clip.html", {"video_url": video_url})