permission = 2

usage = {
    'tag': '-------------------- \u00A7bKICK 帮助文档 \u00A7r--------------------',
    'help': '    踢出玩家 \u00A76> \u00A7r!!kick [玩家名]''',
}
display = {
    'success': '\u00A7a已将 \u00A76{} \u00A7a踢出服务器',
    'permission': '\u00A7c权限不足'
}

def on_info(server, info):
    if info.is_player == 1:
        if info.content.startswith('!!kick'):
            args = info.content.split()
            if len(args) == 1:
                server.say(usage['tag'])
                for line in usage['help'].splitlines():
                    server.say(line)
                server.say(usage['tag'])
            elif server.get_permission_level(info) >= permission:
                for player in args[1:]:
                    server.execute('kick {}'.format(player))
                    server.say(display['success'].format(player))
            else:
                server.say(display['permission'])

def on_load(server, old):
	server.add_help_message('!!kick', '踢出玩家')