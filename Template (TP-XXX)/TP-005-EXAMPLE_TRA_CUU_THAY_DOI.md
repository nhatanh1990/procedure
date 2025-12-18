# Ví dụ Tra Cứu Thay Đổi - Deploy tính năng mới

## THÔNG TIN CHUNG

- **Ngày tra cứu**: 2024-12-15
- **Người tra cứu**: Nguyễn Văn A
- **Email**: nguyen.van.a@company.com
- **Phòng ban**: Development Team

---

## MÔ TẢ THAY ĐỔI

### Mô tả thay đổi
Cần deploy tính năng Two-Factor Authentication (2FA) cho User Service lên Production. Tính năng này đã được phát triển và test trên UAT/Staging, giờ cần triển khai lên Production.

### Mục đích
Tăng cường bảo mật tài khoản người dùng bằng cách thêm xác thực 2 lớp. Người dùng có thể bật/tắt tính năng này trong cài đặt tài khoản.

### Hệ thống ảnh hưởng
- [x] Production
- [ ] DR
- [ ] UAT
- [ ] Staging

---

## TRA CỨU TRONG DANH SÁCH CHUẨN

### Bước 1: Xác định nhóm

- [ ] **Nhóm A**: Hạ tầng (Infrastructure)
- [x] **Nhóm B**: Ứng dụng (Application)
- [ ] **Nhóm C**: Dữ liệu & Cấu hình (Data & Configuration)
- [ ] **Nhóm D**: Xử lý sự cố (Incident Management)

**Nhóm đã chọn**: B

**Lý do**: Đây là thay đổi về ứng dụng (deploy tính năng mới), không phải thay đổi hạ tầng, dữ liệu hay xử lý sự cố.

### Bước 2: Tra cứu mã thay đổi

**Đã tra cứu trong**: `QT-008-DANH_SACH_THAY_DOI_CHUAN.md`

**Kết quả tra cứu**:
- [x] **Tìm thấy**: Mã thay đổi: B2.1
- [ ] **Không tìm thấy**: Chuyển sang xử lý ngoại lệ

**Chi tiết tra cứu**:
- Đã tìm trong Nhóm B - Thay đổi Ứng dụng
- Tìm thấy mã **B2.1**: "Deploy tính năng mới lên Production"
- Mô tả phù hợp với thay đổi cần thực hiện

### Bước 3: Thông tin thay đổi (nếu tìm thấy)

| Thông tin | Giá trị |
|-----------|---------|
| **Mã thay đổi** | B2.1 |
| **Tên thay đổi** | Deploy tính năng mới lên Production |
| **Mức độ rủi ro** | Thấp |
| **Loại thay đổi** | Chuẩn |
| **Cấp độ duyệt** | PM/PDM dự án |
| **Điểm** | 2 |

**Thông tin bổ sung từ QT-008**:
- Đây là Standard Change (Chuẩn)
- Không cần CAB phê duyệt mỗi lần (đã được ủy quyền trước)
- Cần phê duyệt bởi PM/PDM dự án
- Điểm rủi ro thấp (2 điểm)

---

## XỬ LÝ NGOẠI LỆ (nếu không tìm thấy)

**Không áp dụng** - Đã tìm thấy mã thay đổi phù hợp.

---

## XÁC ĐỊNH QUY TRÌNH

### Loại thay đổi

- [x] **Chuẩn (Standard Change)**
 - Quy trình: Đã ủy quyền trước, không cần CAB mỗi lần
 - Tham chiếu: `QT-003-UPCODE.md` - Phần 3.1

- [ ] **Thông thường (Normal Change)**
 - Quy trình: Cần CAB phê duyệt
 - Tham chiếu: `QT-003-UPCODE.md` - Phần 3.2

- [ ] **Khẩn (Emergency Change)**
 - Quy trình: ECAB hoặc Lãnh đạo, có thể phê duyệt sau
 - Tham chiếu: `QT-004-HOTFIX.md`

**Lý do**: Mã B2.1 là Standard Change, đã được ủy quyền trước. Tính năng đã được test kỹ trên UAT/Staging, không có breaking changes.

### Cấp độ phê duyệt

- [x] **Level 1.0**: PM/PDM
- [ ] **Level 2.0**: Ban CLGSP hoặc Lãnh đạo TT
- [ ] **Level 3.0**: Ban CLGSP + Ban KTHT
- [ ] **Level 4.0**: Lãnh đạo Công ty

**Cấp độ đã xác định**: Level 1.0

**Lý do**: Theo QT-008, mã B2.1 có cấp độ duyệt là PM/PDM dự án (Level 1.0).

---

## KẾT QUẢ TRA CỨU

### Tóm tắt

- **Mã thay đổi**: B2.1
- **Tên thay đổi**: Deploy tính năng mới lên Production
- **Loại thay đổi**: Chuẩn (Standard Change)
- **Cấp độ phê duyệt**: Level 1.0 (PM/PDM)
- **Quy trình áp dụng**: QT-003 (Upcode) - Phần 3.1 (Standard Change)
- **Mức độ rủi ro**: Thấp (2 điểm)

### Checklist theo quy trình

**Tham chiếu**: `CL-002-CHECKLIST_UPCODE.md` và `CL-008-CHECKLIST_NHOM_B_UNG_DUNG.md`

**Các bước cần thực hiện**:
1. [x] Tra cứu mã thay đổi (Đã hoàn thành - B2.1)
2. [ ] Tạo RFC (Sử dụng TP-001-TEMPLATE_RFC.md)
3. [ ] Gửi phê duyệt cho PM/PDM (Level 1.0)
4. [ ] Chuẩn bị deployment (code, config, tests)
5. [ ] Thực hiện deployment theo quy trình Standard Change
6. [ ] Verify deployment
7. [ ] Ghi nhận kết quả

### Bước tiếp theo

1. [x] Tra cứu mã thay đổi - **Đã hoàn thành**
2. [ ] Tạo RFC - Sử dụng `TP-001-TEMPLATE_RFC.md`
 - Điền mã thay đổi: B2.1
 - Điền nhóm: B - Ứng dụng
 - Điền loại thay đổi: Standard Change
 - Điền cấp độ phê duyệt: Level 1.0
3. [ ] Gửi phê duyệt cho PM/PDM dự án
4. [ ] Thực hiện theo quy trình Standard Change trong QT-003

---

## GHI CHÚ

- Tính năng 2FA đã được test kỹ trên UAT/Staging
- Không có breaking changes
- Có feature flag để có thể tắt nhanh nếu cần
- Đã có rollback plan
- Cần phê duyệt từ PM/PDM trước khi triển khai

**Tham khảo thêm**:
- Issue: #123 (GitHub)
- PR: #456 (GitHub)
- UAT Test Report: [Link]

---

## VÍ DỤ TRA CỨU KHÁC - Không tìm thấy mã

### Tình huống: Thay đổi không có trong danh sách chuẩn

**Mô tả thay đổi**: Cần tích hợp với một API bên thứ ba mới (chưa từng tích hợp trước đây)

**Kết quả tra cứu**:
- [ ] **Tìm thấy**: Mã thay đổi: [Không có]
- [x] **Không tìm thấy**: Chuyển sang xử lý ngoại lệ

### Xử lý ngoại lệ

**Đánh giá rủi ro**:
- **Likelihood**: 2 - Trung bình (API bên thứ ba có thể không ổn định)
- **Impact**: 2 - Trung bình (Ảnh hưởng đến một phần dịch vụ)
- **Điểm rủi ro**: 2 × 2 = 4
- **Mức độ rủi ro**: Trung bình (4-8)

**Phân loại tạm thời**:
- [x] Phân vào loại gần nhất: B2.2 (Tích hợp với hệ thống bên ngoài)
- [ ] Phân vào loại "Thay đổi thông thường"

**Đề xuất bổ sung**:
- [x] Có đề xuất bổ sung vào danh sách chuẩn
- [ ] Không đề xuất bổ sung

**Lý do**: Đây là loại thay đổi có thể lặp lại trong tương lai, nên bổ sung vào danh sách chuẩn để dễ quản lý.

**Đề xuất mã mới**: B2.5 - Tích hợp API bên thứ ba mới

**Bước tiếp theo**: 
1. Sử dụng quy trình QT-009 để đề xuất bổ sung mã mới
2. Trong khi chờ phê duyệt, sử dụng mã B2.2 tạm thời

---

**Tham chiếu**:
- `QT-008-DANH_SACH_THAY_DOI_CHUAN.md`: Danh sách thay đổi chuẩn
- `QT-003-UPCODE.md`: Quy trình Upcode
- `QT-004-HOTFIX.md`: Quy trình Hotfix
- `QT-009-QUY_TRINH_BO_SUNG_THAY_DOI.md`: Quy trình bổ sung thay đổi mới
- `CL-006-TRA_CUU_THAY_DOI.md`: Checklist tra cứu
- `QUICK_REFERENCE_THAY_DOI.md`: Bảng tra cứu nhanh

---

**Phiên bản**: 1.0

