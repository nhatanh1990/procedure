 # Ví dụ Yêu Cầu Cấp Quyền - Deploy lên Production

## THÔNG TIN CHUNG

- **Request ID**: REQ-20241217-001
- **Ngày tạo**: 2024-12-17
- **Người yêu cầu**: Trần Văn B
- **Email**: tran.van.b@company.com
- **Điện thoại**: 0987654321
- **Phòng ban**: DevOps Team

---

## THÔNG TIN YÊU CẦU

### Lý do cần quyền

Cần quyền deploy tính năng Two-Factor Authentication (2FA) lên môi trường Production. Tính năng đã được phát triển, test trên UAT/Staging và đã được phê duyệt qua RFC-20241215-001. Cần quyền deploy và cấu hình để triển khai tính năng này.

### Quyền cần

- **Role/Quyền**: DevOps - Deploy access
- **Hệ thống**: Production environment
- **Môi trường**: Production

### Thời gian

- [ ] **Vĩnh viễn**
- [x] **Tạm thời**
  - **Thời gian bắt đầu**: 2024-12-17 14:00
  - **Thời gian kết thúc**: 2024-12-17 16:00
  - **Thời hạn**: 2 giờ

### Chi tiết quyền

**Quyền truy cập**:
- [x] SSH/Server access
- [ ] Database access
- [x] Deploy access
- [x] Configuration access
- [x] Log access
- [ ] Khác: [Mô tả]

**Quyền cụ thể**:
- [ ] Read-only
- [x] Read/Write
- [ ] Admin/Full access
- [ ] Khác: [Mô tả]

---

## PHÊ DUYỆT

### Cấp độ phê duyệt

- [ ] **Level 1.0**: PM/PDM
- [ ] **Level 2.0**: Ban CLGSP hoặc Lãnh đạo TT
- [x] **Level 3.0**: Ban CLGSP + Ban KTHT
- [ ] **Level 4.0**: Lãnh đạo Công ty

### Phê duyệt bởi

- **Người phê duyệt**: Nguyễn Thị C
- **Chức vụ**: Trưởng phòng DevOps
- **Ngày phê duyệt**: 2024-12-17
- [x] Đã phê duyệt
- [ ] Từ chối
- [ ] Cần bổ sung thông tin

**Ghi chú**: Đã phê duyệt theo RFC-20241215-001. Quyền tạm thời (JIT) trong 2 giờ để deploy tính năng 2FA.

---

## THỰC HIỆN

### Cấp quyền

- **Người cấp quyền**: Lê Văn D - IT Team
- **Ngày cấp quyền**: 2024-12-17 13:55
- **Quyền đã cấp**: 
  - Deploy access trên Production environment
  - SSH access đến production servers (10.0.1.10, 10.0.1.11)
  - Configuration access để cập nhật config
  - Log access để monitor deployment
- **IP whitelist**: 10.0.1.50 (IP của người yêu cầu)
- **MFA**: Đã kích hoạt

### Ghi log

- [x] Đã ghi log đầy đủ
- **Log ID**: LOG-20241217-001

---

## THU HỒI QUYỀN (Nếu tạm thời)

### Thu hồi

- **Ngày thu hồi**: 2024-12-17 15:45
- **Lý do**: Đã hoàn thành deploy, quyền tự động hết hạn
- **Người thu hồi**: Hệ thống tự động (JIT)
- [x] Đã thu hồi thành công
- [x] Đã ghi log thu hồi

---

## GHI CHÚ

- Deploy thành công tính năng 2FA lên Production
- Không có sự cố trong quá trình deploy
- Đã test và verify tính năng hoạt động đúng
- Quyền đã được tự động thu hồi sau khi hoàn thành

---

**Tham chiếu**:
- `CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU.md` - Phần 7
- `CL-011-CHECKLIST_QUYEN_TRUY_CAP.md` - Checklist cấp quyền
- `QUICK_REFERENCE_QUYEN_TRUY_CAP.md` - Bảng tra cứu nhanh
- RFC-20241215-001 - Request for Change

---

**Phiên bản**: 1.0
