import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from application import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
