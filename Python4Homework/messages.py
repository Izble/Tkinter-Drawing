import time


class Message:
    def __init__(self, content):
        self.content = content

    def write_message(self, new_content):
        self.content = new_content

    def read_message(self):
        print("Message:", self.content)

    def send_message(self):
        print("Message sent.")


class Email(Message):
    def __init__(self, content):
        super().__init__(content)

    def send_message(self):
        for i in "Sending email":
            time.sleep(0.1)
            print(i)
        time.sleep(1)
        super().send_message()


class TextMassage(Message):
    def __init__(self, content):
        super().__init__(content)
        self.charaLimit = 114

    def send_message(self):
        if len(self.content) <= self.charaLimit:
            for i in "Sending text":
                time.sleep(0.05)
                print(i)
            time.sleep(0.5)
            super().send_message()

        elif len(self.content) > self.charaLimit:
            print("Over character limit. Would you like to change your message? Y/N")
            x = input()
            answer = x.lower()

            if answer == "n":
                print("Your message has been cut short.")
                self.content = (self.content[:self.charaLimit])
                for i in "Sending text":
                    time.sleep(0.01)
                    print(i)
                time.sleep(0.5)
                super().send_message()

            elif answer == "y":
                print("Not sent.")
                print("Please rewrite.")

            else:
                print("NA")


class Letter(Message):
    def __init__(self, content):
        super().__init__(content)

    def send_message(self):
        for i in "Mailing letter":
            time.sleep(0.8)
            print(i)
        time.sleep(1)
        super().send_message()

