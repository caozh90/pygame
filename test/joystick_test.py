import unittest
from pygame.tests.test_utils import question, prompt

import pygame

pygame.joystick.init()
# The number of joysticks available for testing.
JOYSTICK_COUNT = pygame.joystick.get_count()
pygame.joystick.quit()

class JoystickTypeTest(unittest.TestCase):
    def todo_test_Joystick(self):

        # __doc__ (as of 2008-08-02) for pygame.joystick.Joystick:

        # pygame.joystick.Joystick(id): return Joystick
        # create a new Joystick object
        #
        # Create a new joystick to access a physical device. The id argument
        # must be a value from 0 to pygame.joystick.get_count()-1.
        #
        # To access most of the Joystick methods, you'll need to init() the
        # Joystick. This is separate from making sure the joystick module is
        # initialized. When multiple Joysticks objects are created for the
        # same physical joystick device (i.e., they have the same ID number),
        # the state and values for those Joystick objects will be shared.
        #
        # The Joystick object allows you to get information about the types of
        # controls on a joystick device. Once the device is initialized the
        # Pygame event queue will start receiving events about its input.
        #
        # You can call the Joystick.get_name() and Joystick.get_id() functions
        # without initializing the Joystick object.
        #

        self.fail()


class JoystickModuleTest(unittest.TestCase):
    @unittest.skipIf(0 == JOYSTICK_COUNT, "No joysticks detected")
    def test_get_count(self):
        # Test get_count correctly identifies number of connected joysticks
        prompt("Please add or remove joysticks as necessary before the test.")

        pygame.joystick.init()
        # pygame.joystick.get_count(): return count
        # number of joysticks on the system, 0 means no joysticks connected
        JOYSTICK_COUNT = pygame.joystick.get_count()

        self.assertGreaterEqual(JOYSTICK_COUNT, 0, ("joystick.get_count() must "
                                            "return a value >= 0"))

        response = question(
            ("NOTE: Having Steam open may add an extra virtual joystick for "
             "each joystick physically plugged in.\n"
             "Is the correct number of joysticks connected to this system [{}]?"
             .format(JOYSTICK_COUNT))
        )

        self.assertTrue(response)

        # When you create Joystick objects using Joystick(id), you pass an
        # integer that must be lower than this count.
        # Test Joystick(id) for each connected joystick
        for x in range(0,JOYSTICK_COUNT):
            pygame.joystick.Joystick(x)
        with self.assertRaises(pygame.error):
            pygame.joystick.Joystick(JOYSTICK_COUNT)

        pygame.joystick.quit()


    def test_get_init(self):
        # Check that get_init() matches what is actually happening
        def error_check_get_init():
            try:
                pygame.joystick.get_count()
            except pygame.error:
                return False
            return True

        # Start uninitialised
        self.assertEqual(pygame.joystick.get_init(), False)

        pygame.joystick.init()
        self.assertEqual(pygame.joystick.get_init(), error_check_get_init()) # True
        pygame.joystick.quit()
        self.assertEqual(pygame.joystick.get_init(), error_check_get_init()) # False

        pygame.joystick.init()
        pygame.joystick.init()
        self.assertEqual(pygame.joystick.get_init(), error_check_get_init()) # True
        pygame.joystick.quit()
        self.assertEqual(pygame.joystick.get_init(), error_check_get_init()) # False

        pygame.joystick.quit()
        self.assertEqual(pygame.joystick.get_init(), error_check_get_init())  # False

        for i in range(100):
            pygame.joystick.init()
        self.assertEqual(pygame.joystick.get_init(), error_check_get_init()) # True
        pygame.joystick.quit()
        self.assertEqual(pygame.joystick.get_init(), error_check_get_init()) # False

        for i in range(100):
            pygame.joystick.quit()
        self.assertEqual(pygame.joystick.get_init(), error_check_get_init()) # False



    def test_init(self):
        """
        This unit test is for joystick.init()
        It was written to help reduce maintenance costs
        and to help test against changes to the code or
        different platforms.
        """
        pygame.quit()
        #test that pygame.init automatically calls joystick.init
        pygame.init()
        self.assertEqual(pygame.joystick.get_init(), True)

        #test that get_count doesn't work w/o joystick init
        #this is done before and after an init to test
        #that init activates the joystick functions
        pygame.joystick.quit()
        with self.assertRaises(pygame.error):
            pygame.joystick.get_count()

        #test explicit call(s) to joystick.init.
        #Also test that get_count works once init is called
        iterations = 20
        for i in range(iterations):
            pygame.joystick.init()
        self.assertEqual(pygame.joystick.get_init(), True)
        self.assertIsNotNone(pygame.joystick.get_count())

    def test_quit(self):
        """Test if joystick.quit works."""

        pygame.joystick.init()

        self.assertIsNotNone(pygame.joystick.get_count()) #Is not None before quit

        pygame.joystick.quit()

        with self.assertRaises(pygame.error):  #Raises error if quit worked
            pygame.joystick.get_count()


################################################################################

if __name__ == "__main__":
    unittest.main()
