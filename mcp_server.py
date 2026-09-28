import sys
import json
from client import EPA2D

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "epa_penetration_test",
                        "description": "Calculate penetration depth and contact normal for given terminating simplex",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "simplex": {
                                    "type": "array",
                                    "items": {"type": "array", "items": {"type": "number"}}
                                }
                            },
                            "required": ["simplex"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "epa_penetration_test":
            s = [tuple(p) for p in args["simplex"]]
            d, n = EPA2D.compute_penetration(s)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"penetration_depth": d, "contact_normal": n})}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if line.strip():
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
