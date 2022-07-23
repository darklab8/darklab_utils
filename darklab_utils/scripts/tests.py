import unittest
import subprocess

def capturing_shell(cmd):
    return subprocess.run(cmd, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout

python = "python3.10"

def test_try_envreader():
    output = capturing_shell(f"{python} example.py env_example")
    assert "default_value" in output

def test_try_envreader_with_changing_value():
    output = capturing_shell(f"NOT_EXISTING_VAR=555 {python} example.py env_example")
    assert "555" in output
    
def test_try_clireader():
    output = capturing_shell(f"{python} example.py cli_example")
    assert "example" in output

def test_try_clireader_with_changing_value():
    output = capturing_shell(f"{python} example.py cli_example --cliargument=666")
    assert "666" in output

def test_trying_extra_clivalue():
    output = capturing_shell(f"{python} example.py cli_extra_arg_example")
    assert "456" in output

def test_trying_extra_clivalue():
    output = capturing_shell(f"{python} example.py cli_extra_arg_example --argument=777")
    assert "777" in output