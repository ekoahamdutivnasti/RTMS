import logging

def setup_logging():
    logging.basicConfig(
        filename='logs/rtms.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
