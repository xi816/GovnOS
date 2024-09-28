govnocodePage00 = [
  "\\0", "$", "%", "!", " ", "?", "&", "*", "\"", "#", "@", ":", ";", "+", "-", "=",
  "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "/", "", "_", "(", ")", ".",
  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
  "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[", "]", "{", "}", "<", ">",
  "|", "`", "~", "", "", "", "", "", "", "", "", "", "", "", "", "",
  "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
  "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
  "\n", "\\d", "\\f", "\\g", "\\A", "\\B", "\\C", "\\D", "\\E", "\\f", "\\G", "\\H", "\\I", "\\J", "\\K", "\\Z",
];

GC_EOF = 0x7F;

def govnocodeToUnicode(l: list):
  for i, j in enumerate(l):
    l[i] = govnocodePage00[j];
  return l;

def govnocodeToUnicode00(c: str):
  return govnocodePage00[c];

def govnocodeToUnicode01(l: list):
  return "".join(govnocodeToUnicode(l));

def unicodeToGovnocodeDir(l: str):
  l = list(l);
  for i, j in enumerate(l):
    if (ord(j) in range(65, 91)):
      l[i] = ord(j)-33;
    elif (ord(j) in range(48, 58)):
      l[i] = ord(j)-32;
    elif (j == "."):
      l[i] = 0x1F;
    elif (ord(j) == 33):
      l[i] = 0x03;
    elif (ord(j) == 60):
      l[i] = 0x3E;
    elif (ord(j) == 62):
      l[i] = 0x3F;
    elif (ord(j) == 34):
      l[i] = 0x09;
    elif (ord(j) == 42):
      l[i] = 0x07;
    else:
      print(f"\x1B[31mUnknown symbol: {hex(ord(j))}\x1B[0m");
  return l;
