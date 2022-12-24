from bot_core import BotCore
from Database.core import *

session = Session()
core = BotCore(session)

req_user = session.query(User).join(Role).filter_by(telegram_id='12314123123').first()
req_user.role.do_smth()
print('a')


