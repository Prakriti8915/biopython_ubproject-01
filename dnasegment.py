


original_base= input("Enter the original base : ").upper()
new_base= input("Enter the new base : ").upper()

if original_base not in ['A','T','G','C'] or new_base not in ['A','T','G','C'] :
   print("INVALID DNA BASE")
elif original_base == new_base:
   print("No mutation has occurred")
elif (original_base == 'A' and new_base == 'G') or (original_base == 'G' and new_base == 'A') or (original_base == 'C' and new_base == 'T') or (original_base == 'T' and new_base == 'C'):
   print("Transition mutation has occurred")
else:
   print("Transversion mutation has occurred")
