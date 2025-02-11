import ctypes
import os
import os.path as osp

dir_path = osp.join(os.path.expanduser('~'), 'space/trt_plugin/build/lib/')

if not osp.exists(dir_path):
    if 'AMIRSTAN_LIBRARY_PATH' in os.environ:
        dir_path = os.environ['AMIRSTAN_LIBRARY_PATH']
    else:
        dir_path = os.path.dirname(os.path.realpath(__file__))


def load_plugin_library():
    # ctypes.CDLL(osp.join(dir_path, 'libamirstan_plugin.so'))
    ctypes.CDLL(osp.join(osp.expanduser("~"), 'torchtrt_plugins/build/lib/libtorchtrt_plugins.so'))
