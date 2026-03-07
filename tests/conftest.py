import pytest
import copy
from fastapi.testclient import TestClient

from src.app import app, activities as global_activities

# Store initial state of activities for resetting between tests
initial_activities = copy.deepcopy(global_activities)


@pytest.fixture
def client():
    """FastAPI TestClient fixture for testing the API."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset activities to initial state before each test."""
    global global_activities
    global_activities.clear()
    global_activities.update(copy.deepcopy(initial_activities))