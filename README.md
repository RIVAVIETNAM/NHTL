# Digital Portfolio - Nguyễn Hoàng Tùng Lâm

## 📋 Mô tả

Digital Portfolio (Hồ sơ kỹ thuật số) cho chương trình PhD của **Nguyễn Hoàng Tùng Lâm**. Portfolio này trình bày các thành tựu, dự án, nghiên cứu và tài liệu học thuật với hệ thống trích dẫn nguồn theo chuẩn IEEE.

## 🎯 Mục đích

Portfolio này được thiết kế để:
- Trình bày các dự án đạt huy chương vàng tại SVIIF (Silicon Valley International Invention Festival)
- Giới thiệu các công trình nghiên cứu và xuất bản
- Hiển thị các thư giới thiệu từ các giáo sư và chuyên gia
- Cung cấp Statement of Purpose cho các trường đại học
- Trích dẫn đầy đủ nguồn tài liệu theo chuẩn IEEE

## 🚀 Cách chạy Portfolio Local

### Phương pháp 1: Mở trực tiếp (Đơn giản nhất)

1. **Tìm file `index.html`** trong thư mục:
   ```
   D:\OneDrive\2026\PROFILE NGUYỄN HOÀNG TÙNG LÂM\index.html
   ```

2. **Double-click** vào file `index.html` hoặc **Right-click** → **Open with** → Chọn trình duyệt (Chrome, Edge, Firefox...)

3. Portfolio sẽ mở trực tiếp trong trình duyệt!

### Phương pháp 2: Sử dụng Local Server (Khuyến nghị)

#### Với Python (nếu đã cài đặt):

1. Mở **Command Prompt** hoặc **PowerShell**
2. Di chuyển đến thư mục:
   ```bash
   cd "D:\OneDrive\2026\PROFILE NGUYỄN HOÀNG TÙNG LÂM"
   ```

3. Chạy lệnh:
   ```bash
   # Python 3
   python -m http.server 8000
   
   # Hoặc Python 2
   python -m SimpleHTTPServer 8000
   ```

4. Mở trình duyệt và truy cập:
   ```
   http://localhost:8000
   ```

#### Với Node.js (nếu đã cài đặt):

1. Cài đặt `http-server` (chỉ cần 1 lần):
   ```bash
   npm install -g http-server
   ```

2. Di chuyển đến thư mục và chạy:
   ```bash
   cd "D:\OneDrive\2026\PROFILE NGUYỄN HOÀNG TÙNG LÂM"
   http-server -p 8000
   ```

3. Mở trình duyệt: `http://localhost:8000`

#### Với VS Code (Nếu dùng VS Code):

1. Cài đặt extension **Live Server**
2. Right-click vào file `index.html`
3. Chọn **Open with Live Server**

## 📁 Cấu trúc File

```
PROFILE NGUYỄN HOÀNG TÙNG LÂM/
├── index.html          # File chính của portfolio
├── styles.css          # File CSS cho styling
├── script.js           # File JavaScript cho tương tác
├── README.md           # File hướng dẫn này
│
├── POSTER HƯỚNG DẪN HỌC SINH/
│   ├── POSTER VN1.pdf
│   ├── POSTER VN3.pdf
│   └── POSTER VN3 (1).pdf
│
├── SOP/                # Statement of Purpose
├── LOR/                # Letters of Recommendation
├── RESUME/             # Resume
├── WRITING SAMPLE/     # Writing samples
├── ESSAY/              # Essays
└── ... (các file khác)
```

## ✨ Tính năng

- ✅ **Responsive Design**: Tự động điều chỉnh trên mọi thiết bị
- ✅ **Smooth Scrolling**: Cuộn mượt mà giữa các section
- ✅ **Animations**: Hiệu ứng fade-in khi scroll
- ✅ **IEEE Citations**: Hệ thống trích dẫn nguồn đầy đủ
- ✅ **Mobile Menu**: Menu hamburger cho mobile
- ✅ **Direct Links**: Liên kết trực tiếp đến tất cả tài liệu

## 📝 Các Section trong Portfolio

1. **Trang chủ (Hero)**: Giới thiệu tổng quan
2. **Giới thiệu (About)**: Thông tin về bản thân
3. **Dự án (Projects)**: 3 dự án SVIIF đạt huy chương vàng
4. **Giải thưởng (Awards)**: SVIIF Invitation và các công nhận
5. **Nghiên cứu (Research)**: Bài báo, báo cáo học thuật
6. **Xuất bản (Publications)**: Sách và tài liệu đã xuất bản
7. **Thư giới thiệu (Recommendations)**: 4 LOR từ các giáo sư
8. **Ứng tuyển PhD (Applications)**: SOP cho các trường đại học
9. **Bài luận (Essays)**: Các bài luận học thuật
10. **Học vấn (Education)**: Bảng điểm, chứng chỉ
11. **Tài liệu tham khảo (References)**: Danh sách trích dẫn IEEE
12. **Liên hệ (Contact)**: Thông tin và tài liệu

## 🔗 Liên kết tài liệu

Tất cả các liên kết trong portfolio đều trỏ đến các file PDF, DOCX, JPG trong thư mục. Đảm bảo:
- Các file tài liệu nằm đúng vị trí như trong cấu trúc
- Đường dẫn file không bị thay đổi
- File PDF có thể mở được

## 📌 Lưu ý

- Portfolio này **chạy hoàn toàn local**, không cần internet (trừ font Google Fonts)
- Tất cả nội dung được **trích dẫn đầy đủ** với ghi chú nguồn
- Có thể **tùy chỉnh** nội dung trong file `index.html`
- Styling có thể chỉnh sửa trong file `styles.css`
- Tương tác có thể thêm vào file `script.js`

## 🌐 Deploy lên Web (Tùy chọn)

Nếu muốn đưa portfolio lên web, có thể sử dụng:
- **GitHub Pages**: Miễn phí, dễ sử dụng
- **Netlify**: Deploy tự động từ Git
- **Vercel**: Tốc độ nhanh, miễn phí
- **Firebase Hosting**: Từ Google

## 📧 Hỗ trợ

Nếu có vấn đề khi chạy portfolio, kiểm tra:
1. File `index.html`, `styles.css`, `script.js` có trong cùng thư mục
2. Đường dẫn file PDF/DOCX đúng
3. Trình duyệt hỗ trợ HTML5/CSS3/ES6

---

**Tác giả**: Nguyễn Hoàng Tùng Lâm  
**Mục đích**: Digital Portfolio cho ứng tuyển chương trình PhD  
**Năm**: 2025

