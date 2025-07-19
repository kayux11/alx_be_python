# 1. Prompt for a Single Task
task = input("Enter the task description: ")
priority = input("Enter the task priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# 2. Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        message = f"🔴 HIGH PRIORITY: {task}"
    case "medium":
        message = f"🟡 MEDIUM PRIORITY: {task}"
    case "low":
        message = f"🟢 LOW PRIORITY: {task}"
    case _:
        message = f"⚪ UNKNOWN PRIORITY: {task}"

# Add time-bound info
if time_bound == "yes":
    message += " — that requires immediate attention today!"

# 3. Provide a Customized Reminder
print("\n📌 Daily Reminder:")
print(message)
