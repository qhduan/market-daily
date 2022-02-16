import os
from datetime import datetime
import akshare as ak

today = str(datetime.now())[:10]
stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
# print(stock_zh_a_spot_em_df)
if len(stock_zh_a_spot_em_df) > 100:
    data = stock_zh_a_spot_em_df.to_json()
    root = 'market_daily'
    os.makedirs(root, exist_ok=True)
    output_path = os.path.join(root, today + 'json')
    with open(output_path, 'w') as fp:
        fp.write(data)
