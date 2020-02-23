from stupid_model import RandomModel
from write_all_logger import WriteAllLogger
import logging
from paper_testing import Agent, Emulator, Environment


with open('../settings/cryptos.txt') as file:
    cryptos = [a[:-1] for a in file.readlines()]
balance = {asset: 0. for asset in cryptos}
balance['usdt'] = 200.
logging.basicConfig(level=logging.INFO)

model = RandomModel()
agent = Agent(balance, model)
emulator = Emulator()
env = Environment(agent, emulator, WriteAllLogger, 600)
env.start()
