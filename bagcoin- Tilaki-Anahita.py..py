print(" Program to sort and count a bag of coins")
print(" Anahita Tilaki")
print("Date: 09-08-2024")
print("This program counts US coins from a bag based on their size") 
print("displays the coin count, and calculates the total value of the bag.")

# Constants for US coin sizes (in mm)
QUARTER = 24
DIME = 18
NICKEL = 21
PENNY = 19

def coin_tally(bag_of_coins):
    
    # Initialize counters for each type of coin
    quarter_count = 0
    dime_count = 0
    nickel_count = 0
    penny_count = 0
    foreign_count = 0
    
    # Loop through the bag of coins and tally them
    for coin in bag_of_coins:
        if coin == QUARTER:
            quarter_count += 1
        elif coin == DIME:
            dime_count += 1
        elif coin == NICKEL:
            nickel_count += 1
        elif coin == PENNY:
            penny_count += 1
        else:
            foreign_count += 1
    
    # Return a list of counts in the required order
    return [quarter_count, dime_count, nickel_count, penny_count, foreign_count]

def bag_value(coin_counts):
    
    # The values of the coins in USD
    quarter_value = 0.25
    dime_value = 0.10
    nickel_value = 0.05
    penny_value = 0.01
    
    # Calculate total value (exclude foreign coins)
    total_value = (coin_counts[0] * quarter_value +
                   coin_counts[1] * dime_value +
                   coin_counts[2] * nickel_value +
                   coin_counts[3] * penny_value)
    
    return total_value

def output_coin_count(coin_counts):
    
    print(f"The bag has {coin_counts[0]} quarter(s), {coin_counts[1]} dime(s), "
          f"{coin_counts[2]} nickel(s), {coin_counts[3]} cent(s), and {coin_counts[4]} foreign coin(s)")

def main():
    
    # Simulate a bag of coins using a list of 22 integers
    bag_coin = [19, 21, 20, 19, 18, 20, 19, 24, 25, 19, 24, 18, 23, 21, 19, 24, 18, 24, 18, 21, 32, 24]
    
    # Call the coin_tally function
    coin_counts = coin_tally(bag_coin)
    
    # Display the coin tally
    output_coin_count(coin_counts)
    
    # Calculate and display the total value of the bag
    total_value = bag_value(coin_counts)
    print(f"Total Value: ${total_value:.2f}")

# Ensure the main function runs when the script is executed
if __name__ == "__main__":
    main()
    input(" press Enter to exit")
