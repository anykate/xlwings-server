import os
from pathlib import Path
from typing import List, Literal, Optional

from pydantic import UUID4, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """See .env.template for documentation"""

    model_config = SettingsConfigDict(
        env_prefix="XLWINGS_", env_file=os.getenv("DOTENV_PATH", ".env"), extra="ignore"
    )
    add_security_headers: bool = True
    auth_providers: Optional[List[str]] = []
    auth_required_roles: Optional[List[str]] = []
    auth_entraid_client_id: Optional[str] = None
    auth_entraid_tenant_id: Optional[str] = None
    auth_entraid_multitenant: bool = False
    app_path: str = ""
    base_dir: Path = Path(__file__).resolve().parent
    object_cache_url: Optional[str] = None
    object_cache_expire_at: Optional[str] = "0 12 * * sat"
    object_cache_enable_compression: bool = True
    cors_allow_origins: List[str] = ["*"]
    date_format: Optional[str] = None
    enable_alpinejs_csp: bool = True
    enable_bootstrap: bool = True
    enable_examples: bool = True
    enable_excel_online: bool = True
    enable_htmx: bool = True
    enable_socketio: bool = True
    environment: Literal["dev", "qa", "uat", "staging", "prod"] = "prod"
    functions_namespace: str = "XLWINGS"
    hostname: Optional[str] = None
    log_level: str = "INFO"
    # These UUIDs will be overwritten by: python run.py init
    manifest_id_dev: UUID4 = "dcc4d25f-3fb0-4a65-84a7-a09178f1c89d"
    manifest_id_qa: UUID4 = "52d6620d-f445-428b-b7d8-e4a6b40d4614"
    manifest_id_uat: UUID4 = "1a421e95-576f-4ab2-9bfc-bb974d43a3e1"
    manifest_id_staging: UUID4 = "96eb657a-b8b4-49a3-83a1-5e5357f6d9e1"
    manifest_id_prod: UUID4 = "81513a27-f17b-4c2d-a5ae-585a2b48d73c"
    project_name: str = "xlwings Server"
    public_addin_store: bool = False
    secret_key: Optional[str] = None
    socketio_message_queue_url: Optional[str] = None
    socketio_server_app: bool = False
    static_url_path: str = "/static"
    license_key: Optional[str] = ""

    @computed_field
    @property
    def static_dir(self) -> Path:
        return self.base_dir / "static"


settings = Settings()

# TODO: refactor once xlwings offers a runtime config
if settings.license_key and not os.getenv("XLWINGS_LICENSE_KEY"):
    os.environ["XLWINGS_LICENSE_KEY"] = settings.license_key

if settings.date_format:
    os.environ["XLWINGS_DATE_FORMAT"] = settings.date_format
