from pyngrok import ngrok

# Set your ngrok auth token here (get from https://dashboard.ngrok.com/get-started/your-authtoken)
ngrok.set_auth_token("37ALONobJpHV6LCKlFHcj4dzUAw_5bQdC6e7NJ87ddULbMy9Y")  # Replace with your token

# Start ngrok tunnel to port 8080
public_url = ngrok.connect(8080)
print(f"Public URL: {public_url}")

# Keep the tunnel open
ngrok_process = ngrok.get_ngrok_process()
try:
    ngrok_process.proc.wait()
except KeyboardInterrupt:
    print("Shutting down ngrok")
    ngrok.kill()