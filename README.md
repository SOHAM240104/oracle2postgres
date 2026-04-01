# oracle2postgres

Helpers and artifacts for migrating Oracle objects to PostgreSQL.

## Contents

- `TABLE_enterprise_pg.sql`, `PROCEDURE_enterprise_pg.sql`, `SEQUENCE_enterprise_pg.sql`, `TRIGGER_enterprise_pg.sql`: extracted/translated SQL artifacts.
- `*_pg_translation.sql`: translation outputs.
- `ora2pg.conf`: sample `ora2pg` configuration.
- `ai_translator.py`: small helper that extracts a stored procedure's source from Oracle.

## `ai_translator.py` usage

Install the Oracle DB Python driver (example):

```bash
python -m venv .venv
source .venv/bin/activate
pip install oracledb
```

Set connection env vars:

```bash
export ORACLE_USER="dev_user"
export ORACLE_PASSWORD="password"
export ORACLE_DSN="localhost:1521/FREEPDB1"
```

Run:

```bash
python ai_translator.py
```

## Notes

- Don’t commit secrets. Use environment variables (or a local `.env` file) for credentials.
