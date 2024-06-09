import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext
import requests
from threading import Thread
import asyncio
import websockets
import json
import time

# Global variable to store the token
token = None

# Function to fetch board messages
def fetch_board_messages():
    try:
        headers = {'Authorization': f'Token {token}'}
        response = requests.get('http://127.0.0.1:8000/api/board/', headers=headers)
        response.raise_for_status()
        messages = response.json()
        return messages
    except requests.exceptions.RequestException as e:
        print(f"Error fetching board messages: {e}")
        return []

# Function to fetch direct messages
def fetch_direct_messages():
    try:
        headers = {'Authorization': f'Token {token}'}
        response = requests.get('http://127.0.0.1:8000/api/direct/', headers=headers)
        response.raise_for_status()
        messages = response.json()
        return messages
    except requests.exceptions.RequestException as e:
        print(f"Error fetching direct messages: {e}")
        return []

# Function to update board messages in the GUI
def update_board_messages():
    while True:
        messages = fetch_board_messages()
        board_messages_text.config(state=tk.NORMAL)
        board_messages_text.delete(1.0, tk.END)
        for message in messages[-10:]:  # Show only the latest 10 messages
            try:
                board_messages_text.insert(tk.END, f"{message['user']}: {message['message']}\n")
            except (TypeError, KeyError) as e:
                print(f"Error processing message data: {message}, error: {e}")
        board_messages_text.config(state=tk.DISABLED)
        time.sleep(10)

# Function to update direct messages in the GUI
def update_direct_messages():
    while True:
        messages = fetch_direct_messages()
        direct_messages_text.config(state=tk.NORMAL)
        direct_messages_text.delete(1.0, tk.END)
        for message in messages:
            try:
                direct_messages_text.insert(tk.END, f"{message['sender']}: {message['message']}\n")
            except (TypeError, KeyError) as e:
                print(f"Error processing direct message data: {message}, error: {e}")
        direct_messages_text.config(state=tk.DISABLED)
        time.sleep(10)

# WebSocket function to get active users
async def get_active_users():
    uri = "ws://127.0.0.1:8000/ws/activity/"
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({'token': token}))

        while True:
            message = await websocket.recv()
            data = json.loads(message)
            if data.get('type') == 'user_join':
                print(f"User joined: {data['user']}")
                update_active_users(data['user'], 'join')
            elif data.get('type') == 'user_leave':
                print(f"User left: {data['user']}")
                update_active_users(data['user'], 'leave')
            else:
                print(f"Message: {data}")

# Function to update active users in the GUI
def update_active_users(user, action):
    active_users_text.config(state=tk.NORMAL)
    users = active_users_text.get(1.0, tk.END).splitlines()
    
    if action == 'join':
        if user not in users:
            active_users_text.insert(tk.END, f"{user}\n")
    elif action == 'leave':
        if user in users:
            users.remove(user)
            active_users_text.delete(1.0, tk.END)
            for user in users:
                active_users_text.insert(tk.END, f"{user}\n")
    
    active_users_text.config(state=tk.DISABLED)

# Function to show login popup and get the token
def login():
    global token
    username = simpledialog.askstring("Login", "Enter your username")
    password = simpledialog.askstring("Login", "Enter your password", show='*')

    if username and password:
        try:
            response = requests.post('http://127.0.0.1:8000/auth/', data={'username': username, 'password': password})
            response.raise_for_status()
            token = response.json().get('token')

            if not token:
                raise ValueError("No token returned")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Login Failed", f"Error: {e}")
            login()  # Retry login
        except ValueError as e:
            messagebox.showerror("Login Failed", str(e))
            login()  # Retry login
    else:
        messagebox.showerror("Login Failed", "Username and password cannot be empty")
        login()  # Retry login

# Function to start the WebSocket client
def start_websocket_client():
    asyncio.new_event_loop().run_until_complete(get_active_users())

# Initialize Tkinter window
root = tk.Tk()
root.title("Social Network App")

# Show login popup before running the main loop
login()

# Active Users Frame
active_users_frame = tk.Frame(root)
active_users_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
active_users_label = tk.Label(active_users_frame, text="Active Users")
active_users_label.pack()
active_users_text = scrolledtext.ScrolledText(active_users_frame, state=tk.DISABLED)
active_users_text.pack(fill=tk.BOTH, expand=True)

# Board Messages Frame
board_messages_frame = tk.Frame(root)
board_messages_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
board_messages_label = tk.Label(board_messages_frame, text="Board Messages")
board_messages_label.pack()
board_messages_text = scrolledtext.ScrolledText(board_messages_frame, state=tk.DISABLED)
board_messages_text.pack(fill=tk.BOTH, expand=True)

# Direct Messages Frame
direct_messages_frame = tk.Frame(root)
direct_messages_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
direct_messages_label = tk.Label(direct_messages_frame, text="Direct Messages")
direct_messages_label.pack()
direct_messages_text = scrolledtext.ScrolledText(direct_messages_frame, state=tk.DISABLED)
direct_messages_text.pack(fill=tk.BOTH, expand=True)

# Start threads to update the GUI with live data
Thread(target=update_board_messages, daemon=True).start()
Thread(target=update_direct_messages, daemon=True).start()

# Start the WebSocket client in a new thread
Thread(target=start_websocket_client, daemon=True).start()

# Run the Tkinter main loop
root.mainloop()
