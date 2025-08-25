'''
A simple program to set the circle's radius to 20, compute the area using the formula:
area = PI * radius * radius, and display the result on the screen.
'''
# Filename: compute_area.py
def main():
    # Define the radius of the circle
    radius = 20
    # Define PI as 3.14159
    PI = 3.14159
    # Compute area
    area = PI * radius * radius
    # Display results
    print("The area for the circle of radius", radius, "is", area)

if __name__ == "__main__":
    main()