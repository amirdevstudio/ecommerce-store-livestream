import uvicorn
from src.infrastructure.orm.postgresql.setup import reset_tables


if __name__ == "__main__":
    reset_tables()
    uvicorn.run(
        "src.web.app:app",
        reload=True,
        reload_delay=1
    )
