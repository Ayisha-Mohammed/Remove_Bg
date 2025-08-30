#### 1\. Run the FastAPI backend



Inside your bg\_remover folder, you already have src/api.py. That’s your FastAPI entrypoint.



Open a terminal inside your project folder and run:



**uvicorn src.api:app --reload --host 127.0.0.1 --port 8000**

* src.api:app → means inside src/api.py, the variable app = FastAPI().

* --reload → auto-restarts server when you edit code.

* Server will run at 👉 http://127.0.0.1:8000



Test it in browser:

http://127.0.0.1:8000/docs

(You should see FastAPI’s Swagger UI)



#### 2\. Setup your Chrome extension



You’ll have something like this in extension/:



manifest.json



popup.html



popup.js



icon.png (the one we just made 🎨)



Make sure your extension code is sending requests to your backend API (http://127.0.0.1:8000/remove-bg).



#### 3\. Load the extension in Chrome



Open Chrome → Extensions → Manage Extensions



Enable Developer Mode (top right).



Click Load unpacked.



Select your extension/ folder.



You’ll see your icon appear in the browser.

#### 

#### 4\. Workflow



Backend:

Run with uvicorn → always keep it running.



Extension:

Click the icon → upload an image → request goes to backend → backend processes with U²-Net → sends back image with background removed.



