import uvicorn
from src.infrastructure.database.postgresql.orm.setup import reset_tables
from src.infrastructure.configs import configure_dependencies as configure_infrastructure_dependencies
from src.application.configs import configure_dependencies as configure_application_dependencies
from src.domain.configs import configure_dependencies as configure_domain_dependencies
from src.web.configs import configure_dependencies as configure_web_dependencies


if __name__ == "__main__":
    reset_tables()
    configure_domain_dependencies()
    configure_application_dependencies()
    configure_infrastructure_dependencies()
    configure_web_dependencies()
    uvicorn.run(
        "src.web.app:app",
        reload=True,
        reload_delay=1
    )
