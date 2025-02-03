import sys


def compile_dncl_to_llvm(dncl_code):
    llvm_code = """
@.str = private unnamed_addr constant [4 x i8] c"%d\\0A\\00", align 1
declare i32 @printf(i8*, ...)

define i32 @main() {
entry:
"""
    variables = {}

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
            var_names = [tok for tok in tokens if tok in variables]
            for var in var_names:
                llvm_code += f"  %{var}_val = load i32, i32* %{var}, align 4\n"
                llvm_code += f"  call i32 (i8*, ...) @printf(i8* getelementptr ([4 x i8], [4 x i8]* @.str, i32 0, i32 0), i32 %{var}_val)\n"

    llvm_code += "  ret i32 0\n}\n"
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

    print(f"Compiled {input_filename} to {output_filename}")
    print(f"Run `clang -o program {output_filename} && ./program` to execute.")
