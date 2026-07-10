import re

# Open and read the input text file
with open("input.txt", "r") as file:
    content = file.read()

# Regular expression pattern for email addresses
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Find all email addresses
emails = re.findall(email_pattern, content)

# Save extracted emails to a new file
with open("emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Email addresses extracted successfully!")
print("Found Emails:")
for email in emails:
    print(email)
