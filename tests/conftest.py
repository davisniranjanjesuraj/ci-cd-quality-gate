import pytest
import threading
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from app.app import create_app

@pytest.fixture(scope="session", autouse=True)
def flask_server():
    app = create_app()

    server = threading.Thread(
        target=app.run,
        kwargs={
            "host": "0.0.0.0",
            "port": 5000,
            "use_reloader": False
        }
    )
    server.daemon = True
    server.start()

    # Wait until app is ready
    for _ in range(10):
        try:
            r = requests.get("http://localhost:5000/health")
            if r.status_code == 200:
                break
        except:
            time.sleep(1)
    else:
        raise RuntimeError("Flask app failed to start")

@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
