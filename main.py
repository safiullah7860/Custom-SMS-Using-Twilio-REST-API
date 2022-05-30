from twilio.rest import Client

client = Client(
    "*********************************","********************************" #id (34 chars) & pass (32 chars)
)

for message in client.messages.list(): 
    print(message.body) #prints all sent messages
    #message.delete() #use this to delete all messages in your account history
body = input('Enter the message you want sent to your phone: ')
message = client.messages.create (  
    to= "**************",   #the number you want to send it to
    from_ = "**********",  #your twilio number
    body = body,
)
print(f"Created a new message: {message}")