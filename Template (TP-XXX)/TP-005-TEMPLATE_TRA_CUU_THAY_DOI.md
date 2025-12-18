# TP-005: TEMPLATE TRA CỨU THAY ĐỔI

**Mã template**: TP-005 
**Tham chiếu**: `QT-008-DANH_SACH_THAY_DOI_CHUAN.md`

---

## THÔNG TIN CHUNG

- **Ngày tra cứu**: [YYYY-MM-DD]
- **Người tra cứu**: [Tên]
- **Email**: [Email]
- **Phòng ban**: [Phòng ban]

---

## MÔ TẢ THAY ĐỔI

### Mô tả thay đổi
[Mô tả chi tiết thay đổi cần thực hiện]

### Mục đích
[Mục đích của thay đổi]

### Hệ thống ảnh hưởng
- [ ] Production
- [ ] DR
- [ ] UAT
- [ ] Staging

---

## TRA CỨU TRONG DANH SÁCH CHUẨN

### Bước 1: Xác định nhóm

- [ ] **Nhóm A**: Hạ tầng (Infrastructure)
- [ ] **Nhóm B**: Ứng dụng (Application)
- [ ] **Nhóm C**: Dữ liệu & Cấu hình (Data & Configuration)
- [ ] **Nhóm D**: Xử lý sự cố (Incident Management)

**Nhóm đã chọn**: [A/B/C/D]

### Bước 2: Tra cứu mã thay đổi

**Đã tra cứu trong**: `QT-008-DANH_SACH_THAY_DOI_CHUAN.md`

**Kết quả tra cứu**:
- [ ] **Tìm thấy**: Mã thay đổi: [Mã, ví dụ: A1.1, B2.1, ...]
- [ ] **Không tìm thấy**: Chuyển sang xử lý ngoại lệ

### Bước 3: Thông tin thay đổi (nếu tìm thấy)

| Thông tin | Giá trị |
|-----------|---------|
| **Mã thay đổi** | [Mã] |
| **Tên thay đổi** | [Tên] |
| **Mức độ rủi ro** | [Thấp/Trung bình/Cao/Nghiêm trọng] |
| **Loại thay đổi** | [Chuẩn/Thông thường/Khẩn] |
| **Cấp độ duyệt** | [PM/PDM/Ban CLGSP/Lãnh đạo] |
| **Điểm** | [Điểm] |

---

## XỬ LÝ NGOẠI LỆ (nếu không tìm thấy)

### Đánh giá rủi ro

**Likelihood (Khả năng xảy ra)**:
- [ ] 1 - Thấp
- [ ] 2 - Trung bình
- [ ] 3 - Cao
- [ ] 4 - Rất cao

**Impact (Tác động)**:
- [ ] 1 - Thấp
- [ ] 2 - Trung bình
- [ ] 3 - Cao
- [ ] 4 - Nghiêm trọng

**Điểm rủi ro**: [Likelihood × Impact = X]

**Mức độ rủi ro**:
- [ ] Thấp (1-3)
- [ ] Trung bình (4-8)
- [ ] Cao (9-12)
- [ ] Nghiêm trọng (13-16)

### Phân loại tạm thời

- [ ] Phân vào loại gần nhất: [Mã loại gần nhất]
- [ ] Phân vào loại "Thay đổi thông thường"

### Đề xuất bổ sung

- [ ] Có đề xuất bổ sung vào danh sách chuẩn
- [ ] Không đề xuất bổ sung

**Lý do**: [Lý do nếu có đề xuất]

---

## XÁC ĐỊNH QUY TRÌNH

### Loại thay đổi

- [ ] **Chuẩn (Standard Change)**
 - Quy trình: Đã ủy quyền trước, không cần CAB mỗi lần
 - Tham chiếu: `QT-003-UPCODE.md` - Phần 3.1

- [ ] **Thông thường (Normal Change)**
 - Quy trình: Cần CAB phê duyệt
 - Tham chiếu: `QT-003-UPCODE.md` - Phần 3.2

- [ ] **Khẩn (Emergency Change)**
 - Quy trình: ECAB hoặc Lãnh đạo, có thể phê duyệt sau
 - Tham chiếu: `QT-004-HOTFIX.md`

### Cấp độ phê duyệt

- [ ] **Level 1.0**: PM/PDM
- [ ] **Level 2.0**: Ban CLGSP hoặc Lãnh đạo TT
- [ ] **Level 3.0**: Ban CLGSP + Ban KTHT
- [ ] **Level 4.0**: Lãnh đạo Công ty

**Cấp độ đã xác định**: [Level]

---

## KẾT QUẢ TRA CỨU

### Tóm tắt

- **Mã thay đổi**: [Mã hoặc "Ngoại lệ"]
- **Loại thay đổi**: [Chuẩn/Thông thường/Khẩn]
- **Cấp độ phê duyệt**: [Level]
- **Quy trình áp dụng**: [QT-003/QT-004]

### Bước tiếp theo

1. [ ] Tạo RFC (nếu cần) - Sử dụng `TP-001-TEMPLATE_RFC.md`
2. [ ] Gửi phê duyệt theo cấp độ
3. [ ] Thực hiện theo quy trình đã xác định

---

## GHI CHÚ

[Ghi chú khác nếu có]

---

**Tham chiếu**:
- `QT-008-DANH_SACH_THAY_DOI_CHUAN.md`: Danh sách thay đổi chuẩn
- `QT-003-UPCODE.md`: Quy trình Upcode
- `QT-004-HOTFIX.md`: Quy trình Hotfix
- `CL-006-TRA_CUU_THAY_DOI.md`: Checklist tra cứu
- `QUICK_REFERENCE_THAY_DOI.md`: Bảng tra cứu nhanh

---

**Phiên bản**: 1.0

