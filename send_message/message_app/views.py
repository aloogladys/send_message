from django.shortcuts import render
import africastalking

def message(request):
    if request.method == 'POST':

        phone_number = request.POST['phone_number']
        message = request.POST['message']

        #Initialize SDK
        username = 'message_app'
        api_key = 'ec239632c120c9cbbe076998fe491a8bf3fac7dc0682b35b020f5e59ca187f53'
        africastalking.initialize(username, api_key)


        # Initialize a service e.g. SMS
        sms = africastalking.SMS


        # Use the service synchronously
        response = sms.send(message, [phone_number])
        print(response)

        print(phone_number, message)
    
    return render(request,'message.html')

x = {'username':'mungai'}
print(x['username'])