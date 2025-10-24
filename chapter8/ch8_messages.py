def show_messages(messages):
    """Ex8-9 Print all messages in the list."""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Ex8-10 Print each message, and then move it to sent_messages."""
    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["hello there", "how are u?", ":)"]
show_messages(messages)

sent_messages = []
send_messages(messages, sent_messages)
# Ex8-11 call function with a copy of the list of messages
#send_messages(messages[:], sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)
