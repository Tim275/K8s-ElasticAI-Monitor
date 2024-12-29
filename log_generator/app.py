from flask import Flask, request
import random
import time

app = Flask(__name__)

def random_error_logs():
    """Randomly generate different types of error messages"""
    errors = [
        lambda: 1 / 0,  # ZeroDivisionError
        lambda: my_undefined_var,  # NameError
        lambda: int("not_a_number")  # ValueError
    ]
    try:
        error = random.choice(errors)
        error()
    except Exception as e:
        print(f"ERROR: {type(e).__name__} occurred: {e}")

# Simulated endpoint for a variety of variable-related and random errors
@app.route('/variable_not_found')
def variable_not_found_log():
    for _ in range(10):
        try:
            random_error_logs()  # Generate random errors
        except NameError as e:
            print(f"ERROR: Variable not found: {e}")
        except ValueError as e:
            print(f"ERROR: Value conversion failed: {e}")
    return "Variable-related logs generated!"

# Simulated endpoint for logging repeated and diverse outputs
@app.route('/repeated_log')
def repeated_log():
    messages = ["INFO: User login attempt", "DEBUG: Processing data", "INFO: Data saved successfully"]
    for i in range(400):
        print(f"DEBUG: Repeated log {i}: {random.choice(messages)}")
    return "Repeated and diverse log messages generated!"

# Simulated endpoint for logging different math and random errors
@app.route('/division_by_zero')
def division_by_zero_log():
    for _ in range(10):
        try:
            result = 1 / random.choice([0, 1])  # Randomly raise ZeroDivisionError
        except ZeroDivisionError as e:
            print(f"ERROR: Division by zero: {e}")
        random_error_logs()  # Additional random error logs
    return "Division and other math error logs generated!"

# Simulated endpoint for logging larger and diverse data entries
@app.route('/log_large_data')
def log_large_data():
    for i in range(5):
        large_data = "data_chunk_" + str(i) + ": " + "a" * random.randint(50000, 100000)
        print(f"INFO: Logging large data {i}: {large_data[:100]}... (truncated)")
    return "Large data logs generated!"

# Simulated endpoint for logging frequent diverse messages
@app.route('/frequent_logs')
def frequent_logs():
    log_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    messages = ["Frequent log message", "Processing request", "System load high", "Memory usage at threshold", "Disk almost full"]
    for i in range(500):
        print(f"{random.choice(log_levels)}: {random.choice(messages)} - Instance {i}")
        time.sleep(0.005)  # Rapid logging
    return "Frequent logs with diverse messages generated!"

# Simulated endpoint for generating various types of mixed logs
@app.route('/generate_mixed_logs')
def generate_mixed_logs():
    log_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    messages = [
        "Debugging info for troubleshooting.",
        "User login successful.",
        "Low disk space warning.",
        "Database connection lost.",
        "Critical server error: immediate attention needed."
    ]
    for _ in range(50):
        print(f"{random.choice(log_levels)}: {random.choice(messages)}")
    return "Mixed logs with various types generated!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)