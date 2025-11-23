import os
import sys

# Keep working directory setup (important)
root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root)
os.chdir(root)

# -------------------------
#  PRIVATE MODE (NO UPDATES)
# -------------------------
print("Running private Fooocus... (auto-updates disabled)")
print("This version will NOT contact GitHub for updates.")
print("All code is loaded locally from your repository only.")

# -------------------------
#  DO NOT REMOVE THIS
#  (Starts Fooocus normally)
# -------------------------
from launch import *

