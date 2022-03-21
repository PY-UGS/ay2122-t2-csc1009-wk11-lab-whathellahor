class ClockTime:
    # Constructor
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    # Function to let user set hours
    def setHours(self, hours):
        self.hours = hours

    # Function to let user set the minutes
    def setMinutes(self, minutes):
        self.minutes = minutes

    # Function to let user set the seconds
    def setSeconds(self, seconds):
        self.seconds = seconds

    # Function to let user set the hours, minutes, seconds all at once
    def setTime(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    # Function to show time to user
    def showTime(self):
        print("The time is ", self.hours, ":", self.minutes, ":", self.seconds)


# Set the default hours, minutes and seconds to be 0
clockTime = ClockTime(0, 0, 0)
clockTime.setHours(input("Enter Hours: "))      # Take in the input from users to set the hours
clockTime.setMinutes(input("Enter Minutes: "))  # Take in the input from users to set the minutes
clockTime.setSeconds(input("Enter Seconds: "))  # Take in the input from users to set the seconds
clockTime.showTime()                            # Print the time as defined by the user