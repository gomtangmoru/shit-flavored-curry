if __name__ == '__main__':
    try:
        import importlib
        module_list = ['discord', 'dotenv', 'os', 'modules.core']
        for module in module_list:
            try:
                globals()[module.replace('.', '_')] = importlib.import_module(module)
                if module == 'modules.core':
                    P = modules_core.core()
                print(f"Successfully imported {module}")
            except ImportError as e: P.catch("import_error");exit()

        P.panel("모듈 가져오기 시작")
    except ImportError:
        print("바보");exit()
    dotenv.load_dotenv();TOKEN = os.getenv('TOKEN')# env 파일 사용선언 및 가져오기
    if TOKEN == "INPUT_YOUR_TOKEN": P.catch("token_default"); exit() # 토큰 없으면 빠꾸
    print(locale.get('success_token')) # 토큰 성공적으로 가져왔다 출력
    import discord, asyncio, os, dotenv;from discord.ext import commands # 본격적인 모듈 가져오기
    intents = discord.Intents.default();intents.message_content = True # 봇 인텐트 설정
else:
    print(ER_catch('name_error')) # 이 파일이 메인 파일이 아니면 빠꾸

def importmodule(modulename):
    import importlib





class core():
    def __init__(self):
        self.bot = commands.Bot(command_prefix="", intents=intents)
        for i in os.listdir('cogs'):
            if i.endswith('.py'):
                self.bot.load_extension(f'cogs.{i[:-3]}')
        self.bot.run(os.getenv('TOKEN'))


core()