def main():
    mass = int(input("Enter mass: "))
    
    # Speed of light in m/s
    c = 300000000  # 3 * 10^8 meters per second
    
    # Calculate energy using the equation E = mc^2
    energy = mass * c ** 2
    
    # Output the result
    print(energy)

if __name__ == "__main__":
    main()
