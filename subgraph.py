from datetime import date
from datetime import datetime

from subgrounds import Subgrounds
from subgrounds.subgraph import SyntheticField, FieldPath

sub_g = Subgrounds()

uniswap_v3_graph = sub_g.load_subgraph("https://gateway.thegraph.com/api/7e84918e033afc7990e423669f37749d/subgraphs/id/3hCPRGf4z88VC5rsBKU5AA9FBBq5nF3jbKJG7VZCbhjm")

# Querrying top pools by Locked USD Value
top_pools_query = uniswap_v3_graph.Query.pools(
    first=10,
    orderBy='totalValueLockedUSD',
    orderDirection='desc'
)

# Fetching the data
top_pools = sub_g.query_df([
    top_pools_query.id,
    top_pools_query.token0.symbol,
    top_pools_query.token1.symbol,
    top_pools_query.totalValueLockedUSD
])

print(top_pools)
