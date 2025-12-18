# CL-007: CHECKLIST NHÓM A - HẠ TẦNG

**Mã checklist**: CL-007 
**Tham chiếu**: `QT-008-DANH_SACH_THAY_DOI_CHUAN.md` - Nhóm A

---

## TỔNG QUAN

Nhóm A bao gồm 19 loại thay đổi liên quan đến hạ tầng:
- A1: Cập nhật và nâng cấp hệ thống (4 loại)
- A2: Dịch chuyển và tách cụm (3 loại)
- A3: Cấu hình mạng và bảo mật (4 loại)
- A4: Quản lý tài nguyên và giám sát (5 loại)
- A5: Cấu hình hệ thống (3 loại)

---

## CHECKLIST CHUNG CHO NHÓM A

### Trước khi thực hiện

- [ ] Đã tra cứu mã thay đổi trong QT-008
- [ ] Đã xác định mức độ rủi ro
- [ ] Đã xác định cấp độ phê duyệt
- [ ] Đã lập kế hoạch triển khai
- [ ] Đã lập kế hoạch rollback
- [ ] Đã backup hệ thống
- [ ] Đã backup cấu hình
- [ ] Đã thông báo team liên quan

### Trong khi thực hiện

- [ ] Đã thực hiện theo kế hoạch
- [ ] Đã ghi log đầy đủ
- [ ] Đã kiểm tra từng bước
- [ ] Đã xử lý lỗi (nếu có)

### Sau khi thực hiện

- [ ] Đã kiểm tra hệ thống hoạt động bình thường
- [ ] Đã kiểm tra monitoring/alerting
- [ ] Đã kiểm tra log không có lỗi
- [ ] Đã ghi nhận kết quả
- [ ] Đã thông báo team

---

## CHECKLIST THEO TỪNG LOẠI

### A1: Cập nhật và nâng cấp hệ thống

#### A1.1 - Update windows (UAT/DR)
- [ ] Đã kiểm tra version hiện tại
- [ ] Đã kiểm tra compatibility
- [ ] Đã test trên môi trường test
- [ ] Đã có kế hoạch rollback

#### A1.2 - Update windows PROD, Linux
- [ ] Đã kiểm tra version hiện tại
- [ ] Đã kiểm tra compatibility
- [ ] Đã test trên môi trường test
- [ ] Đã có kế hoạch rollback
- [ ] Đã backup đầy đủ

#### A1.3 - Nâng cấp hệ điều hành máy chủ
- [ ] Đã đánh giá rủi ro chi tiết
- [ ] Đã test trên môi trường test
- [ ] Đã có kế hoạch rollback chi tiết
- [ ] Đã backup đầy đủ
- [ ] Đã có maintenance window

#### A1.4 - Nâng cấp version phần mềm nền tảng
- [ ] Đã đánh giá rủi ro nghiêm trọng
- [ ] Đã test kỹ trên môi trường test
- [ ] Đã có kế hoạch rollback chi tiết
- [ ] Đã backup đầy đủ
- [ ] Đã có maintenance window
- [ ] Đã được Lãnh đạo Công ty phê duyệt

### A2: Dịch chuyển và tách cụm

#### A2.1 - Dịch chuyển/Chuyển đổi hạ tầng
- [ ] Đã lập kế hoạch chi tiết
- [ ] Đã test trên môi trường test
- [ ] Đã có kế hoạch rollback
- [ ] Đã backup đầy đủ
- [ ] Đã được Lãnh đạo Công ty phê duyệt

#### A2.2 - Tách cụm (Cluster Splitting)
- [ ] Đã lập kế hoạch chi tiết
- [ ] Đã test trên môi trường test
- [ ] Đã có kế hoạch rollback
- [ ] Đã backup đầy đủ
- [ ] Đã được Lãnh đạo Công ty phê duyệt

#### A2.3 - Tách cụm để giảm tải DB và APP
- [ ] Đã xác định sự cố cần xử lý khẩn
- [ ] Đã lập kế hoạch nhanh
- [ ] Đã có kế hoạch rollback
- [ ] Đã backup đầy đủ
- [ ] Đã được Lãnh đạo Công ty phê duyệt khẩn

### A3: Cấu hình mạng và bảo mật

#### A3.1 - Thay đổi cấu hình mạng
- [ ] Đã lập kế hoạch chi tiết
- [ ] Đã test trên môi trường test
- [ ] Đã có kế hoạch rollback
- [ ] Đã backup cấu hình mạng
- [ ] Đã được Lãnh đạo Công ty phê duyệt

#### A3.2 - Thay đổi CDN/load balancer
- [ ] Đã lập kế hoạch
- [ ] Đã test trên môi trường test
- [ ] Đã có kế hoạch rollback
- [ ] Đã backup cấu hình

#### A3.3 - Block IP theo yêu cầu
- [ ] Đã xác nhận IP cần block
- [ ] Đã kiểm tra không ảnh hưởng IP hợp lệ
- [ ] Đã backup cấu hình firewall

#### A3.4 - Cập nhật phần mềm ATBM
- [ ] Đã kiểm tra version mới
- [ ] Đã test trên môi trường test
- [ ] Đã có kế hoạch rollback

### A4: Quản lý tài nguyên và giám sát

#### A4.1 - Thay đổi hệ thống giám sát
- [ ] Đã kiểm tra không ảnh hưởng monitoring
- [ ] Đã test cấu hình mới
- [ ] Đã backup cấu hình

#### A4.2 - Tăng dung lượng ổ cứng
- [ ] Đã kiểm tra dung lượng hiện tại
- [ ] Đã xác định dung lượng cần tăng
- [ ] Đã có kế hoạch mở rộng
- [ ] Đã backup dữ liệu

#### A4.3 - Thay đổi tài nguyên (RAM, CPU)
- [ ] Đã kiểm tra tài nguyên hiện tại
- [ ] Đã xác định tài nguyên cần thay đổi
- [ ] Đã có kế hoạch thay đổi
- [ ] Đã test trên môi trường test

#### A4.4 - Restart VM
- [ ] Đã kiểm tra không có job đang chạy
- [ ] Đã thông báo team
- [ ] Đã có kế hoạch restart
- [ ] Đã kiểm tra sau restart

#### A4.5 - Cài đặt/nâng cấp công cụ quản trị
- [ ] Đã kiểm tra version mới
- [ ] Đã test trên môi trường test
- [ ] Đã có kế hoạch rollback
- [ ] Đã được Lãnh đạo Công ty phê duyệt

### A5: Cấu hình hệ thống

#### A5.1 - Thay đổi cấu hình Domain
- [ ] Đã kiểm tra cấu hình hiện tại
- [ ] Đã test trên môi trường test
- [ ] Đã backup cấu hình

#### A5.2 - Thay đổi tham số cấu hình hệ thống
- [ ] Đã kiểm tra tham số hiện tại
- [ ] Đã test trên môi trường test
- [ ] Đã backup cấu hình

#### A5.3 - Thay đổi cấu hình backup
- [ ] Đã kiểm tra cấu hình backup hiện tại
- [ ] Đã test backup mới
- [ ] Đã backup cấu hình
- [ ] Đã test restore

---

## LƯU Ý ĐẶC BIỆT

### Cho thay đổi rủi ro cao/nghiêm trọng

- [ ] Phải có maintenance window
- [ ] Phải có kế hoạch rollback chi tiết
- [ ] Phải test kỹ trên môi trường test
- [ ] Phải có người giám sát 24/7
- [ ] Phải có communication plan

### Cho thay đổi khẩn

- [ ] Phải có kế hoạch nhanh nhưng đầy đủ
- [ ] Phải có kế hoạch rollback
- [ ] Phải backup đầy đủ
- [ ] Phải ghi log đầy đủ
- [ ] Phải bổ sung hồ sơ sau

---

**Tham chiếu**:
- `QT-008-DANH_SACH_THAY_DOI_CHUAN.md`: Danh sách thay đổi chuẩn
- `QT-003-UPCODE.md`: Quy trình Upcode
- `QT-005-PROVISIONING.md`: Quy trình Provisioning

---

**Phiên bản**: 1.0

