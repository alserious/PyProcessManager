import os
import sys
from subprocess import run, STDOUT, PIPE
from typing import Callable, List, Optional

import psutil


class PyProcess(psutil.Process):
    """Python process class allows to create processes from separate python modules,
    and monitoring their statistics and logs.
    There is also a functionality of the library psutil.
    """

    def __init__(self, pid: Optional[int] = None) -> None:
        self.py_pid: Optional[int] = None
        self.py_name: Optional[str] = None
        self.py_log_file: Optional[str] = None
        self.py_process: Optional[psutil.Process] = None

        if pid is None:
            super().__init__()
            self.py_pid = super().pid

        else:
            self.py_pid = pid
            super().__init__(pid=self.py_pid)

    def _get_py_module_path(self, py_module: Callable) -> str:
        """Getting the absolute path to a python module.
        Returns:
            str: Absolute path to the file.
        """
        return str(os.path.abspath(py_module.__file__))

    def _get_py_module_dir(self, py_module: Callable) -> str:
        """Getting the absolute path to a python directory.
        Returns:
            str: Absolute path to the directory.
        """
        path: str = self._get_py_module_path(py_module=py_module)
        return str(os.path.dirname(path))

    def _get_cmd_for_start_process(self, path_to_module: str) -> List[str]:
        """Generating a command to start a python process.
        Returns:
            str: Сommand to start python process.
        """
        return [str(sys.executable), "-u", str(path_to_module)]

    def create_process(
        self, py_module: Callable, log_file: Optional[str] = None
    ) -> str:
        """Creating and running a process from a python module.
        Returns:
            str: Process ID.
        """
        module_path: str = self._get_py_module_path(py_module=py_module)
        module_dir: str = self._get_py_module_dir(py_module=py_module)
        print(module_dir)
        cmd: list = self._get_cmd_for_start_process(path_to_module=module_path)

        if log_file:
            self.py_log_file = log_file

        else:
            self.py_log_file = module_path.replace(".py", ".log")

        self.py_process = psutil.Popen(
            cmd,
            stdout=os.open(
                path=self.py_log_file, flags=os.O_CREAT | os.O_WRONLY | os.O_APPEND
            ),
            stderr=STDOUT,
            # cwd=module_dir,
            # env={"PATH": module_dir},
            # env={"PYTHONPATH": "/root/process_manager/process_manager/src/apps/"},
            # cwd="/root",
        )

        self.py_pid = self.py_process.pid
        self.py_name = str(py_module.__name__)

        return f"Process ID: {self.py_pid}"

    def get_process_log(self, lines: int = 10) -> str:
        """Getting the last number lines of log entries N of process.
        Returns:
            str: STDOUT of process python.
        """
        p = run(
            args=["tail", "-n", str(lines), self.py_log_file],
            stdout=PIPE,
            stderr=STDOUT,
        )
        return p.stdout.decode("utf-8")
