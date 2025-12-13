# HƯỚNG DẪN SỬ DỤNG QUYỀN TRUY CẬP
## Tổng hợp - Chính sách Quyền Truy Cập Tối Thiểu

**Phiên bản**: 2.0

---

## 📋 TỔNG QUAN

Tài liệu này tổng hợp hướng dẫn sử dụng **Chính sách Quyền Truy Cập Tối Thiểu** trong các quy trình và phương pháp thực hiện nhanh.

**Tham chiếu chính**: `../CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU.md`

---

## 💡 TẠI SAO BẠN NÊN ĐỌC TÀI LIỆU NÀY?

### ✅ Lợi ích cho bạn
- ⚡ **Làm việc hiệu quả hơn**: Biết rõ quyền của mình và cách yêu cầu quyền bổ sung nhanh chóng
- 🛡️ **Bảo vệ bản thân**: Tránh các lỗi vô ý có thể gây hậu quả nghiêm trọng
- 📚 **Hiểu rõ quy trình**: Không bị lúng túng khi cần quyền, biết ai cần phê duyệt
- ⏱️ **Tiết kiệm thời gian**: Quy trình rõ ràng giúp bạn nhận quyền nhanh chóng
- 🔒 **An toàn hơn**: Bảo vệ bạn và công ty khỏi các mối đe dọa bảo mật

### 📊 Số liệu thuyết phục
- **Giảm 80-90%** rủi ro bị tấn công khi tuân thủ Least Privilege
- **Giảm 60-70%** lỗi do con người
- **74%** các vụ vi phạm bảo mật liên quan đến quyền quá cao
- **$4.45 triệu USD** - chi phí trung bình cho mỗi vụ vi phạm dữ liệu

**👉 Muốn biết thêm?** Xem phần 1.1-1.5 trong `../CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU.md`

---

## 🚀 PHƯƠNG PHÁP THỰC HIỆN NHANH

### Tôi cần cấp quyền, làm gì?

#### Scenario 1: Cấp quyền vĩnh viễn

1. **Tra cứu quyền**
   - Mở `../QUICK_REFERENCE_QUYEN_TRUY_CAP.md`
   - Tìm quyền theo vai trò và hoạt động

2. **Điền template**
   - Mở `../Template (TP-XXX)/TP-006-TEMPLATE_YEU_CAU_CAP_QUYEN.md`
   - Điền thông tin đầy đủ

3. **Xác định cấp phê duyệt**
   - Level 1.0 → PM/PDM
   - Level 2.0 → Ban CLGSP hoặc Lãnh đạo TT
   - Level 3.0 → Ban CLGSP + Ban KTHT
   - Level 4.0 → Lãnh đạo Công ty

4. **Gửi phê duyệt**
   - Gửi template đã điền cho người phê duyệt đúng cấp

5. **IT cấp quyền**
   - IT sử dụng `../Checklist (CL-XXX)/CL-011-CHECKLIST_QUYEN_TRUY_CAP.md`
   - Cấp quyền theo role và ghi log

#### Scenario 2: Cấp quyền tạm thời JIT

1. **Điền template**
   - Ghi rõ "Tạm thời (JIT)" và thời gian cần

2. **Phê duyệt nhanh**
   - Có thể phê duyệt qua chat/phone

3. **IT cấp quyền**
   - Cấp quyền với thời gian hết hạn tự động

4. **Tự động thu hồi**
   - Quyền tự động hết hạn sau thời gian quy định

#### Scenario 3: Cấp quyền khẩn cấp cho Hotfix

1. **Yêu cầu khẩn cấp**
   - Ghi rõ "Hotfix khẩn cấp"

2. **Phê duyệt nhanh**
   - PM/PDM hoặc ECAB phê duyệt qua chat/phone
   - Ghi log sau

3. **Cấp quyền ngay**
   - IT cấp quyền tạm thời (JIT)

4. **Thu hồi sau hotfix**
   - Tự động thu hồi hoặc thu hồi ngay sau khi hoàn thành

---

## 🎯 QUYỀN TRUY CẬP TRONG CÁC QUY TRÌNH

### QT-002: Quản trị Vận hành

**Quyền cần thiết**:
- Giám sát hệ thống: Read-only
- Xem log: Read-only
- Quản lý backup: Read/Write (sau phê duyệt)
- Quản lý cấu hình: Read/Write (sau phê duyệt)

**Xem chi tiết**: `../Quy trình (QT-XXX)/QT-002-QUAN_TRI_VAN_HANH.md` - Phần 9

### QT-003: Upcode

**Quyền cần thiết**:
- Deploy lên Production: Read/Write (sau phê duyệt)
- Truy cập database: Read/Write (sau phê duyệt)
- Thay đổi cấu hình: Read/Write (sau phê duyệt)
- Quyền tạm thời (JIT)

**Xem chi tiết**: `../Quy trình (QT-XXX)/QT-003-UPCODE.md` - Phần 9

### QT-004: Hotfix

**Quyền cần thiết**:
- Deploy khẩn cấp: Read/Write (phê duyệt khẩn cấp)
- Truy cập database khẩn cấp: Read/Write (phê duyệt khẩn cấp)
- Quyền tạm thời (JIT)

**Xem chi tiết**: `../Quy trình (QT-XXX)/QT-004-HOTFIX.md` - Phần 7

### QT-005: Provisioning

**Quyền cần thiết**:
- Tạo server: Read/Write (sau phê duyệt)
- Tạo database: Read/Write (sau phê duyệt)
- Cấu hình network: Read/Write (sau phê duyệt)

**Xem chi tiết**: `../Quy trình (QT-XXX)/QT-005-PROVISIONING.md` - Phần 6

### QT-007: Release

**Quyền cần thiết**:
- Tạo release: Read/Write (sau phê duyệt)
- Publish release: Read/Write (sau phê duyệt)
- Deploy release: Read/Write (sau phê duyệt)

**Xem chi tiết**: `../Quy trình (QT-XXX)/QT-007-RELEASE_SAN_PHAM.md` - Phần 8

---

## 📋 QUY TRÌNH CẤP QUYỀN TỔNG QUÁT

### Bước 1: Tra cứu quyền

1. Mở `../QUICK_REFERENCE_QUYEN_TRUY_CAP.md`
2. Tìm quyền theo vai trò và hoạt động
3. Xác định cấp phê duyệt cần thiết

### Bước 2: Yêu cầu quyền

1. Mở `../Template (TP-XXX)/TP-006-TEMPLATE_YEU_CAU_CAP_QUYEN.md`
2. Điền thông tin đầy đủ
3. Gửi phê duyệt

### Bước 3: Phê duyệt

- Level 1.0-2.0: PM/PDM
- Level 3.0: Ban CLGSP
- Level 4.0: Lãnh đạo
- Khẩn cấp: Có thể phê duyệt nhanh qua chat/phone

### Bước 4: Cấp quyền

- IT cấp quyền theo role
- Ghi log đầy đủ
- Thông báo cho người yêu cầu

### Bước 5: Sử dụng và thu hồi

- Sử dụng quyền theo mục đích
- Thu hồi ngay sau khi hoàn thành (nếu tạm thời)
- Ghi log sử dụng

---

## ✅ CHECKLIST NHANH

### Trước khi yêu cầu quyền

- [ ] Đã tra cứu quyền trong Quick Reference
- [ ] Đã xác định đúng quyền cần
- [ ] Đã xác định cấp phê duyệt
- [ ] Đã điền template yêu cầu đầy đủ

### Khi sử dụng quyền

- [ ] Đã được phê duyệt
- [ ] Đã nhận được thông báo cấp quyền
- [ ] Đã sử dụng quyền đúng mục đích
- [ ] Đã ghi log sử dụng

### Sau khi hoàn thành

- [ ] Đã thu hồi quyền (nếu tạm thời)
- [ ] Đã ghi log thu hồi
- [ ] Đã thông báo cho IT (nếu cần)

---

## 📚 TÀI LIỆU THAM KHẢO

### File chính

1. **CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU.md** - Chính sách đầy đủ
2. **QUICK_REFERENCE_QUYEN_TRUY_CAP.md** - Tra cứu nhanh ⭐
3. **TP-006-TEMPLATE_YEU_CAU_CAP_QUYEN.md** - Template yêu cầu ⭐
4. **CL-011-CHECKLIST_QUYEN_TRUY_CAP.md** - Checklist ⭐

### File theo quy trình

1. **QT-002-QUAN_TRI_VAN_HANH.md** - Phần 9
2. **QT-003-UPCODE.md** - Phần 9
3. **QT-004-HOTFIX.md** - Phần 7
4. **QT-005-PROVISIONING.md** - Phần 6
5. **QT-007-RELEASE_SAN_PHAM.md** - Phần 8

---

## 🎯 TIPS

1. **Sử dụng Quick Reference**: Luôn bắt đầu với Quick Reference để tra cứu nhanh
2. **Yêu cầu sớm**: Yêu cầu quyền trước khi cần
3. **Sử dụng JIT**: Sử dụng quyền tạm thời (JIT) khi có thể
4. **Ghi log đầy đủ**: Ghi log mọi hành động với quyền cao
5. **Phê duyệt nhanh cho khẩn cấp**: Hotfix có thể phê duyệt nhanh, nhưng phải ghi log sau

---

**Phiên bản**: 2.0  
**Ngày cập nhật**: 2024-12-17

