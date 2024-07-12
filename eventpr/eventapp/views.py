from django.shortcuts import render,redirect
from . models import Event
from . forms import BookingForm
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')

def events(request):
    dict_eve={
        'eve':Event.objects.all()
    }
    return render(request,'events.html',dict_eve)

def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)
def contact(request):
    return render(request,'contact.html')





def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()  # or your processing logic
            return redirect('home')  # Redirect to home page after successful form submission
    else:
        form = BookingForm()
    
    return render(request, 'your_template.html', {'form': form})




from django.shortcuts import render, redirect

def contact(request):
    if request.method == 'POST':
        # Process form data here
        # Example: save data or send an email
        return redirect('index')  # Redirect to the home page
    return render(request, 'contact.html')

