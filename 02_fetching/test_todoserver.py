
import unittest
from todoserver import app
import json



app.testing = True


def json_body(resp):
    return json.loads(resp.data.decode("utf-8"))

class TestTodoserver(unittest.TestCase):
    def test_get_empty_list_of_tasks(self):
        client = app.test_client()
        resp = client.get("/tasks/")
        self.assertEqual(200, resp.status_code)
        self.assertEqual( [], json_body(resp) )
    
    def test_create_task_and_get_its_details(self):
        client = app.test_client()
        #verify test pre-conditions
        resp = client.get("/tasks/")
        self.assertEqual( [], json_body(resp) )
        # create a new task
        new_task_data = { 
                        "summary": "get data",
                        "description": "testing the getting data"
                        }

        resp = client.post("/tasks/", data = json.dumps(new_task_data))
        self.assertEqual( 201, resp.status_code )
        data = json_body(resp)
        self.assertIn("id", data )
        #self.assertTrue( "id" in data )
        # get task details
        task_id = data["id"]
        resp = client.get("/tasks/{:d}/".format(task_id))  # if strings ERROR
        self.assertEqual( 200, resp.status_code )
        task = json_body(resp)
        self.assertEqual(task_id, task["id"] )
        self.assertEqual( "get data", task["summary"] )
        self.assertEqual( "testing the getting data", task["description"] )





