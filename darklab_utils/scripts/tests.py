import unittest
import subprocess

def capturing_shell(cmd):
    return subprocess.run(cmd, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

python = "python3.10"

def test_try_envreader():
    output = capturing_shell(f"{python} example.py env_example")
    assert "default_value" in output.stdout

def test_try_envreader_with_changing_value():
    output = capturing_shell(f"NOT_EXISTING_VAR=555 {python} example.py env_example")
    assert "debug_555" in output.stdout
    
def test_try_clireader():
    output = capturing_shell(f"{python} example.py cli_example")
    assert "debug_example" in output.stdout

def test_try_clireader_with_changing_value():
    output = capturing_shell(f"{python} example.py cli_example --cli_argument=666")
    assert "debug_666" in output.stdout

def test_trying_extra_clivalue():
    output = capturing_shell(f"{python} example.py cli_extra_arg_example")
    print(output)
    print(output)
    assert "debug_456" in output.stdout

def test_trying_extra_clivalue_with_changing_value():
    output = capturing_shell(f"{python} example.py cli_extra_arg_example --argument=777")
    print(output)
    print(output)
    assert "debug_777" in output.stdout
