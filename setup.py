import os
import shutil
import subprocess

# Check if dependencies are installed
if not os.path.exists('venv/Lib/site-packages/installed'):
    if os.path.exists('requirements.txt'):
        print("Installing wheel for faster installing...")
        subprocess.run(['pip', 'install', 'wheel'])  # Install wheel

        print("Installing dependencies...")
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'])  # Install dependencies

        # Create an 'installed' marker file
        with open('venv/Lib/site-packages/installed', 'w') as f:
            pass
    else:
        print("requirements.txt not found, skipping dependency installation.")
else:
    print("Dependencies already installed, skipping installation.")

# Check if .env file exists and copy from .env-example if not
if not os.path.exists('.env'):
    print("Copying configuration file...")
    shutil.copy('.env-example', '.env')
else:
    print("Skipping .env copying.")

# Start the bot
print("Starting the bot...")
subprocess.run(['python', 'main.py'])  # Execute main.py

print("done")
print("PLEASE EDIT .ENV FILE")
