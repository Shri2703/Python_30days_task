'''Problem Statement:
get the friends name as a input and print like join  all names and one message  we all together  '''

#Solution


names_input = input("Enter the names of your friends, separated by commas: ")
friend_names = names_input.split(',')
all_friends = ', '.join(friend_names)
print(f"We all together: {all_friends}")


