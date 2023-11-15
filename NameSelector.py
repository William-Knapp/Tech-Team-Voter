import os

class TechTeamVoter:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_list_from_file(self):
        with open(self.file_path, 'r') as reader:
            return [line.strip() for line in reader]

    def write_list_to_file(self, name_list):
        with open(self.file_path, 'w') as writer:
            writer.write('\n'.join(name_list))

    def create_list(self):
        name_list = []
        keep_going = input("Warning! This option overwrites any existing lists. Are you sure you want to continue? (y/n): ")
        if keep_going.lower() != "y":
            print("List creation canceled.")
            return self.read_list_from_file()
        while keep_going.lower() == "y":
            new_name = input("Please enter a name: ").capitalize()
            name_list.append(new_name)
            keep_going = input("Keep going? (y/n): ")
        self.write_list_to_file(name_list)
        print("List created successfully.")
        return name_list

    def show_list(self):
        name_list = self.read_list_from_file()
        print("The current list of names is:", name_list)
        return name_list

    #old code that wouldn't allow adding a name that was in list already
    # def add_name(self, name):
    #     name = name.capitalize()
    #     if name not in self.read_list_from_file():
    #         name_list = self.read_list_from_file()
    #         name_list.append(name)
    #         self.write_list_to_file(name_list)
    #         return f"{name} has been added successfully."
    #     return f"{name} is already in the list."


    def add_name(self, name):
        name = name.capitalize()
        name_list = self.read_list_from_file()

        if name in name_list:
            name_list = [n for n in name_list if n != name]  # Remove duplicates

        name_list.append(name)
        self.write_list_to_file(name_list)
        return f"{name} has been added successfully."


    def remove_name(self, name):
        name = name.capitalize()
        name_list = self.read_list_from_file()
        if name in name_list:
            name_list.remove(name)
            self.write_list_to_file(name_list)
            return f"{name} removed successfully."
        return f"Could not find {name} in the list."

    def cast_vote(self):
        team_members = self.read_list_from_file()
        return team_members[0]
    
    def display_menu(self):
        print("\n*** Main Menu ***")
        print("1. Create List")
        print("2. Show List")
        print("3. Add Name")
        print("4. Remove Name")
        print("5. Tech Team Vote")
        print("6. Quit\n")


def main():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "TechTeamNames.txt")
    voter = TechTeamVoter(file_path)

    menu_options = {
        '1': voter.create_list,
        '2': voter.show_list,
        '3': lambda: print(voter.add_name(input("Enter a new name into the list: "))),
        '4': lambda: print(voter.remove_name(input("Enter a name to remove from the list: "))),
        '5': lambda: voter.add_name(input(f"The winner of this month's vote should be {voter.cast_vote()}. Enter the actual winner: ")),
        '6': exit
    }


    #old code that didnt' have the prompt for who actually won
    # menu_options = {
    #     '1': voter.create_list,
    #     '2': voter.show_list,
    #     '3': lambda: print(voter.add_name(input("Enter a new name into the list: "))),
    #     '4': lambda: print(voter.remove_name(input("Enter a name to remove from the list: "))),
    #     '5': lambda: print(f"The winner of this month's vote should be {voter.cast_vote()}"),
    #     '6': exit
    # }



    while True:
        voter.display_menu()
        
        choice = input("Please enter a number corresponding to the menu above: ")

        if choice in menu_options:
            menu_options[choice]()
        else:
            print("Invalid input. Please enter a number 1 - 6.\n")

if __name__ == "__main__":
    main()
