from django.shortcuts import render
from django.http import JsonResponse  
import json

from chat import process_input

def chat(request):
    return render(request, 'chat.html')
def home(request):
    return render(request, 'index.html')
def query_view(request):
    if request.method == 'POST':

        try:
            data = json.loads(request.body)  
            message = data.get('message')  
            
            print("Received message:", message)  
            var = process_input(message)
            print(var)
            response_data = {
                "message": f"{var}",
                "status": "success"
            }
            return JsonResponse(response_data)  

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"error": "Only POST allowed"}, status=405)

def audio(request):
    print("Received request")

    if request.method != "POST":
        return JsonResponse({"Message": "Only POST requests are allowed"}, status=405)

    print("request.FILES:", request.FILES)  # Debugging line

    audio_file = request.FILES.get('audio')  # Use .get() to avoid KeyError

    if not audio_file:
        return JsonResponse({"Message": "No audio file provided"}, status=400)

    with open("file3.webm", 'wb') as f:
        f.write(audio_file.read())
        f.close()

    return JsonResponse({"Message": "Received successfully"})