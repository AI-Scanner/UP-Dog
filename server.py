import os
from updog import Updog

app = Updog(directory='./static', port=8000)

if __name__ == "__main__":
    app.run()
