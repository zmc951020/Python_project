"""鐖櫕鍏ュ彛妯″潡

姝ゆ枃浠朵綔涓烘暣涓埇铏」鐩殑鍚姩鍏ュ彛锛?- 鍔犺浇閰嶇疆锛堣姹傚ご銆佷唬鐞嗐€佺埇鍙栭棿闅旂瓑锛?- 鍒濆鍖栫埇铏牳蹇冩ā鍧椾笌瑙ｆ瀽妯″潡
- 鎺у埗鐖彇娴佺▼涓庢暟鎹寔涔呭寲
"""

from modules.spider import Spider
from modules.parser import Parser
from modules.utils import load_config


def run():
    """鍚姩鐖櫕涓绘祦绋嬨€?""
    # 鍔犺浇閰嶇疆
    config = load_config()

    # 鍒濆鍖栫埇铏笌瑙ｆ瀽鍣?    spider = Spider(config=config)
    parser = Parser(config=config)

    # 绀轰緥涓诲惊鐜紙鏍规嵁瀹為檯涓氬姟瀹屽杽锛?    for item in spider.fetch():
        data = parser.parse(item)
        # 鍦ㄦ澶勬坊鍔犳暟鎹繚瀛橀€昏緫锛屼緥濡備繚瀛樺埌鏂囦欢鎴栨暟鎹簱
        # save_data(data)


if __name__ == "__main__":
    # 鐖櫕鍚姩鍏ュ彛
    run()
