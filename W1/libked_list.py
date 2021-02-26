import copy

class Element:
    def __init__(self, data):
        self.data = data
        self.status = False
        self.next = None

    def __str__(self):
        return str(self.data)

    def check_status(self):
        if self.status:
            raise ValueError("elm can't be in two linked list")

        self.status = True



class LinkedList:
    def __init__(self):
        self.header = None

    def add_begin(self, elm):
        elm.check_status()

        if not self.header:
            self.header = elm
        else:
            elm.next = self.header
            self.header = elm


    def append(self, elm):    
        elm.check_status()

        if not self.header:
            self.header = elm
        else:
            temp = self.header
            while True:
                if not temp.next:
                    temp.next = elm
                    break
                temp = temp.next

    def pop(self):
        if not self.header:
            raise ValueError("Linked List is empty!")
        else:
            temp = self.header
            while True:
                if not temp.next.next:
                    res = temp.next
                    temp.next.status = False
                    temp.next = None
                    return res
                temp = temp.next
        

    def get_by_index(self, index):
        pass

    def remove(self, elm):
        pass

    def reverse(self):
        pass

    def __str__(self):
        if not self.header:
            return "[]"
        res = "["
        temp = self.header
        while True:
            if not temp.next:
                res += (str(temp.data))
                break
            res += (str(temp.data) + " ,")
            temp = temp.next

        res += "]"
        return res



elm1 = Element("ashkan")
elm2 = Element(2)
elm3 = Element(True)
elm4 = Element("Arian Zang bezar")


ll = LinkedList()
ll.add_begin(elm1)
ll.add_begin(elm2)
ll.add_begin(elm3)
ll.append(elm4)


list()

ll1 = LinkedList()
# ll1.append(elm4)
# ll.append(elm3)



print(ll)
print("-----------------------")
print(ll.pop())
print(ll)


# a = 4
# b = "ash"
# fl = 2.5
# bl = True
# elm5 = Element("as")
# list1  = [1, 2]
# my_list = [a, elm5, list1, b, fl, bl]
# my_list1 = [a, list1]

# b = "asss"
# list1.append(3)
# a = 8
# fl = 2.6
# bl = False
# elm5.data = "av"

# c = 2

# d = 4

# print(id(my_list[0]), id(d))



# print(my_list)