from adminconsult.api.clientcredentials import ClientCredentials
from adminconsult.api.lists import NamedList, ListItem


class Countries(NamedList):

    def __init__(self, client_credentials: ClientCredentials):

        #IMPROV# Log ticket to add country_codes to the /ap1/v1/countries endpoint
        self._country_codes = dict({2: 'AX',
                          3: 'AL',
                          4: 'DZ',
                          5: 'AS',
                          6: 'AD',
                          7: 'AO',
                          8: 'AI',
                          9: 'AQ',
                          10: 'AG',
                          11: 'AR',
                          12: 'AM',
                          13: 'AW',
                          14: 'AU',
                          15: 'AT',
                          16: 'AZ',
                          17: 'BS',
                          18: 'BH',
                          19: 'BD',
                          20: 'BB',
                          21: 'BY',
                          22: 'BE',
                          23: 'BZ',
                          24: 'BJ',
                          25: 'BM',
                          26: 'BT',
                          27: 'BO',
                          28: 'BA',
                          29: 'BW',
                          30: 'BV',
                          31: 'BR',
                          32: 'IO',
                          33: 'BN',
                          34: 'BG',
                          35: 'BF',
                          36: 'BI',
                          37: 'KH',
                          38: 'CM',
                          39: 'CA',
                          40: 'CV',
                          41: 'KY',
                          42: 'CF',
                          43: 'TD',
                          44: 'CL',
                          45: 'CN',
                          46: 'CX',
                          47: 'CC',
                          48: 'CO',
                          49: 'KM',
                          50: 'CG',
                          51: 'CD',
                          52: 'CK',
                          53: 'CR',
                          54: 'CI',
                          55: 'HR',
                          56: 'CU',
                          57: 'CY',
                          58: 'CZ',
                          59: 'DK',
                          60: 'DJ',
                          61: 'DM',
                          62: 'DO',
                          63: 'EC',
                          64: 'EG',
                          65: 'SV',
                          66: 'GQ',
                          67: 'ER',
                          68: 'EE',
                          69: 'ET',
                          70: 'FK',
                          71: 'FO',
                          72: 'FJ',
                          73: 'FI',
                          74: 'FR',
                          75: 'GF',
                          76: 'PF',
                          77: 'TF',
                          78: 'GA',
                          79: 'GM',
                          80: 'GE',
                          81: 'DE',
                          82: 'GH',
                          83: 'GI',
                          84: 'GR',
                          85: 'GL',
                          86: 'GD',
                          87: 'GP',
                          88: 'GU',
                          89: 'GT',
                          90: 'GG',
                          91: 'GN',
                          92: 'GW',
                          93: 'GY',
                          94: 'HT',
                          95: 'HM',
                          96: 'VA',
                          97: 'HN',
                          98: 'HK',
                          99: 'HU',
                          100: 'IS',
                          101: 'IN',
                          102: 'ID',
                          103: 'IR',
                          104: 'IQ',
                          105: 'IE',
                          106: 'IM',
                          107: 'IL',
                          108: 'IT',
                          109: 'JM',
                          110: 'JP',
                          111: 'JE',
                          112: 'JO',
                          113: 'KZ',
                          114: 'KE',
                          115: 'KI',
                          116: 'KP',
                          117: 'KR',
                          118: 'KW',
                          119: 'KG',
                          120: 'LA',
                          121: 'LV',
                          122: 'LB',
                          123: 'LS',
                          124: 'LR',
                          125: 'LY',
                          126: 'LI',
                          127: 'LT',
                          128: 'LU',
                          129: 'MO',
                          130: 'MK',
                          131: 'MG',
                          132: 'MW',
                          133: 'MY',
                          134: 'MV',
                          135: 'ML',
                          136: 'MT',
                          137: 'MH',
                          138: 'MQ',
                          139: 'MR',
                          140: 'MU',
                          141: 'YT',
                          142: 'MX',
                          143: 'FM',
                          144: 'MD',
                          145: 'MC',
                          146: 'MN',
                          147: 'ME',
                          148: 'MS',
                          149: 'MA',
                          150: 'MZ',
                          151: 'MM',
                          152: 'NA',
                          153: 'NR',
                          154: 'NP',
                          155: 'NL',
                          156: 'AN',
                          157: 'NC',
                          158: 'NZ',
                          159: 'NI',
                          160: 'NE',
                          161: 'NG',
                          162: 'NU',
                          163: 'NF',
                          164: 'MP',
                          165: 'NO',
                          166: 'OM',
                          167: 'PK',
                          168: 'PW',
                          169: 'PS',
                          170: 'PA',
                          171: 'PG',
                          172: 'PY',
                          173: 'PE',
                          174: 'PH',
                          175: 'PN',
                          176: 'PL',
                          177: 'PT',
                          178: 'PR',
                          179: 'QA',
                          180: 'RE',
                          181: 'RO',
                          182: 'RU',
                          183: 'RW',
                          184: 'SH',
                          185: 'KN',
                          186: 'LC',
                          187: 'PM',
                          188: 'VC',
                          189: 'WS',
                          190: 'SM',
                          191: 'ST',
                          192: 'SA',
                          193: 'SN',
                          194: 'RS',
                          195: 'SC',
                          196: 'SL',
                          197: 'SG',
                          198: 'SK',
                          199: 'SI',
                          200: 'SB',
                          201: 'SO',
                          202: 'ZA',
                          203: 'GS',
                          204: 'ES',
                          205: 'LK',
                          206: 'SD',
                          207: 'SR',
                          208: 'SJ',
                          209: 'SZ',
                          210: 'SE',
                          211: 'CH',
                          212: 'SY',
                          213: 'TW',
                          214: 'TJ',
                          215: 'TZ',
                          216: 'TH',
                          217: 'TL',
                          218: 'TG',
                          219: 'TK',
                          220: 'TO',
                          221: 'TT',
                          222: 'TN',
                          223: 'TR',
                          224: 'TM',
                          225: 'TC',
                          226: 'TV',
                          227: 'UG',
                          228: 'UA',
                          229: 'AE',
                          230: 'GB',
                          231: 'US',
                          232: 'UM',
                          233: 'UY',
                          234: 'UZ',
                          235: 'VU',
                          236: 'VE',
                          237: 'VN',
                          238: 'VG',
                          239: 'VI',
                          240: 'WF',
                          241: 'EH',
                          242: 'YE',
                          243: 'ZM',
                          244: 'ZW',
                          245: 'CW',
                          246: 'XK',
                          })

        super().__init__(client_credentials, list_name='countries')


    def set_attributes(self, payload: dict):

        for val in payload:
            val['CountryCode'] = self._country_codes[val['ListValueId']]
            self._client_credentials.lists = (self.list_id, ListItem(self.list_id, val))

    def get_country_id(self, refresh=False, **filter_field):
        '''
        Filter on country_name or country_code
        '''

        if len(filter_field) != 1:
            raise Exception('Must add exactly one filter_field.')

        if list(filter_field.items())[0][0] == 'country_name':
            return self._get_item(item_value=list(filter_field.items())[0][1], refresh=refresh).item_id
        else:
            return self._get_item(**filter_field, refresh=refresh).item_id
    
    def get_country_name(self, country_id, refresh=False):

        return self.get_item_value(item_id=country_id, refresh=refresh)
    
    def get_country_code(self, country_id, refresh=False):

        country: ListItem = self._get_item(item_id = country_id, refresh=refresh)

        return country.country_code