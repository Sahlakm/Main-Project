from django.shortcuts import render
from django.http import JsonResponse
import joblib
# Create your views here.

loaded_model = joblib.load(r'C:\Users\HP\OneDrive\Desktop\Main Project\cyber_sentinel\app1\phishing.pkl')

def predict_url(request):
    if request.method == 'POST':
        url = request.POST.get('url')  # Assuming the URL data is sent in the request body
        
        # Perform prediction using your model
        prediction = loaded_model.predict(url)
        
        # Return the prediction result as JSON response
        return JsonResponse({'prediction': prediction})
    else:
        # Return an error response for other request methods
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)