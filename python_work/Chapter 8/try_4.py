# 8-9. Messages:
text_msgs = ['how r u', 'omv', 'hey hey hey hey']
def show_messages(list_of_msgs):
    while list_of_msgs:
        msg = list_of_msgs.pop()
        print(msg)

show_messages(text_msgs)

#8-10. Sent Messages
unsent_messages = ['how r u', 'omw', 'hey wat up', '*thumbs up emoji*']
sent_messages = []

def send_messages(unsent_messages, sent_messages):
    while unsent_messages:
        message = unsent_messages.pop()
        print(f"The message '{message}' is being sent.")
        sent_messages.append(message)
    
    print("All messages have been sent.")

send_messages(unsent_messages[:], sent_messages)
print("\nThese were the messages that were sent:")
print(sent_messages)
print("And this was the original list of messages:")
print(unsent_messages)