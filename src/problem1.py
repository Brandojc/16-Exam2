"""
Exam 2, problem 1.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and James Brandon.  April 2018.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem1()


###############################################################################
# Done: 2.  READ the code of the  Rect  class below.
#
#   Once you are confident that you understand the  Rect  class and its code,
#   change the TO-DO for this problem to DONE.
#
#   If you do NOT understand the  Rect  class and its code,
#   talk to your instructor to see how to proceed.
###############################################################################
class Rect(object):
    def __init__(self, width, height):
        self.w = width
        self.h = height


def run_test_problem1():
    """ Tests the   problem1   function. """
    # -------------------------------------------------------------------------
    # Done: 3. Implement at least 2 tests of the  problem1  function.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1   function:')
    print('--------------------------------------------------')

    print('Test 1:')

    expected = 762
    actual = problem1([Rect(5, 10), Rect(4, 3), Rect(100, 7)])

    print()
    print('Expected =', expected)
    print('Actual =', actual)
    if actual == expected:
        print('True')
    print()

    print('Test 2:')

    expected = 140
    actual = problem1([Rect(10, 10), Rect(5, 5), Rect(3, 3), Rect(2, 3)])

    print()
    print('Expected =', expected)
    print('Actual =', actual)
    if actual == expected:
        print('True')
    print()


def problem1(rectangles):
    """
    What comes in:  A sequence of  Rect  objects.
    What goes out:  Returns the sum of the areas of the given  Rect  objects.
    Side effects:   None.
    Example:
      problem1([Rect(5, 10),
                Rect(4, 3),
                Rect(100, 7)]
         returns 50 + 12 + 700, which is 762

    Type hints:
    :param rectangles: [Rect]
    :return: int
    """
    # -------------------------------------------------------------------------
    # Done: 4. Implement and test this function.
    # -------------------------------------------------------------------------

    total_area = 0
    for k in range(len(rectangles)):
        total_area = total_area + (rectangles[k].w * rectangles[k].h)
    return total_area

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()