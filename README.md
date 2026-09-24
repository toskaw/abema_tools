## mkedl.py
yt-dlpでabemaから落とした動画ファイル名を指定すると、abemaから主題歌やエンディングのタイミングを取得して、edl形式のファイルを出力します。
kodiで再生するとedlを自動で読み込んでスキップが可能です。

### edlについて
このツールは取得した時間情報をコマーシャルとしてedlを出力します。
kodiでコマーシャルを自動スキップするにはkeymap editor アドオンを使って、
Fullscreen Video->PVR->Toggle Commskipにキーを割り当ててください
割り当てたキーを押すことで自動スキップのon/offができます。