class GroceryList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Add an item to the grocery list."""
        self.items.append(item)
        print(f"{item} added to the list.")

    def remove_item(self, item):
        """Remove an item from the grocery list."""
        if item in self.items:
            self.items.remove(item)
            print(f"{item} removed from the list.")
        else:
            print(f"{item} not found in the list.")

    def view_list(self):
        """View all items in the grocery list."""
        if not self.items:
            print("Your grocery list is empty.")
        else:
            print("------------------------------------")
            print("Grocery List:")
            for item in self.items:
                print(f"- {item}")
            print("------------------------------------")

    def update_item(self, old_item, new_item):
        """Update an item in the grocery list."""
        if old_item in self.items:
            index = self.items.index(old_item)
            self.items[index] = new_item
            print(f"{old_item} updated to {new_item}.")
        else:
            print(f"{old_item} not found in the list.")

def main():
    grocery_list = GroceryList()

    while True:
        print("\nGrocery List Menu:")
        print("1. View List")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Update Item")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            grocery_list.view_list()
        elif choice == '2':
            item = input("Enter the item to add: ")
            grocery_list.add_item(item)
        elif choice == '3':
            item = input("Enter the item to remove: ")
            grocery_list.remove_item(item)
        elif choice == '4':
            old_item = input("Enter the item to update: ")
            new_item = input("Enter the new item: ")
            grocery_list.update_item(old_item, new_item)
        elif choice == '5':
            print("Exiting the grocery list.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
