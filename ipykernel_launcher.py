"""Entry point for launching an IPython kernel.

This is separate from the ipykernel package so we can avoid doing imports until
after removing the cwd from sys.path.
"""
import asyncio
from tornado.platform.asyncio import AnyThreadEventLoopPolicy
import sys

if __name__ == '__main__':
    # Remove the CWD from sys.path while we load stuff.
    # This is added back by InteractiveShellApp.init_path()
    if sys.path[0] == '':
        del sys.path[0]

    from ipykernel import kernelapp as app
    # Quantopian Note: this is a py35/tornado/ipykernel patch.
    # Pleas remove it if we update this one day
    asyncio.set_event_loop_policy(AnyThreadEventLoopPolicy())
    app.launch_new_instance()
