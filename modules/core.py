class core:
    def __init__(self):
        try:
            import importlib
        except ImportError:
            print('Error to import "')
        print(f"{'*'*5} core.py {'*'*5}\ninitlizing language module...")
        module_list = ['os','json','datetime']
        print(f"[INFO] Importing Modules...")
        for module in module_list:
            try:
                globals()[module] = importlib.import_module(module)
                print(f"[INFO] Successfully imported {module}")
                if module == 'json':
                    print(f"[INFO] Importing JSON Files...")
                    jsonfile = ['setting.json']
                    with open(jsonfile[0], 'r') as f:
                        s = json.load(f)
                        locale = s['language']
                        with open(os.path.join(os.path.dirname(__file__), f'../locale/{locale}.json'), 'r') as f:
                            global lang_file;lang_file = json.load(f)
            except ImportError as e:
                print(f"[ERROR] {e}")
                pass
    def module_catch(RequestData):
        print(f"{'*' * 50}\n\n{RequestData['error']['name_error']}\n\n{'*' * 50}")
    def catch(self, RequestData):
        print(f"{'*' * 50}\n\n{lang_file['error'][RequestData]}\n\n{'*' * 50}")
    def panel(self, RequestData):
        logtime = datetime.datetime.now().time().strftime("%H:%M:%S")
        print(f"({logtime})[INFO] : {RequestData}가 정상적으로 승인된")
    def importmodule(self, modulename):


if __name__ == "__main__":
    import json
    with open('../locale/ko-KR.json', 'r') as f: locale = json.load(f)
    PrintLog.module_catch(locale)