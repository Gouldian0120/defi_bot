from defiwar.dex.compound import Compound
from defiwar.dex.one_inch import OneInch
from defiwar.dex.radar_relay import RadarRelay
from defiwar.dex.zero_x import ZeroX


if __name__ == "__main__":

    compound_dex = Compound()
    one_inch_dex = OneInch()
    radar_relay_exchange = RadarRelay()
    zero_x_exchange = ZeroX()

    # Compound API Calls
    '''print(compound_dex.get_account('addresses[]=0x4B3897e40749587FFBfB2732008d026DB2C8D588', 'block_number=0'))
    print(compound_dex.get_ctoken('addresses[]=0x4B3897e40749587FFBfB2732008d026DB2C8D588'))
    print(compound_dex.get_graph('asset=0xf5dce57282a584d2746faf1593d3121fcac444dc'))
    print(compound_dex.get_gov_proposals())
    print(compound_dex.get_gov_proposal_vote_receipts('proposal_id=2'))
    print(compound_dex.get_gov_accounts('page_size=1'))
    print(compound_dex.get_gov_history())

    # One1inch API Calls
    print(one_inch_dex.get_quote('100', from_token_symbol='DAI', to_token_symbol='ETH'))
    print(one_inch_dex.get_tokens())
    print(one_inch_dex.get_exchanges())

    # Radar Relay API Calls
    print(radar_relay_exchange.list_markets())
    print(radar_relay_exchange.get_market('marketId=ZRX-WETH'))
    print(radar_relay_exchange.get_market_ticker('ZRX-WETH'))
    print(radar_relay_exchange.get_market_stats('ZRX-WETH'))
    print(radar_relay_exchange.get_market_history('ZRX-WETH'))'''

    # ZeroX API Calls
    print(zero_x_exchange.get_swap_tokens())
