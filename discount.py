def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Parameters:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage.

    Returns:
        float: The final price after discount (if applied).
    """
    if price < 0 or discount_percent < 0:
        raise ValueError("Price and discount_percent must be non-negative.")

    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return round(final_price, 2)
    else:
        return round(price, 2)


# --- Main Program ---
try:
    # Prompt user for input
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate final price
    final_price = calculate_discount(original_price, discount_percent)

    # Print result
    if discount_percent >= 20:
        print(f"Final price after {discount_percent}% discount: {final_price}")
    else:
        print(f"No discount applied. Original price: {final_price}")

except ValueError:
    print("Invalid input! Please enter numeric values for price and discount.")