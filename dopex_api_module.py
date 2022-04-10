###################
# Author: slurpxbt
###################

import requests


def get_dpx_token_price():
    """
    Returns usd and eth price of DPX token
    """
    try:
        resp = requests.get("https://api.dopex.io/api/v1/dpx/price").json()

        usd_prc = resp["price"]["usd"]
        eth_prc = resp["price"]["eth"]

        return usd_prc, eth_prc
    except:
        print(f"Api error: {resp}")
        return None, None


def get_dpx_tokenSupply_info():
    """
    Returns total supply, max supply and circulating supply of DPX token
    """
    try:
        resp = requests.get("https://api.dopex.io/api/v1/dpx/supply").json()

        total = resp["totalSupply"]
        max = resp["maxSupply"]
        circ = resp["circulatingSupply"]

        return total, max, circ
    except:
        print(f"Api error: {resp}")
        return None, None, None


def get_dpx_marketCap():
    """
    Returns market cap of DPX token
    """
    try:
        resp = requests.get("https://api.dopex.io/api/v1/dpx/market-cap").json()

        mc = resp["marketCap"]

        return mc
    except:
        print(f"Api error: {resp}")
        return None


def get_rdpx_token_price():
    """
    Returns usd and eth price of rDPX token
    """
    try:
        resp = requests.get("https://api.dopex.io/api/v1/rdpx/price").json()

        usd_prc = resp["price"]["usd"]
        eth_prc = resp["price"]["eth"]

        return usd_prc, eth_prc
    except:
        print(f"Api error: {resp}")
        return None, None


def get_rdpx_tokenSupply_info():
    """
    Returns total supply, max supply and circulating supply of rDPX token
    """
    try:
        resp = requests.get("https://api.dopex.io/api/v1/rdpx/supply").json()

        total = resp["totalSupply"]
        max = resp["maxSupply"]
        circ = resp["circulatingSupply"]

        return total, max, circ
    except:
        print(f"Api error: {resp}")
        return None, None, None


def get_rdpx_marketCap():
    """
    Returns market cap of rDPX token
    """
    try:
        resp = requests.get("https://api.dopex.io/api/v1/rdpx/market-cap").json()

        mc = resp["marketCap"]

        return mc
    except:
        print(f"Api error: {resp}")
        return None


def get_dpx_farms_totalTvl():
    """
       Returns market of DPX token
       """
    try:
        resp = requests.get("https://api.dopex.io/api/v1/farms/tvl").json()

        tvl = resp["tvl"]

        return tvl
    except:
        print(f"Api error: {resp}")
        return None


def get_farmsTVL_per_pool():
    """
    Returns TVL of the specific farm in DPX pools

    pools: dpx | dpx-weth | rdpx-weth | rdpx
    """

    pools = ["dpx", "dpx-weth", "rdpx-weth", "rdpx"]
    pool_tvls = {}
    try:
        for pool in pools:
            resp = requests.get(f"https://api.dopex.io/api/v1/farms/tvl?pool={pool}").json()
            print(resp)
            tvl = resp["tvl"]

            pool_tvls[pool] = tvl

        return pool_tvls
    except:
        print(f"Api error: {resp}")
        return None


def get_dpx_totalTVL():
    """
   Returns DPX total TVL
   """
    try:
        resp = requests.get("https://api.dopex.io/api/v1/tvl").json()

        tvl = resp["tvl"]

        return tvl
    except:
        print(f"Api error: {resp}")
        return None


def get_TVL_per_contract():
    """
   Returns DPX total TVL

   contracts: dpx-farm | rdpx-farm | dpx-weth-farm | rdpx-weth-farm | dpx-ssov | rdpx-ssov
   """
    contracts = ["dpx-farm", "rdpx-farm", "dpx-weth-farm", "rdpx-weth-farm", "dpx-ssov", "rdpx-ssov"]
    contract_tvls = {}
    try:
        for con in contracts:
            resp = requests.get(f"https://api.dopex.io/api/v1/tvl?include={con}").json()
            tvl = resp["tvl"]
            contract_tvls[con] = tvl

        return contract_tvls
    except:
        print(f"Api error: {resp}")
        return None



