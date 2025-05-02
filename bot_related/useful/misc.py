def get_formatted_currencies_pages(currencies_dict):
    currencies_list = [f'*{c}*: {v}' for c, v in currencies_dict.items()]
    sorted_by_pairs = [f'{currencies_list[i]}  {currencies_list[i + 1]}' for i in range(len(currencies_list) - 1) if
                       i % 2 == 0]
    pages = []
    page = []

    for pair in sorted_by_pairs:
        page.append(pair)

        if len(page) == 6:
            pages.append(page)

            page = []

    formatted_pages = ['\n'.join([pair for pair in page]) for page in pages]

    return formatted_pages


currencies = ['TONCOIN', 'XROCK', 'SCALE', 'BOLT', 'TAKE', 'TNX', 'GRBS', 'JBCT', 'IVS', 'BTC', 'ANON', 'ATL', 'NUDES',
              'WIF', 'MARGA', 'DUREV', 'SOX', 'UNIC', 'VIRUS1', 'ICTN', 'JMT', 'FID', 'CATS', 'WALL', 'NOT', 'OPEN',
              'DHD', 'KINGY', 'GGT', 'JETTON', 'BNB', 'USDT', 'LIFEYT', 'GEMSTON', 'TRX', 'PUNK', 'TONNEL', 'DFC',
              'ETH', 'ARBUZ', 'RAFF', 'DRIFT', 'FISH', 'MEOW', 'TINU', 'GRAM', 'WEB3', 'MRDN', 'LKY', 'STBL', '1RUSD',
              'JVT', 'DRA', 'STATHAM', 'PLANKTON', 'VWS', 'SAU', 'CAVI', 'ALENKA', 'TIME', 'CES', 'KKX', 'HYDRA',
              'GRC', 'tsTON', 'STON', 'DOGS', 'SOL', 'THNG', 'SP', 'AQUAXP', 'CATI', 'HMSTR', 'STORM', 'SPN', 'JETTY',
              'MAJOR', 'FTON', 'CATSTG', 'BUILD', 'TRUMP', 'MELANIA', 'USDC', 'WOOF']
