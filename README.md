# English

## Purpose
FastAPI tracking service that turns consecutive object centroids into displacement, speed and frame metrics. It serves as an explainable core for an OpenCV video worker.

## Features
- Accepts POST `/api/v1/track` with previous/current pixel coordinates, frame count and FPS.
- Computes displacement, speed and frame‑level metrics from centroid streams.
- Built with FastAPI for automatic OpenAPI docs.
- Integrates with OpenCV via a simple boundary; expects an external detector to provide centroids.
- Containerised with Docker Compose.
- Test suite using pytest; CI workflow defined in `.github/workflows/ci.yml`.

## Stack
- Python (project managed with `pyproject.toml`)
- OpenCV (integration boundary)
- Centroid tracking math
- FastAPI
- Docker & Docker Compose
- pytest
- GitHub Actions CI

## Setup & Usage
```bash
# Install dependencies (including dev extras)
pip install -e ".[dev]"

# Run the API locally with hot reload
uvicorn app.main:app --reload

# Run tests
pytest -q

# Or start with Docker Compose
docker compose up --build
```
API documentation is available at `/docs` when the service is running.

## Limitations
- The service does **not** perform object detection; it expects pre‑computed centroids from an upstream detector.
- It is intended as a core tracking component; additional logic (e.g., video I/O, storage) must be supplied by the caller.
- No guarantees about real‑time performance; performance depends on the detector and hardware.

## License
This project is licensed under the terms found in the `LICENSE` file.

# Türkçe

## Amaç
Nesne centroidlerinin ardışık verilerinden déplacement, hız ve frame metriklerini hesaplayan FastAPI takip hizmeti. OpenCV video işçisi için açıklanabilir bir çekirdek sağlar.

## Özellikler
- POST `/api/v1/track` endpointi, önceki/geçerli piksel koordinatları, frame sayısı ve FPS alır.
- Centroid akışından déplacement, hız ve frame‑seviyesi metriklerini çıkarır.
- FastAPI ile otomatik OpenAPI dokümantasyonu sunar.
- OpenCV ile sınırlı entegrasyon; dışarıdan bir detector tarafından centroidler beklenir.
- Docker Compose ile konteynerleştirilmiş.
- pytest ile test süiti; CI iş akışı `.github/workflows/ci.yml` içinde tanımlı.

## Yığın
- Python (`pyproject.toml` ile proje yönetimi)
- OpenCV (entegrasyon sınırı)
- Centroid takip matematik
- FastAPI
- Docker & Docker Compose
- pytest
- GitHub Actions CI

## Kurulum & Kullanım
```bash
# Bağımlılıkları yükle (dev ekstraları dahil)
pip install -e ".[dev]"

# Yerel API'yı hot reload ile çalıştır
uvicorn app.main:app --reload

# Testleri çalıştır
pytest -q

# Veya Docker Compose ile başlat
docker compose up --build
```
API dokümantasyonu hizmet çalışırken `/docs` adresinde mevcuttur.

## Sınırlar
- Hizmet nesne algılama yapmaz; upstream bir detector tarafından önceden hesaplanmış centroidler bekler.
- Temel bir takip bileşeni olarak tasarlanmıştır; video G/Ç, depolama gibi ek mantık çağıran tarafta sağlanmalıdır.
- Gerçek zamanlı performans garantisi yok; performans detector ve donanıma bağlıdır.

## Lisans
Bu proje `LICENSE` dosyasında bulunan koşullar altında lisanslanmıştır.

# Deutsch

## Zweck
Ein FastAPI-Tracking-Dienst, der aufeinanderfolgende Objektzentroiden in Verschiebung, Geschwindigkeit und Frame-Metriken umwandelt. Er bildet einen erklärbaren Kern für einen OpenCV-Video-Worker.

## Funktionen
- Akzeptiert POST `/api/v1/track` mit vorherigen/aktuellen Pixelkoordinaten, Bildzahl und FPS.
- Berechnet Verschiebung, Geschwindigkeit und framebasierte Metriken aus Zentroidenströmen.
- Nutzt FastAPI für automatische OpenAPI-Dokumentation.
- Integriert OpenCV über eine einfache Schnittstelle; erwartet einen externen Detektor, der Zentroiden liefert.
- Containerisiert mit Docker Compose.
- Testsuite mit pytest; CI-Workflow definiert in `.github/workflows/ci.yml`.

## Stack
- Python (Projektverwaltung mittels `pyproject.toml`)
- OpenCV (Integrationsgrenze)
- Zentroid-Tracking-Mathematik
- FastAPI
- Docker & Docker Compose
- pytest
- GitHub Actions CI

## Einrichtung & Nutzung
```bash
# Abhängigkeiten installieren (inkl. dev-Extras)
pip install -e ".[dev]"

# API lokal mit Hot-Reload starten
uvicorn app.main:app --reload

# Tests ausführen
pytest -q

# Oder mit Docker Compose starten
docker compose up --build
```
Die API-Dokumentation ist beim laufenden Dienst unter `/docs` verfügbar.

## Einschränkungen
- Der Dienst führt **keine** Objekterkennung durch; er setzt voraus, dass ein upstream-Detektor bereits Zentroiden liefert.
- Er ist als Kern-Tracking-Komponente konzipiert; zusätzliche Logik (z. B. Video-E/A, Speicherung) muss vom Aufrufer bereitgestellt werden.
- Es gibt keine Echtzeit-Leistungsgarantien; die Performance hängt vom Detektor und der Hardware ab.

## Lizenz
Dieses Projekt steht unter den Bedingungen der `LICENSE` Datei.
