#Programmer: Timothy Pickering
#Date: 3/25/25
#Title: Classy car program

class Car:
    #Initialize the Car object with year model, make, and speed set to 0
    def __init__(self, year_model, make):
        #Attribute for year model
        self.__year_model = year_model
        #Attribute for car make
        self.__make = make
        # Speed starts at 0
        self.__speed = 0

    def accelerate(self):
        #Increase the speed by 5
        self.__speed += 5

    def brake(self):
        #Decrease the speed by 5, ensuring it does not go below 0
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            #Prevents negative speed
            self.__speed = 0

    def get_speed(self):
        #Return the current speed of the car
        return self.__speed

#Main program to test the Car class
def main():
    #Create a Car object with user input
    year = input("Enter the car's year model: ")
    make = input("Enter the car's make: ")
    my_car = Car(year, make)

    print("\nAccelerating the car...")
    #Call accelerate 5 times
    for _ in range(5):
        my_car.accelerate()
        print(f"Current speed: {my_car.get_speed()} mph")

    print("\nApplying brakes...")
    #Call brake 5 times
    for _ in range(5):
        my_car.brake()
        print(f"Current speed: {my_car.get_speed()} mph")

    print("\nCar stopped.")

#Run the program
if __name__ == "__main__":
    main()
