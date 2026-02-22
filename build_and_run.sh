if [ -d "out/" ]; then
  mkdir out
fi

docker compose --env-file .env up --build --remove-orphans 