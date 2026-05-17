# 🦅 ANKA - MEP Site Kontrol Aracı

Bu araç, web sitelerinin durumunu ve kontrolünü sağlamak için Termux üzerinde Python ile çalışacak şekilde geliştirilmiştir.

## 🛠️ Kurulum Komutları

Termux'u açın ve sırasıyla aşağıdaki komutları kopyalayıp yapıştırın:

```bash
# 1. Gerekli sistem paketlerini kurun
pkg update && pkg upgrade -y
pkg install git python -y

# 2. Tool'u GitHub'dan indirin
git clone https://github.com/anka71/anka-tool-mep-site-kontrol-(https://github.com/anka71/anka-tool-mep-site-kontrol-)

# 3. Tool'un klasörüne giriş yapın
cd anka-tool-mep-site-kontrol-

# 4. Gerekli tüm Python modüllerini tek seferde yükleyin
python3 -m pip install -r requirements.txt

# 5. Aracı çalıştırın!
python anka_tool.py
