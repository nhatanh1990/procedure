# CL-002: CHECKLIST UPCODE

**Mã checklist**: CL-002  
**Tham chiếu quy trình**: QT-003

---

## 1. CHECKLIST TRƯỚC TRIỂN KHAI

### 1.1. Chuẩn bị code

- [ ] Code đã được review và merge
- [ ] Tất cả tests đã pass
- [ ] Code coverage: ≥ 80%
- [ ] Security scan: Pass
- [ ] Documentation đã được update

### 1.2. Đánh giá và phê duyệt

- [ ] Đã xác định loại thay đổi (Standard/Normal/Emergency)
- [ ] Đã đánh giá rủi ro
- [ ] Đã xác định Level phê duyệt
- [ ] Đã lập kế hoạch triển khai
- [ ] Đã lập kế hoạch rollback
- [ ] Đã được phê duyệt

### 1.3. Kiểm thử

- [ ] Unit tests: Pass
- [ ] Integration tests: Pass
- [ ] Regression tests: Pass (nếu Level ≥ 3.0)
- [ ] Load tests: Pass (nếu Level = 4.0)
- [ ] Security tests: Pass (nếu Level = 4.0)

---

## 2. CHECKLIST TRONG TRIỂN KHAI

### 2.1. Backup

- [ ] Đã backup hệ thống
- [ ] Đã backup database
- [ ] Đã backup cấu hình
- [ ] Backup đã được verify

### 2.2. Triển khai

- [ ] Đã deploy code
- [ ] Đã update cấu hình (nếu cần)
- [ ] Đã run migration (nếu cần)
- [ ] Đã restart service (nếu cần)
- [ ] Đã kiểm tra deployment

### 2.3. Kiểm tra

- [ ] Service đã start thành công
- [ ] Health check pass
- [ ] Log không có lỗi
- [ ] Smoke test pass

---

## 3. CHECKLIST SAU TRIỂN KHAI

### 3.1. Giám sát

- [ ] Đã giám sát hệ thống (ít nhất 1 giờ)
- [ ] Error rate trong giới hạn cho phép
- [ ] Response time trong giới hạn cho phép
- [ ] Resource usage trong giới hạn cho phép
- [ ] Không có cảnh báo từ monitoring

### 3.2. Xác nhận

- [ ] Hệ thống hoạt động bình thường
- [ ] Không có lỗi trong log
- [ ] Metrics trong giới hạn cho phép
- [ ] Đã ghi nhận
- [ ] Đã thông báo team

---

## 4. CHECKLIST ROLLBACK (NẾU CẦN)

### 4.1. Quyết định rollback

- [ ] Đã đánh giá tình hình
- [ ] Đã quyết định rollback
- [ ] Đã thông báo team

### 4.2. Thực hiện rollback

- [ ] Đã xác định version cần rollback
- [ ] Đã restore backup (nếu cần)
- [ ] Đã deploy version cũ
- [ ] Đã restore database (nếu cần)
- [ ] Đã restore cấu hình (nếu cần)

### 4.3. Kiểm tra sau rollback

- [ ] Service đã start thành công
- [ ] Smoke test pass
- [ ] Hệ thống hoạt động bình thường
- [ ] Đã ghi nhận rollback
- [ ] Đã phân tích nguyên nhân

---

**Phiên bản**: 1.0

