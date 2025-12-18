# Ví dụ Hotfix Request - Sửa lỗi session timeout

## THÔNG TIN CHUNG

- **Hotfix ID**: HOTFIX-20241216-001
- **Ngày tạo**: 2024-12-16 10:30
- **Người tạo**: Nguyễn Văn A
- **Email**: nguyen.van.a@company.com
- **Điện thoại**: 0912345678

---

## THÔNG TIN SỰ CỐ

### Mô tả sự cố
Session timeout không hoạt động đúng trên Production. Người dùng bị logout sớm hơn thời gian cấu hình (30 phút), gây ảnh hưởng đến trải nghiệm người dùng. Một số người dùng báo cáo bị logout sau 5-10 phút không hoạt động.

### Mức độ nghiêm trọng
- [ ] Critical - Hệ thống down, mất dữ liệu
- [x] High - Ảnh hưởng nghiêm trọng đến dịch vụ
- [ ] Medium - Ảnh hưởng một phần dịch vụ
- [ ] Low - Ảnh hưởng nhỏ

### Hệ thống ảnh hưởng
- [x] Production
- [ ] DR
- [ ] UAT
- [ ] Staging

### Danh sách hệ thống
- user-service (Production)
- user-service-api (Production)

### Số người dùng ảnh hưởng
Khoảng 30% người dùng đang hoạt động (ước tính ~5000 người dùng)

---

## NGUYÊN NHÂN

### Nguyên nhân sơ bộ
Sau khi phân tích code và log, phát hiện bug trong logic tính toán session timeout. Code đang sử dụng timestamp tính bằng giây thay vì milliseconds, dẫn đến session bị timeout sớm hơn 1000 lần.

**File có bug**: `src/services/session.service.js` - Line 45

### Log/Error messages
```
[2024-12-16 10:15:23] ERROR: Session expired for user_id=12345, session_id=abc123
[2024-12-16 10:15:23] INFO: Session created_at=2024-12-16T10:05:23Z, expires_at=2024-12-16T10:10:23Z
[2024-12-16 10:15:23] WARN: Session timeout calculated incorrectly: 300000ms instead of 1800000ms
```

### Link đến issue/ticket
- GitHub Issue: #125
- JIRA Ticket: PROD-1234

---

## GIẢI PHÁP ĐỀ XUẤT

### Mô tả giải pháp
Sửa lỗi tính toán session timeout bằng cách chuyển đổi đúng từ milliseconds sang seconds. Thay đổi nhỏ, chỉ 1 dòng code, không ảnh hưởng đến logic khác.

### Code changes
```javascript
// Cũ (sai)
const expiresAt = createdAt + (timeoutSeconds * 1000); // timeoutSeconds đã là milliseconds

// Mới (đúng)
const expiresAt = createdAt + (timeoutSeconds * 1000); // timeoutSeconds là seconds, cần nhân 1000
// Hoặc nếu timeoutSeconds đã là milliseconds thì không cần nhân
const expiresAt = createdAt + timeoutSeconds;
```

**Fix cụ thể**: Sửa line 45 trong `src/services/session.service.js`:
```javascript
// Trước
const expiresAt = new Date(createdAt.getTime() + sessionTimeout);

// Sau
const expiresAt = new Date(createdAt.getTime() + (sessionTimeout * 1000));
```

### Files thay đổi
- `src/services/session.service.js` (Line 45)

### Testing plan
1. Unit test: Test hàm tính toán session timeout
2. Integration test: Test session flow end-to-end
3. Manual test: Test trên Staging với các scenario khác nhau
4. Smoke test: Test nhanh trên Production sau khi deploy

---

## PHÊ DUYỆT KHẨN

### Phê duyệt bởi
- **Người phê duyệt**: Phạm Văn D
- **Chức vụ**: Product Manager
- **Ngày phê duyệt**: 2024-12-16 11:00
- [x] Đã phê duyệt
- [ ] Có thể phê duyệt sau
- [ ] Từ chối

**Lý do**: Đã review code fix, thay đổi nhỏ và an toàn. Phê duyệt triển khai ngay.

---

## THỰC HIỆN

### Hotfix branch
hotfix/v1.2.4-session-timeout

### Người thực hiện
- **Development**: Nguyễn Văn A
- **DevOps**: Trần Văn B

### Thời gian thực hiện
- **Bắt đầu**: 2024-12-16 11:30
- **Kết thúc**: 2024-12-16 12:15

### Kết quả
- [x] Đã triển khai thành công
- [ ] Đã rollback
- [ ] Đã hủy

### Mô tả kết quả
Triển khai thành công. Hotfix đã được deploy lên Production lúc 12:00. Sau 15 phút monitoring, không có lỗi mới phát sinh. Session timeout đã hoạt động đúng với thời gian cấu hình 30 phút.

**Verification**:
- Test session timeout: Pass
- Không có lỗi trong log
- Metrics bình thường
- Không có complaint từ người dùng

---

## BỔ SUNG HỒ SƠ (Sau khi hotfix)

### Merge vào main
- [x] Đã merge vào main
- [x] Branch: hotfix/v1.2.4-session-timeout
- [x] Commit: a1b2c3d4e5f6

### Update version
- [x] Version mới: 1.2.4
- [x] CHANGELOG.md đã được update

### Đánh giá sau
- [x] Nguyên nhân đã được phân tích: Bug trong logic tính toán session timeout
- [x] Quy trình đã được đánh giá: Cần cải thiện unit test coverage
- [x] Đề xuất cải tiến đã được ghi nhận: 
 - Tăng unit test coverage cho session service
 - Thêm integration test cho session flow
 - Code review kỹ hơn các thay đổi liên quan đến time calculation
- [x] Runbook đã được cập nhật: Thêm troubleshooting guide cho session issues

---

**Phiên bản**: 1.0

