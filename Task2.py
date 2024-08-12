import time
import threading
from flask import Flask, jsonify
import requests

class BaseAlgorithm:
    """
    Base class for algorithms with common functionality is defined.  # Abstraction: Common interface is defined for subclasses.
    """
    def __init__(self, run_duration=600):
        self.run_duration = run_duration  # Encapsulation: Internal state is managed.
        self.running = False
        self.thread = None
        self.start_time = None

    def run(self):
        """
        Abstract method to be implemented by subclasses is defined.  # Abstraction: Concrete implementation is required from subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def start(self):
        """
        Algorithm is started in a separate thread.  # Encapsulation: Thread management and state handling are performed.
        """
        if not self.running:
            self.thread = threading.Thread(target=self.run)
            self.running = True
            self.start_time = time.time()  # Encapsulation: Start time is tracked.
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
        Algorithm is run and status updates are printed.  # Inheritance: Specific implementation of run method is provided.
        """
        print("TimerAlgorithm started.")
        while self.running and (time.time() - self.start_time) < self.run_duration:
            print("TimerAlgorithm is running...")
            time.sleep(1)  # Simulated work is performed.
        self.running = False
        print("TimerAlgorithm stopped.")


app = Flask(__name__)
algorithm = TimerAlgorithm(run_duration=600)  # Instantiation: Instance of TimerAlgorithm is created.

@app.route('/start_algo', methods=['POST'])
def start_algorithm():
    """
    Algorithm is started via POST request.  # Polymorphism: Start method of BaseAlgorithm is called.
    """
    try:
        response = algorithm.start()  # Polymorphism: Start method is used.
        return jsonify({"message": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def run_flask_app():
    """
    Flask application is run.  # Encapsulation: Flask server execution is managed.
    """
    app.run(debug=True, use_reloader=False)

if __name__ == '__main__':
    # Flask app is started in a new thread.
    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.start()

    # Wait is performed to ensure server is running.
    time.sleep(5)

    # HTTP requests are made using session.
    with requests.Session() as session:
        # Algorithm is started.
        try:
            start_response = session.post("http://127.0.0.1:5000/start_algo")
            print("Start Response:", start_response.json())
        except requests.RequestException as e:
            print(f"Request failed: {e}")
