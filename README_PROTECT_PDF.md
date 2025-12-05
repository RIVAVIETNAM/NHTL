# Hướng dẫn bảo vệ file PDF bằng mật khẩu

## Yêu cầu
- Python 3.7 trở lên
- Thư viện pypdf

## Cài đặt

1. Cài đặt Python (nếu chưa có):
   - Tải từ: https://www.python.org/downloads/
   - Đảm bảo chọn "Add Python to PATH" khi cài đặt

2. Cài đặt thư viện pypdf:
   ```bash
   pip install pypdf
   ```
   
   Hoặc sử dụng file requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

## Sử dụng

1. Mở Terminal/Command Prompt
2. Di chuyển đến thư mục NHTL:
   ```bash
   cd "D:\OneDrive\2026\PROFILE NGUYỄN HOÀNG TÙNG LÂM\NHTL"
   ```

3. Chạy script:
   ```bash
   python protect_pdfs.py
   ```

4. Script sẽ:
   - Tìm tất cả các file PDF trong thư mục và các thư mục con
   - Hiển thị danh sách các file sẽ được bảo vệ
   - Yêu cầu xác nhận (gõ "yes" để tiếp tục)
   - Đặt mật khẩu cho tất cả các file PDF
   - Tạo backup tự động trước khi thay đổi (sẽ xóa sau khi thành công)

## Cấu hình mật khẩu

**QUAN TRỌNG**: Mật khẩu không được lưu trong code để bảo mật. Bạn cần cấu hình mật khẩu bằng một trong các cách sau:

### Cách 1: Sử dụng biến môi trường (khuyến nghị)
```bash
# Windows PowerShell
$env:PDF_PASSWORD="your_password_here"
python protect_pdfs.py

# Windows CMD
set PDF_PASSWORD=your_password_here
python protect_pdfs.py

# Linux/Mac
export PDF_PASSWORD="your_password_here"
python protect_pdfs.py
```

### Cách 2: Tạo file pdf_password.txt (local, không commit)
Tạo file `pdf_password.txt` trong thư mục NHTL và ghi mật khẩu vào đó (chỉ một dòng, không có khoảng trắng thừa).

## Lưu ý

- **Bảo mật**: Mật khẩu không được lưu trong code hoặc commit lên git
- Script sẽ thay thế file gốc bằng file đã được bảo vệ
- Backup tự động được tạo trong quá trình xử lý
- Sau khi chạy xong, người dùng cần nhập mật khẩu để mở các file PDF

## Khôi phục (nếu cần)

Nếu có lỗi xảy ra, script sẽ tự động khôi phục từ backup. Nếu cần khôi phục thủ công, tìm các file có đuôi `.backup` và đổi tên lại.

