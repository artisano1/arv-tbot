import sys
import os

# Add your project directory to Python path
project_dir = '/home/toparvea/arv-tbot'
if project_dir not in sys.path:
    sys.path.append(project_dir)

from app import app as application
