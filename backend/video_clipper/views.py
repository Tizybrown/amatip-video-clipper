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
    
    # If no URL is provided in the request, return an error response
    if not url:
        return JsonResponse({"error": "No URL provided"}, status=400)

    video_id = extract_video_id(url)
    
    # If video ID extraction fails, return an error response
    if not video_id:
        return JsonResponse({"error": "Invalid YouTube URL"}, status=400)

    try:
        # Simulate the video clipping process (replace with actual clipping logic in the future)
        clipped_video_url = f"https://www.youtube.com/watch?v={video_id}"
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"

        # Return the JSON response with video details
        return JsonResponse({
            "video_id": video_id,
            "clipped_video_url": clipped_video_url,
            "thumbnail": thumbnail_url
        })
    except Exception as e:
        # If an error occurs, return an error response with the exception message
        return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)

def home(request):
    """Renders the homepage"""
    return render(request, "index.html")  # This renders the index.html file

def process_clip(request):
    """Renders the clip processing page with the video URL"""
    video_url = request.GET.get("url", "")
    
    if not video_url:
        # If no video URL is provided, show an error message on the process_clip page
        return render(request, "process_clip.html", {"error": "No video URL provided"})
    
    # If the video URL is valid, proceed with rendering the page and passing the video URL to the template
    return render(request, "process_clip.html", {"video_url": video_url})
