"""
my utility module
"""


def mygraph(func, prefix: str = 'mygraph', dtime: bool = True, maxdepth: int = 9):
    """
    Args:
        func:
        prefix:
        dtime:
        maxdepth:
    Returns:
    """
    # my_profiler = None
    # my_profiler = 'pycallgraph_svg_via_dot' ==> implemented here !
    # *** my_profiler = 'pycallgraph_svg' // .dot 출력이 cp949라서, svg가 직접은 제대로 안된다.
    from pycallgraph2 import PyCallGraph
    from pycallgraph2 import Config
    from pycallgraph2 import GlobbingFilter
    from pycallgraph2.output import GraphvizOutput
    from datetime import datetime
    import subprocess

    graphviz: GraphvizOutput = GraphvizOutput()
    graphviz.output_type = 'dot'
    # if len(func) == 0:
    #     func = 'main'
    # output_file0 = 'xplusx_o11_pycallgraph2_' + datetime.now().strftime("%Y%m%d_%H%M%S")[2:]
    output_file0 = prefix
    if dtime:
        output_file0 += '_' + datetime.now().strftime("%Y%m%d_%H%M%S")[2:]
    graphviz.output_file = output_file0 + '.dot'
    graphviz.encoding = 'UTF-8'
    config = Config(max_depth=maxdepth)
#    config.trace_filter = GlobbingFilter(exclude=[
#        'pycallgraph2.*', '_*', 'split', 'join', 'cb', 'dirname',
#        'splitext', 'normpath', 'IterParseIterator.*', 'ModuleSpec.*',
#        'shibokensupport.*', 'Spines.*', '<lambda>', 'abspath', 'fsdecode',
#        'expanduser', 'expandvars', 'splitdrive', 'realpath', 'isfile',
#        'getenv', 'ValuesView.*', 'isabs', 'normcase', 'genexpr',
#    ])
    config.trace_filter = GlobbingFilter(exclude=[
        'pycallgraph2.*', '_*', 'pygame'])

    with PyCallGraph(output=graphviz, config=config):
        # exitv = eval(func + '()')
        exitv = func()
    # with open(graphviz.output_file, encoding='cp949') as file:
    #     dot_content = file.read()
    # with open(graphviz.output_file, 'w', encoding='utf-8') as file:
    #     file.write(dot_content)
    subprocess.run(['dot', '-Tsvg', graphviz.output_file, '-o', output_file0 + '.svg'])

    return exitv
