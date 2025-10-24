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