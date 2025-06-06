"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Guru Shreyas Potta and Ray Arcand, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: gp23568
UT EID 2: ra42693
"""


class Node:
    """
    A modified version of the Node class for linked lists (using proper class
    coding practices). Instead of a data instance variable, this node class has both
    a coefficient and an exponent instance variable, which is used to represent each
    term in a polynomial.
    """

    def __init__(self, coeff, exp, link=None):
        """
        Node Constructor for polynomial linked lists.

        Args:
        - coeff: The coefficient of the term.
        - exp: The exponent of the term.
        - link: The next node in the linked list.
        """
        self.coeff = coeff
        self.exp = exp
        self.next = link

    @property
    def coeff(self):
        """
        Getter method for the coefficient attribute.
        """
        return self.__coeff

    @coeff.setter
    def coeff(self, value):
        """
        Setter method for the coefficient attribute.
        """
        if value is None or isinstance(value, int):
            self.__coeff = value
        else:
            raise ValueError("Coefficient must be an integer or None.")

    @property
    def exp(self):
        """
        Getter method for the exponent attribute.
        """
        return self.__exp

    @exp.setter
    def exp(self, value):
        """
        Setter method for the exponent attribute.
        """
        if value is None or isinstance(value, int):
            self.__exp = value
        else:
            raise ValueError("Exponent must be an integer or None.")

    @property
    def next(self):
        """
        Getter method for the next attribute.
        """
        return self.__next

    @next.setter
    def next(self, value):
        """
        Setter method for the next attribute.
        """
        if value is None or isinstance(value, Node):
            self.__next = value
        else:
            raise ValueError("Next must be a Node instance or None.")

    def __str__(self):
        """
        String representation of each term in a polynomial linked list.
        """
        return f"({self.coeff}, {self.exp})"


class LinkedList:
    '''DataStructure'''
    def __init__(self):
        # You are also welcome to use a sentinel/dummy node!
        # It is definitely recommended, which will we learn more
        # about in class on Monday 3/24. If you choose to use
        # a dummy node, comment out the self.head = None
        # and comment in the below line. We use None to make sure
        # if there is an error where you accidentally include the
        # dummy node in your calculation, it will throw an error.
        # self.dummy = Node(None, None)
        self.head = None
        self.size = 0

    # Insert the term with the coefficient coeff and exponent exp into the polynomial.
    # If a term with that exponent already exists, add the coefficients together.
    # You must keep the terms in descending order by exponent.
    def insert_term(self, coeff, exp):
        '''Adding terms'''
        # print("adding: ", coeff, " and ", exp)
        if coeff == 0:
            return

        if self.head is None:
            self.head = Node(coeff, exp)
            # print("first term:", self.head)
            self.size += 1
            return

        if exp > self.head.exp:
            temp_node = Node(coeff, exp)
            temp_node.next = self.head
            self.head = temp_node
            # print("higher exp", self.head, "and next is: ", self.head.next)
            self.size += 1
            return

        temp = self.head
        while temp:
            if temp.exp == exp:
                temp.coeff += coeff
                return
            temp = temp.next

        temp = self.head
        previous = None
        while temp and exp < temp.exp:
            temp = temp.next
            if previous is None:
                previous = self.head
            else:
                previous = previous.next
        temp_node = Node(coeff, exp, previous.next)
        previous.next = temp_node
        self.size += 1
        return

    # Add a polynomial p to the polynomial and return the resulting polynomial as a new linked list.
    def add(self, p):
        '''adding polynomials'''
        temp = self.head
        other = p.head

        result = LinkedList()
        while temp:
            result.insert_term(temp.coeff, temp.exp)
            temp = temp.next
        while other:
            result.insert_term(other.coeff, other.exp)
            other = other.next

        iterator = result.head
        if result.size == 1 and iterator.coeff == 0:
            result.head = None
            result.size = 0
            return result

        result2 = LinkedList()
        while iterator:
            if iterator.coeff != 0:
                result2.insert_term(iterator.coeff, iterator.exp)
            iterator = iterator.next
        return result2

    # Multiply a polynomial p with the polynomial and return the product as a new linked list.
    def mult(self, p):
        '''Multiplication method'''
        result = LinkedList()
        temp = self.head
        other = p.head
        while temp:
            other = p.head
            while other:
                result.insert_term(temp.coeff * other.coeff, temp.exp + other.exp)
                other = other.next
            temp = temp.next

        iterator = result.head
        if result.size == 1 and iterator.coeff == 0:
            result.head = None
            result.size = 0
            return result

        result2 = LinkedList()
        while iterator:
            if iterator.coeff != 0:
                result2.insert_term(iterator.coeff, iterator.exp)
            iterator = iterator.next
        return result2

    # Return a string representation of the polynomial.
    def __str__(self):
        '''To string'''
        if self.size == 0:
            return ""
        string_output = ""
        temp = self.head
        size = 0
        while temp:
            size += 1
            temp = temp.next

        temp = self.head
        for _ in range(size - 1):
            string_output = string_output + str(temp) + " + "
            temp = temp.next
        string_output = string_output + str(temp)
        return string_output

def main():
    '''Main Functions'''
    # read data from stdin (terminal/file) using input() and create polynomial p
    p = LinkedList()
    iterate = int(input())
    for _ in range(iterate):
        temp = input().split(" ")
        coeff = int(temp[0])
        exp = int(temp[1])
        # print(coeff, exp)
        p.insert_term(coeff, exp)

    # print("hi", p)
    input()
    # read data from stdin (terminal/file) using input() and create polynomial q
    q = LinkedList()
    iterate = int(input())
    for _ in range(iterate):
        temp = input().split(" ")
        coeff = int(temp[0])
        exp = int(temp[1])
        # print(coeff, exp)
        q.insert_term(coeff, exp)
    # get sum of p and q as a new linked list and print sum
    print(q.add(p))
    # print(q)
    # get product of p and q as a new linked list and print product
    print(q.mult(p))
    # print(q)


if __name__ == "__main__":
    main()
