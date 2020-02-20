'''
Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double
booking.

Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval
[start, end), the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to
both events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without
causing a double booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
'''


class MyCalendar:

    def __init__(self):
        k = 0

    def book(self, start, end):
        a = 1
#https://leetcode.com/problems/my-calendar-i/discuss/509703/Python-3-solutions-Brute-force-binary-search-bisect


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
nums1 = [1,6,1]
function = MyCalendar()
function.book(3, 3)
