import time
import threading
from flask import Flask, jsonify, request, render_template_string
import logging

# Basic logging setup is performed.
logging.basicConfig(level=logging.DEBUG)


class BaseAlgorithm:
    """
    Base class for algorithms with common functionality is defined.  # Abstraction: Common interface is provided for subclasses.
    """

    def __init__(self, run_duration=600):
        """
        Initialization of the algorithm parameters is performed.  # Encapsulation: Internal state is managed.
        """
        self.run_duration = run_duration
        self.running = False
        self.thread = None
        self.start_time = None

    def run(self):
        """
        Abstract method for running the algorithm is defined.  # Abstraction: Concrete implementation is required from subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def start(self):
        """
        Algorithm is started in a separate thread if it is not already running.  # Encapsulation: Thread management and state handling are performed.
        """
        if not self.running:
            self.thread = threading.Thread(target=self.run)
            self.running = True
            self.start_time = time.time()
            self.thread.start()
            return "Algorithm started."
        else:
            return "Algorithm is already running."


class TimerAlgorithm(BaseAlgorithm):
    """
    Concrete algorithm that runs for a specified duration is defined.  # Inheritance: Specific implementation is provided by extending BaseAlgorithm.
    """

    def run(self):
        """
        Execution of the algorithm and status updates are performed.  # Inheritance: Specific implementation of run method is provided.
        """
        logging.info("TimerAlgorithm started.")
        while self.running and (time.time() - self.start_time) < self.run_duration:
            logging.info("TimerAlgorithm is running...")
            time.sleep(1)
        self.running = False
        logging.info("TimerAlgorithm stopped.")


app = Flask(__name__)
algorithm = TimerAlgorithm(run_duration=600)  # Instantiation: Instance of TimerAlgorithm is created.


@app.route('/')
def welcome():
    """
    A welcome page with instructions on how to trigger the algorithm is rendered.  # Presentation: User interface is provided.
    """
    return render_template_string('''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Welcome</title>
    </head>
    <body>
        <h1>Welcome to the Algorithm Server</h1>
        <p>To start the algorithm, use one of the following methods:</p>
        <ul>
            <li><b>Using Postman:</b> Send a <code>POST</code> request to <code>http://127.0.0.1:5000/start_algo</code></li>
            <li><b>Using curl:</b> Run the command <code>curl -X POST http://127.0.0.1:5000/start_algo</code></li>
        </ul>
        <p><b>Note:</b> The algorithm will start running when the <code>POST</code> request is received.</p>
    </body>
    </html>
    ''')


@app.route('/start_algo', methods=['POST'])
def start_algorithm():
    """
    The algorithm is started via a POST request.  # Polymorphism: Start method of BaseAlgorithm is called.
    """
    logging.debug(f"Request method: {request.method}")
    logging.debug(f"Request URL: {request.url}")
    logging.debug(f"Request headers: {request.headers}")
    logging.debug(f"Request data: {request.data}")

    if request.method != 'POST':
        return jsonify({"error": "Method not allowed"}), 405

    try:
        response = algorithm.start()  # Polymorphism: Start method is used.
        return jsonify({"message": response})
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500


def run_flask_app():
    """
    The Flask application is run.  # Encapsulation: Flask server execution is managed.
    """
    app.run(debug=True, use_reloader=False)


if __name__ == '__main__':
    # The Flask server is started in a new thread.
    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.start()
