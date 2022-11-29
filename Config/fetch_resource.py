from pathlib import Path
import sys

def fetch_resource(rsrc_path):
  """Loads resources from the temp dir used by pyinstaller executables"""
  if hasattr(sys, '_MEIPASS'):
      base_path = Path(getattr(sys, '_MEIPASS'))
      return base_path.joinpath(rsrc_path)
  else:
      # not running as exe, just return the unaltered path
      return Path(rsrc_path)