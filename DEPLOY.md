# Hướng dẫn Deploy Portfolio Lên Web

> **💡 Có tên miền riêng?** Xem file `DEPLOY-DOMAIN.md` để hướng dẫn deploy lên hosting với tên miền riêng!

## 🚀 Các cách để người khác xem portfolio online

### Phương pháp 1: GitHub Pages (Miễn phí, Dễ nhất)

#### Bước 1: Tạo tài khoản GitHub
1. Truy cập: https://github.com
2. Đăng ký tài khoản miễn phí

#### Bước 2: Tạo Repository mới
1. Click nút **"New"** hoặc **"+"** → **"New repository"**
2. Đặt tên: `digital-portfolio` (hoặc tên bạn muốn)
3. Chọn **Public** (để miễn phí)
4. **KHÔNG** tích vào "Initialize with README"
5. Click **"Create repository"**

#### Bước 3: Upload files lên GitHub
1. Trong repository mới, click **"uploading an existing file"**
2. Kéo thả các file từ thư mục `Digital Portfolio`:
   - `index.html`
   - `styles.css`
   - `script.js`
   - `ẢNH NHTL.jpg`
   - `README.md` (tùy chọn)
3. Click **"Commit changes"**

#### Bước 4: Bật GitHub Pages
1. Vào **Settings** (cài đặt) của repository
2. Scroll xuống phần **"Pages"** ở sidebar trái
3. Trong **"Source"**, chọn **"main"** branch
4. Click **"Save"**
5. Đợi vài phút, GitHub sẽ cung cấp link: `https://[username].github.io/digital-portfolio`

**Lưu ý**: Các file PDF/DOCX trong `THÔNG TIN XỬ LÝ` cần upload riêng hoặc dùng GitHub LFS.

---

### Phương pháp 2: Netlify (Miễn phí, Tự động deploy)

#### Bước 1: Chuẩn bị
1. Tạo tài khoản tại: https://www.netlify.com
2. Có thể đăng nhập bằng GitHub

#### Bước 2: Deploy
1. Vào **"Sites"** → **"Add new site"** → **"Deploy manually"**
2. Kéo thả toàn bộ thư mục `Digital Portfolio` vào
3. Netlify sẽ tự động deploy và cung cấp link: `https://[random-name].netlify.app`

#### Bước 3: Đổi tên domain (tùy chọn)
1. Vào **"Site settings"** → **"Change site name"**
2. Đổi thành tên bạn muốn: `nguyen-hoang-tung-lam-portfolio`
3. Link mới: `https://nguyen-hoang-tung-lam-portfolio.netlify.app`

**Ưu điểm**: Tự động deploy khi có thay đổi, SSL miễn phí

---

### Phương pháp 3: Vercel (Miễn phí, Nhanh)

#### Bước 1: Tạo tài khoản
1. Truy cập: https://vercel.com
2. Đăng nhập bằng GitHub

#### Bước 2: Deploy
1. Click **"Add New Project"**
2. Import từ GitHub hoặc upload thư mục `Digital Portfolio`
3. Click **"Deploy"**
4. Link: `https://[project-name].vercel.app`

---

### Phương pháp 4: Firebase Hosting (Google, Miễn phí)

#### Bước 1: Cài đặt Firebase CLI
```bash
npm install -g firebase-tools
```

#### Bước 2: Đăng nhập
```bash
firebase login
```

#### Bước 3: Khởi tạo project
```bash
cd "Digital Portfolio"
firebase init hosting
```

#### Bước 4: Deploy
```bash
firebase deploy
```

---

### Phương pháp 5: Surge.sh (Đơn giản nhất)

#### Bước 1: Cài đặt
```bash
npm install -g surge
```

#### Bước 2: Deploy
```bash
cd "Digital Portfolio"
surge
```
- Nhập email và password (tạo tài khoản mới)
- Chọn domain hoặc dùng domain tự động
- Link: `https://[your-name].surge.sh`

---

## 📝 Lưu ý quan trọng

### Về các file PDF/DOCX
Các file trong `THÔNG TIN XỬ LÝ` cần được upload riêng vì:
- GitHub Pages có giới hạn kích thước file
- Nên upload lên Google Drive hoặc Dropbox và dùng link công khai
- Hoặc dùng GitHub LFS (Large File Storage) nhưng có giới hạn

### Cách thay thế link PDF bằng Google Drive:
1. Upload file PDF lên Google Drive
2. Click chuột phải → **"Get link"** → Chọn **"Anyone with the link"**
3. Copy link và thay thế trong `index.html`:
   ```html
   <a href="https://drive.google.com/file/d/[FILE_ID]/view?usp=sharing" target="_blank">
   ```

### Tối ưu hóa
- Nén ảnh trước khi upload
- Sử dụng format WebP cho ảnh (nhỏ hơn JPG)
- Kiểm tra tất cả link hoạt động

---

## ✅ Khuyến nghị

**Cho người mới bắt đầu**: Dùng **Netlify** hoặc **Surge.sh** - đơn giản nhất

**Cho người có GitHub**: Dùng **GitHub Pages** - tích hợp tốt với Git

**Cho tốc độ cao**: Dùng **Vercel** - CDN toàn cầu

---

## 🔗 Sau khi deploy

Sau khi có link, bạn có thể:
- Chia sẻ link với hội đồng tuyển sinh
- Thêm vào CV/Resume
- Đăng lên LinkedIn
- Gửi trong email ứng tuyển

**Ví dụ link**: `https://nguyen-hoang-tung-lam.netlify.app`

