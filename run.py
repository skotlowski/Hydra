from hydra import HTest


# TODO: Create example unit test case

class Testing(HTest):
    def __init__(self):
        super().__init__(Testing)

    @staticmethod
    def method_lol() -> str:
        return "method"


test = Testing()

test.assert_true(cond=False, class_name=Testing, method_name=Testing.method_lol)




