from datetime import datetime

def chatbot():
    print("=" * 40)
    print("      WELCOME TO SMART BOT")
    print("=" * 40)
    print("Commands:")
    print("hello, how are you, name, time, date")
    print("calculator, joke, help, bye")
    print()

    while True:
        user = input("You: ").lower().strip()

        if user in ["hello", "hi", "hey"]:
            print("Bot: Hello! How can I help you today?")

        elif user == "how are you":
            print("Bot: I'm doing great! Thanks for asking.")

        elif user == "name":
            print("Bot: My name is SmartBot.")

        elif user == "time":
            print("Bot:", datetime.now().strftime("%H:%M:%S"))

        elif user == "date":
            print("Bot:", datetime.now().strftime("%d-%m-%Y"))

        elif user == "calculator":
            try:
                num1 = float(input("Enter first number: "))
                op = input("Enter operation (+, -, *, /): ")
                num2 = float(input("Enter second number: "))

                if op == "+":
                    print("Result =", num1 + num2)
                elif op == "-":
                    print("Result =", num1 - num2)
                elif op == "*":
                    print("Result =", num1 * num2)
                elif op == "/":
                    print("Result =", num1 / num2)
                else:
                    print("Invalid operator!")
            except:
                print("Invalid input!")

        elif user == "joke":
            print("Bot: Why do programmers prefer dark mode?")
            print("Bot: Because light attracts bugs!")

        elif user == "help":
            print("\nAvailable Commands:")
            print("hello")
            print("how are you")
            print("name")
            print("time")
            print("date")
            print("calculator")
            print("joke")
            print("bye\n")

        elif user == "bye":
            print("Bot: Goodbye! Have a great day.")
            break

        else:
            print("Bot: Sorry, I don't understand that command.")

chatbot()
