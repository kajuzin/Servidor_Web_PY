import http.server
import socketserver
import logging

PORT = 80
LOG_FILENAME = "conects_log.log"

# Configurando o logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

fh = logging.FileHandler(LOG_FILENAME)
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)

logger.addHandler(fh)

class MyHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        # Log da requisição
        logger.info("{} - - {} - {}".format(self.client_address[0], self.log_date_time_string(), self.requestline))
        # Servindo o arquivo
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("Servidor ativo na porta:", PORT)
    httpd.serve_forever()