import random
import time


class Remote_Controller():
    def __init__(self, TV_Status="OFF", TV_Volume="-", Channel_List=["BBC1"], Channel_Name="BBC1"):
        print("Creating a remote controller: ")

        self.TV_Status = TV_Status
        self.TV_Volume = TV_Volume
        self.Channel_List = Channel_List
        self.Channel_Name = Channel_Name

    def TV_On(self):
        if self.TV_Status == "ON":
            print("TV is already On!!")
        else:
            print("TV is turning On")
            self.TV_Status = "ON"

    def TV_Off(self):
        if self.TV_Status == "OFF":
            print("TV is already OFF!!")
        else:
            print("TV is turning Off")
            self.TV_Status = "OFF"

    def Volume_Adjustment(self):
        while True:
            Answer = input("Volume Down: '-' \nVolume Up: '+' \nExit: 'exit'")

            if Answer == "-":
                if self.TV_Volume != 0:
                    self.TV_Volume -= 1
                    print("Volume: ", self.TV_Volume)
            elif Answer == "+":
                if self.TV_Volume != 50:
                    self.TV_Volume += 1
                    print("Volume: ", self.TV_Volume)
            else:
                print("Sound level has updated.")
                break

    def Add_Channel(self, Channel_Name):
        print("Adding Channel...")
        time.sleep(1)

        self.Channel_List.append(Channel_Name)
        print("Channel added.")

    def Random_Channel(self):
        Random = random.randint(0, len(self.Channel_List) - 1)
        self.Channel_Name = self.Channel_List[Random]
        print("You are watching now ", self.Channel_Name)

    def __len__(self):
        return len(self.Channel_List)

    def __str__(self):
        return "TV Status: {} \nTV Volume: {} \nChannel List {} \nWatching Channel: {}".format(self.TV_Status,
                                                                                               self.TV_Volume,
                                                                                               self.Channel_List,
                                                                                               self.Channel_Name)


Remote_Controller_1 = Remote_Controller()
print("""

1. Turn on TV
2. Turn off TV
3. Volume Adjustment
4. Add Channel
5. Number of Channels
6. Open Random Channel
7. TV Info

For exit process Q

""")
while True:
    Operation = input("Choose the operation you want: ")

    if Operation == "Q" or Operation == "q":
        print("Program is closing... ")
    elif Operation == "1":
        Remote_Controller_1.TV_On()
    elif Operation == "2":
        Remote_Controller_1.TV_Off()
    elif Operation == "3":
        Remote_Controller_1.Volume_Adjustment()
    elif Operation == "4":
        Channel_Names = input("Input channel name: ")
        Channel_List = Channel_Names.split(",")
        for adding in Channel_List:
            Remote_Controller_1.Add_Channel(adding)
    elif Operation == "5":
        print("Number of Channel: ", len(Remote_Controller_1))
    elif Operation == "6":
        Remote_Controller_1.Random_Channel()
    elif Operation == "7":
        print(Remote_Controller_1)
    else:
        print("Invalid operation")
