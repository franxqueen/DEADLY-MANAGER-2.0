
name: sameerpanthi

on: push

jobs:

  build:

    runs-on: ubuntu-latest

    steps:

      - uses: actions/checkout@v2

      - name: Find and Replace

        uses: jacobtomlinson/gha-find-replace@master

        with:

          find: "deadly"

          replace: "missshasa"

      - name: Create Pull Request

        uses: stefanzweifel/git-auto-commit-action@v4

        with:

          commit_message: 'Things'

          commit_options: '--no-verify'

          repository: .

          commit_user_name: savagesameer
