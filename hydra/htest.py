from .logger import create_logger


class HTest:
    def __init__(self):
        self.logger = create_logger(__name__)
        
        self.logger.info("Test case initialized")

    def assertTrue(self, cond: bool):
        if not cond:
            print("FAILED")

    def assertFalse(self, cond: bool):
        pass

    def assertEqual(self, value, expected):
        pass

    def assertNotEqual(self, value, expected):
        pass


