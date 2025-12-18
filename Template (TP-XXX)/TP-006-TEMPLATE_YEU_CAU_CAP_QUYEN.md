# TP-006: TEMPLATE YÊU CẦU CẤP QUYỀN

**Mã template**: TP-006 
**Tham chiếu**: `CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU.md`

---

## THÔNG TIN CHUNG

- **Request ID**: [REQ-YYYYMMDD-XXX]
- **Ngày tạo**: [YYYY-MM-DD]
- **Người yêu cầu**: [Tên]
- **Email**: [Email]
- **Điện thoại**: [SĐT]
- **Phòng ban**: [Phòng ban]

---

## THÔNG TIN YÊU CẦU

### Lý do cần quyền

[Mô tả chi tiết lý do cần quyền, ví dụ: Deploy tính năng mới lên Production, Debug sự cố, ...]

### Quyền cần

- **Role/Quyền**: [Ví dụ: DevOps, DBAdmin, ReadWrite, ...]
- **Hệ thống**: [Ví dụ: Production, Database, Server, ...]
- **Môi trường**: [Development/Staging/UAT/Production/DR]

### Thời gian

- [ ] **Vĩnh viễn**
- [ ] **Tạm thời**
 - **Thời gian bắt đầu**: [YYYY-MM-DD HH:mm]
 - **Thời gian kết thúc**: [YYYY-MM-DD HH:mm]
 - **Thời hạn**: [X giờ/phút/ngày]

### Chi tiết quyền

**Quyền truy cập**:
- [ ] SSH/Server access
- [ ] Database access
- [ ] Deploy access
- [ ] Configuration access
- [ ] Log access
- [ ] Khác: [Mô tả]

**Quyền cụ thể**:
- [ ] Read-only
- [ ] Read/Write
- [ ] Admin/Full access
- [ ] Khác: [Mô tả]

---

## PHÊ DUYỆT

### Cấp độ phê duyệt

- [ ] **Level 1.0**: PM/PDM
- [ ] **Level 2.0**: Ban CLGSP hoặc Lãnh đạo TT
- [ ] **Level 3.0**: Ban CLGSP + Ban KTHT
- [ ] **Level 4.0**: Lãnh đạo Công ty

### Phê duyệt bởi

- **Người phê duyệt**: [Tên]
- **Chức vụ**: [Chức vụ]
- **Ngày phê duyệt**: [YYYY-MM-DD]
- [ ] Đã phê duyệt
- [ ] Từ chối
- [ ] Cần bổ sung thông tin

**Ghi chú**: [Ghi chú nếu có]

---

## THỰC HIỆN

### Cấp quyền

- **Người cấp quyền**: [Tên - IT Team]
- **Ngày cấp quyền**: [YYYY-MM-DD HH:mm]
- **Quyền đã cấp**: [Mô tả quyền đã cấp]
- **IP whitelist**: [IP đã whitelist, nếu có]
- **MFA**: [Đã kích hoạt/Chưa kích hoạt]

### Ghi log

- [ ] Đã ghi log đầy đủ
- [ ] Log ID: [ID nếu có]

---

## THU HỒI QUYỀN (Nếu tạm thời)

### Thu hồi

- **Ngày thu hồi**: [YYYY-MM-DD HH:mm]
- **Lý do**: [Lý do thu hồi]
- **Người thu hồi**: [Tên]
- [ ] Đã thu hồi thành công
- [ ] Đã ghi log thu hồi

---

## GHI CHÚ

[Ghi chú khác nếu có]

---

**Tham chiếu**:
- `CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU.md` - Phần 7
- `CL-011-CHECKLIST_QUYEN_TRUY_CAP.md` - Checklist cấp quyền
- `QUICK_REFERENCE_QUYEN_TRUY_CAP.md` - Bảng tra cứu nhanh

---

**Phiên bản**: 1.0

