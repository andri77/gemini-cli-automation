# Playwright MPC Tests

This project contains Playwright tests for the NAPLAN public demonstration site.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gemini-cli-automation/playwright-mpc-tests.git
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the tests

To run the tests, use the following command:

```bash
pytest
```

To run the tests in headed mode, use the following command:

```bash
pytest --headed
```
