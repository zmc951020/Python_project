"""鏁版嵁瑙ｆ瀽妯″潡銆?
鑱岃矗锛?- 瑙ｆ瀽鍝嶅簲鍐呭锛圚TML / JSON / XML 绛夛級
- 鎶藉彇缁撴瀯鍖栨暟鎹?"""

from typing import Any, Dict

from bs4 import BeautifulSoup
import requests


class Parser:
    """鍩虹瑙ｆ瀽鍣ㄧ被锛屾牴鎹笟鍔″畾鍒惰В鏋愰€昏緫銆?""

    def __init__(self, config: Dict[str, Any] | None = None) -> None:
        self.config = config or {}

    def parse(self, response: requests.Response) -> Dict[str, Any]:
        """瑙ｆ瀽鍗曚釜鍝嶅簲瀵硅薄锛岃繑鍥炵粨鏋勫寲鏁版嵁銆?""
        data: Dict[str, Any] = {}

        # 绀轰緥锛氳В鏋?HTML 鏍囬
        soup = BeautifulSoup(response.text, "lxml")
        data["url"] = str(response.url)
        data["status_code"] = int(response.status_code)
        data["title"] = soup.title.string if soup.title else ""

        return data
