def main():
    
    shopping_list = []
    

    while True:
        # Display menu
        print("\n=== Shopping List Manager ===")
        print("1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Exit")
        
        # Get user choice
        choice = input("Enter your choice (1-4): ").strip()
        
        # Add item
        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:  # Check if item is not empty
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("Item cannot be empty.")
        
        # Remove item
        elif choice == '2':
            if not shopping_list:
                print("The shopping list is empty.")
            else:
                print("Current shopping list:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                
                item_to_remove = input("Enter the item to remove: ").strip()
                if item_to_remove in shopping_list:
                    shopping_list.remove(item_to_remove)
                    print(f"'{item_to_remove}' has been removed from the shopping list.")
                else:
                    print(f"'{item_to_remove}' was not found in the shopping list.")
        
        # View list
        elif choice == '3':
            if not shopping_list:
                print("The shopping list is empty.")
            else:
                print("\n=== Current Shopping List ===")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                print(f"Total items: {len(shopping_list)}")
        
        # Exit
        elif choice == '4':
            print("Thank you for using Shopping List Manager. Goodbye!")
            break
        
        # Handle invalid menu choices
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Run the program
if __name__ == "__main__":
    main()