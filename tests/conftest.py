"""
Pytest configuration and fixtures for FastAPI activities API tests.

This module provides fixtures for:
- app: The FastAPI application instance
- client: A TestClient for making requests to the app
- reset_activities: Fixture that resets the activities database before each test
"""

import pytest
from fastapi.testclient import TestClient
import sys
from pathlib import Path

# Add src directory to path so we can import app
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from app import app, activities


@pytest.fixture(autouse=True)
def reset_activities():
    """
    Reset the activities database to a known state before each test.
    
    This fixture ensures test isolation by resetting the in-memory
    activities dictionary to its initial state before every test.
    """
    # Store original state
    original_activities = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Basketball Team": {
            "description": "Competitive basketball team for intramural and inter-school tournaments",
            "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
            "max_participants": 15,
            "participants": ["alex@mergington.edu"]
        },
        "Soccer Club": {
            "description": "Play soccer and develop teamwork skills",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 5:00 PM",
            "max_participants": 18,
            "participants": ["noah@mergington.edu", "ava@mergington.edu"]
        },
        "Art Studio": {
            "description": "Explore painting, drawing, and sculpture techniques",
            "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 16,
            "participants": ["isabella@mergington.edu"]
        },
        "Drama Club": {
            "description": "Perform in theatrical productions and develop acting skills",
            "schedule": "Thursdays, 4:00 PM - 5:30 PM",
            "max_participants": 20,
            "participants": ["liam@mergington.edu", "mia@mergington.edu"]
        },
        "Debate Team": {
            "description": "Develop critical thinking and public speaking through competitive debate",
            "schedule": "Mondays and Fridays, 3:30 PM - 4:45 PM",
            "max_participants": 10,
            "participants": ["lucas@mergington.edu"]
        },
        "Science Club": {
            "description": "Conduct experiments and explore STEM topics",
            "schedule": "Tuesdays, 3:30 PM - 4:30 PM",
            "max_participants": 25,
            "participants": ["harper@mergington.edu", "charlotte@mergington.edu"]
        }
    }
    
    # Clear existing activities
    activities.clear()
    
    # Restore original state (deep copy to avoid reference issues)
    for name, activity in original_activities.items():
        activities[name] = {
            "description": activity["description"],
            "schedule": activity["schedule"],
            "max_participants": activity["max_participants"],
            "participants": activity["participants"].copy()
        }
    
    yield
    
    # Cleanup after test (optional, but good practice)
    activities.clear()


@pytest.fixture
def client():
    """
    Provide a TestClient for the FastAPI application.
    
    This fixture creates a test client that can be used to make
    requests to the API without running a live server.
    """
    return TestClient(app)
