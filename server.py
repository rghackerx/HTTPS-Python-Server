import http.server
import ssl
import os

# Absolute path of the current script
thisScriptPath = os.path.dirname(os.path.abspath(__file__)) + "/"

# Generate self-signed certificate if not present
def generate_selfsigned_cert():
    cert_path = thisScriptPath + "cert.pem"
    key_path = thisScriptPath + "key.pem"

    if not os.path.exists(cert_path) or not os.path.exists(key_path):
        OpenSslCommand = (
            f'openssl req -newkey rsa:4096 -x509 -sha256 -days 3650 -nodes '
            f'-out {cert_path} -keyout {key_path} '
            f'-subj "/C=IN/ST=Maharashtra/L=Satara/O=Wannabees/OU=KahiHiHa Department/CN=www.iamselfdepartment.com"'
        )
        os.system(OpenSslCommand)
        print("<<<< Certificate Generated >>>>>")
    else:
        print("Certificate already exists. Skipping generation.")

# Start the HTTPS server
def startServer(host, port):
    server_address = (host, port)
    httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

    # Secure the server with SSL
    httpd.socket = ssl.wrap_socket(
        httpd.socket,
        server_side=True,
        certfile=thisScriptPath + "cert.pem",
        keyfile=thisScriptPath + "key.pem",
        ssl_version=ssl.PROTOCOL_TLS_SERVER  # Secure TLS version
    )

    print(f"🚀 File Server started at https://{host}:{port}")
    httpd.serve_forever()

# Entry point
def main():
    try:
        generate_selfsigned_cert()
        # Use the specified IP and port
        startServer("IP", 5555) #change you IP
    except KeyboardInterrupt:
        print("\nFile Server Stopped!")

# Call main function
if __name__ == "__main__":
    main()