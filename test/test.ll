@.int_format = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1
@.str0 = private unnamed_addr constant [17 x i8] c"\E6\95\B4\E3\81\84\E3\81\BE\E3\81\97\E3\81\9F\0A\00", align 1
@.str1 = private unnamed_addr constant [20 x i8] c"\E5\80\8B\E8\A6\8B\E3\81\A4\E3\81\8B\E3\81\A3\E3\81\9F\0A\00", align 1
@.str2 = private unnamed_addr constant [3 x i8] c"\28\0A\00", align 1
@.str3 = private unnamed_addr constant [5 x i8] c"\EF\BC\8C\0A\00", align 1
@.str4 = private unnamed_addr constant [3 x i8] c"\29\0A\00", align 1

declare i32 @printf(i8*, ...)

define i32 @main() {
entry:
  %kosu = alloca i32, align 4
  store i32 3, i32* %kosu, align 4
  %x = alloca i32, align 4
  store i32 5, i32* %x, align 4
  %y = alloca i32, align 4
  store i32 -1, i32* %y, align 4
  call i32 (i8*, ...) @printf(i8* getelementptr ([17 x i8], [17 x i8]* @.str0, i32 0, i32 0))
  %kosu_val = load i32, i32* %kosu, align 4
  call i32 (i8*, ...) @printf(i8* getelementptr ([4 x i8], [4 x i8]* @.int_format, i32 0, i32 0), i32 %kosu_val)
  call i32 (i8*, ...) @printf(i8* getelementptr ([20 x i8], [20 x i8]* @.str1, i32 0, i32 0))
  call i32 (i8*, ...) @printf(i8* getelementptr ([3 x i8], [3 x i8]* @.str2, i32 0, i32 0))
  %x_val = load i32, i32* %x, align 4
  call i32 (i8*, ...) @printf(i8* getelementptr ([4 x i8], [4 x i8]* @.int_format, i32 0, i32 0), i32 %x_val)
  call i32 (i8*, ...) @printf(i8* getelementptr ([5 x i8], [5 x i8]* @.str3, i32 0, i32 0))
  %y_val = load i32, i32* %y, align 4
  call i32 (i8*, ...) @printf(i8* getelementptr ([4 x i8], [4 x i8]* @.int_format, i32 0, i32 0), i32 %y_val)
  call i32 (i8*, ...) @printf(i8* getelementptr ([3 x i8], [3 x i8]* @.str4, i32 0, i32 0))
  ret i32 0
}
