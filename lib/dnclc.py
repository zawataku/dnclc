import sys

def compile_dncl_to_llvm(dncl_code):
    llvm_code = """
declare i32 @printf(i8*, ...)

define i32 @main() {
entry:
"""
    variables = {}
    string_constants = {}
    string_counter = 0  # 文字列定義用のカウンタ

    lines = dncl_code.split("\n")
    for line in lines:
        tokens = line.split()
        if not tokens:
            continue

        if "←" in tokens:
            var_name = tokens[0]
            value = tokens[2]
            variables[var_name] = f"%{var_name}"
            llvm_code += f"  %{var_name} = alloca i32, align 4\n"
            llvm_code += f"  store i32 {value}, i32* %{var_name}, align 4\n"

        elif "を表示する" in line:
            display_tokens = line.replace("を表示する", "").strip().split("と")
            for tok in display_tokens:
                tok = tok.strip()
                if tok in variables:  # 変数の場合
                    llvm_code += f"  %{tok}_val = load i32, i32* %{tok}, align 4\n"
                    llvm_code += f"  call i32 (i8*, ...) @printf(i8* getelementptr ([4 x i8], [4 x i8]* @.int_format, i32 0, i32 0), i32 %{tok}_val)\n"
                elif tok.startswith("「") and tok.endswith("」"):  # 文字列リテラルの場合
                    clean_str = tok[1:-1]  # 「」 を削除
                    utf8_bytes = clean_str.encode('utf-8')  # UTF-8 のバイト列
                    byte_len = len(utf8_bytes) + 2  # 改行 `\0A` + 終端 `\00`
                    str_var = f"@.str{string_counter}"
                    string_constants[str_var] = utf8_bytes.decode('utf-8')  # Python 文字列に戻す
                    llvm_code += f"  call i32 (i8*, ...) @printf(i8* getelementptr ([{byte_len} x i8], [{byte_len} x i8]* {str_var}, i32 0, i32 0))\n"
                    string_counter += 1

    llvm_code += "  ret i32 0\n}\n"

    # 文字列定数を上部に追加
    string_defs = '\n'.join([f'{var} = private unnamed_addr constant [{len(val) + 2} x i8] c"{val}\\0A\\00", align 1' for var, val in string_constants.items()])
    llvm_code = string_defs + "\n" + llvm_code

    # 数値フォーマット定義
    llvm_code = '@.int_format = private unnamed_addr constant [4 x i8] c"%d\\0A\\00", align 1\n' + llvm_code

    return llvm_code


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python dnclc.py <source.dncl>")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = input_filename.replace(".dncl", ".ll")

    with open(input_filename, "r", encoding="utf-8") as f:
        dncl_code = f.read()

    llvm_code = compile_dncl_to_llvm(dncl_code)

    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(llvm_code)

    print(f"Compiled completed.")