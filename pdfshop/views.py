import time
from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render
import os
from django.http import HttpResponse
import razorpay


BASE_DIR = settings.BASE_DIR

'''
def index(request):
    return render(request, 'index.html')
'''
    
def index(request):
    # Check if payment was successful and enable the download button accordingly
    payment_successful = request.session.get('payment_successful', False)
    return render(request, 'index.html', {'payment_successful': payment_successful})
    
   


def download_pdf(request):
    pdf_path = os.path.join(BASE_DIR, 'media', 'pdfs', 'revision.pdf')
    filename = os.path.basename(pdf_path)
    with open(pdf_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response
    

# creating the order for the payment
def create_order(request):
    client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))

    data = {
        'amount': 2500,  # ₹25 * 100 (amount in paisa)
        'currency': 'INR',
        'receipt': 'receipt_' + str(time.time()),  # Generate a unique receipt ID
    }

    order = client.order.create(data=data)

    return render(request, 'index.html', {'order_id': order['id']})
    
    
def payment_success(request):
    # Handle payment success logic
    pass
    
    

def webhook_view(request):
    if request.method == 'POST':
        # Extract relevant information from the webhook notification
        data = request.POST.get('payload')  # Assuming the payload is sent as a POST parameter named 'payload'
        # Process the data and update your database based on the payment status
        
        # Enable the download button if the payment is successful
        payment_successful = True  # Update this based on your logic
        
        # Set the payment status in the session
        request.session['payment_successful'] = payment_successful

    return HttpResponse(status=200)  # Return a response indicating successful handling of the webhook

