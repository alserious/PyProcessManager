from pyProcessManager import PyProcess

from apps import first, second


p_1 = PyProcess()
p_2 = PyProcess()
result_1 = p_1.create_process(py_module=first)
result_2 = p_2.create_process(py_module=second)

print(result_1)
print(result_2)

print(p_1.py_pid)
print(p_1.py_name)
print(p_2.py_pid)
print(p_2.py_name)

import time

# time.sleep(2)

print(p_1.environ())

# log_1 = p_1.get_process_log()
# log_2 = p_2.get_process_log()

# print(log_1)
# print(log_2)
