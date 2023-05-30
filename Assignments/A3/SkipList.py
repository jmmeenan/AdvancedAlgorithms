import random
class ListNode:
  def __init__(self, val):
      self.val = val
      self.next = None
      self.down = None


class LookUpSkipList:
    def __init__(self):
        # Any variables for intialization
        self.levels = []
        self.numberOfLevels = 0

    def lookup_search(self, target: int) -> bool:
        # Complete this function
        # Returns True if the element is present in skip list else False
        level = len(self.levels)-1
        hold = self.levels[level]
        while (target < hold.val or hold.next == None) and level >= 0 :
            level -= 1
            hold = self.levels[level]
        
        if hold.val == target:
            return True
        while hold.next != None:
            if hold.next.val == target:
                return True
            elif target > hold.next.val:
                if hold.next == None:
                    print("From1 " + str(hold.val) + " to " + str(hold.down.val))
                    hold = hold.down
                else:
                    print("From2 " + str(hold.val) + " to " + str(hold.next.val))
                    if hold.next == None and hold.down != None:
                        while(hold.next == None):
                            hold = hold.down
                    elif hold.next != None:
                        hold = hold.next
                    else:
                        hold = self.levels[0]
            elif target > hold.val and target < hold.next.val:
                print("From3 " + str(hold.val) + " to " + str(hold.down.val))
                hold = hold.down
        return False

        


    def insert(self, num: int) -> None:
        if self.levels == []:
            self.insertListBase(num, 0)
        else:
            hold = self.levels[0]
            pointer = self.insertListBase(num, 0)
            newLvl = random.randint(0,2)
            count = 1
            while(newLvl == 2):
                pointer2 = self.insertList(num, count, pointer)
                pointer = pointer2
                newLvl = random.randint(1,2)
                count += 1

    def insertList(self, num: int, lvl: int, pointer: ListNode):
        
        if self.numberOfLevels == 0:
            i = ListNode(num)
            i.down = pointer
            self.levels.append(i)
            self.numberOfLevels += 1
            return i
        if self.numberOfLevels < lvl+1:
            i = ListNode(num)
            i.down = pointer
            self.levels.append(i)
            self.numberOfLevels += 1
            return i
        hold = self.levels[lvl]
        if num < hold.val:
            i = ListNode(num)
            i.down = pointer
            i.next = hold
            self.levels[lvl] = i
            return i
        else:
            while num >= hold.val:
                if hold.next == None:
                    break
                hold = hold.next
            if(hold.next == None and num >= hold.val):
                hold.next = ListNode(num)
                hold.down = pointer
                return hold.next
            else:
                n = hold.val
                down = hold.down
                ne = hold.next
                hold.val = num
                hold.down = pointer
                hold.next = ListNode(n)
                hold.next.next = ne
                hold.next.down = down
                return hold
    
    def insertListBase(self, num: int, lvl: int):
        
        if self.numberOfLevels == 0:
            self.levels.append(ListNode(num))
            self.numberOfLevels += 1
            return ListNode(num)
        if self.numberOfLevels < lvl+1:
            self.levels.append(ListNode(num))
            self.numberOfLevels += 1
            return ListNode(num)
        hold = self.levels[lvl]
        if num < hold.val:
            i = ListNode(num)
            i.next = hold
            self.levels[lvl] = i
            return i
        else:
            while num >= hold.val:
                if hold.next == None:
                    break
                hold = hold.next
            if(hold.next == None and num >= hold.val):
                hold.next = ListNode(num)
                return hold.next
            else:
                n = hold.val
                down = hold.down
                ne = hold.next
                hold.val = num
                hold.down = None
                hold.next = ListNode(n)
                hold.next.next = ne
                hold.next.down = down
                return hold


            
    def remove(self, value:int, pointer:ListNode):
        pass

    def delete(self, num: int) -> bool:
        # Complete this function
        # Deletes the value num from the Skiplist and returns true
        # If num does not exist in the Skiplist, do nothing and return false
        count = 0
        result = False
        for i in self.levels:
            hold = i
            prev = None
            while hold != None:
                if hold.val == num:
                    result = True
                    if prev == None:
                        self.levels[count] = hold.next
                        break
                    else:
                        prev.next = hold.next
                        break
                else:
                    prev = hold
                    hold = hold.next
            count += 1
        return result
                    



    
    def toString2(self) -> str:
        output = ""
        if self.next.val != None:
            output += str(self.next.val) + " "
            if self.next.down != None:
                print(self.next.down.val)
                output += str(self.next.down.toString2())
            hold = self.next.next
            while(hold != None):
                if hold.down != None:
                    output += str(hold.down.toString())
                output += str(hold.val) + " "
                hold = hold.next
        return output

    def toString(self) -> str:
        for i in self.levels:
            lvl = ""
            hold = i
            while i != None:
                lvl += str(i.val) + " "
                i = i.next
            print(lvl)
            print()

if __name__ == '__main__':
    sl = LookUpSkipList()
    sl.insert(30) # None
    sl.insert(60) # None
    sl.insert(90) # None
    sl.insert(62) # None
    sl.insert(31)
    sl.insert(29)
    sl.insert(91)
    for i in range(1,20,1):
        sl.insert(i)
    print(sl.toString())
    print(sl.lookup_search(18))
    print(sl.delete(0))
    print(sl.toString())
    #print(sl.lookup_search(30))
    #print(sl.lookup_search(0)) # False
    #sl.insert(4) # None
    #print(sl.lookup_search(1)) # True
    #print(sl.delete(0)) # False
    #print(sl.delete(1)) # True
    #print(sl.lookup_search(1)) # False