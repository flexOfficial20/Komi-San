from nksama import bot


def send_log(err, module):
    bot.send_message(-1002100475470, f"error in {module}\n\n{err}")
