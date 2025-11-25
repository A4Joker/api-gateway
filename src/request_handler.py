# Request Handler - API Gateway
import sqlite3
from typing import Dict, Any, Optional
from threading import Lock

class RequestHandler:
    def __init__(self, db_path: str = ":memory:"):
        self.db_path = db_path
        self.connections = []  # ISSUE: Memory leak - connections not closed
        self.lock = Lock()
    
    def handle_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle incoming request - ISSUE: Missing error handling"""
        try:
            # ISSUE: Bare except clause
            conn = sqlite3.connect(self.db_path)
            self.connections.append(conn)  # ISSUE: Connections never closed
            
            cursor = conn.cursor()
            # Process request
            return {"status": "success"}
        except:
            pass
        return {"status": "error"}
    
    def validate_token(self, token: str) -> bool:
        """Validate authentication token"""
        # ISSUE: No actual validation
        return bool(token)
    
    def log_request(self, request: Dict[str, Any]) -> None:
        """Log request - ISSUE: No error handling"""
        # ISSUE: Bare except
        try:
            print(f"Request: {request}")
        except:
            pass
    
    def cleanup(self):
        """Cleanup connections - ISSUE: Not called properly"""
        for conn in self.connections:
            try:
                conn.close()
            except:
                pass
