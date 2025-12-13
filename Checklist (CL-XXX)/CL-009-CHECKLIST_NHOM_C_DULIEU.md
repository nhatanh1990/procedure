# CL-009: CHECKLIST NHÓM C - DỮ LIỆU & CẤU HÌNH

**Mã checklist**: CL-009  
**Tham chiếu**: `QT-008-DANH_SACH_THAY_DOI_CHUAN.md` - Nhóm C

---

## TỔNG QUAN

Nhóm C bao gồm 7 loại thay đổi liên quan đến dữ liệu và cấu hình:
- C1: Cấu trúc dữ liệu (1 loại)
- C2: Cấu hình nghiệp vụ (3 loại)
- C3: Quản lý người dùng và quyền (3 loại)

---

## CHECKLIST CHUNG CHO NHÓM C

### Trước khi thực hiện

- [ ] Đã tra cứu mã thay đổi trong QT-008
- [ ] Đã backup database (nếu liên quan)
- [ ] Đã backup cấu hình
- [ ] Đã xác định mức độ rủi ro
- [ ] Đã xác định cấp độ phê duyệt
- [ ] Đã lập kế hoạch triển khai
- [ ] Đã lập kế hoạch rollback
- [ ] Đã thông báo team liên quan

### Trong khi thực hiện

- [ ] Đã thực hiện theo kế hoạch
- [ ] Đã ghi log đầy đủ
- [ ] Đã kiểm tra từng bước
- [ ] Đã xử lý lỗi (nếu có)

### Sau khi thực hiện

- [ ] Đã kiểm tra dữ liệu/cấu hình đúng
- [ ] Đã kiểm tra hệ thống hoạt động bình thường
- [ ] Đã kiểm tra log không có lỗi
- [ ] Đã ghi nhận kết quả
- [ ] Đã thông báo team

---

## CHECKLIST THEO TỪNG LOẠI

### C1: Cấu trúc dữ liệu

#### C1.1 - Thay đổi cấu trúc CSDL (schema/index/migration)
- [ ] Đã backup database đầy đủ
- [ ] Đã test migration trên môi trường test
- [ ] Đã test rollback migration
- [ ] Đã kiểm tra không ảnh hưởng dữ liệu hiện có
- [ ] Đã test performance sau migration
- [ ] Đã được Ban CLGSP phê duyệt
- [ ] Đã có maintenance window (nếu cần)

**Lưu ý đặc biệt**:
- Migration phải được test kỹ
- Phải có kế hoạch rollback migration
- Phải backup database trước khi migration
- Phải test với dữ liệu thực tế

### C2: Cấu hình nghiệp vụ

#### C2.1 - Cấu hình hệ thống chuẩn
- [ ] Đã xác định cấu hình cần thay đổi
- [ ] Đã test cấu hình mới trên môi trường test
- [ ] Đã backup cấu hình cũ
- [ ] Đã được Ban CLGSP phê duyệt

#### C2.2 - Config cấu hình tự động
- [ ] Đã xác định cấu hình cần tự động hóa
- [ ] Đã test config tự động trên môi trường test
- [ ] Đã backup cấu hình cũ
- [ ] Đã được Ban CLGSP phê duyệt

#### C2.3 - Thêm giá trị vào danh mục
- [ ] Đã xác nhận giá trị mới
- [ ] Đã kiểm tra không trùng lặp
- [ ] Đã test hiển thị
- [ ] Đã được Lãnh đạo TT/PDM duyệt

### C3: Quản lý người dùng và quyền

#### C3.1 - Change liên quan tài khoản
- [ ] Đã xác nhận thay đổi cần thực hiện
- [ ] Đã kiểm tra quyền hiện tại
- [ ] Đã test thay đổi trên môi trường test
- [ ] Đã backup thông tin tài khoản

**Lưu ý**:
- Tuân thủ chính sách quyền truy cập tối thiểu
- Ghi log đầy đủ
- Thông báo cho người dùng (nếu cần)

#### C3.2 - Mở khóa tài khoản (sai MK)
- [ ] Đã xác nhận yêu cầu từ người dùng
- [ ] Đã xác minh danh tính người dùng
- [ ] Đã mở khóa tài khoản
- [ ] Đã yêu cầu người dùng đổi mật khẩu
- [ ] Đã được Lãnh đạo TT/PDM duyệt

**Lưu ý**:
- Phải xác minh danh tính người dùng
- Phải yêu cầu đổi mật khẩu sau khi mở khóa
- Ghi log đầy đủ

#### C3.3 - Gán/Thu Hồi Quyền Truy Cập
- [ ] Đã xác nhận quyền cần gán/thu hồi
- [ ] Đã kiểm tra quyền hiện tại
- [ ] Đã test trên môi trường test
- [ ] Đã backup thông tin quyền
- [ ] Đã được Lãnh đạo TT/PDM duyệt

**Lưu ý**:
- Tuân thủ chính sách quyền truy cập tối thiểu
- Ghi log đầy đủ
- Thông báo cho người dùng
- Tham chiếu: `QT/CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU.md`

---

## LƯU Ý ĐẶC BIỆT

### Cho thay đổi database

- [ ] Phải backup database trước khi thay đổi
- [ ] Phải test migration trên môi trường test
- [ ] Phải có kế hoạch rollback migration
- [ ] Phải test với dữ liệu thực tế
- [ ] Phải có maintenance window (nếu cần)

### Cho thay đổi cấu hình

- [ ] Phải backup cấu hình cũ
- [ ] Phải test cấu hình mới trên môi trường test
- [ ] Phải có kế hoạch rollback
- [ ] Phải ghi log đầy đủ

### Cho thay đổi quyền

- [ ] Phải tuân thủ chính sách quyền truy cập tối thiểu
- [ ] Phải ghi log đầy đủ
- [ ] Phải thông báo cho người dùng
- [ ] Phải xác minh danh tính (nếu cần)

---

**Tham chiếu**:
- `QT-008-DANH_SACH_THAY_DOI_CHUAN.md`: Danh sách thay đổi chuẩn
- `QT-003-UPCODE.md`: Quy trình Upcode
- `QT/CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU.md`: Chính sách quyền truy cập

---

**Phiên bản**: 1.0

