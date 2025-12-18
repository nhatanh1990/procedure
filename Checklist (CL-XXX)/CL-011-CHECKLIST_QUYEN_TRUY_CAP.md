# CL-011: CHECKLIST QUYỀN TRUY CẬP TỐI THIỂU

**Mã checklist**: CL-011 
**Tham chiếu**: `CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU.md`

---

## CHECKLIST CẤP QUYỀN

### Bước 1: Yêu cầu quyền

- [ ] Đã xác định role/quyền cần thiết
- [ ] Đã mô tả lý do cần quyền rõ ràng
- [ ] Đã xác định thời gian cần quyền (vĩnh viễn/tạm thời)
- [ ] Đã xác định hệ thống cần quyền
- [ ] Đã tạo yêu cầu trong hệ thống quản lý quyền
- [ ] Đã điền đầy đủ thông tin trong template yêu cầu

### Bước 2: Phê duyệt

- [ ] Đã xác định cấp độ phê duyệt (Level 1.0-4.0)
- [ ] Đã gửi yêu cầu cho người phê duyệt đúng cấp
- [ ] Đã nhận được phê duyệt
- [ ] Đã kiểm tra tính hợp lý của yêu cầu

### Bước 3: Cấp quyền

- [ ] Đã cấp quyền theo role đã định nghĩa
- [ ] Đã kiểm tra không cấp quyền dư thừa
- [ ] Đã thiết lập thời gian hết hạn (nếu tạm thời)
- [ ] Đã cấu hình IP whitelist (nếu cần)
- [ ] Đã cấu hình MFA (nếu cần)
- [ ] Đã ghi log đầy đủ

### Bước 4: Thông báo

- [ ] Đã thông báo cho người dùng
- [ ] Đã thông báo cho quản lý
- [ ] Đã cung cấp hướng dẫn sử dụng (nếu cần)

---

## CHECKLIST RÀ SOÁT QUYỀN

### Thu thập dữ liệu

- [ ] Danh sách tài khoản đã được thu thập
- [ ] Danh sách quyền của từng tài khoản đã được thu thập
- [ ] Lịch sử sử dụng quyền đã được thu thập
- [ ] Log truy cập đã được thu thập

### Phân tích

- [ ] Quyền không cần thiết đã được xác định
- [ ] Quyền chưa sử dụng đã được xác định
- [ ] Quyền tạm thời đã hết hạn đã được xác định
- [ ] Tài khoản không hoạt động đã được xác định
- [ ] Tài khoản admin không dùng đã được xác định

### Đề xuất

- [ ] Đề xuất thu hồi quyền không cần thiết đã được tạo
- [ ] Đề xuất khóa tài khoản không hoạt động đã được tạo
- [ ] Đề xuất điều chỉnh quyền đã được tạo
- [ ] Đề xuất đã được gửi cho quản lý

### Thực hiện

- [ ] Quản lý đã phê duyệt đề xuất
- [ ] IT đã thực hiện thu hồi/điều chỉnh
- [ ] Log đã được ghi đầy đủ
- [ ] Người dùng đã được thông báo

---

## CHECKLIST CẤP QUYỀN TẠM THỜI (JIT)

### Yêu cầu

- [ ] Đã mô tả lý do cần quyền tạm thời
- [ ] Đã xác định thời gian cần quyền (thường 1-2 giờ)
- [ ] Đã xác định quyền cụ thể cần
- [ ] Đã tạo yêu cầu trong hệ thống

### Phê duyệt

- [ ] Đã gửi yêu cầu cho người phê duyệt
- [ ] Đã nhận được phê duyệt

### Cấp quyền

- [ ] Đã cấp quyền theo role
- [ ] Đã thiết lập thời gian hết hạn tự động
- [ ] Đã ghi log đầy đủ
- [ ] Đã thông báo cho người dùng

### Thu hồi

- [ ] Đã thu hồi quyền sau khi hoàn thành
- [ ] Đã kiểm tra quyền đã được thu hồi
- [ ] Đã ghi log thu hồi

---

## CHECKLIST THIẾT LẬP MFA

### Chuẩn bị

- [ ] Đã xác định loại tài khoản cần MFA
- [ ] Đã chọn phương thức MFA (TOTP/SMS)
- [ ] Đã cài đặt ứng dụng MFA (nếu TOTP)

### Thiết lập

- [ ] Đã quét QR code hoặc nhập secret key
- [ ] Đã xác nhận bằng mã MFA
- [ ] Đã lưu backup codes
- [ ] Đã test MFA hoạt động đúng

### Hoàn tất

- [ ] MFA đã được kích hoạt
- [ ] Backup codes đã được lưu trữ an toàn
- [ ] Đã thông báo cho IT (nếu cần)

---

## CHECKLIST QUYỀN MÁY CHỦ (SSH/SUDO)

### Cấp quyền SSH

- [ ] Đã xác định máy chủ cần truy cập
- [ ] Đã xác định quyền cần (read-only/read-write)
- [ ] Đã tạo tài khoản riêng (không dùng chung)
- [ ] Đã cấu hình SSH key (không dùng password)
- [ ] Đã cấu hình IP whitelist (nếu cần)
- [ ] Đã ghi log đầy đủ

### Cấp quyền sudo

- [ ] Đã xác định lệnh cụ thể cần sudo
- [ ] Đã cấu hình sudo với quyền cụ thể (không sudo su)
- [ ] Đã cấu hình timeout (15 phút)
- [ ] Đã cấu hình ghi log
- [ ] Đã cấu hình MFA (nếu có thể)
- [ ] Đã test sudo hoạt động đúng

---

## CHECKLIST QUYỀN DATABASE

### Cấp quyền database

- [ ] Đã xác định database cần truy cập
- [ ] Đã xác định role cần (ReadOnly/ReadWrite/DBAdmin)
- [ ] Đã cấp quyền theo role
- [ ] Đã cấu hình IP whitelist
- [ ] Đã cấu hình SSL/TLS encryption
- [ ] Đã cấu hình VPN (nếu truy cập từ xa)
- [ ] Đã ghi log đầy đủ

### Kiểm tra

- [ ] Đã test kết nối database
- [ ] Đã test quyền hoạt động đúng
- [ ] Đã kiểm tra không có quyền dư thừa

---

## CHECKLIST QUYỀN DEPLOY

### Kiểm tra quyền deploy

- [ ] Đã xác định môi trường cần deploy (Staging/Production/DR)
- [ ] Đã kiểm tra role có quyền deploy không
- [ ] Đã có phê duyệt (nếu deploy Production/DR)
- [ ] Đã có RFC/Change Request (nếu cần)

### Thực hiện deploy

- [ ] Đã sử dụng tài khoản đúng role
- [ ] Đã ghi log đầy đủ
- [ ] Đã thu hồi quyền tạm thời sau khi deploy (nếu có)

---

## CHECKLIST RÀ SOÁT ĐỊNH KỲ

### Rà soát hàng tháng (Quyền admin)

- [ ] Đã thu thập danh sách tài khoản admin
- [ ] Đã kiểm tra lịch sử sử dụng quyền admin
- [ ] Đã xác định tài khoản admin không sử dụng
- [ ] Đã đề xuất thu hồi/điều chỉnh
- [ ] Đã thực hiện thu hồi/điều chỉnh

### Rà soát hàng quý (Toàn bộ tài khoản)

- [ ] Đã thu thập danh sách tất cả tài khoản
- [ ] Đã kiểm tra quyền của từng tài khoản
- [ ] Đã xác định quyền không cần thiết
- [ ] Đã xác định tài khoản không hoạt động
- [ ] Đã đề xuất thu hồi/điều chỉnh
- [ ] Đã thực hiện thu hồi/điều chỉnh

### Rà soát hàng tuần (Quyền tạm thời)

- [ ] Đã kiểm tra quyền tạm thời đã hết hạn
- [ ] Đã thu hồi quyền đã hết hạn
- [ ] Đã ghi log thu hồi

---

## CHECKLIST XỬ LÝ TÀI KHOẢN NGHỈ VIỆC

### Khi nhận thông báo nghỉ việc

- [ ] Đã xác định tất cả tài khoản của người nghỉ việc
- [ ] Đã thu hồi tất cả quyền trong vòng 24 giờ
- [ ] Đã khóa tất cả tài khoản
- [ ] Đã ghi log đầy đủ
- [ ] Đã thông báo cho quản lý

---

## CHECKLIST KIỂM TRA BẢO MẬT

### Kiểm tra định kỳ

- [ ] Đã kiểm tra tài khoản không có MFA (nếu cần)
- [ ] Đã kiểm tra tài khoản dùng password yếu
- [ ] Đã kiểm tra tài khoản không đổi password trong 90 ngày
- [ ] Đã kiểm tra log truy cập bất thường
- [ ] Đã kiểm tra quyền không được sử dụng

---

## CHECKLIST QUYỀN CLOUD/CONTAINER

### Kubernetes RBAC

- [ ] Đã xác định namespace cần quyền
- [ ] Đã tạo Role/ClusterRole (nếu chưa có)
- [ ] Đã tạo RoleBinding/ClusterRoleBinding
- [ ] Đã gán cho Service Account hoặc User
- [ ] Đã test quyền
- [ ] Đã ghi log đầy đủ

### Docker Registry

- [ ] Đã xác định registry và quyền cần
- [ ] Đã tạo user/robot account
- [ ] Đã cấp quyền theo role
- [ ] Đã cấu hình IP whitelist (nếu cần)
- [ ] Đã test quyền
- [ ] Đã ghi log đầy đủ

### Cloud IAM

- [ ] Đã xác định cloud provider và quyền cần
- [ ] Đã tạo IAM role/policy (nếu chưa có)
- [ ] Đã gán role cho user/service account
- [ ] Đã test quyền
- [ ] Đã thiết lập rotation (nếu access keys)
- [ ] Đã ghi log đầy đủ

---

## CHECKLIST QUYỀN API/APPLICATION

### API Key Management

- [ ] Đã yêu cầu API key
- [ ] Đã được phê duyệt
- [ ] Đã tạo API key trong hệ thống
- [ ] Đã cấu hình rate limiting
- [ ] Đã cấu hình IP whitelist (nếu cần)
- [ ] Đã ghi log đầy đủ
- [ ] Đã cung cấp API key qua secure channel

### OAuth/JWT

- [ ] Đã cấu hình OAuth provider
- [ ] Đã cấu hình JWT token expiration
- [ ] Đã cấu hình refresh token
- [ ] Đã test authentication flow
- [ ] Đã test token refresh
- [ ] Đã test token revocation

### Feature Flags

- [ ] Đã tạo feature flag
- [ ] Đã cấu hình permissions
- [ ] Đã test feature flag
- [ ] Đã deploy với feature flag disabled
- [ ] Đã có kế hoạch enable feature flag

---

## CHECKLIST QUẢN LÝ SECRET

### Tạo Secret

- [ ] Đã yêu cầu tạo secret
- [ ] Đã được phê duyệt
- [ ] Đã tạo secret trong secret management tool
- [ ] Đã cấu hình access permissions
- [ ] Đã ghi log đầy đủ
- [ ] Đã thông báo cho người cần

### Truy cập Secret

- [ ] Đã authenticate với secret management tool
- [ ] Đã có proper permissions
- [ ] Đã request secret
- [ ] Đã ghi log truy cập
- [ ] Đã verify secret không được expose trong logs

### Rotation Secret

- [ ] Đã tạo secret mới
- [ ] Đã update application với secret mới
- [ ] Đã verify application hoạt động
- [ ] Đã revoke secret cũ
- [ ] Đã ghi log rotation

### Revoke Secret

- [ ] Đã xác định secret cần revoke
- [ ] Đã được phê duyệt
- [ ] Đã revoke secret
- [ ] Đã update applications
- [ ] Đã ghi log revoke
- [ ] Đã thông báo cho người liên quan

---

## CHECKLIST AUDIT VÀ COMPLIANCE

### Audit Log

- [ ] Đã cấu hình audit logging
- [ ] Đã verify log được ghi đầy đủ
- [ ] Đã cấu hình retention policy
- [ ] Đã backup audit logs
- [ ] Đã cấu hình access control cho audit logs

### Compliance Review

- [ ] Đã xác định compliance requirements
- [ ] Đã review current access controls
- [ ] Đã identify gaps
- [ ] Đã implement controls
- [ ] Đã document controls
- [ ] Đã schedule regular audit

---

## CHECKLIST INCIDENT RESPONSE

### Phát hiện lạm dụng quyền

- [ ] Đã phát hiện lạm dụng quyền
- [ ] Đã đánh giá mức độ nghiêm trọng
- [ ] Đã thu hồi quyền ngay lập tức
- [ ] Đã khóa tài khoản (nếu cần)
- [ ] Đã thu thập evidence
- [ ] Đã phân tích và báo cáo
- [ ] Đã khắc phục và cải thiện

### Thu hồi quyền khẩn cấp

- [ ] Đã xác định tài khoản/quyền cần thu hồi
- [ ] Đã thu hồi quyền ngay lập tức
- [ ] Đã khóa tài khoản (nếu cần)
- [ ] Đã thông báo cho Security Team và IT Manager
- [ ] Đã ghi log đầy đủ
- [ ] Đã báo cáo sau (trong 24 giờ)

### Khôi phục quyền

- [ ] Đã yêu cầu khôi phục quyền
- [ ] Đã được phê duyệt
- [ ] Đã xác minh tài khoản an toàn
- [ ] Đã khôi phục quyền
- [ ] Đã ghi log đầy đủ
- [ ] Đã schedule monitor tài khoản (7 ngày)

---

**Phiên bản**: 2.0

