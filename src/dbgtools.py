# Debug tools for GovnOS

def dbg_print(msg: str):
  print(f"\x1B[32m{msg}\x1B[0m");

def err_print(msg: str):
  print(f"\x1B[31m{msg}\x1B[0m");
  exit(100);

def nhex(a: int):
  return "0x"+hex(a)[2:].upper();
