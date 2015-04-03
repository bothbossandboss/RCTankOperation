# RCTankOperation
2015年度五月祭 電気系展示 AR企画

戦車ラジコンの操作部分のコード

##2015/4/4 戦車操作URLの変更
http://[IP Address]/move/[direction]/[full or half]

[direction] : stop, forward, backward, right, left

[full or half] : fullで通常運転(maxスピード)、halfで速度半減(5秒経ったら自動的にmaxスピードに移行)

問題点があるので、2015_4_4_problem.txtも参照してください。

##ダウンロードに関して
GitHubの右メニューのdownload zipでzipファイルをダウンロードしてください。

GitHubが使える人は、勿論git cloneしてもOK。

##flaskディレクトリ

Raspberry Pi内にコピーすべきコードを含んだディレクトリ。

設定詳細はWiki見てください。