from apollox.api import API


class Client(API):
    def __init__(self, key=None, secret=None, **kwargs):
        if "base_url" not in kwargs:
            kwargs["base_url"] = "https://fapi.apollox.finance"
        super().__init__(key, secret, **kwargs)

    # MARKETS
    from apollox.rest_api.market import ping
    from apollox.rest_api.market import time
    from apollox.rest_api.market import exchange_info
    from apollox.rest_api.market import depth
    from apollox.rest_api.market import trades
    from apollox.rest_api.market import historical_trades
    from apollox.rest_api.market import agg_trades
    from apollox.rest_api.market import klines
    from apollox.rest_api.market import index_price_klines
    from apollox.rest_api.market import mark_price_klines
    from apollox.rest_api.market import mark_price
    from apollox.rest_api.market import funding_rate
    from apollox.rest_api.market import ticker_24hr_price_change
    from apollox.rest_api.market import ticker_price
    from apollox.rest_api.market import book_ticker

    # ACCOUNT(including orders and trades)
    from apollox.rest_api.account import change_position_mode
    from apollox.rest_api.account import get_position_mode
    from apollox.rest_api.account import change_multi_asset_mode
    from apollox.rest_api.account import get_multi_asset_mode
    from apollox.rest_api.account import new_order
    from apollox.rest_api.account import new_batch_order
    from apollox.rest_api.account import query_order
    from apollox.rest_api.account import cancel_order
    from apollox.rest_api.account import cancel_open_orders
    from apollox.rest_api.account import cancel_batch_order
    from apollox.rest_api.account import countdown_cancel_order
    from apollox.rest_api.account import get_open_orders
    from apollox.rest_api.account import get_orders
    from apollox.rest_api.account import get_all_orders
    from apollox.rest_api.account import balance
    from apollox.rest_api.account import account
    from apollox.rest_api.account import change_leverage
    from apollox.rest_api.account import change_margin_type
    from apollox.rest_api.account import modify_isolated_position_margin
    from apollox.rest_api.account import get_position_margin_history
    from apollox.rest_api.account import get_position_risk
    from apollox.rest_api.account import get_account_trades
    from apollox.rest_api.account import get_income_history
    from apollox.rest_api.account import leverage_brackets
    from apollox.rest_api.account import adl_quantile
    from apollox.rest_api.account import force_orders
    from apollox.rest_api.account import commission_rate

    # STREAMS
    from apollox.rest_api.data_stream_listen_key import new_listen_key
    from apollox.rest_api.data_stream_listen_key import renew_listen_key
    from apollox.rest_api.data_stream_listen_key import close_listen_key
 


 