from http.server import HTTPServer, BaseHTTPRequestHandler

class manipuladorWeb(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        mensagem = b"Ola sou o servidor rodando na rede docker"
        self.wfile.write(mensagem)

servidor = HTTPServer(('0.0.0.0', 8080), manipuladorWeb)
print("Servidor iniciado na porta 8080")
servidor.serve_forever()