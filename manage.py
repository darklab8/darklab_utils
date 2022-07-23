from types import SimpleNamespace

import darklab_utils as utils

class InputDataFactory(utils.AbstractInputDataFactory):

    @staticmethod
    def register_cli_arguments(argpase_reader: utils.ArgparseReader) -> utils.ArgparseReader:
        return argpase_reader

    @staticmethod
    def register_env_arguments(env_reader: utils.EnvReader) -> utils.EnvReader:
        return env_reader

class MyScripts(utils.AbstractScripts):
    input_data_factory = InputDataFactory

    @utils.registered_action
    def build(self, input_: SimpleNamespace):
        self.shell(f"echo {input_.cli_argument}")

if __name__=="__main__":
    MyScripts().process()