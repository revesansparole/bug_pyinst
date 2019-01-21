========================
nitrogen_ferti
========================

fake package created to reproduce bug in pyinstaller.

 - clone project
 - cd root of project
 - conda create -n bug_pyinst python=3.6 --file=requirements.txt
 - activate bug_pyinst
 - pip install https://github.com/pyinstaller/pyinstaller/archive/develop.zip
 - pip install -e .
 - pyinstaller n_ferti.spec


error message:
Traceback (most recent call last):
  File "c:\users\jchopard\appdata\local\continuum\miniconda3\envs\bug_pyinst\lib\runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "c:\users\jchopard\appdata\local\continuum\miniconda3\envs\bug_pyinst\lib\runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "C:\Users\jchopard\AppData\Local\Continuum\miniconda3\envs\bug_pyinst\Scripts\pyinstaller.exe\__main__.py", line 9, in <module>
  File "c:\users\jchopard\appdata\local\continuum\miniconda3\envs\bug_pyinst\lib\site-packages\PyInstaller\__main__.py", line 111, in run
    run_build(pyi_config, spec_file, **vars(args))
  File "c:\users\jchopard\appdata\local\continuum\miniconda3\envs\bug_pyinst\lib\site-packages\PyInstaller\__main__.py", line 63, in run_build
    PyInstaller.building.build_main.main(pyi_config, spec_file, **kwargs)
  File "c:\users\jchopard\appdata\local\continuum\miniconda3\envs\bug_pyinst\lib\site-packages\PyInstaller\building\build_main.py", line 844, in main
    build(specfile, kw.get('distpath'), kw.get('workpath'), kw.get('clean_build'))
  File "c:\users\jchopard\appdata\local\continuum\miniconda3\envs\bug_pyinst\lib\site-packages\PyInstaller\building\build_main.py", line 791, in build
    exec(code, spec_namespace)
  File "n_ferti.spec", line 23, in <module>
    noarchive=True)
  File "c:\users\jchopard\appdata\local\continuum\miniconda3\envs\bug_pyinst\lib\site-packages\PyInstaller\building\build_main.py", line 243, in __init__
    self.__postinit__()
  File "c:\users\jchopard\appdata\local\continuum\miniconda3\envs\bug_pyinst\lib\site-packages\PyInstaller\building\datastruct.py", line 158, in __postinit__
    self.assemble()
  File "c:\users\jchopard\appdata\local\continuum\miniconda3\envs\bug_pyinst\lib\site-packages\PyInstaller\building\build_main.py", line 597, in assemble
    for name, path, typecode in compile_py_files(new_toc, CONF['workpath']):
  File "c:\users\jchopard\appdata\local\continuum\miniconda3\envs\bug_pyinst\lib\site-packages\PyInstaller\utils\misc.py", line 150, in compile_py_files
    with open(obj_fnm, 'rb') as fh:
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\jchopard\\AppData\\Local\\Continuum\\miniconda3\\envs\\bug_pyinst\\Scripts\\pyinstaller.exe\\__main__.pyo'
