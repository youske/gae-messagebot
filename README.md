gae-messagebot
==============

# 導入
pipにて一部のライブラリを導入するためpipをインストールしておく

    $> sudo apt-get install pip

pipを使った必須ライブラリのインストール、GAE側にもインストールするため libフォルダにインストール
デプロイ時にこのファイルがappengineのサーバに送られるため必ず実行のこと

    $> pip install -U -r requirements -t lib/ 

## cloud9での設定
    wget appengine_sdk
    PATHを通す
    
    Cloud9の環境では利用できるポートが限られているので用調査
    現状では
    https://docs.c9.io/v1.0/docs/multiple-ports
    
    Cloud9側のアクセス先
    https://<workspacename>-<username>.c9users.io　<- 8080 ポートにマッピング
    
# copying file
設定の中で特に実行時に依存する設定、アプリケーションキーとかがあるので
設定ファイルをコピーして使う

    $> cp aliases.template alias
    $> cp app.yaml.template app.yaml
    $> cp appengine_config.py.template appengine_config.py


# alias
いくつかエイリアスを用意しているのでコンソールから次のようにエイリアスをかける

    $> . aliases

環境変数に依存するところがあるため、以下の環境変数に設定を入れておく

    export IP=0.0.0.0
    export PORT=8080


特にポートは環境によって空いているところが異なるので環境変数にて指定すること


開発用ローカルサーバのコマンド
dev 

リモートサーバにデプロイを実施
deploy

# rewrite file

# access limit

target/config.py
REMOTE_WHITELIST
