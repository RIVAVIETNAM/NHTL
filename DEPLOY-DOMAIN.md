# Hướng dẫn Deploy Portfolio Lên Tên Miền Riêng

## 🌐 Có thể đẩy từ web local lên tên miền riêng không?

**CÓ!** Bạn hoàn toàn có thể đẩy portfolio từ máy local lên tên miền riêng để mọi người xem online.

---

## 📋 Các bước thực hiện

### Bước 1: Mua Hosting (Nơi lưu trữ website)

Bạn cần mua hosting để lưu trữ các file website. Các nhà cung cấp phổ biến tại Việt Nam:

#### Nhà cung cấp Hosting Việt Nam:
1. **Hostinger** - https://www.hostinger.vn
   - Giá: ~50,000-100,000 VNĐ/tháng
   - Hỗ trợ tiếng Việt
   - Dễ sử dụng

2. **Tenten** - https://tenten.vn
   - Giá: ~100,000-200,000 VNĐ/tháng
   - Phổ biến tại Việt Nam

3. **Matbao** - https://www.matbao.net
   - Giá: ~80,000-150,000 VNĐ/tháng
   - Uy tín lâu năm

4. **P.A Vietnam** - https://www.pavietnam.vn
   - Giá: ~100,000-200,000 VNĐ/tháng

#### Nhà cung cấp Quốc tế:
1. **Namecheap** - https://www.namecheap.com
   - Giá: ~$3-5/tháng
   - Tốt, giá rẻ

2. **Bluehost** - https://www.bluehost.com
   - Giá: ~$3-5/tháng
   - Phổ biến

3. **SiteGround** - https://www.siteground.com
   - Giá: ~$4-6/tháng
   - Tốc độ cao

---

### Bước 2: Mua Tên Miền (Domain)

Nếu chưa có tên miền, bạn cần mua:

#### Nơi mua tên miền:
- **Tenten.vn** - https://tenten.vn
- **Matbao.net** - https://www.matbao.net
- **Namecheap.com** - https://www.namecheap.com
- **GoDaddy** - https://www.godaddy.com

#### Gợi ý tên miền:
- `nguyenhoangtunglam.com`
- `tunglam-portfolio.com`
- `nhtl-portfolio.com`
- `tunglam-education.com`

**Lưu ý**: Nhiều nhà cung cấp có gói **Hosting + Domain** combo, tiết kiệm hơn!

---

### Bước 3: Kết nối Domain với Hosting

Sau khi có cả hosting và domain:

1. **Lấy thông tin DNS từ hosting**:
   - Vào cPanel/Quản lý hosting
   - Tìm phần "DNS" hoặc "Nameservers"
   - Copy 2 nameservers (ví dụ: `ns1.hostinger.com`, `ns2.hostinger.com`)

2. **Cập nhật DNS cho domain**:
   - Vào trang quản lý domain
   - Tìm phần "DNS Settings" hoặc "Nameservers"
   - Thay đổi nameservers thành nameservers của hosting
   - Đợi 24-48 giờ để DNS cập nhật

**Hoặc** nếu mua cùng nhà cung cấp, họ sẽ tự động kết nối!

---

### Bước 4: Upload Files Lên Hosting

Có 3 cách chính:

#### Cách 1: Sử dụng File Manager (cPanel) - Dễ nhất

1. Đăng nhập vào **cPanel** của hosting
2. Tìm và click **"File Manager"**
3. Vào thư mục `public_html` (hoặc `www`, `htdocs`)
4. Upload các file từ thư mục `Digital Portfolio`:
   - `index.html`
   - `styles.css`
   - `script.js`
   - `ẢNH NHTL.jpg`
   - `README.md` (tùy chọn)
5. **Lưu ý**: Đảm bảo `index.html` nằm ở thư mục gốc `public_html`

#### Cách 2: Sử dụng FTP (FileZilla) - Nhanh hơn

1. **Cài đặt FileZilla**: https://filezilla-project.org
2. Lấy thông tin FTP từ hosting:
   - FTP Host: `ftp.yourdomain.com` hoặc IP
   - FTP Username: (từ hosting)
   - FTP Password: (từ hosting)
   - Port: 21
3. Kết nối FileZilla với thông tin trên
4. Kéo thả các file từ `Digital Portfolio` vào thư mục `public_html`

#### Cách 3: Sử dụng Git (Nâng cao)

1. Cài đặt Git trên máy
2. Khởi tạo repository:
   ```bash
   cd "Digital Portfolio"
   git init
   git add .
   git commit -m "Initial commit"
   ```
3. Push lên hosting (nếu hosting hỗ trợ Git)

---

### Bước 5: Cấu hình Website

1. **Kiểm tra file index.html**:
   - Đảm bảo `index.html` ở thư mục gốc
   - Kiểm tra tất cả đường dẫn file đúng

2. **Cập nhật đường dẫn** (nếu cần):
   - Nếu các file PDF ở thư mục khác, cần cập nhật đường dẫn trong `index.html`
   - Hoặc upload các file PDF lên Google Drive và dùng link công khai

3. **Kiểm tra quyền truy cập file**:
   - Đảm bảo file có quyền đọc (644)

---

### Bước 6: Kiểm tra Website

1. Mở trình duyệt
2. Truy cập: `http://yourdomain.com` hoặc `https://yourdomain.com`
3. Kiểm tra:
   - Website hiển thị đúng
   - Tất cả link hoạt động
   - Ảnh hiển thị
   - CSS/JS load đúng

---

## 🔒 Bật SSL (HTTPS) - Quan trọng!

SSL giúp website an toàn và chuyên nghiệp hơn:

1. **Let's Encrypt (Miễn phí)**:
   - Vào cPanel → **"SSL/TLS"**
   - Click **"Let's Encrypt"**
   - Chọn domain và cài đặt
   - Tự động gia hạn miễn phí

2. **Hoặc dùng Cloudflare** (Miễn phí):
   - Đăng ký: https://www.cloudflare.com
   - Thêm domain
   - Cloudflare tự động cung cấp SSL

---

## 📁 Cấu trúc File Trên Hosting

```
public_html/
├── index.html          ← File chính
├── styles.css          ← CSS
├── script.js           ← JavaScript
├── ẢNH NHTL.jpg        ← Ảnh profile
└── assets/             ← (Tùy chọn) Thư mục cho file khác
    └── documents/      ← Các file PDF nếu cần
```

---

## ⚠️ Lưu ý Quan Trọng

### Về File PDF/DOCX:
- **Không nên** upload trực tiếp lên hosting (tốn dung lượng, chậm)
- **Nên** upload lên Google Drive/Dropbox và dùng link công khai
- Hoặc dùng dịch vụ lưu trữ file riêng

### Cách thay thế link PDF:
1. Upload PDF lên Google Drive
2. Click chuột phải → **"Get link"** → **"Anyone with the link"**
3. Copy link và cập nhật trong `index.html`:
   ```html
   <a href="https://drive.google.com/file/d/[FILE_ID]/view?usp=sharing" target="_blank">
   ```

### Tối ưu hóa:
- Nén ảnh trước khi upload (dùng TinyPNG)
- Kiểm tra kích thước file (không quá 5MB/file)
- Sử dụng CDN nếu có nhiều người truy cập

---

## 💰 Chi phí ước tính

- **Hosting**: 50,000 - 200,000 VNĐ/tháng
- **Domain**: 200,000 - 500,000 VNĐ/năm
- **Tổng**: ~300,000 - 700,000 VNĐ/năm đầu

**Hoặc** dùng gói combo: Hosting + Domain = ~500,000 - 1,000,000 VNĐ/năm

---

## 🆚 So sánh: Hosting vs GitHub Pages/Netlify

| Tính năng | Hosting (Tên miền riêng) | GitHub Pages/Netlify |
|-----------|-------------------------|---------------------|
| **Tên miền** | Tên miền riêng (.com) | Subdomain (.github.io) |
| **Chi phí** | ~500k-1tr/năm | Miễn phí |
| **Độ chuyên nghiệp** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Tốc độ** | Tùy hosting | Rất nhanh (CDN) |
| **Dễ sử dụng** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Hỗ trợ** | Có (tiếng Việt) | Community |

**Kết luận**: 
- Nếu muốn **tên miền riêng chuyên nghiệp** → Dùng Hosting
- Nếu muốn **miễn phí và đơn giản** → Dùng GitHub Pages/Netlify

---

## ✅ Checklist Trước Khi Deploy

- [ ] Đã mua hosting
- [ ] Đã mua domain (hoặc dùng subdomain)
- [ ] Đã kết nối domain với hosting
- [ ] Đã upload tất cả file lên hosting
- [ ] Đã kiểm tra đường dẫn file đúng
- [ ] Đã bật SSL (HTTPS)
- [ ] Đã test website trên mobile
- [ ] Đã test tất cả link hoạt động
- [ ] Đã tối ưu ảnh (nén file)

---

## 🆘 Hỗ trợ

Nếu gặp vấn đề:
1. Liên hệ support của nhà cung cấp hosting
2. Kiểm tra file `.htaccess` (nếu cần)
3. Kiểm tra quyền truy cập file (644 cho file, 755 cho thư mục)

---

**Chúc bạn deploy thành công! 🚀**

