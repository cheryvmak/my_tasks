
 #  Task 3

nigerian_state =  []
state_1 =  input("Enter state 1: ")
state_2 =  input("Enter state 2: ")
state_3 =  input("Enter state 3: ")
state_4 =  input("Enter state 4: ")
state_5 =  input("Enter state 5: ")

print(nigerian_state.append(state_1))
print(nigerian_state.append(state_2))
print(nigerian_state.append(state_3))
print(nigerian_state.append(state_4))
print(nigerian_state.append(state_5))
nigerian_state = tuple(nigerian_state)
print(nigerian_state)
print(nigerian_state[0:5:4])
print("Lagos" in nigerian_state)
print(len(nigerian_state))
