from math import hypot

from fastapi import FastAPI
from pydantic import BaseModel, Field


class TrackRequest(BaseModel):
    previous: list[float] = Field(min_length=2, max_length=2)
    current: list[float] = Field(min_length=2, max_length=2)
    frame_count: int = Field(default=1, ge=1)
    fps: float = Field(default=30.0, gt=0, le=240)


class TrackResult(BaseModel):
    displacement_px: float
    speed_px_per_second: float
    frames_processed: int
    tracker: str


def track(payload: TrackRequest) -> TrackResult:
    distance = hypot(
        payload.current[0] - payload.previous[0], payload.current[1] - payload.previous[1]
    )
    return TrackResult(
        displacement_px=round(distance, 3),
        speed_px_per_second=round(distance * payload.fps, 3),
        frames_processed=payload.frame_count,
        tracker="opencv-centroid-demo",
    )


def create_app() -> FastAPI:
    app = FastAPI(title="OpenCV Object Tracker", version="0.1.0")

    @app.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "ok", "service": "opencv-object-tracker"}

    @app.post("/api/v1/track", response_model=TrackResult)
    async def track_object(payload: TrackRequest) -> TrackResult:
        return track(payload)

    return app


app = create_app()
