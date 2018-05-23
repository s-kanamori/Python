import subprocess
from datetime import datetime
d = datetime.now().strftime("%Y%m%d")

for line in open('hostlist.txt', 'r'):
        itemlist = line[:-1].split('\t')
        Host = itemlist[0]
        Tgt = itemlist[1]
        Com = itemlist[2]
        Ver = itemlist[3]

        snmpwalk = subprocess.run(["snmpwalk", Tgt, "-c", Com, "-v", Ver, "1.3.6.1.2.1"], stdout=subprocess.PIPE).stdout

        with open(Host + '_success_' + d + '.txt', 'w') as f:
                f.write(snmpwalk.decode("sjis"))
        print (Host + 'の取得が完了しました！')

        snmpwalk = subprocess.run(["snmpwalk", Tgt, "-c", Com+"a", "-v", Ver, "1.3.6.1.2.1"], stderr=subprocess.PIPE).stderr
        with open(Host + '_fail_' + d + '.txt', 'w') as f:
                f.write(snmpwalk.decode("sjis"))
        print (Host + 'のコミュニティ名誤りの実行が完了しました！')
