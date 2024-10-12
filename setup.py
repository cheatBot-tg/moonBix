import os
import subprocess

# Проверка на наличие папки venv
if not os.path.isdir("venv"):
    print("Creating virtual environment...")
    subprocess.run(["python3", "-m", "venv", "venv"])

print("Activating virtual environment...")
subprocess.run(["source", "venv/bin/activate"], shell=True)

# Проверка на наличие установленного флага в виртуальном окружении
if not os.path.isfile("venv/lib/python3.12/site-packages/installed"):  # Update the Python version if different
    if os.path.isfile("requirements.txt"):
        print("Installing wheel for faster installation...")
        subprocess.run(["pip", "install", "wheel"])
        print("Installing dependencies...")
        subprocess.run(["pip", "install", "-r", "requirements.txt"])
        # Mark dependencies as installed
        with open("venv/lib/python3.12/site-packages/installed", "w") as f:  # Update the Python version if different
            f.write('')
    else:
        print("requirements.txt not found, skipping dependency installation.")
else:
    print("Dependencies already installed, skipping installation.")

if not os.path.isfile(".env"):
    print("Copying configuration file...")
    subprocess.run(["cp", ".env-example", ".env"])
else:
    print("Skipping .env copying.")

print("Starting the bot...")
subprocess.run(["python3", "main.py"])

print("done")
print("PLEASE EDIT .ENV FILE")
