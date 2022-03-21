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
        print("The time is " + self.hours + ":" + self.minutes + ":" + self.seconds)


userHours = input("Enter Hours: ")                          # Take in user input for hours
userMinutes = input("Enter Minutes: ")                      # Take in user input for minutes
userSeconds = input("Enter Seconds: ")                      # Take in user input for seconds
clockTime = ClockTime(userHours, userMinutes, userSeconds)  # Pass the values into function setTime
clockTime.showTime()                                        # Print the time as defined by the user