def test_login_ui(driver):
    driver.get("http://localhost:5000")

    driver.execute_script("""
        fetch('/login', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({username: 'admin', password: 'admin123'})
        }).then(res => res.json()).then(data => {
            document.body.innerHTML = data.message;
        });
    """)

    assert "Login successful" in driver.page_source
