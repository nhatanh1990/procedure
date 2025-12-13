# QUICK REFERENCE: TRA CỨU NHANH THAY ĐỔI

**Tham chiếu chi tiết**: `QT-008-DANH_SACH_THAY_DOI_CHUAN.md`

---

## 📋 TRA CỨU THEO MÃ

| Mã | Tên thay đổi | Nhóm | Rủi ro | Loại | Cấp duyệt |
|----|--------------|------|--------|------|-----------|
| **A1.1** | Update windows (UAT/DR) | A | Thấp | Chuẩn | PM/PDM |
| **A1.2** | Update windows PROD, Linux | A | Thấp | Chuẩn | PM/PDM |
| **A1.3** | Nâng cấp hệ điều hành máy chủ | A | TB | Chuẩn | PM/PDM |
| **A1.4** | Nâng cấp version phần mềm nền tảng | A | Nghiêm trọng | TT | Lãnh đạo |
| **A2.1** | Dịch chuyển/Chuyển đổi hạ tầng | A | Nghiêm trọng | TT | Lãnh đạo |
| **A2.2** | Tách cụm (Cluster Splitting) | A | Nghiêm trọng | TT | Lãnh đạo |
| **A2.3** | Tách cụm để giảm tải DB và APP | A | Nghiêm trọng | Khẩn | Lãnh đạo |
| **A3.1** | Thay đổi cấu hình mạng | A | Cao | Chuẩn | Lãnh đạo |
| **A3.2** | Thay đổi CDN/load balancer | A | TB | Chuẩn | Lãnh đạo |
| **A3.3** | Block IP theo yêu cầu | A | Thấp | Chuẩn | PM/PDM |
| **A3.4** | Cập nhật phần mềm ATBM | A | Thấp | Chuẩn | PM/PDM |
| **A4.1** | Thay đổi hệ thống giám sát | A | Thấp | Chuẩn | DevOps |
| **A4.2** | Tăng dung lượng ổ cứng | A | Thấp | Chuẩn | PM/PDM |
| **A4.3** | Thay đổi tài nguyên (RAM, CPU) | A | Thấp | Chuẩn | PM/PDM |
| **A4.4** | Restart VM | A | Thấp | Chuẩn | PM/PDM |
| **A4.5** | Cài đặt/nâng cấp công cụ quản trị | A | TB | Chuẩn | Lãnh đạo |
| **A5.1** | Thay đổi cấu hình Domain | A | Thấp | Chuẩn | PM/PDM |
| **A5.2** | Thay đổi tham số cấu hình hệ thống | A | Thấp | Chuẩn | PM/PDM |
| **A5.3** | Thay đổi cấu hình backup | A | TB | Chuẩn | PM/PDM |
| **B1.1** | Sửa lỗi giao diện (UI/UX) | B | Thấp | Chuẩn | PM/PDM |
| **B1.2** | Cập nhật pop-up, FAQ | B | Thấp | Chuẩn | Lãnh đạo TT |
| **B1.3** | Cập nhật hướng dẫn sử dụng | B | Thấp | Chuẩn | Lãnh đạo TT |
| **B1.4** | Chỉnh sửa phiếu in, báo cáo | B | Thấp | Chuẩn | PM/PDM |
| **B1.5** | Tạo báo cáo/phiếu in đơn giản | B | Thấp | Chuẩn | PM/PDM |
| **B1.6** | Deploy báo cáo đặc thù | B | TB | Chuẩn | Lãnh đạo TT |
| **B2.1** | Thêm chức năng nhỏ (rủi ro thấp) | B | Thấp | Chuẩn | PM/PDM |
| **B2.2** | Thêm chức năng nhỏ (rủi ro TB) | B | TB | TT | Ban CLGSP |
| **B2.3** | Thêm module/chức năng mới | B | Thấp | Chuẩn | Lãnh đạo TT |
| **B2.4** | Tắt hoặc ẩn nút chức năng | B | TB | TT | Ban CLGSP |
| **B2.5** | Chỉnh sửa chức năng phần mềm | B | TB | Chuẩn | Lãnh đạo TT |
| **B2.6** | Thêm, sửa chức năng chung | B | TB | TT | Ban CLGSP |
| **B2.7** | Thêm giá trị vào danh mục | B | Thấp | Chuẩn | Lãnh đạo TT |
| **B2.8** | Chỉnh sửa rules hoặc validation | B | TB | TT | Ban CLGSP |
| **B2.9** | Thay đổi quy trình xác thực | B | Thấp | TT | PM/PDM |
| **B3.1** | Thay đổi thư viện (Lib) - Level 1.5 | B | TB | TT | Ban CLGSP |
| **B3.2** | Thay đổi thư viện (Lib) - Level 2 | B | TB | TT | Ban CLGSP |
| **B3.3** | Thay đổi phiên bản runtime | B | TB | TT | PM/PDM |
| **B3.4** | Tái cấu trúc code (Refactor) | B | TB | TT | Ban CLGSP |
| **B3.5** | Thay đổi logging/exception | B | Thấp | TT | PM/PDM |
| **B3.6** | Cập nhật license phần mềm | B | TB | TT | PM/PDM |
| **B3.7** | Thêm module mới hoặc plugin | B | Cao | Chuẩn | PM/PDM |
| **B3.8** | Thay đổi pipeline CI/CD | B | Cao | Chuẩn | Ban CLGSP |
| **B3.9** | Tích hợp hệ thống ngoài | B | Cao | TT | PM/PDM |
| **B3.10** | Tối ưu câu lệnh chậm (DB) | B | TB | Chuẩn | Lãnh đạo TT |
| **B4.1** | Sửa lỗi (bug fixing) | B | TB | Chuẩn | PM/PDM |
| **B4.2** | Code lỗi cần hotfix luôn | B | TB | Chuẩn | Lãnh đạo TT |
| **B4.3** | Xử lý lỗi ATBM (Rủi ro Thấp) | B | Thấp | Chuẩn | Lãnh đạo TT |
| **B4.4** | Xử lý lỗ hổng bảo mật nghiêm trọng | B | Cao | TT | Tùy quy mô |
| **B5.1** | Nâng cấp phiên bản sản phẩm | B | Cao | TT | Lãnh đạo |
| **C1.1** | Thay đổi cấu trúc CSDL | C | TB | Chuẩn | Ban CLGSP |
| **C2.1** | Cấu hình hệ thống chuẩn | C | TB | TT | Ban CLGSP |
| **C2.2** | Config cấu hình tự động | C | TB | TT | Ban CLGSP |
| **C2.3** | Thêm giá trị vào danh mục | C | Thấp | Chuẩn | Lãnh đạo TT |
| **C3.1** | Change liên quan tài khoản | C | Thấp | Chuẩn | PM/PDM |
| **C3.2** | Mở khóa tài khoản (sai MK) | C | Thấp | Chuẩn | Lãnh đạo TT |
| **C3.3** | Gán/Thu Hồi Quyền Truy Cập | C | Thấp | Chuẩn | Lãnh đạo TT |
| **D1.1** | Xử lý sự cố thông thường | D | Thấp | Chuẩn | Lãnh đạo TT |
| **D2.1** | Xử lý Sự cố Lớn (Major) | D | Cao | Khẩn | Ban CLGSP |
| **D2.2** | Xử lý sự cố lớn (APP) | D | TB | TT | Ban CLGSP |
| **D3.1** | Xử lý Sự cố Nghiêm trọng | D | Nghiêm trọng | Khẩn | Lãnh đạo |

**Chú thích**:
- **TB**: Trung bình
- **TT**: Thông thường
- **ATBM**: An toàn Bảo mật

---

## 🔍 TRA CỨU THEO NHÓM

### Nhóm A: Hạ tầng (19 loại)
**Mã**: A1.1 - A5.3

**Thường gặp**:
- A1.2: Update windows PROD, Linux
- A3.3: Block IP theo yêu cầu
- A4.4: Restart VM
- A5.2: Thay đổi tham số cấu hình hệ thống

### Nhóm B: Ứng dụng (28 loại)
**Mã**: B1.1 - B5.1

**Thường gặp**:
- B1.1: Sửa lỗi giao diện (UI/UX)
- B2.1: Thêm chức năng nhỏ (rủi ro thấp)
- B4.1: Sửa lỗi (bug fixing)
- B3.10: Tối ưu câu lệnh chậm (DB)

### Nhóm C: Dữ liệu & Cấu hình (7 loại)
**Mã**: C1.1 - C3.3

**Thường gặp**:
- C2.3: Thêm giá trị vào danh mục
- C3.1: Change liên quan tài khoản
- C3.3: Gán/Thu Hồi Quyền Truy Cập

### Nhóm D: Xử lý sự cố (4 loại)
**Mã**: D1.1 - D3.1

**Thường gặp**:
- D1.1: Xử lý sự cố thông thường
- D2.1: Xử lý Sự cố Lớn (Major)

---

## ⚠️ TRA CỨU THEO MỨC ĐỘ RỦI RO

### Rủi ro Thấp (25 loại)
**Cấp duyệt**: PM/PDM, Lãnh đạo TT

**Ví dụ**: A1.1, A1.2, B1.1, B2.1, C2.3, C3.1

### Rủi ro Trung bình (22 loại)
**Cấp duyệt**: PM/PDM, Ban CLGSP, Lãnh đạo TT

**Ví dụ**: A1.3, A3.2, B1.6, B2.2, C1.1

### Rủi ro Cao (7 loại)
**Cấp duyệt**: Ban CLGSP, Lãnh đạo Công ty

**Ví dụ**: A3.1, B3.7, B3.8, B4.4, D2.1

### Rủi ro Nghiêm trọng (4 loại)
**Cấp duyệt**: Lãnh đạo Công ty

**Ví dụ**: A1.4, A2.1, A2.2, A2.3, D3.1

---

## 🚨 TRA CỨU THEO LOẠI THAY ĐỔI

### Chuẩn (34 loại)
**Quy trình**: Đã ủy quyền trước, không cần CAB mỗi lần

**Ví dụ**: A1.1, A1.2, B1.1, B2.1, C2.3

### Thông thường (20 loại)
**Quy trình**: Cần CAB phê duyệt

**Ví dụ**: A1.4, A2.1, B2.2, B3.1, C2.1

### Khẩn (4 loại)
**Quy trình**: ECAB hoặc Lãnh đạo, có thể phê duyệt sau

**Ví dụ**: A2.3, D2.1, D3.1

---

## 📞 LIÊN HỆ

- **Xem chi tiết**: `QT-008-DANH_SACH_THAY_DOI_CHUAN.md`
- **Quy trình Upcode**: `QT-003-UPCODE.md`
- **Quy trình Hotfix**: `QT-004-HOTFIX.md`

---

**Phiên bản**: 1.0
**Cập nhật**: [Ngày hiện tại]

