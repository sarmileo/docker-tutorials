# calculator.py
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python calculator.py <operation> <num1> <num2>")
        sys.exit(1)

    operation = sys.argv[1]
    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])

    if operation == "add":
        print(f"The result is: {num1 + num2}")
    elif operation == "subtract":
        print(f"The result is: {num1 - num2}")
    elif operation == "multiply":
        print(f"The result is: {num1 * num2}")
    elif operation == "divide":
        if num2 != 0:
            print(f"The result is: {num1 / num2}")
        else:
            print("Error: Division by zero.")
    else:
        print("Error: Unsupported operation.")

if __name__ == "__main__":
    main()