from multiprocessing import cpu_count
from os import environ


# Bind to $PORT or 5000
bind = '0.0.0.0:' + environ.get('PORT', '5000')

# Run ($CORES * 2) + 1 workers
workers = (cpu_count() * 2) + 1
worker_class = 'sync'

# Kill requests after 25 seconds
timeout = 25
