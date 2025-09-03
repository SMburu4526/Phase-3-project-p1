Sports Locker CLI 

Manage teams and their player lockers from a friendly CLI.

Features
- Two ORM models: Team (one) → Locker (many)
- Full CRUD for both models
- View related objects (team → lockers, locker → team)
- Input validation & helpful errors
- Alembic migrations or on-the-fly table creation (dev)

Migrations 
alembic upgrade head

python cli.py

Menus
- Teams: create, list, find by name, view lockers, update, delete
- Lockers: create, list, find by player, update, delete

Notes
- Relationship cascade delete: deleting a team removes its lockers.
