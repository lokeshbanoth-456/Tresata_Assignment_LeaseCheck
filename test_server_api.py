"""Mocked local Ollama API contract test; does not call a real model."""
import json, threading, unittest
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.request import Request, urlopen
import server

class FakeOllama(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-Length', '0'))
        request = json.loads(self.rfile.read(length))
        self.server.received_model = request['model']
        self.server.received_stream = request['stream']
        response = {'message': {'content': json.dumps({
            'term_months': {'value': 36, 'quote': 'Term is 36 months', 'reason': 'explicit'},
            'monthly_rent': {'value': 45000, 'quote': 'Rent is INR 45,000 per month', 'reason': 'explicit'},
            'annual_escalation_percent': None,
            'fields': {'currency': 'INR', 'flags': []}
        })}}
        body = json.dumps(response).encode()
        self.send_response(200); self.send_header('Content-Type','application/json')
        self.send_header('Content-Length',str(len(body))); self.end_headers(); self.wfile.write(body)
    def log_message(self, *args): pass

class ServerApiTests(unittest.TestCase):
    def setUp(self):
        self.fake = HTTPServer(('127.0.0.1', 0), FakeOllama)
        threading.Thread(target=self.fake.serve_forever, daemon=True).start()
        self.old_url = server.OLLAMA_URL
        server.OLLAMA_URL = f'http://127.0.0.1:{self.fake.server_port}/api/chat'
        self.http = HTTPServer(('127.0.0.1', 0), server.Handler)
        threading.Thread(target=self.http.serve_forever, daemon=True).start()
        self.base = f'http://127.0.0.1:{self.http.server_port}'

    def tearDown(self):
        self.http.shutdown(); self.http.server_close()
        self.fake.shutdown(); self.fake.server_close()
        server.OLLAMA_URL = self.old_url

    def test_local_model_request_and_response_contract(self):
        payload = json.dumps({'text':'Term is 36 months. Rent is INR 45,000 per month.', 'model':'mock-model'}).encode()
        req = Request(self.base+'/api/propose', data=payload, headers={'Content-Type':'application/json'}, method='POST')
        with urlopen(req, timeout=3) as response: result = json.loads(response.read())
        self.assertEqual(result['provider'], 'local Ollama')
        self.assertEqual(result['model'], 'mock-model')
        self.assertEqual(result['proposal']['term_months']['value'], 36)
        self.assertEqual(self.fake.received_model, 'mock-model')
        self.assertFalse(self.fake.received_stream)

    def test_health_endpoint_does_not_require_model_call(self):
        with urlopen(self.base+'/api/health', timeout=3) as response: result=json.loads(response.read())
        self.assertTrue(result['ok'])
        self.assertEqual(result['mode'], 'local')

if __name__ == '__main__': unittest.main(verbosity=2)
