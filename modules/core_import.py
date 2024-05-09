import importlib, language
class core_import():
    P = core()
    def load_library(self, getModuleName):
        module_list = getModuleName
        for module in module_list:
            try:
                globals()[module.replace('.', '_')] = importlib.import_module(module)
                print(f"Successfully imported {module}")
            except ImportError as e: P.catch("import_error");exit()