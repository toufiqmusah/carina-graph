# subgraph.py

import os
from dotenv import load_dotenv
from subgrounds import Subgrounds
from subgrounds.pagination import LegacyStrategy, ShallowStrategy

# Getting API Key, etc
load_dotenv()
api_key = os.getenv('API_KEY')

sub_g = Subgrounds()
uniswap_v3_graph = sub_g.load_subgraph(f"https://gateway.thegraph.com/api/{api_key}/subgraphs/id/3hCPRGf4z88VC5rsBKU5AA9FBBq5nF3jbKJG7VZCbhjm")

# Querrying Top Pools
def get_top_pools_data(strategy):
    top_pools_query = uniswap_v3_graph.Query.pools(
        first=10,
        orderBy='totalValueLockedUSD',
        orderDirection='desc'
    )
    top_pools = sub_g.query_df([
        top_pools_query.id,
        top_pools_query.token0.symbol,
        top_pools_query.token1.symbol,
        top_pools_query.totalValueLockedUSD
    ], pagination_strategy=strategy)
    
    return top_pools

# Getting Fee Analysis
def get_fee_analysis_data(strategy):
    fee_analysis_query = uniswap_v3_graph.Query.pools(
        first=10,
        orderBy='totalValueLockedUSD',
        orderDirection='desc'
    )
    fee_data = sub_g.query_df([
        fee_analysis_query.id,
        fee_analysis_query.feeTier,
        fee_analysis_query.volumeUSD,
        fee_analysis_query.feesUSD
    ], pagination_strategy=strategy)
    
    return fee_data

# Getting Comparative Analysis Data
def get_comparative_analysis_data(strategy):
    fields_query = uniswap_v3_graph.Query.pools(
        first=10,
        orderBy='totalValueLockedUSD',
        orderDirection='desc'
    )
    pools_data = sub_g.query_df([
        fields_query.id,
        fields_query.token0.symbol,
        fields_query.token1.symbol,
        fields_query.totalValueLockedUSD,
        fields_query.volumeUSD
    ], pagination_strategy=strategy)
    
    comparative_analysis = pools_data.copy()
    comparative_analysis['volume_to_liquidity_ratio'] = (
        comparative_analysis['pools_volumeUSD'] / comparative_analysis['pools_totalValueLockedUSD']
    )
    
    return comparative_analysis