# Wal IN dIR
import os

for root, dir, files in os.walk("D:\Automation_via_Python\PythonProject_Automation"):
    print(f"Current Dir {root}")
    print(f"Sub Dir Dir {dir}")
    print(f"files Dir Dir {files}")
    print(len(files))