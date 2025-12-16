"""鐖櫕鏍稿績妯″潡銆?
鑱岃矗锛?- 鏋勯€犺姹?- 鍙戦€?HTTP 璇锋眰锛堟垨鍏朵粬鍗忚锛?- 鎺у埗鐖彇鑺傚锛堢粨鍚堥厤缃腑鐨勭埇鍙栭棿闅斾笌浠ｇ悊锛?"""

import time
from typing import Any, Dict, Iterator, Optional

import requests

from src.config.config import settings


class Spider:
    """鍩虹鐖櫕绫伙紝鍙牴鎹洰鏍囩珯鐐硅繘琛屾墿灞曘€?""

    def __init__(self, config: Optional[Dict[str, Any]] = None) -> None:
        self.config = config or {}
        self.headers = self.config.get("headers", settings.DEFAULT_HEADERS)
        self.proxies = self.config.get("proxies", settings.DEFAULT_PROXIES)
        self.interval = self.config.get("interval", settings.DEFAULT_INTERVAL)

    def fetch(self) -> Iterator[requests.Response]:
        """绀轰緥鎶撳彇鏂规硶锛屾寜閰嶇疆鑺傚閫愪釜璇锋眰銆?
        鏍规嵁瀹為檯涓氬姟灏?URL 鍒楄〃銆佸垎椤甸€昏緫绛夋帴鍏ヨ繖閲屻€?        """
        urls = self.config.get("start_urls", [])
        for url in urls:
            resp = requests.get(url, headers=self.headers, proxies=self.proxies or None, timeout=10)
            yield resp
            time.sleep(self.interval)
