# coding=UTF8
import pytest
import app as main


@pytest.fixture
def test_hello_world(app):
    res = main.get("/")
    assert res.status_code == 200
