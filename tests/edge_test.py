import requests
import time

EDGE1_SERVER_URL = "http://0.0.0.0:5001"
EDGE2_SERVER_URL = "http://0.0.0.0:5002"

TEST_FILENAME = "6-7.mp3"


def test_caching():
    edge1url = f"{EDGE1_SERVER_URL}/audio/{TEST_FILENAME}"
    start_time_miss = time.time()
    response_miss = requests.get(edge1url)
    end_time_miss = time.time()
    time_for_miss = end_time_miss - start_time_miss

    start_time_hit = time.time()
    response_hit = requests.get(edge1url)
    end_time_hit = time.time()
    time_for_hit = end_time_hit - start_time_hit

    print(f"Time for cache MISS: {time_for_miss:.4f}s")
    print(f"Time for cache HIT: {time_for_hit:.4f}s")

    assert response_miss.status_code == 200
    assert response_hit.status_code == 200

    assert time_for_hit < time_for_miss

    edge2url = f"{EDGE2_SERVER_URL}/audio/{TEST_FILENAME}"
    start_time_miss = time.time()
    response_miss = requests.get(edge2url)
    end_time_miss = time.time()
    time_for_miss = end_time_miss - start_time_miss

    start_time_hit = time.time()
    response_hit = requests.get(edge2url)
    end_time_hit = time.time()
    time_for_hit = end_time_hit - start_time_hit

    print(f"Time for cache MISS: {time_for_miss:.4f}s")
    print(f"Time for cache HIT: {time_for_hit:.4f}s")

    assert response_miss.status_code == 200
    assert response_hit.status_code == 200

    assert time_for_hit < time_for_miss
