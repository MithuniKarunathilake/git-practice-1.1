class GroceryList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Add an item to the grocery list."""
        item = item.strip()
        if not item:
            print("Cannot add an empty item.")
        elif item.lower() in (i.lower() for i in self.items):
            print(f"{item} is already in the list.")
        else:
            self.items.append(item)
            print(f"{item} added to the list.")

    def remove_item(self, item):
        """Remove an item from the grocery list."""
        if self._item_exists(item):
            self.items.remove(item)
            print(f"{item} removed from the list.")

    def update_item(self, old_item, new_item):
        """Update an item in the grocery list."""
        if self._item_exists(old_item):
            new_item = new_item.strip()
            if not new_item:
                print("Cannot update to an empty item.")
            elif new_item.lower() in (i.lower() for i in self.items):
                print(f"{new_item} is already in the list.")
            else:
                index = self.items.index(old_item)
                self.items[index] = new_item
                print(f"{old_item} updated to {new_item}.")

    def view_list(self):
        """View all items in the grocery list."""
        if not self.items:
            print("Your grocery list is empty.")
        else:
            print("------------------------------------")
            print("Grocery List:")
            for index, item in enumerate(self.items, start=1):
                print(f"{index}. {item}")
            print("------------------------------------")

    def _item_exists(self, item):
        """Check if an item exists in the grocery list."""
        for i in self.items:
            if i.lower() == item.lower():
                return True
        print(f"{item} not found in the list.")
        return False


def show_menu():
    """Display the menu options."""
    print("\nGrocery List Menu:")
    print("1. View List")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Update Item")
    print("5. Exit")


def main():
    grocery_list = GroceryList()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == '1':
            grocery_list.view_list()
        elif choice == '2':
            item = input("Enter the item to add: ").strip()
            grocery_list.add_item(item)
        elif choice == '3':
            item = input("Enter the item to remove: ").strip()
            grocery_list.remove_item(item)
        elif choice == '4':
            old_item = input("Enter the item to update: ").strip()
            new_item = input("Enter the new item: ").strip()
            grocery_list.update_item(old_item, new_item)
        elif choice == '5':
            print("Exiting the grocery list. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
