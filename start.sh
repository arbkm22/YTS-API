bash alive.sh &
uvicorn src:app --host=0.0.0.0 --port=${PORT:-5000}