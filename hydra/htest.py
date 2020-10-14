from .logger import create_logger


class HTest:
    def __init__(self, class_name):
        self.logger = create_logger(class_name.__name__)
        
        self.logger.info("Test case initialized")

    def assertTrue(self, cond: bool):
        if not cond:
            print("FAILED")
        else:
            print("PASSED")

    def assertFalse(self, cond: bool):
        pass

    def assertEqual(self, value, expected):
        if value == expected:
            pass
        pass

    def assertNotEqual(self, value, expected):
        pass


