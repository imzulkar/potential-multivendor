# Apply database migrations

python manage.py collectstatic --noinput
echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate

echo "Creating Superuser"
python manage.py init

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000