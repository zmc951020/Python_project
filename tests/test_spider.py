"""鐖櫕璇锋眰涓庢暟鎹В鏋愬熀纭€娴嬭瘯鐢ㄤ緥銆?""

from typing import Dict, Any

import requests

from src.modules.spider import Spider
from src.modules.parser import Parser


class DummyResponse(requests.Response):
    """鐢ㄤ簬瑙ｆ瀽娴嬭瘯鐨勮櫄鎷熷搷搴斿璞°€?""

    def __init__(self, text: str, url: str = "http://example.com", status_code: int = 200) -> None:
        super().__init__()
        self._content = text.encode("utf-8")
        self.url = url
        self.status_code = status_code


def test_spider_init() -> None:
    """鍩虹娴嬭瘯锛歋pider 鑳藉浣跨敤榛樿閰嶇疆鍒濆鍖栥€?""
    spider = Spider(config={"start_urls": []})
    assert spider.interval > 0


def test_parser_parse_html_title() -> None:
    """鍩虹娴嬭瘯锛歅arser 鑳藉瑙ｆ瀽 HTML 鏍囬銆?""
    html = """<html><head><title>test title</title></head><body></body></html>"""
    resp = DummyResponse(text=html)

    parser = Parser(config={})
    data: Dict[str, Any] = parser.parse(resp)

    assert data["title"] == "test title"
    assert data["status_code"] == 200
