# -*- coding: utf-8 -*-
from ghidra.app.decompiler import DecompileOptions, DecompInterface
from ghidra.util.task import ConsoleTaskMonitor
import os

# Define the directory and file path
output_dir = "C:\\Users\\input_file_path\\Ghidra_Decompilation"
output_file = os.path.join(output_dir, "decompiled_code.c")

# Create the directory if it doesn’t exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Open the file for writing
with open(output_file, "w") as f:
    # Initialize the decompiler interface
    decomp_interface = DecompInterface()
    decomp_interface.openProgram(currentProgram)

    # Loop through each function in the program
    for func in currentProgram.getFunctionManager().getFunctions(True):
        # Decompile the function
        decompiled = decomp_interface.decompileFunction(func, 60, ConsoleTaskMonitor()).getDecompiledFunction()
        
        # Check if the decompilation succeeded
        if decompiled is not None:
            # Write function name and decompiled code to file using .format()
            f.write("/* Function: {} */\n".format(func.getName()))
            f.write(decompiled.getC() + "\n\n")

print("Decompiled code has been saved to {}".format(output_file))
