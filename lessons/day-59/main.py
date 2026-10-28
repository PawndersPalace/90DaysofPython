import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logging.info("Program started")
items = ["book", "pen"]
logging.info("Loaded %d items", len(items))
