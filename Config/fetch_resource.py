from pathlib import Path
import sys

def fetch_resource(rsrc_path):
  """Loads resources from the temp dir used by pyinstaller executables"""
  try:
    base_path = Path(sys._MEIPASS)
  except AttributeError:
    return rsrc_path  # not running as exe, just return the unaltered path
  else:
    return base_path.joinpath(rsrc_path)