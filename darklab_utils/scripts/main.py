from types import SimpleNamespace
import abc
from darklab_utils.argparsereader import ArgparseReader
from darklab_utils.envreader import EnvReader
from darklab_utils.shellmixin import ShellMixin


class AbstractInputDataFactory(abc.ABC):
    def __init__(self, registered_actions: list):
        self._argpase_reader = ArgparseReader() \
            .add_argument(
                'action',
                type=str,
                help='positional argument to choose action',
                choices=registered_actions
            )
        self._env_reader = EnvReader()

    @abc.abstractstaticmethod
    def register_cli_arguments(cli_reader: ArgparseReader) -> ArgparseReader:
        pass

    @abc.abstractstaticmethod
    def register_env_arguments(env_reader: EnvReader) -> EnvReader:
        pass

    def _get_cli_vars(self) -> SimpleNamespace:
        args = self.register_cli_arguments(self._argpase_reader) \
            .get_data(ignore_others=True)
        data: dict = args.get_as_dict()
        return SimpleNamespace(**data)

    def _get_env_vars(self) -> SimpleNamespace:
        return self.register_env_arguments(self._env_reader).get_storage()

    def get_input_data(self) -> 'SimpleNamespace':
        
        env_vars = self._get_env_vars()
        cli_vars = self._get_cli_vars()
        instance = SimpleNamespace(
            **env_vars.__dict__,
            **cli_vars.__dict__,
            cli_reader = self._argpase_reader,
        )
        return instance


def registered_action(f):
    def wrapper(*args):
        return f(*args)
    return wrapper


class NullDataFactory(AbstractInputDataFactory):

    @staticmethod
    def register_cli_arguments(argpase_reader: ArgparseReader) -> ArgparseReader:
        return argpase_reader

    @staticmethod
    def register_env_arguments(env_reader: EnvReader) -> EnvReader:
        return env_reader

class AbstractScripts(ShellMixin):
    input_data_factory = NullDataFactory

    globals = SimpleNamespace()
    
    def __init__(
        self,
    ):
        self.registered_actions: list = [
            key for key, value in self.__class__.__dict__.items()
            if callable(value) and "registered_action" in value.__qualname__
        ]

    def process(self):
        input_data_factory: AbstractInputDataFactory = self.input_data_factory
        input_: SimpleNamespace = input_data_factory(
            registered_actions=self.registered_actions
        ).get_input_data()
        self.globals = input_
        getattr(self, input_.action)()




