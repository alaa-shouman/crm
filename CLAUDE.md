# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## How to work with the owner of this repo — read first

The owner is **learning Django** (background: Node.js). This repo exists to learn on, not to
be delivered. Code written by Claude is code the owner did not learn from, so the default
behavior is inverted from normal:

- **Do not create, scaffold, or modify files unless explicitly asked.** Not "want me to?"
  followed by doing it — wait for a clear yes to a specific action.
- **Do not run commands that change project state** (`django-admin startproject`,
  `startapp`, `uv add`, `makemigrations`, `migrate`) unless explicitly asked. Reading,
  searching, and inspecting are fine.
- **Instruct instead.** Explain what step comes next, what command to run, and what it will
  produce. Give the owner the command to type; do not type it for them.
- **Explain the why**, not just the what. Especially where Django's conventions differ from
  Express/Prisma habits — apps vs. layers, fat models/thin views, sync-by-default,
  migrations as generated artifacts.
- When the owner asks "what's next", that is a request for **direction, not execution**.

If a task genuinely needs code written, say so and ask first.

## Project status

This repository is an empty scaffold, not a working application. It contains a `uv init`
skeleton with Django added as a dependency, but **no Django project has been generated yet** —
there is no `manage.py`, no settings module, and no apps. `main.py` is an unrelated
`uv init` stub and is not an entrypoint for anything.

Once `django-admin startproject` has been run and real apps exist, this file should be
rewritten to describe the actual architecture. Until then, there is no architecture to describe.

## Environment

- Python 3.12 (pinned in `.python-version`)
- Dependencies managed by **uv** — `uv.lock` is committed; do not hand-edit it
- Django 6.0.7

## Commands

```bash
uv sync                  # install/refresh the venv from uv.lock
uv add <package>         # add a dependency (updates pyproject.toml + uv.lock)
uv run <command>         # run inside the project venv
```

Run Python through `uv run` rather than activating `.venv` manually, so the lockfile stays
authoritative.

## Once Django is scaffolded

These become the working commands and are recorded here in advance so they are not
re-derived:

```bash
uv run python manage.py runserver
uv run python manage.py makemigrations
uv run python manage.py migrate
uv run python manage.py test                    # full suite
uv run python manage.py test app.tests.TestCase.test_name   # single test
```

## Database

The intended database is **Neon** (hosted Postgres). Neon exposes two endpoints and the
distinction matters:

- **Pooled** host (contains `-pooler`) — use for the running app. PgBouncer in transaction
  mode; does not support session-level state.
- **Direct** host (no `-pooler`) — use for `migrate`, `createsuperuser`, and anything else
  needing a session. Migrations against the pooled endpoint fail in confusing ways.

Keep these as separate env vars (e.g. `DATABASE_URL` and `DIRECT_URL`). Neon suspends idle
compute, so set `CONN_HEALTH_CHECKS = True` to avoid handing out connections dropped during
a suspend.
