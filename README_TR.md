# OpenCV Object Tracker

[English](README.md) | [Türkçe](README_TR.md)

Ardışık nesne merkezlerini yer değiştirme, hız ve kare metriklerine dönüştüren FastAPI takip servisi. OpenCV video worker'ı için açıklanabilir çekirdek sağlar.

![Demo](docs/demo.svg)

## Teknolojiler
Python, OpenCV entegrasyon sınırı, centroid takip matematiği, FastAPI, Docker, pytest ve CI. Üretimde cv2 ile video kareleri okunur, detector bağlanır ve track'ler saklanır.

## Çalıştırma
POST /api/v1/track önceki/son piksel koordinatlarını, kare sayısını ve FPS'i alır.

    pip install -e ".[dev]"
    uvicorn app.main:app --reload
    pytest -q

Docker: docker compose up --build. Doküman: /docs.

