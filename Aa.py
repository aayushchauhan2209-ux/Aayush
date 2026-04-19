def duplicate_count(text):
    st = str(text)
    Str = st.lower()
    lis = list(Str)
    checked = [] # An empty list which will store every character that are checked 
    found = False # to check if any number or character is not reepeted 
    for i in lis:
        if i not in checked:
            count = lis.count(i)
            if count > 1:
                print(i," repeted",count,"times")
                found = True
            checked.append(i)
    if not lis or not found:
        print("0 repetation")
     
A = str(input("Enter your string: "))
duplicate_count(A)
