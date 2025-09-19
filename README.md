# INTER-SOFTWARE-PROJECT-2
Repository for project 2 in CS369-Intermediate Software Project.

Repository Structure:

Origin Directory

    - Dockerfile
    - origin.py
        - Flask app serving audio files

Edge Directory

    - Dockerfile
    - edge.py 
        - Flask app with caching logic

Audio Files Directory

    - Example audio files of various formats for local dev/testing

CI/CD Directory

    - github-actions.yml
        - GitHub Actions Workflow 
            - Build & Push Images
    - test-script.sh
        - Example automated test

Monitoring Directory

    - prometheus.yml
    - grafana-dashboard.json

Tests Directory

    - test_origin.py
    - test_edge.py

To Add In Main Directory

    - docker-compose.yml
        - Run origin + edges simultaneously
