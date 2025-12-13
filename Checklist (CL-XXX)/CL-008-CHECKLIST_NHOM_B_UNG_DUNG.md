# CL-008: CHECKLIST NHÓM B - ỨNG DỤNG

**Mã checklist**: CL-008  
**Tham chiếu**: `QT-008-DANH_SACH_THAY_DOI_CHUAN.md` - Nhóm B

---

## TỔNG QUAN

Nhóm B bao gồm 28 loại thay đổi liên quan đến ứng dụng:
- B1: Giao diện và nội dung (6 loại)
- B2: Chức năng nghiệp vụ (9 loại)
- B3: Kỹ thuật và tích hợp (10 loại)
- B4: Sửa lỗi và bảo mật (4 loại)
- B5: Nâng cấp sản phẩm (1 loại)

---

## CHECKLIST CHUNG CHO NHÓM B

### Trước khi thực hiện

- [ ] Đã tra cứu mã thay đổi trong QT-008
- [ ] Code đã được review
- [ ] Code đã được test (unit test, integration test)
- [ ] Đã xác định mức độ rủi ro
- [ ] Đã xác định cấp độ phê duyệt
- [ ] Đã lập kế hoạch triển khai
- [ ] Đã lập kế hoạch rollback
- [ ] Đã backup code và database
- [ ] Đã thông báo team liên quan

### Trong khi thực hiện

- [ ] Đã deploy code
- [ ] Đã chạy migration (nếu cần)
- [ ] Đã kiểm tra deployment
- [ ] Đã smoke test
- [ ] Đã ghi log đầy đủ

### Sau khi thực hiện

- [ ] Đã kiểm tra ứng dụng hoạt động bình thường
- [ ] Đã kiểm tra log không có lỗi
- [ ] Đã kiểm tra metrics
- [ ] Đã giám sát hệ thống (ít nhất 1 giờ)
- [ ] Đã ghi nhận kết quả
- [ ] Đã thông báo team

---

## CHECKLIST THEO TỪNG LOẠI

### B1: Giao diện và nội dung

#### B1.1 - Sửa lỗi giao diện (UI/UX)
- [ ] Đã test trên nhiều trình duyệt
- [ ] Đã test responsive
- [ ] Đã test accessibility
- [ ] Đã review với designer (nếu cần)

#### B1.2 - Cập nhật pop-up, FAQ
- [ ] Đã review nội dung
- [ ] Đã test hiển thị
- [ ] Đã được Lãnh đạo TT/PDM duyệt

#### B1.3 - Cập nhật hướng dẫn sử dụng
- [ ] Đã review nội dung
- [ ] Đã test hiển thị
- [ ] Đã được Lãnh đạo TT/PDM duyệt

#### B1.4 - Chỉnh sửa phiếu in, báo cáo
- [ ] Đã test in thử
- [ ] Đã kiểm tra format
- [ ] Đã test với dữ liệu thực tế

#### B1.5 - Tạo báo cáo/phiếu in đơn giản
- [ ] Đã thiết kế layout
- [ ] Đã test in thử
- [ ] Đã kiểm tra format

#### B1.6 - Deploy báo cáo đặc thù
- [ ] Đã test kỹ với dữ liệu thực tế
- [ ] Đã test performance
- [ ] Đã được Lãnh đạo TT/PDM duyệt

### B2: Chức năng nghiệp vụ

#### B2.1 - Thêm chức năng nhỏ (rủi ro thấp)
- [ ] Đã test chức năng mới
- [ ] Đã test không ảnh hưởng chức năng cũ
- [ ] Đã review với business

#### B2.2 - Thêm chức năng nhỏ (rủi ro trung bình)
- [ ] Đã test kỹ chức năng mới
- [ ] Đã test regression
- [ ] Đã review với business
- [ ] Đã được Ban CLGSP phê duyệt

#### B2.3 - Thêm module/chức năng mới
- [ ] Đã thiết kế architecture
- [ ] Đã test kỹ
- [ ] Đã review với business
- [ ] Đã được Lãnh đạo TT/PDM duyệt

#### B2.4 - Tắt hoặc ẩn nút chức năng
- [ ] Đã xác nhận với business
- [ ] Đã test không ảnh hưởng chức năng khác
- [ ] Đã được Ban CLGSP phê duyệt

#### B2.5 - Chỉnh sửa chức năng phần mềm
- [ ] Đã test kỹ chức năng mới
- [ ] Đã test regression
- [ ] Đã được Lãnh đạo TT/PDM duyệt

#### B2.6 - Thêm, sửa chức năng chung
- [ ] Đã test kỹ
- [ ] Đã test với nhiều khách hàng
- [ ] Đã được Ban CLGSP phê duyệt

#### B2.7 - Thêm giá trị vào danh mục
- [ ] Đã xác nhận giá trị mới
- [ ] Đã test hiển thị
- [ ] Đã được Lãnh đạo TT/PDM duyệt

#### B2.8 - Chỉnh sửa rules hoặc validation
- [ ] Đã test kỹ rules mới
- [ ] Đã test với dữ liệu thực tế
- [ ] Đã được Ban CLGSP phê duyệt

#### B2.9 - Thay đổi quy trình xác thực
- [ ] Đã test kỹ quy trình mới
- [ ] Đã test security
- [ ] Đã review với security team

### B3: Kỹ thuật và tích hợp

#### B3.1, B3.2 - Thay đổi thư viện (Lib)
- [ ] Đã kiểm tra compatibility
- [ ] Đã test kỹ
- [ ] Đã test regression
- [ ] Đã được Ban CLGSP phê duyệt

#### B3.3 - Thay đổi phiên bản runtime
- [ ] Đã kiểm tra compatibility
- [ ] Đã test kỹ
- [ ] Đã test regression
- [ ] Đã có kế hoạch rollback

#### B3.4 - Tái cấu trúc code (Refactor)
- [ ] Đã test kỹ
- [ ] Đã test regression
- [ ] Đã review code
- [ ] Đã được Ban CLGSP, Ban KTHT phê duyệt

#### B3.5 - Thay đổi logging/exception
- [ ] Đã test logging mới
- [ ] Đã kiểm tra không ảnh hưởng performance
- [ ] Đã test exception handling

#### B3.6 - Cập nhật license phần mềm
- [ ] Đã kiểm tra license mới
- [ ] Đã test compatibility
- [ ] Đã có kế hoạch rollback

#### B3.7 - Thêm module mới hoặc plugin
- [ ] Đã test kỹ module mới
- [ ] Đã test integration
- [ ] Đã test performance

#### B3.8 - Thay đổi pipeline CI/CD
- [ ] Đã test pipeline mới
- [ ] Đã test trên môi trường test
- [ ] Đã được Ban CLGSP phê duyệt

#### B3.9 - Tích hợp hệ thống ngoài
- [ ] Đã test integration
- [ ] Đã test error handling
- [ ] Đã test security
- [ ] Đã có kế hoạch rollback

#### B3.10 - Tối ưu câu lệnh chậm (DB)
- [ ] Đã xác định câu lệnh cần tối ưu
- [ ] Đã test performance
- [ ] Đã test không ảnh hưởng kết quả
- [ ] Đã được Lãnh đạo TT/PDM duyệt

### B4: Sửa lỗi và bảo mật

#### B4.1 - Sửa lỗi (bug fixing)
- [ ] Đã xác định root cause
- [ ] Đã test fix
- [ ] Đã test regression
- [ ] Đã test không tạo bug mới

#### B4.2 - Code lỗi cần hotfix luôn
- [ ] Đã xác định lỗi nghiêm trọng
- [ ] Đã test fix nhanh
- [ ] Đã có kế hoạch rollback
- [ ] Đã được Lãnh đạo TT/PDM duyệt khẩn

#### B4.3 - Xử lý lỗi ATBM (Rủi ro Thấp)
- [ ] Đã xác định lỗ hổng
- [ ] Đã test fix
- [ ] Đã test security
- [ ] Đã được Lãnh đạo TT/PDM duyệt

#### B4.4 - Xử lý lỗ hổng bảo mật nghiêm trọng
- [ ] Đã xác định lỗ hổng nghiêm trọng
- [ ] Đã test fix kỹ
- [ ] Đã test security
- [ ] Đã có kế hoạch rollback
- [ ] Đã được phê duyệt theo quy mô

### B5: Nâng cấp sản phẩm

#### B5.1 - Nâng cấp phiên bản sản phẩm
- [ ] Đã lập kế hoạch nâng cấp chi tiết
- [ ] Đã test kỹ trên môi trường test
- [ ] Đã có kế hoạch rollback
- [ ] Đã backup đầy đủ
- [ ] Đã được Lãnh đạo Công ty phê duyệt

---

## LƯU Ý ĐẶC BIỆT

### Cho thay đổi code

- [ ] Code phải được review
- [ ] Code phải được test đầy đủ
- [ ] Phải có kế hoạch rollback
- [ ] Phải backup code và database

### Cho thay đổi tích hợp

- [ ] Phải test integration kỹ
- [ ] Phải test error handling
- [ ] Phải test security
- [ ] Phải có kế hoạch rollback

### Cho thay đổi bảo mật

- [ ] Phải test security kỹ
- [ ] Phải review với security team
- [ ] Phải có kế hoạch rollback
- [ ] Phải ưu tiên xử lý

---

**Tham chiếu**:
- `QT-008-DANH_SACH_THAY_DOI_CHUAN.md`: Danh sách thay đổi chuẩn
- `QT-003-UPCODE.md`: Quy trình Upcode
- `QT-004-HOTFIX.md`: Quy trình Hotfix

---

**Phiên bản**: 1.0

