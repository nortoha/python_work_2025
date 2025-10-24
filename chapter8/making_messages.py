from message_functions import *

messages = ["hello there", "how are u?", ":)"]
show_messages(messages)

sent_messages = []
send_messages(messages, sent_messages)
# Ex8-11 call function with a copy of the list of messages
#send_messages(messages[:], sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)
