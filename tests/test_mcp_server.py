import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from mcp_server import MCPAcademicServer


class MCPAcademicServerTests(unittest.TestCase):
    def test_call_tool_returns_json_rpc_envelope_with_parsed_result(self):
        server = MCPAcademicServer()

        response = server.call_tool(
            "academic_query",
            {"student_id": "SV2026001"},
        )

        self.assertEqual(response["jsonrpc"], "2.0")
        self.assertEqual(response["server"], "vinuni-academic-mcp-server")
        self.assertEqual(response["tool"], "academic_query")
        self.assertEqual(response["result"]["status"], "SUCCESS")
        self.assertEqual(response["result"]["student_id"], "SV2026001")
        self.assertIsInstance(response["result"], dict)


if __name__ == "__main__":
    unittest.main()
