"""閫氱敤宸ュ叿妯″潡銆?""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from src.config.config import settings


def load_config(config_path: str | None = None) -> Dict[str, Any]:
    """鍔犺浇鐖櫕閰嶇疆銆?
    浼樺厛浣跨敤浼犲叆璺緞锛屽叾娆′娇鐢ㄩ粯璁ら厤缃矾寰勩€?    """
    if config_path is None:
        config_path = settings.DEFAULT_CONFIG_PATH

    path = Path(config_path)
    if not path.exists():
        # 鑻ユ棤棰濆閰嶇疆鏂囦欢锛岃繑鍥炲唴缃粯璁ら厤缃?        return {
            "headers": settings.DEFAULT_HEADERS,
            "proxies": settings.DEFAULT_PROXIES,
            "interval": settings.DEFAULT_INTERVAL,
            "start_urls": [],
        }

    with path.open("r", encoding="utf-8") as f:
        config: Dict[str, Any] = json.load(f)

    return config
