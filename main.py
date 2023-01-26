import uvicorn
from src.infrastructure.orm.setup import setup_tables
from src.infrastructure.orm.configs import database


if __name__ == "__main__":
    setup_tables(database, [])
    uvicorn.run(
        "src.web.app:app",
        reload=True,
        reload_delay=1
    )
