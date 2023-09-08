import requests
import time
#Messages
print("Welcome to discord webhook spammer!")
print("Discord bot messanger is coming soon!")
print("Check out discord bot messanger! https://replit.com/@StudioHawaii/discord-webhook-message-sender-multi-messages")
print("Rate limit protection is on this repl to protect your account from getting rate limited the messages are still fast though")
#Values and inputs
wait_time = 1 #not recommended to change since this is rate limit protection
Url = input('Webhook Url:')
discord_webhook_url = '%s' % Url
Message = input('Message:')
Amount = int(input("How many times do you want to send the message?:"))
#embeds a json file called message.json
Message = {
   "content" : '%s' % Message
}
print("Spammer has started")
#main loop
while True:
  time.sleep(wait_time)
  print("Message Sent")
  requests.post(discord_webhook_url, data=Message)
  Amount -= 1
  if Amount == 0:
   print("Task Completed")
   break