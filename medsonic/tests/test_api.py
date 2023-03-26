from medsonic.tests.conftest import client

def test_server(client):
    """GET <host_address>/

    Pass with 404 returncode.
    """
    response = client.get("/")
    assert response.status_code == 404
    assert response.json["error"] == "The requested URL was not found on the server."
