# AES-128 Encryption Demo

## Mô tả
Đây là chương trình mã hóa AES-128 (ECB mode) đơn giản bằng C++. Bạn nhập thông điệp, chương trình sẽ mã hóa và xuất ra file `output.aes`.

## Yêu cầu
- Đã cài đặt MinGW-w64/MSYS2 (có lệnh `g++`)
- Đã có file `main.cpp` trong thư mục này

## Cách biên dịch
1. Mở terminal MINGW64 hoặc MSYS2
2. Chuyển vào thư mục chứa mã nguồn:
   ```sh
   cd /c/ANtoanbaomatt/Lab5/AES_Project
   ```
3. Biên dịch chương trình:
   ```sh
   g++ main.cpp -o main.exe
   ```

## Cách sử dụng
1. Chạy chương trình:
   ```sh
   ./main.exe
   ```
2. Nhập thông điệp bất kỳ khi được yêu cầu, nhấn Enter.
3. Chương trình sẽ mã hóa và tạo file `output.aes` trong cùng thư mục.
4. Mã hóa dạng hex sẽ được in ra màn hình.

## Sau khi chạy
- File `output.aes` chứa dữ liệu đã mã hóa (dạng nhị phân).
- Để giải mã, bạn cần viết thêm hàm giải mã tương ứng (chưa có trong project này).

## Ví dụ sử dụng

### 1. Mã hóa thông điệp
Giả sử bạn chạy chương trình và nhập thông điệp:
```
Nhap thong diep: antoanthongtin
```
Chương trình sẽ xuất ra:
```
Ciphertext (hex): 7e2a... (dãy hex dài)
```
Và tạo file `output.aes` chứa dữ liệu mã hóa.

### 2. Kiểm tra file mã hóa
Bạn có thể mở file `output.aes` bằng phần mềm hex editor để xem dữ liệu đã bị mã hóa (không đọc được nội dung gốc).

### 3. Giải mã (nếu có)
Nếu có chương trình giải mã, bạn sẽ lấy lại được thông điệp gốc từ file `output.aes`.

## Lưu ý
- Nếu gặp lỗi về thư viện trong VS Code, hãy cập nhật `includePath` trong `.vscode/c_cpp_properties.json` như hướng dẫn ở trên.
- Chương trình này chỉ mã hóa, không giải mã.

----
**Mọi thắc mắc hoặc cần bổ sung chức năng giải mã, vui lòng liên hệ lại!**
