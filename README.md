# Python Argparse

## Argparseでコマンドライン引数をパース

### 位置引数の場合
nargsを使って複数の引数を指定することも可能です。

    python cli_args_position.py 1 aaa

    or

    python cli_args_position.py 1 2 3 aaa

### オプション引数の場合

    python cli_args_option.py --v1 aaa --v2 bbb

オプション引数の場合は引数がなくても実行可能です。
    
    python cli_args_option.py



### 位置引数とオプション引数を組み合わせた場合

    python cli_args.py aaa --v2 bbb

