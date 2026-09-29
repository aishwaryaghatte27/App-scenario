import csv
import sys

# Check whether filename is provided
if len(sys.argv) != 2:
    print("Usage: python grocery.py <filename>")
    sys.exit()

filename = sys.argv[1]

# Read grocery records
try:
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        groceries = list(reader)

except FileNotFoundError:
    print("File not found!")
    sys.exit()

# Display all grocery items
def display_items():
    print("\n--- Grocery Inventory ---")

    for item in groceries:
        print(
            "ID:", item["ItemID"],
            "| Name:", item["ItemName"],
            "| Category:", item["Category"],
            "| Quantity:", item["Quantity"],
            "| Price:", item["Price"]
        )


# Search item using Item ID
def search_item(item_id):
    for item in groceries:
        if item["ItemID"] == item_id:
            print("\nItem Found!")
            print("Item ID :", item["ItemID"])
            print("Item Name :", item["ItemName"])
            print("Category :", item["Category"])
            print("Quantity :", item["Quantity"])
            print("Price :", item["Price"])
            return

    print("\nItem not found!")


# Main program
display_items()

item_id = input("\nEnter Item ID to search: ")
search_item(item_id)