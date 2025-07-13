import sys, base64, hashlib

def xor(d, k): return bytes([b ^ k[i % len(k)] for i, b in enumerate(d)])
def key(gf): return hashlib.sha256(gf.encode()).digest()
if len(sys.argv) < 3:
    print("wtf"); sys.exit(1)

fg, gf = sys.argv[1], sys.argv[2]
script_args = sys.argv[3:]

with open(fg, "rb") as f:
    encrypted = base64.b64decode(f.read())
decrypted_code = xor(encrypted, key(gf)).decode()
exec_globals = {"__name__": "__main__", "__file__": fg, "sys": sys}
sys.argv = [fg] + script_args
exec(decrypted_code, exec_globals)
# p b a k q m