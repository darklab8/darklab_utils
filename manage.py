import os
import darklab_utils as utils

python_path = "/usr/bin/python3.10"
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
    def build(self):
        README_template = """
# Library of darklab utility programms

contains:

## Scripts:

A package built on top of argparse.
intended usage to be a python version of makefile, for uniform command acceess to run tests/lints in dev env and CI

## code example:

```py
{code}
```

## Link to Pypi
https://pypi.org/project/darklab-utils/
""" 
        with open("example.py", "r") as code_example_file:
            code_example = code_example_file.read()
        with open("README.md", "w") as readme_file:
            readme_file.write(README_template.format(code=code_example))

        os.system("rm -R dist")
        os.system("rm -R darklab_utils.egg-info")
        self.shell(f"{python_path} -m build")

    @utils.registered_action
    def deploy(self):
        self.shell(f"{python_path} -m twine upload dist/*")


if __name__=="__main__":
    MyScripts().process()