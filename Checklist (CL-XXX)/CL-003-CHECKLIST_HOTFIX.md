# CL-003: CHECKLIST HOTFIX

**Mã checklist**: CL-003 
**Tham chiếu quy trình**: QT-004

---

## 1. CHECKLIST PHÁT HIỆN VÀ ĐÁNH GIÁ

### 1.1. Phát hiện sự cố

- [ ] Sự cố đã được ghi nhận
- [ ] Thông tin ban đầu đã được thu thập
- [ ] Mức độ nghiêm trọng đã được xác định

### 1.2. Đánh giá sự cố

- [ ] Nguyên nhân đã được xác định
- [ ] Quyết định hotfix đã được thực hiện
- [ ] Hotfix Request đã được tạo

---

## 2. CHECKLIST PHÁT TRIỂN HOTFIX

### 2.1. Tạo hotfix

- [ ] Hotfix branch đã được tạo
- [ ] Lỗi đã được sửa
- [ ] Code đã được test nhanh
- [ ] Test nhanh đã pass

### 2.2. Code review

- [ ] Code review đã được thực hiện (nếu có thời gian)
- [ ] Hoặc đã ghi nhận sẽ review sau

---

## 3. CHECKLIST TRIỂN KHAI HOTFIX

### 3.1. Chuẩn bị

- [ ] Backup đã được thực hiện
- [ ] Rollback plan đã được chuẩn bị
- [ ] Team đã được thông báo

### 3.2. Triển khai

- [ ] Hotfix đã được deploy
- [ ] Deployment đã được kiểm tra
- [ ] Service đã start thành công
- [ ] Health check pass

### 3.3. Xác nhận

- [ ] Log không có lỗi
- [ ] Test case liên quan đến lỗi đã pass
- [ ] Lỗi đã được xác nhận sửa
- [ ] Đã giám sát hệ thống (ít nhất 30 phút)

---

## 4. CHECKLIST HOÀN THIỆN

### 4.1. Merge

- [ ] Hotfix đã được merge vào main
- [ ] Conflicts đã được resolve (nếu có)
- [ ] Version đã được update (nếu cần)
- [ ] CHANGELOG.md đã được update

### 4.2. Bổ sung hồ sơ

- [ ] Hotfix Request đã được bổ sung (nếu chưa có)
- [ ] Changelog đã được update
- [ ] Documentation đã được update (nếu cần)
- [ ] Issue tracker đã được update

### 4.3. Đánh giá sau

- [ ] Nguyên nhân sự cố đã được phân tích
- [ ] Quy trình xử lý đã được đánh giá
- [ ] Đề xuất cải tiến đã được ghi nhận
- [ ] Runbook đã được cập nhật (nếu cần)
- [ ] Báo cáo đã được tạo

---

**Phiên bản**: 1.0

