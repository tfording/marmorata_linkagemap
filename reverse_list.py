#author=Tyler Fording

list_to_be_reversed = ['Scpiz6a_49', 'Scpiz6a_55.1', 'Scpiz6a_26', 'Scpiz6a_73', 'Scpiz6a_37', 'Scpiz6a_28', 'Scpiz6a_146', 'Scpiz6a_30.1', 'Scpiz6a_65', 'Scpiz6a_27', 'Scpiz6a_72', 'Scpiz6a_11.1', 'Scpiz6a_1', 'Scpiz6a_43', 'Scpiz6a_17.2', 'Scpiz6a_120', 'Scpiz6a_74', 'Scpiz6a_147', 'Scpiz6a_118', 'Scpiz6a_122', 'Scpiz6a_45', 'Scpiz6a_47', 'Scpiz6a_44', 'Scpiz6a_29', 'Scpiz6a_44.1', 'Scpiz6a_86', 'Scpiz6a_75', 'Scpiz6a_148', 'Scpiz6a_113']
reversed_list = []


'''
This looks like homework, so I won't really give a full solution, but I'll provide a way to get there. If the numbers 
are being taken in as a list, then we can break down our solution as such:

if rest(lst).length == 0: #Check to see if we're down the first item
    return lst
else: #We need to break the list down some more
    return "call the method again on the rest of the list" + [first(lst)]
Break down the list into individual values
When we get down to a single item, start building the list back up (Base Case)
With Python, using  stuff + [item] will concatenate lists together (so long as "stuff" is another list). The else block 
above will call the recursive function to break down the list, and as it begins to return up the recursive dive, it 
will concatenate on the first item in the list in reverse order. This return up the dive occurs when the you get down 
to the singleton list, which the if block catches.

'''

def reverse_list(l):
    return l and reverse_list(l[1:]) + [l[0]]


reverse_list(list_to_be_reversed)


list2 =['Scpiz6a_113', 'Scpiz6a_148', 'Scpiz6a_75', 'Scpiz6a_86', 'Scpiz6a_44.1', 'Scpiz6a_29', 'Scpiz6a_44', 'Scpiz6a_47', 'Scpiz6a_45', 'Scpiz6a_122', 'Scpiz6a_118', 'Scpiz6a_147', 'Scpiz6a_74', 'Scpiz6a_120', 'Scpiz6a_17.2', 'Scpiz6a_43', 'Scpiz6a_1', 'Scpiz6a_11.1', 'Scpiz6a_72', 'Scpiz6a_27', 'Scpiz6a_65', 'Scpiz6a_30.1', 'Scpiz6a_146', 'Scpiz6a_28', 'Scpiz6a_37', 'Scpiz6a_73', 'Scpiz6a_26', 'Scpiz6a_55.1', 'Scpiz6a_49']
