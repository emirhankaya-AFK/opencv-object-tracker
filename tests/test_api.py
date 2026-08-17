from fastapi.testclient import TestClient

from app.main import TrackRequest, create_app, track


def test_centroid_tracking_calculates_speed() -> None:
    result = track(TrackRequest(previous=[0, 0], current=[3, 4], frame_count=10, fps=20))
    assert result.displacement_px == 5
    assert result.speed_px_per_second == 100


def test_tracking_endpoint_rejects_invalid_fps() -> None:
    with TestClient(create_app()) as client:
        response = client.post(
            "/api/v1/track",
            json={"previous": [0, 0], "current": [1, 1], "fps": 0},
        )
    assert response.status_code == 422
