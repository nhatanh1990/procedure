# FOLDER HỖ TRỢ (SUPPORT)
## Tài liệu hỗ trợ cho Hệ thống Quy trình

**Phiên bản**: 2.0

---

## TỔNG QUAN

Folder này chứa các tài liệu hỗ trợ giúp người dùng sử dụng hệ thống quy trình một cách hiệu quả.

---

## DANH SÁCH FILE

### Hướng dẫn sử dụng

#### 1. QUICK_START.md

**Mục đích**: Hướng dẫn nhanh cho người mới

**Khi nào sử dụng**:
- Bạn là người mới và cần bắt đầu nhanh
- Cần hướng dẫn các bước đầu tiên

**Nội dung**:
- Tôi là người mới, bắt đầu từ đâu?
- Quy tắc vàng
- Tài liệu tham khảo

**Lưu ý**: File này là bản tóm tắt ngắn gọn. Xem `../README.md` để biết quy trình chi tiết cho từng tình huống.

---

#### 2. HUONG_DAN_SU_DUNG_QUYEN_TRUY_CAP.md 

**Mục đích**: Hướng dẫn tổng hợp về quyền truy cập

**Khi nào sử dụng**:
- Cần cấp quyền truy cập
- Cần tra cứu quyền trong các quy trình
- Cần phương pháp thực hiện nhanh

**Nội dung**:
- Phương pháp thực hiện nhanh (cấp quyền vĩnh viễn, JIT, khẩn cấp)
- Quyền truy cập trong các quy trình (QT-002, QT-003, QT-004, QT-005, QT-007)
- Quy trình cấp quyền tổng quát
- Checklist nhanh
- Tips thực hiện

---

### Xử lý vấn đề

#### 3. TROUBLESHOOTING.md

**Mục đích**: Hướng dẫn xử lý vấn đề thường gặp

**Khi nào sử dụng**:
- Gặp vấn đề khi sử dụng quy trình
- Không biết cách xử lý một tình huống cụ thể
- Cần tìm câu trả lời nhanh

**Nội dung**:
- FAQ - Câu hỏi thường gặp
- Vấn đề kỹ thuật
- Vấn đề quy trình
- Liên hệ hỗ trợ
- Báo cáo vấn đề

---

### Tài liệu kỹ thuật

### Tài liệu kỹ thuật

#### 5. CHANGELOG.md

**Mục đích**: Lịch sử thay đổi của hệ thống quy trình

**Khi nào sử dụng**:
- Muốn xem các thay đổi gần đây
- Cần biết version hiện tại
- Cần theo dõi lịch sử cập nhật

**Nội dung**:
- Lịch sử các phiên bản
- Các tính năng mới
- Các thay đổi và cải thiện
- Các lỗi đã sửa

---

#### 6. HUONG_DAN_CHANGELOG.md

**Mục đích**: Hướng dẫn về CHANGELOG.md cho sản phẩm/service

**Khi nào sử dụng**:
- Cần hiểu CHANGELOG.md là gì
- Cần biết cách viết và cập nhật CHANGELOG.md
- Chuẩn bị release và cần update CHANGELOG.md

**Nội dung**:
- Định nghĩa CHANGELOG.md
- Cấu trúc và format
- Các loại thay đổi (Added, Changed, Fixed, Security, etc.)
- Quy trình cập nhật
- Best practices
- Template CHANGELOG.md
- Mối quan hệ với Release Note

---

#### 7. METADATA_CONFIG.md

**Mục đích**: Quản lý metadata tập trung

**Khi nào sử dụng**:
- Cần thông tin metadata (ngày ban hành, người soạn, etc.)
- Cần cập nhật metadata cho các file
- Cần thông tin liên hệ

**Nội dung**:
- Thông tin tổ chức
- Thông tin liên hệ
- Thông tin người phụ trách
- Format ngày tháng
- Quy trình cập nhật

---

#### 8. HUONG_DAN_TRAINING.md

**Mục đích**: Hướng dẫn training nhân viên mới

**Khi nào sử dụng**:
- Cần training nhân viên mới
- Cần kế hoạch training
- Cần tài liệu training

**Nội dung**:
- Kế hoạch training
- Nội dung training
- Tài liệu training
- Đánh giá training

---

## HƯỚNG DẪN SỬ DỤNG

### Cho người mới

1. **Bắt đầu với**: `QUICK_START.md`
2. **Nếu gặp vấn đề**: Xem `TROUBLESHOOTING.md`
3. **Cần thông tin chi tiết**: Xem các quy trình trong folder `../Quy trình (QT-XXX)`

### Cho Developer/DevOps

1. **Hướng dẫn sử dụng nhanh**: `../HUONG_DAN_SU_DUNG_NHANH.md`
2. **Best Practices**: `../BEST_PRACTICES.md`
3. **Quyền truy cập**: `HUONG_DAN_SU_DUNG_QUYEN_TRUY_CAP.md`
4. **Troubleshooting**: `TROUBLESHOOTING.md`

### Cho người quản lý

1. **Theo dõi thay đổi**: `CHANGELOG.md`
2. **Quản lý metadata**: `METADATA_CONFIG.md`
3. **Xem đánh giá**: Xem phần đánh giá trong `CHANGELOG.md`

### Cho người phát triển

1. **Xem changelog hệ thống**: `CHANGELOG.md`
2. **Hướng dẫn CHANGELOG sản phẩm**: `HUONG_DAN_CHANGELOG.md`
3. **Cập nhật metadata**: `METADATA_CONFIG.md`
4. **Báo cáo vấn đề**: Sử dụng format trong `TROUBLESHOOTING.md`

---

## LƯU Ý

- Tất cả file trong folder này là tài liệu hỗ trợ
- File chính vẫn nằm ở root folder QT
- Các file này được cập nhật định kỳ
- Nếu có vấn đề, xem `TROUBLESHOOTING.md` trước

---

## LIÊN KẾT

- **README chính**: [`../README.md`](../README.md) 
- **Hướng dẫn sử dụng nhanh**: [`../HUONG_DAN_SU_DUNG_NHANH.md`](../HUONG_DAN_SU_DUNG_NHANH.md)
- **Best Practices**: [`../BEST_PRACTICES.md`](../BEST_PRACTICES.md)

---

## CẤU TRÚC FOLDER

```
Hỗ trợ (Support)/
 README.md (File này)
 QUICK_START.md (Hướng dẫn nhanh cho người mới)
 HUONG_DAN_SU_DUNG_QUYEN_TRUY_CAP.md (Hướng dẫn quyền truy cập) 
 TROUBLESHOOTING.md (Xử lý vấn đề)
 CHANGELOG.md (Lịch sử thay đổi)
 HUONG_DAN_CHANGELOG.md (Hướng dẫn CHANGELOG)
 METADATA_CONFIG.md (Quản lý metadata)
```

---

**Phiên bản**: 2.0 
**Ngày cập nhật**: 2024-12-17
