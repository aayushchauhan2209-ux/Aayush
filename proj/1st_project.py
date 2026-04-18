# This code defines a solution for adding two numbers represented as lists of digits. The `solution` class has a method `add` that takes two lists of digits, reverses them, and then uses the `AddNum` class to perform the addition. The `AddNum` class has a method `add2` that iterates through the digits, adds them together along with any carry from the previous addition, and constructs the result list. Finally, the result is reversed back to the correct order before being printed.
class solution(object):
    def add(self,L1,L2):
        self.L1 = L1
        self.L2 = L2
        list1 = L1.copy()
        list1.reverse()
        list2 = L2.copy()
        list2.reverse()
        A1 = AddNum(list1,list2)
        return A1.add2()

class AddNum(object):
    def __init__(self,list1,list2):
        self.list1 = list1
        self.list2 = list2

    def add2(self):
        carry = 0
        result = []
        for i in range(max(len(self.list1),len(self.list2))):
            digit1 = self.list1[i] if i < len(self.list1) else 0
            digit2 = self.list2[i] if i < len(self.list2) else 0
            total = digit1 + digit2 + carry
            carry = total // 10
            result.append(total % 10)
        if carry:
            result.append(carry)
        return result
    

s1 = solution()
Res = s1.add([2,3,4],[1,2,3])
Result = Res.copy()
Result.reverse()
print(Result)

