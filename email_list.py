# Initialize empty sets
subscribers = set()
unsubscribers = set()

# Function to add an email
def add_email(email, set_name):
    normalized_email = email.lower()
    if normalized_email in set_name:
        print(f"The email {normalized_email} is already in {'subscribers' if set_name == subscribers else 'unsubscribers'}.")
    else:
        set_name.add(normalized_email)
        print(f"Email '{email}' added to {'subscribers' if set_name == subscribers else 'unsubscribers'}.")

# Function to remove an email
def remove_email(email, set_name):
    normalized_email = email.lower()
    if normalized_email in set_name:
        print(f"The email {normalized_email} is already in {'subscribers' if set_name == subscribers else 'unsubscribers'}.")
    else:
        set_name.add(normalized_email)
        print(f"Email '{email}' removed from {'subscribers' if set_name == subscribers else 'unsubscribers'}.")

# Function to display emails
def display_emails(set_name):
    # print(f"Emails in {'subscribers' if set_name == subscribers else 'unsubscribers'}")
    for email in set_name:
        print(email)
    print("")

# Function to find active subscribers. Return the set.
def find_active_subscribers(set1, set2):
    return set1.difference(set2)

# Adding emails to subscribers (notice that some people subscribe more than once)
add_email("user1@example.com", subscribers)
add_email("user3@example.com", subscribers)
add_email("user4@example.com", subscribers)
add_email("user11@example.com", subscribers)
add_email("user5@example.com", subscribers)
add_email("user6@example.com", subscribers)
add_email("user2@example.com", subscribers)
add_email("user5@example.com", subscribers)
add_email("user2@example.com", subscribers)
add_email("user7@example.com", subscribers)
add_email("user8@example.com", subscribers)
add_email("user9@example.com", subscribers)
add_email("user2@example.com", subscribers)
add_email("user11@example.com", subscribers)
add_email("user7@example.com", subscribers)
add_email("user10@example.com", subscribers)
add_email("user12@example.com", subscribers)

# Adding emails to unsubscribers
add_email("user6@example.com", unsubscribers)
add_email("user8@example.com", unsubscribers)
add_email("user1@example.com", unsubscribers)
add_email("user10@example.com", unsubscribers)

# Displaying subscribers and unsubscribers
print("All Subscribers:")
display_emails(subscribers)

print("All Unsubscribers:")
display_emails(unsubscribers)

# Finding active subscribers
print("Active Subscribers:")
display_emails(find_active_subscribers(subscribers, unsubscribers))