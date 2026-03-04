1.Project Overview:

This is a real-time dashboard I built to solve the challenge of monitoring driver safety at scale. The system simulates a live dashcam feed and pairs it with real-time telemetry analytics to detect speeding and safety violations instantly.

2.Technical Implementation:

Backend (FastAPI): I chose FastAPI for the backend because its asynchronous capabilities are perfect for handling high-frequency data ingestion from multiple sensors.

Real-Time Data Sync: I implemented WebSockets to ensure that data moves from the server to the browser with zero latency—crucial for road safety where every second counts.

Safety Logic: I developed a custom event listener that monitors speed. If the telemetry exceeds 80 kmph, the system triggers a "RED ALERT" state and dynamically adjusts the driver's Risk Score.

Frontend: Built with a "Mobile-First" approach using CSS Grid for a clean, professional dark-mode dashboard.

3. System Architecture
I designed the data flow to ensure low latency and real-time reliability:

```mermaid
graph LR
    A[Python Data Simulator] -->|JSON Stream| B(FastAPI Backend)
    B -->|WebSockets| C{Live Dashboard}
    C -->|Speed > 80| D[RED ALERT Status]
    C -->|Speed < 80| E[Normal Status]
