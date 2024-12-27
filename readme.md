# Setup Instructions

## 1. Set up Environment Variables

Ensure that all necessary environment variables are set up properly before running the application. These include configurations for your proxy, Chrome profile, and any other required settings.

## 2. Proxy Authentication and Chrome Setup

The script uses Google Chrome with a **default profile** to scrape data from Twitter. During the browser startup, **proxy authentication** is handled automatically.

## 3. Use Another Browser for Frontend Interaction

While Chrome is used for backend data extraction (Twitter scraping), you should use **any other browser** (such as Firefox, Edge, etc.) for interacting with the frontend of the application. This ensures that the data extraction process runs smoothly without interference.

## To Run It, Follow These Steps after cloning the repo:

1. You can either use a **virtual environment** (`venv`) or not, based on your preference.

2. Install all the required dependencies by running:

   ```bash
   pip install -r requirements.txt

3. To start the server, run:

    ```bash
    python run.py

The frontend will start and be available at `http://127.0.0.1:5000`.

## Frontend Interaction

**MAKE SURE TO OPEN THE FRONTEND IN A BROWSER OTHER THAN CHROME**.

After clicking the button, the UI will display a message: **Loading....**. Please be patient during this time.
If any process fails, an error will be displayed clearly.
