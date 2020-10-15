# CustomerSupportAPI

<!-- # Short Description -->

FastAPIのORMとしてDjangoを採用したAPIサーバを作る．

現在，DjangoのサーバーおよびFastAPIのサーバー（いずれも`uvicorn`を採用）との間で通信ができるような状態になった．

<!-- # Badges -->

[![Github issues](https://img.shields.io/github/issues/Ningensei848/CustomerSupportAPI)](https://github.com/Ningensei848/CustomerSupportAPI/issues)
[![Github forks](https://img.shields.io/github/forks/Ningensei848/CustomerSupportAPI)](https://github.com/Ningensei848/CustomerSupportAPI/network/members)
[![Github stars](https://img.shields.io/github/stars/Ningensei848/CustomerSupportAPI)](https://github.com/Ningensei848/CustomerSupportAPI/stargazers)
[![Github top language](https://img.shields.io/github/languages/top/Ningensei848/CustomerSupportAPI)](https://github.com/Ningensei848/CustomerSupportAPI/)
[![Github license](https://img.shields.io/github/license/Ningensei848/CustomerSupportAPI)](https://github.com/Ningensei848/CustomerSupportAPI/)

# Tags

`FastAPI` `Django`

# Advantages

- `FastAPI`を採用した開発しやすく性能も良いAPI
- ORMに`Django`を採用できるように工夫されている（先人の知恵）

### 参考情報：

- [【翻訳記事】FastAPIは実際にDjangoと非常に相性が良い - Qiita](https://qiita.com/Ningensei848/items/ac72ff6edf4d887cdcc1#mainutilspy)
  - こちらは公式のQ&Aでおすすめされているやり方．個人的には`router`の書き方が汚く感じてイヤだったので別の方法を探していた．
- [FastAPIとDjango ORMを組み合わせる - Qiita](https://qiita.com/kigawas/items/80e48ccce98a35f65fff)
  - こちらは簡潔にまとめていて大変印象が良かった．大部分はこちらを参考にしている．

# Installation

- `pipenv install`

# Deployment

- `pipenv run uvicorn mysite.asgi:fastapp --reload`
- `pipenv run gunicorn mysite.asgi:application -w 4 -k uvicorn.workers.UvicornWorker -b localhost:8001`

# Contributors

- [Ningensei848](https://github.com/Ningensei848)

<!-- CREATED_BY_LEADYOU_README_GENERATOR -->