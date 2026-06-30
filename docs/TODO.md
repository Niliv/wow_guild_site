# WoW Guild Site — Project Checklist

## Phase 1 — Project setup
- [X] Create GitHub repo and clone locally
- [X] Set up folder structure (backend/, frontend/, db/)
- [X] Create venv and install packages
  - `python -m venv guild` → activate → `pip install fastapi uvicorn sqlalchemy psycopg2-binary`
- [X] pip freeze into requirements.txt
- [ ] Set up docker-compose.yml for Postgres
- [ ] Create backend/.env with DATABASE_URL
- [ ] Verify .gitignore covers guild/, .env, __pycache__
- [ ] Push initial structure to GitHub

## Phase 2 — FastAPI basics
- [ ] Create main.py with a hello world endpoint
  - `GET /` → `{"hello": "world"}` — confirm uvicorn runs
- [ ] Connect FastAPI to Postgres via SQLAlchemy
  - Create database.py with engine and session
- [ ] Create first database model — GuildMember
  - Fields: id, name, character_name, realm, class, role
- [ ] Run first migration — create the table in Postgres
- [ ] Write GET /members endpoint returning all members
- [ ] Write POST /members endpoint to add a member
- [ ] Test both endpoints in FastAPI /docs (Swagger UI)
- [ ] Seed a few test members into the database

## Phase 3 — Frontend basics
- [ ] Create index.html with basic guild page layout
  - Header, guild name, member list area
- [ ] Add style.css — basic styling, fonts, layout
- [ ] Write JS fetch() call to GET /members
  - Learn about async/await and the fetch API
- [ ] Render member list dynamically from API response
- [ ] Add CORS to FastAPI so browser can call the API
- [ ] Style member cards — show name, class, role

## Phase 4 — Blizzard API
- [ ] Register app on Blizzard developer portal
  - Get client ID and client secret → https://develop.battle.net
- [ ] Add Blizzard credentials to .env
- [ ] Implement OAuth2 client credentials flow
  - Fetch access token from Blizzard
- [ ] Fetch one character's data from WoW API
  - Name, realm, class, level, item level
- [ ] Store fetched character data in Postgres
- [ ] Add POST /members/sync endpoint to trigger a refresh
- [ ] Display live character data on the frontend

## Phase 5 — Polish and extras
- [ ] Add character profile pages
  - Click a member → see full character detail
- [ ] Add search and filter (by class, role, etc.)
- [ ] Add real name ↔ character linking in the DB
- [ ] Migrate frontend to React
  - Rebuild what you have — now it'll make sense
- [ ] Set up Alembic for database migrations
- [ ] Deploy to a VPS so guildies can access it