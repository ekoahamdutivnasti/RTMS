from rtms.ai_system import VrindaAI
from rtms.validation import ResponseValidator
from rtms.simulation import SimulationRedirect
from rtms.security import SecurePasswordGenerator
from rtms.logging_config import setup_logging

def main():
    setup_logging()
    rtms = RealTimeMonitoringSystem()
    rtms.monitor_response("What is 2 + 2?")
    rtms.monitor_response("What is the capital of Germany?")

if __name__ == "__main__":
    main()
