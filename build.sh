#!/bin/bash

set -o errexit  # exit on error

# Navigate to the client directory and run npm commands
echo "Installing client dependencies and building the client..."
cd client
npm install
npm run build

cd ..

# Navigate to the server directory and run pip commands
echo "Installing server dependencies and setting up the database..."
cd server
pip install -r requirements.txt
# python manage.py collectstatic --no-input # we aren't using this anymore because we removed django's ability to serve static files and have it only serve as an api
python manage.py migrate

cd ..

echo "Build and setup completed successfully!"
