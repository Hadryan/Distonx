from ..DataCatcher.database_saver import DB
import time
import datetime


# отслеживает баланс и сделки
class DealsLogger:
    def __init__(self, name='test'):
        self.db = DB()
        self.name = name

    def step(self, data, comment=''):
        req_dct = dict()
        req_dct['time'] = str(time.time())
        for currency, balance in data['agent_response']['balance'].items():
            req_dct['new_balance_' + currency] = str(balance)
        req_dct['new_balance'] = str(data['emulator_response']['new_usdt'])
        for pairname, doing, amount in data['query']:
            req_dct[pairname + '_query_value'] = str(amount)
            req_dct[pairname + '_query_type'] = str(doing)
        req_dct['type'] = self.name
        req_dct['comment'] = comment
        request = 'INSERT INTO `deals` (`' + '`, `'.join(req_dct.keys()) + \
                  "`) VALUES ('" + "', '".join(req_dct.values()) + "')"
        self.db.execute(request)

    def save(self):
        pass
