# HƯỚNG DẪN SỬ DỤNG NHANH
## Hệ thống Quy trình và Quy định

**Phiên bản**: 2.0

---

## TÔI CẦN LÀM GÌ?

### Decision Tree - Chọn đúng file

 **Lưu ý**: File này là hướng dẫn chi tiết. Nếu bạn là người mới, xem phần [Hướng dẫn cho người mới](#6-tôi-là-người-mới-không-biết-bắt-đầu-từ-đâu) trước.

```
BẮT ĐẦU
 
 Tôi muốn DEPLOY CODE?
 
 Lỗi khẩn cấp trên Production?
 → QT-004 (Hotfix) + CL-003 + TP-002
 
 Deploy tính năng mới / thay đổi?
 
 Đã biết mã thay đổi chuẩn?
 → QT-003 (Upcode) + CL-002 + TP-001
 
 Chưa biết mã thay đổi?
 → TP-005 (Tra cứu) → QT-008 → QT-003
 
 Release sản phẩm mới?
 → QT-007 (Release) + CL-005 + TP-003
 
 Tôi muốn QUẢN TRỊ VẬN HÀNH?
 → QT-002 (Vận hành) + CL-001
 
 Tôi muốn TẠO TÀI NGUYÊN MỚI?
 → QT-005 (Provisioning) + CL-004 + TP-004
 
 Tôi muốn QUẢN LÝ PHIÊN BẢN?
 → QT-006 (Versioning)
 
 Tôi muốn CẤP QUYỀN TRUY CẬP?
 → QUICK_REFERENCE_QUYEN_TRUY_CAP → TP-006 → CL-011
 
 Tôi là NGƯỜI MỚI?
 → README.md → QUICK_START.md
```

---

## CÁC TÌNH HUỐNG THƯỜNG GẶP

### 1. Tôi cần deploy code lên Production

#### Bước 1: Xác định loại thay đổi

**Câu hỏi**: Đây là lỗi khẩn cấp hay tính năng mới?

- **Lỗi khẩn cấp** → Xem [Hotfix](#hotfix)
- **Tính năng mới / Thay đổi** → Tiếp tục Bước 2

#### Bước 2: Tra cứu mã thay đổi

**Nếu chưa biết mã thay đổi**:

1. Mở `TP-005-TEMPLATE_TRA_CUU_THAY_DOI.md`
2. Điền thông tin thay đổi
3. Tra cứu trong `QT-008-DANH_SACH_THAY_DOI_CHUAN.md` hoặc `QUICK_REFERENCE_THAY_DOI.md`
4. Xác định mã thay đổi (ví dụ: B2.1)

**Nếu đã biết mã thay đổi**: Bỏ qua bước này

#### Bước 3: Tạo RFC

1. Mở `TP-001-TEMPLATE_RFC.md`
2. Điền thông tin (đã có mã thay đổi từ Bước 2)
3. Xem `TP-001-EXAMPLE_RFC.md` để tham khảo

#### Bước 4: Thực hiện theo quy trình

1. Đọc `QT-003-UPCODE.md`
2. Sử dụng `CL-002-CHECKLIST_UPCODE.md`
3. Sử dụng checklist theo nhóm (nếu cần):
 - Nhóm A (Hạ tầng): `CL-007`
 - Nhóm B (Ứng dụng): `CL-008`
 - Nhóm C (Dữ liệu): `CL-009`
 - Nhóm D (Sự cố): `CL-010`

---

### 2. Tôi cần sửa lỗi khẩn cấp (Hotfix)

1. **Mở template**: `TP-002-TEMPLATE_HOTFIX.md`
2. **Xem ví dụ**: `TP-002-EXAMPLE_HOTFIX.md`
3. **Đọc quy trình**: `QT-004-HOTFIX.md`
4. **Sử dụng checklist**: `CL-003-CHECKLIST_HOTFIX.md`

**Lưu ý**: Hotfix không cần tra cứu mã thay đổi, có thể bỏ qua phê duyệt trong trường hợp khẩn cấp.

---

### 3. Tôi cần release sản phẩm mới


1. **Đọc quy trình**: `QT-007-RELEASE_SAN_PHAM.md`
2. **Sử dụng template**: `TP-003-TEMPLATE_RELEASE_NOTE.md`
3. **Xem ví dụ**: `TP-003-EXAMPLE_RELEASE_NOTE.md`
4. **Sử dụng checklist**: `CL-005-CHECKLIST_RELEASE.md`
5. **Quản lý version**: `QT-006-VERSIONING.md`

---

### 4. Tôi cần tạo tài nguyên mới (Provisioning)

1. **Mở template**: `TP-004-TEMPLATE_PROVISIONING.md`
2. **Xem ví dụ**: `TP-004-EXAMPLE_PROVISIONING.md`
3. **Đọc quy trình**: `QT-005-PROVISIONING.md`
4. **Sử dụng checklist**: `CL-004-CHECKLIST_PROVISIONING.md`

---

### 5. Tôi cần cấp quyền truy cập

1. **Tra cứu nhanh**: `QUICK_REFERENCE_QUYEN_TRUY_CAP.md`
2. **Mở template**: `TP-006-TEMPLATE_YEU_CAU_CAP_QUYEN.md`
3. **Sử dụng checklist**: `CL-011-CHECKLIST_QUYEN_TRUY_CAP.md`
4. **Xem hướng dẫn**: `Hỗ trợ (Support)/HUONG_DAN_SU_DUNG_QUYEN_TRUY_CAP.md`

**Nếu cần chi tiết**: Đọc `CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU.md`

---

### 6. Tôi là người mới, không biết bắt đầu từ đâu

1. **Bắt đầu**: `README.md` (File chính)
 - Xem phần "BẮT ĐẦU TẠI ĐÂY"
 - Xem phần "CÁC TÌNH HUỐNG THƯỜNG GẶP"
 
2. **Xem decision tree**: Phần trên của file này
 - Chọn tình huống phù hợp
 
3. **Làm theo quy trình**: Chọn tình huống và làm theo
 - Mỗi tình huống có quy trình tóm tắt rõ ràng

---

## QUY TRÌNH TÓM TẮT

### Upcode (Deploy thông thường)

```
Tra cứu mã thay đổi (TP-005)
 ↓
Tạo RFC (TP-001)
 ↓
Phê duyệt
 ↓
Thực hiện (QT-003 + CL-002)
 ↓
Kiểm tra và hoàn tất
```

### Hotfix (Sửa lỗi khẩn cấp)

```
Tạo Hotfix Request (TP-002)
 ↓
Phê duyệt khẩn cấp
 ↓
Thực hiện (QT-004 + CL-003)
 ↓
Kiểm tra và hoàn tất
```

### Release

```
Quản lý version (QT-006)
 ↓
Tạo Release Note (TP-003)
 ↓
Thực hiện release (QT-007 + CL-005)
 ↓
Deploy (QT-003)
```

---

## QUY TẮC VÀNG

### 1. Luôn bắt đầu với Quick Reference

- **Tra cứu thay đổi**: `QUICK_REFERENCE_THAY_DOI.md`
- **Tra cứu quyền**: `QUICK_REFERENCE_QUYEN_TRUY_CAP.md`

### 2. Luôn sử dụng Template

- Không tự tạo format
- Xem Example trước khi điền
- Điền đầy đủ thông tin

### 3. Luôn sử dụng Checklist

- Không bỏ sót bước
- Đánh dấu từng bước khi hoàn thành
- Giữ checklist để audit

### 4. Luôn đọc quy trình trước khi thực hiện

- Hiểu rõ quy trình
- Biết các bước cần thiết
- Biết ai cần phê duyệt

### 5. Luôn ghi log đầy đủ

- Ghi log mọi thao tác
- Lưu lại checklist đã hoàn thành
- Lưu lại template đã điền

---

## FILE QUAN TRỌNG NHẤT

### Cho người mới

1. **README.md** - Bắt đầu tại đây 
2. **QUICK_START.md** - Hướng dẫn nhanh cho người mới
3. **HUONG_DAN_SU_DUNG_NHANH.md** - File này - Hướng dẫn chi tiết

### Cho Developer/DevOps

1. **QUICK_REFERENCE_THAY_DOI.md** - Tra cứu nhanh
2. **TP-001-TEMPLATE_RFC.md** - Template RFC
3. **QT-003-UPCODE.md** - Quy trình upcode
4. **CL-002-CHECKLIST_UPCODE.md** - Checklist

### Cho PM/PDM

1. **QT-007-RELEASE_SAN_PHAM.md** - Quy trình release
2. **TP-003-TEMPLATE_RELEASE_NOTE.md** - Template release note
3. **QT-008-DANH_SACH_THAY_DOI_CHUAN.md** - Danh sách thay đổi

### Cho IT/Security

1. **QUICK_REFERENCE_QUYEN_TRUY_CAP.md** - Tra cứu quyền
2. **CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU.md** - Chính sách đầy đủ
3. **CL-011-CHECKLIST_QUYEN_TRUY_CAP.md** - Checklist quyền

---

## TIPS THỰC HIỆN NHANH

### 1. Bookmark các file thường dùng

- Quick Reference files
- Template files
- Checklist files

### 2. Sử dụng Example files

- Luôn xem example trước khi điền template
- Copy example và chỉnh sửa

### 3. Sử dụng Search/Find

- Tìm kiếm trong file bằng Ctrl+F / Cmd+F
- Tìm kiếm theo mã (QT-XXX, CL-XXX, TP-XXX)

### 4. In checklist ra giấy

- In checklist và đánh dấu khi thực hiện
- Giữ lại để audit

### 5. Tạo shortcut

- Tạo shortcut đến folder QT
- Tạo shortcut đến các file thường dùng

---

## GẶP VẤN ĐỀ?

### Không biết bắt đầu từ đâu?

→ Xem `QUICK_START.md`

### Không tìm thấy mã thay đổi?

→ Xem `QT-009-QUY_TRINH_BO_SUNG_THAY_DOI.md`

### Gặp lỗi khi thực hiện?

→ Xem `TROUBLESHOOTING.md`

### Cần training?

→ Xem `Hỗ trợ (Support)/HUONG_DAN_TRAINING.md`

### Cần xem thay đổi gần đây?

→ Xem `Hỗ trợ (Support)/CHANGELOG.md`

---

## CHECKLIST NHANH

### Trước khi bắt đầu

- [ ] Đã xác định mục tiêu (deploy/hotfix/release/provisioning)
- [ ] Đã tìm đúng quy trình
- [ ] Đã tìm đúng template
- [ ] Đã tìm đúng checklist
- [ ] Đã xem example (nếu có)

### Khi thực hiện

- [ ] Đã điền template đầy đủ
- [ ] Đã được phê duyệt (nếu cần)
- [ ] Đã sử dụng checklist
- [ ] Đã ghi log đầy đủ
- [ ] Đã kiểm tra kết quả

### Sau khi hoàn thành

- [ ] Đã lưu lại template đã điền
- [ ] Đã lưu lại checklist đã hoàn thành
- [ ] Đã thông báo cho người liên quan
- [ ] Đã cập nhật tài liệu (nếu cần)

---

**Phiên bản**: 2.0 
**Ngày cập nhật**: 2024-12-17

