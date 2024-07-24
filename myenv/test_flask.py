try:
    from flask import Flask
    print("Flask imported successfully")
except ImportError:
    print("Failed to import Flask")
