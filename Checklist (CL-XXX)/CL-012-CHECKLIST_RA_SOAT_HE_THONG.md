# CL-012: CHECKLIST RÀ SOÁT HỆ THỐNG

**Mã checklist**: CL-012 
**Tham chiếu**: `QT-010-RA_SOAT_HE_THONG_AUDIT.md`

---

## CHECKLIST TRƯỚC RÀ SOÁT

### Bước 1: Lập kế hoạch rà soát

- [ ] Đã xác định mục đích rà soát
- [ ] Đã xác định phạm vi rà soát (hệ thống, quy trình, thời gian)
- [ ] Đã xác định thời gian rà soát
- [ ] Đã xác định người thực hiện
- [ ] Đã xác định tài liệu cần thu thập
- [ ] Đã lập kế hoạch chi tiết
- [ ] Đã xác định phương pháp rà soát

### Bước 2: Phê duyệt kế hoạch

- [ ] Đã gửi kế hoạch cho IT Manager
- [ ] Đã gửi kế hoạch cho Ban CLGSP (nếu cần)
- [ ] Đã nhận được phê duyệt
- [ ] Đã cập nhật kế hoạch theo phản hồi (nếu có)

---

## CHECKLIST TRONG RÀ SOÁT

### Bước 3: Thu thập dữ liệu

#### 3.1. Thu thập dữ liệu quyền truy cập

- [ ] Danh sách tất cả tài khoản
- [ ] Tài khoản đang hoạt động
- [ ] Tài khoản không hoạt động
- [ ] Tài khoản có quyền admin
- [ ] Tài khoản service account
- [ ] Tài khoản của nhân viên đã nghỉ việc
- [ ] Quyền của từng tài khoản
- [ ] Quyền không được sử dụng
- [ ] Quyền tạm thời đã hết hạn
- [ ] Lịch sử cấp quyền
- [ ] Lịch sử sử dụng quyền
- [ ] Audit log quyền truy cập
- [ ] Tài khoản admin có MFA
- [ ] Tài khoản có quyền cao có MFA

#### 3.2. Thu thập dữ liệu quy trình

- [ ] RFC đã được tạo (QT-003)
- [ ] Hotfix Request đã được tạo (QT-004)
- [ ] Release Note đã được tạo (QT-007)
- [ ] Provisioning Request đã được tạo (QT-005)
- [ ] Checklist đã được sử dụng
- [ ] Template đã được điền
- [ ] Ghi nhận deployment
- [ ] Ghi nhận rollback
- [ ] Ghi nhận cấp quyền
- [ ] Ghi nhận sự cố

#### 3.3. Thu thập dữ liệu bảo mật

- [ ] Security scan report
- [ ] Vulnerability scan report
- [ ] Patch management report
- [ ] Incident report
- [ ] Cấu hình firewall
- [ ] Cấu hình network
- [ ] Cấu hình server
- [ ] Cấu hình database
- [ ] Cấu hình cloud
- [ ] Danh sách patch bảo mật đã cài đặt
- [ ] Danh sách update hệ thống

#### 3.4. Thu thập dữ liệu tuân thủ

- [ ] Compliance report
- [ ] Audit trail
- [ ] Access review report
- [ ] Change log
- [ ] ISO 27001 compliance evidence
- [ ] GDPR compliance evidence
- [ ] SOC 2 compliance evidence
- [ ] PCI DSS compliance evidence (nếu có)

#### 3.5. Thu thập dữ liệu tài liệu

- [ ] Tài liệu quy trình đầy đủ
- [ ] Tài liệu quy trình được cập nhật
- [ ] Ghi nhận đầy đủ

### Bước 4: Phân tích dữ liệu

- [ ] Đã phân tích dữ liệu quyền truy cập
- [ ] Đã phân tích dữ liệu quy trình
- [ ] Đã phân tích dữ liệu bảo mật
- [ ] Đã phân tích dữ liệu tuân thủ
- [ ] Đã phân tích dữ liệu tài liệu
- [ ] Đã xác định vấn đề
- [ ] Đã đánh giá mức độ nghiêm trọng
- [ ] Đã ghi nhận kết quả

### Bước 5: Xác định vấn đề

#### 5.1. Vấn đề quyền truy cập

- [ ] Tài khoản không có owner rõ ràng
- [ ] Tài khoản không hoạt động chưa được khóa
- [ ] Tài khoản của nhân viên nghỉ việc chưa được thu hồi
- [ ] Tài khoản admin chưa được rà soát định kỳ
- [ ] Service account được sử dụng để đăng nhập
- [ ] Quyền không phù hợp với vai trò
- [ ] Quyền không được sử dụng chưa được thu hồi
- [ ] Quyền tạm thời đã hết hạn chưa được thu hồi
- [ ] Quyền dư thừa
- [ ] Tài khoản admin chưa có MFA
- [ ] Tài khoản có quyền cao chưa có MFA

#### 5.2. Vấn đề quy trình

- [ ] Deployment không có RFC
- [ ] Deployment không được phê duyệt
- [ ] Deployment không có test
- [ ] Deployment không có rollback plan
- [ ] Deployment không được ghi log
- [ ] Quy trình không được tuân thủ
- [ ] Tài liệu không đầy đủ
- [ ] Ghi nhận không đầy đủ
- [ ] Thiếu checklist
- [ ] Thiếu template

#### 5.3. Vấn đề bảo mật

- [ ] Cấu hình không tuân thủ best practices
- [ ] Có lỗ hổng bảo mật
- [ ] Encryption chưa được sử dụng đúng cách
- [ ] Access control chưa được cấu hình đúng
- [ ] Patch bảo mật quan trọng chưa được cài đặt
- [ ] Hệ thống chưa được update
- [ ] Vulnerability scan chưa được thực hiện định kỳ
- [ ] Security scan chưa được thực hiện định kỳ

#### 5.4. Vấn đề tuân thủ

- [ ] Không tuân thủ ISO 27001
- [ ] Không tuân thủ GDPR
- [ ] Không tuân thủ SOC 2
- [ ] Không tuân thủ PCI DSS (nếu có)
- [ ] Thiếu tài liệu compliance
- [ ] Thiếu bằng chứng tuân thủ

#### 5.5. Vấn đề tài liệu

- [ ] Thiếu tài liệu quy trình
- [ ] Tài liệu quy trình chưa được cập nhật
- [ ] Tài liệu không phản ánh đúng quy trình thực tế
- [ ] Thiếu ghi nhận
- [ ] Ghi nhận không đầy đủ
- [ ] Ghi nhận không được lưu trữ đúng cách
- [ ] Ghi nhận không thể truy vết

---

## CHECKLIST SAU RÀ SOÁT

### Bước 6: Tạo báo cáo

- [ ] Đã tổng hợp kết quả rà soát
- [ ] Đã phân loại vấn đề
- [ ] Đã đánh giá mức độ nghiêm trọng
- [ ] Đã đề xuất cải thiện
- [ ] Đã tạo báo cáo chi tiết (sử dụng TP-007)
- [ ] Đã review báo cáo
- [ ] Đã cập nhật báo cáo theo phản hồi

### Bước 7: Review và phê duyệt báo cáo

- [ ] Đã gửi báo cáo cho IT Manager
- [ ] Đã gửi báo cáo cho Ban CLGSP (nếu cần)
- [ ] Đã nhận được review
- [ ] Đã cập nhật báo cáo theo phản hồi
- [ ] Đã nhận được phê duyệt

### Bước 8: Lập kế hoạch hành động

- [ ] Đã ưu tiên các vấn đề
- [ ] Đã lập kế hoạch khắc phục (sử dụng TP-008)
- [ ] Đã xác định người chịu trách nhiệm
- [ ] Đã xác định thời hạn
- [ ] Đã phê duyệt kế hoạch

### Bước 9: Thực hiện cải thiện

- [ ] Đã thực hiện các cải thiện theo kế hoạch
- [ ] Đã ghi nhận tiến độ
- [ ] Đã báo cáo tiến độ định kỳ
- [ ] Đã kiểm tra kết quả

### Bước 10: Kiểm tra và đóng

- [ ] Đã kiểm tra kết quả cải thiện
- [ ] Đã xác nhận vấn đề đã được khắc phục
- [ ] Đã cập nhật tài liệu
- [ ] Đã đóng rà soát
- [ ] Đã lưu trữ tài liệu

---

## CHECKLIST RÀ SOÁT QUYỀN TRUY CẬP

### Rà soát tài khoản

- [ ] Tất cả tài khoản đều có owner rõ ràng
- [ ] Tài khoản không hoạt động đã được khóa
- [ ] Tài khoản của nhân viên nghỉ việc đã được thu hồi trong 24 giờ
- [ ] Tài khoản admin đã được rà soát định kỳ
- [ ] Service account không được sử dụng để đăng nhập

### Rà soát quyền

- [ ] Quyền phù hợp với vai trò (RBAC)
- [ ] Quyền không được sử dụng đã được thu hồi
- [ ] Quyền tạm thời đã hết hạn đã được thu hồi
- [ ] Không có quyền dư thừa
- [ ] Tuân thủ nguyên tắc Least Privilege

### Rà soát MFA

- [ ] 100% tài khoản admin có MFA
- [ ] 100% tài khoản có quyền cao có MFA
- [ ] MFA được kích hoạt đúng cách

---

## CHECKLIST RÀ SOÁT QUY TRÌNH

### Rà soát quy trình triển khai

- [ ] Tất cả deployment đều có RFC
- [ ] Tất cả deployment đều được phê duyệt
- [ ] Tất cả deployment đều có test
- [ ] Tất cả deployment đều có rollback plan
- [ ] Tất cả deployment đều được ghi log

### Rà soát quy trình quản trị

- [ ] Quy trình được tuân thủ
- [ ] Tài liệu đầy đủ
- [ ] Ghi nhận đầy đủ
- [ ] Có checklist và template

---

## CHECKLIST RÀ SOÁT BẢO MẬT

### Rà soát cấu hình bảo mật

- [ ] Cấu hình tuân thủ best practices
- [ ] Không có lỗ hổng bảo mật
- [ ] Encryption được sử dụng đúng cách
- [ ] Access control được cấu hình đúng

### Rà soát patch và update

- [ ] Tất cả patch bảo mật quan trọng đã được cài đặt
- [ ] Hệ thống đã được update lên phiên bản mới nhất (nếu có thể)
- [ ] Vulnerability scan được thực hiện định kỳ
- [ ] Security scan được thực hiện định kỳ

---

## CHECKLIST RÀ SOÁT TUÂN THỦ

### Rà soát tuân thủ ISO 27001

- [ ] Tuân thủ các control của ISO 27001
- [ ] Tài liệu đầy đủ
- [ ] Ghi nhận đầy đủ
- [ ] Có bằng chứng tuân thủ

### Rà soát tuân thủ GDPR

- [ ] Quyền truy cập dữ liệu cá nhân được kiểm soát
- [ ] Tất cả truy cập dữ liệu cá nhân đều được ghi log
- [ ] Có quy trình xóa dữ liệu cá nhân
- [ ] Có quy trình báo cáo data breach trong 72 giờ

### Rà soát tuân thủ SOC 2

- [ ] Access controls được implement và monitor
- [ ] Changes được authorized
- [ ] Access reviews được thực hiện định kỳ
- [ ] Audit logs được maintain

---

## CHECKLIST RÀ SOÁT TÀI LIỆU

### Rà soát tài liệu quy trình

- [ ] Tất cả quy trình đều có tài liệu
- [ ] Tài liệu được cập nhật định kỳ
- [ ] Tài liệu phản ánh đúng quy trình thực tế

### Rà soát ghi nhận

- [ ] Tất cả hoạt động quan trọng đều được ghi nhận
- [ ] Ghi nhận đầy đủ thông tin
- [ ] Ghi nhận được lưu trữ đúng cách
- [ ] Ghi nhận có thể truy vết

---

**Phiên bản**: 1.0 
**Ngày ban hành**: [Ngày hiện tại] 
**Người soạn**: 
**Trạng thái**: Chính thức
