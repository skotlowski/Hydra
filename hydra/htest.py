from .logger import create_logger


class HTest:
    def __init__(self, class_name):
        self.logger = create_logger(class_name.__name__)
        self.logger.info("Test case initialized")

    def assert_true(self, cond: bool, class_name, method_name):
        class_name = class_name.__name__
        method_name = method_name.__name__
        if not cond:
            self.print_result(cond, class_name, method_name)
        else:
            print("PASSED")

    def assert_false(self, cond: bool):
        pass

    def assert_equal(self, value, expected):
        if value == expected:
            pass
        pass

    def assert_not_equal(self, value, expected):
        pass

    @staticmethod
    def print_result(cond, *conditions) -> None:
        result_list = ["<" + str(item) + "> " for item in conditions]
        if cond:
            print("PASSED: ", ''.join(result_list))
        else:
            print("FAILED: ", ''.join(result_list))
