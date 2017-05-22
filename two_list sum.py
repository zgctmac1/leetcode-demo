class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution(object):
    def AddTwoList(self,l1,l2):
        cur=ListNode(0)
        ret=cur
        sum=0
        while True:
            if l1!=None:
                sum=sum+l1.val
                l1=l1.next
            if l2!=None:
                sum=sum+l2.val
                l2=l2.next
            cur.val=sum%10
            print cur.val
            sum=sum/10
            if l1!=None or l2!=None or sum!=0:
                cur.next=ListNode(0)
                cur=cur.next
            else:
                break
            return cur.val
s1=ListNode(3)
s11=ListNode(5)
s1.next=s11
s2=ListNode(5)
s21=ListNode(6)
s2.next=s21
h=Solution()
print h.AddTwoList(s1,s2)