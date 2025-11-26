import os
import sys
from dotenv import load_dotenv
from redis import Redis
from flask import Flask, jsonify
from cache import cache

load_dotenv()

app = Flask(__name__)

# Load Redis configuration
redis_config = {
    'host': os.getenv('REDIS_HOST', 'localhost'),
    'port': os.getenv('REDIS_PORT', 6379),
    'db': os.getenv('REDIS_DB', 0)
}

# Initialize Redis client
redis_client = Redis(**redis_config)

# Define cache configuration
cache_config = {
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_URL': f'redis://{redis_config["host"]}:{redis_config["port"]}/{redis_config["db"]}'
}

# Initialize cache
cache.init_app(app, config=cache_config)

# Define a route to test the cache
@app.route('/test-cache', methods=['GET'])
def test_cache():
    # Set a cache key with a value
    cache.set('test_key', 'test_value')
    # Get the cache key
    cache_value = cache.get('test_key')
    # Return the cache value as JSON
    return jsonify({'cache_value': cache_value})

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)