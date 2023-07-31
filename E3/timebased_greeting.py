import time

# Get current time in 24-hour format
current_time = time.strftime ('The Current Time is: %H:%M:%S')
print(current_time)

# Get current hour, minute, and second
current_hour = int(time.strftime('%H'))
current_minute = int(time.strftime('%M'))
current_second = int(time.strftime('%S'))

print(f"Current Hour: {current_hour}")
print(f"Current Minute: {current_minute}")
print(f"Current Second: {current_second}")

# Get user's name and display personalized greeting
name = input("Enter your name: ")
if 3 <= current_hour < 12:
    print(f"Hello, {name}! Good Morning")
elif 12 <= current_hour < 16:
    print(f"Hello, {name}! Good Afternoon")
else:
    print(f"Hello, {name}! Good Evening")