"""鐖櫕閰嶇疆妯″潡銆?
鍦ㄦ闆嗕腑绠＄悊涓庣埇铏浉鍏崇殑閰嶇疆锛屼緥濡傦細
- 璇锋眰澶?- 浠ｇ悊閰嶇疆
- 鐖彇闂撮殧
- 榛樿閰嶇疆鏂囦欢璺緞
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class Settings:
    """鍏ㄥ眬閰嶇疆瀵硅薄銆?""

    # 榛樿璇锋眰澶?    DEFAULT_HEADERS: Dict[str, str] = field(
        default_factory=lambda: {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0 Safari/537.36"
            ),
            "Accept-Language": "zh-CN,zh;q=0.9",
        }
    )

    # 榛樿浠ｇ悊閰嶇疆锛堝鏃犻渶瑕侊紝鍙繚鎸佷负绌猴級
    DEFAULT_PROXIES: Dict[str, str] = field(default_factory=dict)

    # 榛樿鐖彇闂撮殧锛堢锛?    DEFAULT_INTERVAL: float = 1.0

    # 榛樿澶栭儴閰嶇疆鏂囦欢璺緞
    DEFAULT_CONFIG_PATH: str = "data/input/spider_config.json"

    # 鍏朵粬鑷畾涔夐厤缃」
    EXTRA: Dict[str, Any] = field(default_factory=dict)


settings = Settings()
