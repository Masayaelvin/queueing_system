from queue_pro import queue

def main():
    '''main function'''
q = queue()
while True:
    print("Welcome to the queue system")
    print("1. Join queue")
    print("2. Leave queue")
    print("3. Check position")
    print("4. queue list")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter your name: ")
        q.join(name)
        main()
    elif choice == 2:
        q.leave()
        main()
    elif choice == 3:
        name = input("Enter your name: ")
        q.position(name)
        main()
    elif choice == 4:
        q.queue_list()
        main()
    elif choice == 5:
        print("Goodbye")
        exit()
    else:
        print("Invalid choice")
        main()




        



