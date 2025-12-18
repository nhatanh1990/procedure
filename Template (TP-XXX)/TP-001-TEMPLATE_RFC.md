# TP-001: TEMPLATE RFC (REQUEST FOR CHANGE)

**Mã template**: TP-001 
**Tham chiếu quy trình**: QT-003

---

## THÔNG TIN CHUNG

- **RFC ID**: [RFC-YYYYMMDD-XXX]
- **Ngày tạo**: [YYYY-MM-DD]
- **Người tạo**: [Tên]
- **Email**: [Email]
- **Điện thoại**: [SĐT]

---

## MÔ TẢ THAY ĐỔI

### Tra cứu trong danh sách chuẩn

**Tham chiếu**: `QT-008-DANH_SACH_THAY_DOI_CHUAN.md` hoặc `QUICK_REFERENCE_THAY_DOI.md`

- [ ] **Đã tra cứu**: Mã thay đổi: [Mã, ví dụ: A1.1, B2.1, C1.1, D1.1]
- [ ] **Không tìm thấy**: Chuyển sang xử lý ngoại lệ (xem QT-003 - Phần 8)

**Nhóm thay đổi**:
- [ ] A - Hạ tầng (Infrastructure)
- [ ] B - Ứng dụng (Application)
- [ ] C - Dữ liệu & Cấu hình (Data & Configuration)
- [ ] D - Xử lý sự cố (Incident Management)

### Tên thay đổi
[Tiêu đề ngắn gọn về thay đổi]

### Mô tả chi tiết
[Mô tả chi tiết về thay đổi, lý do thay đổi, mục tiêu]

### Loại thay đổi
- [ ] Standard Change (Chuẩn)
- [ ] Normal Change (Thông thường)
- [ ] Emergency Change (Khẩn)

### Hệ thống ảnh hưởng
- [ ] Production
- [ ] DR
- [ ] UAT
- [ ] Staging

### Danh sách hệ thống
[List các hệ thống cụ thể bị ảnh hưởng]

---

## ĐÁNH GIÁ RỦI RO

### Likelihood (Khả năng xảy ra)
- [ ] 1 - Thấp
- [ ] 2 - Trung bình
- [ ] 3 - Cao
- [ ] 4 - Rất cao

**Lý do**: [Giải thích]

### Impact (Tác động)
- [ ] 1 - Thấp
- [ ] 2 - Trung bình
- [ ] 3 - Cao
- [ ] 4 - Nghiêm trọng

**Lý do**: [Giải thích]

### Điểm rủi ro
**Điểm**: [Likelihood × Impact = X]

### Mức độ rủi ro
- [ ] Thấp (1-3)
- [ ] Trung bình (4-8)
- [ ] Cao (9-12)
- [ ] Nghiêm trọng (13-16)

### Level phê duyệt
- [ ] 1.0 - PM/PDM
- [ ] 2.0 - Ban CLGSP hoặc Lãnh đạo TT
- [ ] 3.0 - Ban CLGSP + Ban KTHT
- [ ] 4.0 - Lãnh đạo Công ty

---

## KẾ HOẠCH TRIỂN KHAI

### Thời gian triển khai
- **Ngày**: [YYYY-MM-DD]
- **Giờ bắt đầu**: [HH:MM]
- **Giờ kết thúc dự kiến**: [HH:MM]
- **Thời gian dự kiến**: [X giờ/phút]

### Các bước triển khai
1. [Bước 1]
2. [Bước 2]
3. [Bước 3]
...

### Người thực hiện
- **DevOps**: [Tên]
- **Development**: [Tên]
- **QA**: [Tên]

---

## KẾ HOẠCH KIỂM THỬ

### Các loại kiểm thử
- [ ] Unit Test
- [ ] Integration Test
- [ ] Regression Test
- [ ] Load Test
- [ ] Security Test

### Kết quả kiểm thử
[Ghi nhận kết quả kiểm thử]

---

## KẾ HOẠCH ROLLBACK

### Khi nào cần rollback
[Điều kiện cần rollback]

### Các bước rollback
1. [Bước 1]
2. [Bước 2]
3. [Bước 3]
...

### Thời gian rollback dự kiến
[X giờ/phút]

---

## PHÊ DUYỆT

### Phê duyệt bởi
- **Người phê duyệt**: [Tên]
- **Chức vụ**: [Chức vụ]
- **Ngày phê duyệt**: [YYYY-MM-DD]
- [ ] Đã phê duyệt
- [ ] Từ chối
- [ ] Cần bổ sung thông tin

**Ghi chú**: [Ghi chú nếu có]

---

## KẾT QUẢ

### Trạng thái
- [ ] Đã triển khai thành công
- [ ] Đã rollback
- [ ] Đã hủy

### Ngày triển khai
[YYYY-MM-DD HH:MM]

### Kết quả
[Mô tả kết quả triển khai]

### Vấn đề phát sinh
[Mô tả vấn đề nếu có]

### Ghi chú
[Ghi chú khác]

---

**Phiên bản**: 1.0

