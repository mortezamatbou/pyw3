from random import randrange


class CommandClass:
    score = {"cows": 0, "bulls": 0}
    try_count = 0
    bulls = 0
    cows = 0

    current_number = 0
    answer = 0
    digit_count = 0

    command = 0

    def __init__(self):
        pass

    def inc_score(self):
        self.score += 1

    def inc_bulls(self):
        self.bulls += 1

    def inc_cows(self):
        self.cows += 1

    def inc_try(self):
        self.try_count += 1

    def commands_list(self):
        print("1] get number")
        print("2] scores")
        print("3] try")
        print("4] exit")

    def check_command_actions(self, command):
        if command == 1:
            self.current_number = self.generate_number(4)
            self.answer = input("Guess number (4 digit): ")
            try:
                self.answer = int(self.answer)
                self.check_answer()
                self.print_last_try_info()
            except:
                self.answer = 0
                print("Invalid input")

        elif command == 2:
            self.print_total_score()
        elif command == 3:
            self.print_try_info()
        else:
            pass

    def generate_number(self, digit=4):
        self.digit_count = 0
        try:
            self.digit_count = int(digit)
        except:
            self.digit_count = 4
        else:
            if self.digit_count <= 0:
                self.digit_count = 4

        num_from = int("1" + ("0" * (self.digit_count - 1)))
        num_to = int("9" * self.digit_count)

        number = randrange(num_from, num_to)

        return number

    def get_current_number(self):
        return self.current_number

    def check_answer(self):
        answer = str(self.answer)
        current_number = str(self.current_number)
        self.bulls = 0
        self.cows = 0

        self.try_count += 1

        for i in range(0, self.digit_count):
            if answer[i] == current_number[i]:
                self.inc_bulls()
                self.score['bulls'] += 1
            else:
                self.inc_cows()
                self.score['cows'] += 1

        print("Number is: ", self.current_number)
        print("Your Guess:", self.answer)

        print('')

    def print_try_info(self):
        print("")
        print("[INFO] You try {try_count} times".format(try_count=self.try_count))
        print("")

    def print_total_score(self):
        print("")
        print("[INFO] You try {try_count} times".format(try_count=self.try_count))
        print("[INFO] In total, bulls is {bulls}, cows is {cows}".format(bulls=self.score['bulls'],
                                                                         cows=self.score['cows']))
        print("")

    def print_last_try_info(self):
        print("[INFO] Last try, bulls is {bulls}, cows is {cows}".format(bulls=self.bulls, cows=self.cows))
        print("")


command_obj = CommandClass()


def loop():
    global command_obj
    command_obj.commands_list()
    while True:
        command_input = input("Enter command number: ")
        command = 0

        try:
            command = int(command_input)
        except:
            command = 0

        if command == 0:
            print("[[ERROR]] Bad Request")
            continue

        if command == 4:
            print("Bye!")
            exit()

        command_obj.check_command_actions(command)

        command_obj.commands_list()
