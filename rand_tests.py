from bot_core import BotCore
import Database.core as db_core

session = db_core.LocalSession()
core = BotCore(session)

core.add_new_user("12345")

