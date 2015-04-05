# RCTankOperation
2015年度五月祭 電気系展示 AR企画

戦車ラジコンの操作部分のコード

##wiringPiについて
wikiで紹介されているwiringPiではない、WiringPi2-Pythonをpwm_control.pyで用いている。

wiki ... http://tomowatanabe.hatenablog.com/entry/2013/01/14/181116

今回 ... https://github.com/Gadgetoid/WiringPi2-Python

理由としては、wiringPiがC/C++言語用ライブラリなのではないかと疑ったため。
多分wikiのwiringPiでもpythonプログラム内で使えるんだけど、一応別のバージョンも試してみたといった感じ。

##2015/4/4 戦車操作URLの変更
http://[IP Address]/move/[direction]/[full or half]

[direction] : stop, forward, backward, right, left

[full or half] : fullで通常運転(maxスピード)、halfで速度半減(5秒経ったら自動的にmaxスピードに移行)

##問題点
###pwm制御の権限に関して
wiringPiを用いればroot権限でなくとも動く、らしいが確認できなかった。
WiringPi2-Pythonに関しては、サンプルコードの注釈にrun these with sudoと書いてあるし。

結局、root権限が必要なのか。(2015/4/5現在)

###Apache実行ユーザに関して
グループwww-data、ユーザwww-dataでApacheを実行している。
pwm制御のため、www-dataにroot権限を持たせる、もしくはgpioに関する権限を持たせようとしたが上手くいかない。

Apacheをroot権限で実行するのは、ネット環境が閉じているとは言えセキュリティ的に良くないと感じる。
www-dataではなく、条件を満たすユーザ/グループを作成しようとしたが上手くいかない。

参考にしたのは、このあたり。

 https://dissectionbydavid.wordpress.com/2013/10/21/raspberry-pi-using-gpio-wiringpi-without-root-sudo-access/

 http://easyramble.com/create-user-group.html

 http://hnakamur.blogspot.jp/2008/12/debianwheel.html

###pwm実行方法
pwm_controll.pyという、pwm制御専用のファイルを作成し、引数に4つのピンのgpioの番号と、それぞれの電圧値を％で取るよう設定。

hello_flask.pyで/move/[direction]/[full or half]が呼ばれると、
fullの場合は以前と変わらない方法で実行し(修正する手間を省いたため)、
halfの場合は os.system('sudo python pwm_control.py') としてroot権限で別プロセスでプログラムを実行。

###pwmが持続しない問題

pwm_control.pyで wiringpi2.softPwmWrite(PIN_TO_PWM_L1,PARAM_L1) を実行しているが、while文もしくはfor文でループにしないと短時間しか実行されない。
(Lチカだと、一瞬点灯して消える。)

while文で無限ループにした場合、/move/forward/halfで半分の出力が得られるが、その後/move/stop/halfとしても出力は変わらない。(Lチカだと点灯したまま。)

恐らく、pwm_control.pyがhello_flask.pyと別プロセスで実行されており、pwm_control.pyがgpioをwhile文の無限ループで占有しているため、別の命令がgpioに伝わらないのではないかと考えた。

pwmで速度を半減させることを第一の目標としていたため、命令の割り込みに関しては保留し、一定時間経ったらwhile文を自動で抜けるプログラムに変更し、pwm_control.pyを自動で終了させることにした。

他の方法としては、pwm_control.pyのプロセスIDを外部ファイルに出力し、os.system('kill -9 [プロセスID]')とかしてプロセスを強制終了する方法が挙げられる。
試したけど、上手くいかなかった。(2015/4/4時点)

###対応策
pwmで半分の出力にした後(pwm_control.pyが終了した後)に通常モードで運転することで、速度が半減した後にpwm_control.pyが終了したことで突然戦車が停止する問題を回避。

###C++プログラム(PC操作側)からHTTP通信した時の問題
halfモードの時、HTTP送信要求に関するエラーが出る。
原因は解明されていない。(2015/4/5現在)

##ダウンロードに関して
GitHubの右メニューのdownload zipでzipファイルをダウンロードしてください。

GitHubが使える人は、勿論git cloneしてもOK。

##flaskディレクトリ

Raspberry Pi内にコピーすべきコードを含んだディレクトリ。

設定詳細はWiki見てください。