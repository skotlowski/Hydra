from hydra import HTest


# TODO: Create example unit test case

class Testing(HTest):
    def __init__(self):
        super().__init__(Testing)


test = Testing()
test.assertTrue(cond=False)



