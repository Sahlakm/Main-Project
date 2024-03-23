from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import ContactForm
import pickle
import joblib


loaded_model = joblib.load(r'C:\Users\HP\OneDrive\Desktop\Main Project\cyber_sentinel\app1\phishing.pkl')


# Create your views here.
def home(request):
    return render(request, 'home.html')


def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a thank you page or any other page after successful form submission
            return redirect('home')  # Adjust the URL name as per your project setup
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def verify(request):
    if request.method == 'POST':
        url = request.POST.get('url') 
        if url:
            result = loaded_model.predict([url])  # Pass the actual URL in a list

            if result == 'bad':
                result = 'is a phishing site!!!'
            elif result == 'good':
                result = 'is a legitimate site.'
            else:
                result = 'Prediction not available.'
            context = {'result': result}
            return render(request, 'services.html', context)
        #return HttpResponse(f'The entered URL: {url} {result}')
        else:
            error_message = 'Please enter a URL.'
            return render(request, 'services.html', {'error_message': error_message})
    else:
        pass

