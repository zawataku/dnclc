@.int_format = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1
@.str0 = private unnamed_addr constant [9 x i8] c"こんにちは世界\0A\00", align 1

declare i32 @printf(i8*, ...)

define i32 @main() {
entry:
  %x = alloca i32, align 4
  store i32 10, i32* %x, align 4
  %y = alloca i32, align 4
  store i32 20, i32* %y, align 4
  %x_val = load i32, i32* %x, align 4
  call i32 (i8*, ...) @printf(i8* getelementptr ([4 x i8], [4 x i8]* @.int_format, i32 0, i32 0), i32 %x_val)
  %y_val = load i32, i32* %y, align 4
  call i32 (i8*, ...) @printf(i8* getelementptr ([4 x i8], [4 x i8]* @.int_format, i32 0, i32 0), i32 %y_val)
  call i32 (i8*, ...) @printf(i8* getelementptr ([23 x i8], [23 x i8]* @.str0, i32 0, i32 0))
  ret i32 0
}
