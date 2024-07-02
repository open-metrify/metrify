"""
metrify/metrify.py

Entry point script for the Flask application
"""

from metrify import create_app


if __name__ == "__main__":
    app = create_app()
