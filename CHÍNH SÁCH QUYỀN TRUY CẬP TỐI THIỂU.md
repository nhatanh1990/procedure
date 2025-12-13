# CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU (LEAST PRIVILEGE POLICY)
# KẾT HỢP QUY TRÌNH QUẢN TRỊ & VẬN HÀNH HỆ THỐNG

---

## 1. MỤC TIÊU
Chính sách này quy định cách thức cấp quyền, quản lý truy cập và vận hành hệ thống CNTT dựa trên nguyên tắc **Quyền truy cập tối thiểu (Least Privilege)** nhằm:
- Giảm rủi ro bảo mật.
- Ngăn chặn sử dụng sai mục đích quyền truy cập.
- Đảm bảo tính an toàn, toàn vẹn và sẵn sàng của hệ thống.

---

## 1.1. TẠI SAO QUYỀN TRUY CẬP TỐI THIỂU QUAN TRỌNG?

### 🎯 Lợi ích cụ thể

#### 1. Bảo vệ khỏi các mối đe dọa bảo mật
- **Giảm 80-90% rủi ro bị tấn công**: Khi tài khoản bị xâm nhập, kẻ tấn công chỉ có quyền hạn chế, không thể gây thiệt hại lớn
- **Ngăn chặn lateral movement**: Kẻ tấn công không thể di chuyển từ hệ thống này sang hệ thống khác
- **Giảm thiểu thiệt hại khi bị rò rỉ**: Dữ liệu bị rò rỉ chỉ giới hạn trong phạm vi quyền của tài khoản bị xâm nhập

#### 2. Tuân thủ các tiêu chuẩn bảo mật
- **ISO 27001**: Yêu cầu kiểm soát truy cập dựa trên nguyên tắc "need-to-know"
- **GDPR**: Yêu cầu bảo vệ dữ liệu cá nhân, chỉ những người cần thiết mới được truy cập
- **SOC 2**: Yêu cầu kiểm soát truy cập và giám sát hoạt động
- **PCI DSS**: Yêu cầu hạn chế quyền truy cập dữ liệu thẻ tín dụng

#### 3. Giảm thiểu lỗi do con người
- **Giảm 60-70% lỗi vô ý**: Người dùng không thể vô tình xóa hoặc thay đổi dữ liệu quan trọng
- **Bảo vệ khỏi lỗi cấu hình**: Không thể thay đổi cấu hình hệ thống quan trọng một cách vô tình
- **Giảm thiểu downtime**: Tránh các sự cố do thao tác sai với quyền cao

#### 4. Tăng cường khả năng truy vết và trách nhiệm
- **Audit trail rõ ràng**: Dễ dàng xác định ai đã làm gì, khi nào
- **Trách nhiệm rõ ràng**: Mỗi người chỉ chịu trách nhiệm cho các hành động trong phạm vi quyền của mình
- **Điều tra sự cố nhanh chóng**: Dễ dàng xác định nguyên nhân và người liên quan

#### 5. Tối ưu hóa quy trình làm việc
- **Quy trình rõ ràng**: Mọi người biết rõ quyền của mình và cách yêu cầu quyền bổ sung
- **Giảm thời gian chờ đợi**: Quy trình cấp quyền được chuẩn hóa, rõ ràng
- **Tăng hiệu quả**: Người dùng tập trung vào công việc của mình, không bị phân tâm bởi các quyền không cần thiết

#### 6. Bảo vệ danh tiếng và tài chính
- **Tránh vi phạm dữ liệu**: Giảm nguy cơ bị phạt do vi phạm GDPR, PCI DSS
- **Bảo vệ danh tiếng**: Tránh các sự cố bảo mật gây ảnh hưởng đến uy tín công ty
- **Giảm chi phí khắc phục**: Chi phí khắc phục sự cố bảo mật có thể lên đến hàng triệu USD

---

## 1.2. RỦI RO NẾU KHÔNG TUÂN THỦ

### ⚠️ Hậu quả nghiêm trọng

#### 1. Rủi ro bảo mật cao
- **Tài khoản bị xâm nhập = Toàn bộ hệ thống bị đe dọa**: Nếu tài khoản có quyền quá cao bị xâm nhập, kẻ tấn công có thể:
  - Xóa toàn bộ dữ liệu
  - Đánh cắp thông tin nhạy cảm
  - Vô hiệu hóa toàn bộ hệ thống
  - Cài đặt backdoor, malware

#### 2. Vi phạm pháp luật và tiêu chuẩn
- **GDPR**: Phạt lên đến 4% doanh thu hoặc 20 triệu EUR (tùy mức nào cao hơn)
- **PCI DSS**: Mất khả năng xử lý thanh toán thẻ tín dụng
- **ISO 27001**: Mất chứng nhận, ảnh hưởng đến uy tín
- **SOC 2**: Mất chứng nhận, khách hàng mất niềm tin

#### 3. Thiệt hại tài chính
- **Chi phí khắc phục sự cố**: Trung bình $4.45 triệu USD cho mỗi vụ vi phạm dữ liệu (theo IBM Security Report 2023)
- **Mất doanh thu**: Downtime có thể gây thiệt hại hàng triệu USD/giờ
- **Chi phí pháp lý**: Kiện tụng, phạt vi phạm
- **Mất khách hàng**: 60% doanh nghiệp nhỏ phá sản trong vòng 6 tháng sau sự cố bảo mật

#### 4. Thiệt hại danh tiếng
- **Mất niềm tin khách hàng**: 66% khách hàng sẽ không tin tưởng công ty sau sự cố bảo mật
- **Ảnh hưởng đến thương hiệu**: Khó khôi phục danh tiếng sau sự cố
- **Mất đối tác**: Đối tác có thể chấm dứt hợp đồng do lo ngại bảo mật

#### 5. Rủi ro nội bộ
- **Lạm dụng quyền**: Nhân viên có thể sử dụng quyền cao cho mục đích cá nhân
- **Lỗi vô ý**: Xóa nhầm dữ liệu, cấu hình sai hệ thống
- **Khó truy vết**: Không biết ai đã làm gì, khi nào

---

## 1.3. SỐ LIỆU VÀ THỐNG KÊ

### 📊 Bằng chứng về tầm quan trọng

#### Thống kê về vi phạm bảo mật
- **74%** các vụ vi phạm bảo mật liên quan đến quyền truy cập quá cao (Verizon Data Breach Report 2023)
- **80%** các vụ tấn công bắt đầu từ tài khoản bị xâm nhập với quyền quá cao
- **Trung bình 287 ngày** để phát hiện vi phạm bảo mật (IBM Security Report 2023)
- **Chi phí trung bình**: $4.45 triệu USD cho mỗi vụ vi phạm dữ liệu

#### Lợi ích của Least Privilege
- **Giảm 80-90%** rủi ro bị tấn công thành công
- **Giảm 60-70%** lỗi do con người
- **Giảm 50%** thời gian điều tra sự cố
- **Tăng 40%** hiệu quả quy trình cấp quyền

#### Tuân thủ và chứng nhận
- **100%** các tiêu chuẩn bảo mật (ISO 27001, SOC 2, PCI DSS) yêu cầu Least Privilege
- **90%** các công ty Fortune 500 áp dụng Least Privilege
- **85%** các công ty đạt chứng nhận ISO 27001 có chính sách Least Privilege rõ ràng

---

## 1.4. FAQ - CÂU HỎI THƯỜNG GẶP

### ❓ Tại sao tôi không thể có quyền admin để "tiện làm việc"?

**Trả lời**: 
- Quyền admin không chỉ "tiện" cho bạn, mà cũng "tiện" cho kẻ tấn công nếu tài khoản của bạn bị xâm nhập
- 74% các vụ vi phạm bảo mật liên quan đến quyền quá cao
- Quyền tạm thời (JIT) cho phép bạn có quyền cao khi cần, nhưng tự động hết hạn sau đó
- Quy trình cấp quyền đã được tối ưu để nhanh chóng và thuận tiện

### ❓ Quy trình cấp quyền có phức tạp không?

**Trả lời**:
- Không! Quy trình đã được chuẩn hóa và đơn giản hóa
- Sử dụng template có sẵn, chỉ cần điền thông tin
- Quyền cơ bản (Level 1.0-2.0) được phê duyệt nhanh chóng
- Quyền tạm thời (JIT) có thể được cấp trong vài phút

### ❓ Nếu tôi cần quyền khẩn cấp thì sao?

**Trả lời**:
- Quyền khẩn cấp (ví dụ: Hotfix) có thể được phê duyệt nhanh qua chat/phone
- Quyền sẽ được cấp ngay lập tức
- Ghi log sau để đảm bảo tuân thủ
- Quyền tự động hết hạn sau khi hoàn thành

### ❓ Tôi có thể yêu cầu quyền tạm thời (JIT) không?

**Trả lời**:
- Có! JIT là cách tốt nhất để có quyền cao khi cần
- Quyền tự động hết hạn sau thời gian quy định
- Không cần nhớ thu hồi quyền
- An toàn hơn quyền vĩnh viễn

### ❓ Nếu tôi nghỉ việc, quyền của tôi sẽ được xử lý như thế nào?

**Trả lời**:
- Quyền sẽ được thu hồi trong vòng 24 giờ sau khi nghỉ việc
- Đây là quy trình tự động để đảm bảo an toàn
- Nếu bạn quay lại, quyền sẽ được cấp lại theo quy trình

### ❓ Tôi có thể chia sẻ tài khoản với đồng nghiệp không?

**Trả lời**:
- **KHÔNG!** Mỗi người phải có tài khoản riêng
- Chia sẻ tài khoản vi phạm chính sách bảo mật
- Không thể truy vết ai đã làm gì
- Nếu cần quyền, hãy yêu cầu cấp quyền riêng

### ❓ Tại sao tôi phải sử dụng MFA?

**Trả lời**:
- MFA bảo vệ tài khoản của bạn ngay cả khi password bị lộ
- 99.9% các vụ tấn công có thể bị ngăn chặn bằng MFA
- Bắt buộc cho tài khoản admin và quyền cao
- Chỉ mất 30 giây để thiết lập, nhưng bảo vệ bạn suốt đời

### ❓ Tôi có thể xem log của mình không?

**Trả lời**:
- Có! Bạn có thể xem log các hoạt động của mình
- Liên hệ IT Team để được hỗ trợ
- Log giúp bạn biết ai đã truy cập tài khoản của bạn
- Log giúp điều tra sự cố nhanh chóng

---

## 2. PHẠM VI ÁP DỤNG
Áp dụng cho:
- Toàn bộ nhân sự có quyền truy cập hệ thống CNTT.
- Các bộ phận IT, SysAdmin, DevOps, DBA, Security.
- Hệ thống mạng, máy chủ, ứng dụng, cơ sở dữ liệu, cloud.

---

# 3. NGUYÊN TẮC QUYỀN TRUY CẬP TỐI THIỂU (LEAST PRIVILEGE)

## 3.1 Cấp đúng quyền – đủ quyền – chỉ quyền cần thiết

### 3.1.1. Định nghĩa "đủ quyền"

**"Đủ quyền" được định nghĩa là quyền tối thiểu cần thiết để:**
- Hoàn thành nhiệm vụ được giao một cách hiệu quả
- Thực hiện công việc trong phạm vi trách nhiệm của vai trò
- Không bao gồm quyền dư thừa hoặc quyền "phòng hờ" cho tương lai

**Tiêu chí xác định "đủ quyền":**
1. **Need-to-know**: Chỉ cấp quyền khi người dùng thực sự cần biết/thao tác để hoàn thành công việc
2. **Need-to-do**: Chỉ cấp quyền thực hiện (read/write/execute) khi cần thiết cho nhiệm vụ cụ thể
3. **Time-bound**: Quyền chỉ được cấp trong thời gian cần thiết (vĩnh viễn hoặc tạm thời)
4. **Scope-limited**: Quyền chỉ áp dụng cho phạm vi cần thiết (môi trường, hệ thống, resource cụ thể)

**Ví dụ:**
- ✅ **Đủ quyền**: Developer có quyền Read/Write trên môi trường Development để phát triển
- ❌ **Không đủ quyền (thiếu)**: Developer chỉ có Read-only nhưng cần Write để test
- ❌ **Quá quyền (dư thừa)**: Developer có quyền Delete trên Production (không cần thiết)

**Nguyên tắc:**
- Mỗi người dùng, ứng dụng, dịch vụ chỉ được cấp quyền đủ để hoàn thành nhiệm vụ.
- Không cấp quyền dư thừa hoặc quyền mở rộng theo “tiện”.

## 3.2 Phân quyền theo vai trò (RBAC)
- Tất cả quyền được cấp thông qua **Role**.
- Role dựa trên chức danh hoặc nhiệm vụ (IT Support, DBA, Developer…).

## 3.3 Cấp quyền tạm thời (Just-In-Time – JIT)
- Quyền cao (root/admin) chỉ được cấp khi có yêu cầu chính đáng.
- Tự động hết hạn sau khoảng thời gian xác định.

## 3.4 Tài khoản quản trị tách biệt
- Tài khoản làm việc hằng ngày ≠ tài khoản admin.
- Không đăng nhập hàng ngày bằng tài khoản “Administrator” hoặc “root”.

## 3.5 Deny-by-default
- Quy tắc mặc định: **từ chối tất cả**, chỉ cho phép khi được phê duyệt.
- Áp dụng cho firewall, API, DB, hệ thống IAM.

## 3.6 Separation of Duties (SoD)
- Không một cá nhân nào có toàn quyền trong một quy trình.
- Ví dụ: người phát triển không được tự deploy lên Production.

## 3.7 Giám sát và ghi log đầy đủ

### 3.7.1. Ghi nhận (Logging) ra sao

**Yêu cầu ghi log:**
- Mọi hành động với quyền cao đều phải được ghi log tự động
- Mọi thay đổi quyền (cấp, thu hồi, sửa đổi) đều phải được ghi log
- Mọi truy cập vào tài nguyên nhạy cảm đều phải được ghi log

**Nội dung log phải bao gồm:**
1. **Timestamp**: Thời gian chính xác (UTC) của hành động
2. **User/Service Account**: Tài khoản thực hiện hành động (không phải tài khoản được ủy quyền)
3. **Action**: Hành động cụ thể (create, read, update, delete, execute, deploy, etc.)
4. **Resource**: Tài nguyên bị tác động (server, database, file, API endpoint, etc.)
5. **IP Address**: Địa chỉ IP nguồn của yêu cầu
6. **Result**: Kết quả (success/failure/denied)
7. **Reason/Context**: Lý do hoặc ngữ cảnh (nếu có)
8. **Session ID**: ID phiên làm việc (nếu có)

**Ví dụ log entry:**
```
2024-12-17T10:30:15Z | user:devops01@company.com | action:deploy | resource:prod-app-server-01 | ip:10.0.1.50 | result:success | session:abc123 | reason:hotfix-2024-001
```

**Hệ thống ghi log:**
- **Hệ thống IAM**: Ghi log mọi thay đổi quyền, đăng nhập, xác thực
- **Hệ thống máy chủ**: Ghi log qua syslog, auditd (Linux), Event Log (Windows)
- **Hệ thống database**: Ghi log qua audit trail, query log
- **Hệ thống ứng dụng**: Ghi log qua application log, API gateway log
- **Hệ thống cloud**: Ghi log qua CloudTrail (AWS), Activity Log (Azure), Audit Log (GCP)
- **Hệ thống container**: Ghi log qua Kubernetes audit log, container runtime log

**Lưu trữ log:**
- Log được lưu tối thiểu 90 ngày (xem chi tiết ở phần 16.1.2)
- Log quan trọng (admin actions, secret access) được lưu 1 năm
- Log compliance được lưu 7 năm (nếu yêu cầu)
- Log được backup định kỳ và lưu off-site
- Log không được chỉnh sửa hoặc xóa (immutable logs)

**Truy cập log:**
- Chỉ Security Team và IT Manager được truy cập đầy đủ
- Người dùng có thể xem log của chính mình
- Truy cập log phải được ghi log (audit log của audit log)

**Xem chi tiết**: Phần 16.1 - Audit Log

## 3.8 Rà soát quyền định kỳ
- Hàng tháng: xem xét quyền admin.
- Hàng quý: rà soát toàn bộ tài khoản.
- Thu hồi quyền người nghỉ việc trong 24 giờ.

---

## 3.9 CÁCH THỨC THỰC HIỆN VÀ AI THỰC HIỆN

### 3.9.1. Cách thức thực hiện trên các hệ thống

#### A. Hệ thống máy chủ (Server)

**Cách thức:**
- **Linux/Unix**: Sử dụng sudo với file `/etc/sudoers` hoặc `/etc/sudoers.d/`
- **Windows**: Sử dụng Local Security Policy, Group Policy, hoặc Active Directory
- **Container**: Sử dụng Kubernetes RBAC, Docker user namespaces

**Ví dụ cấu hình sudo (Linux):**
```bash
# File: /etc/sudoers.d/devops
devops01 ALL=(ALL) /usr/bin/systemctl restart app-service, /usr/bin/docker
# Cho phép devops01 chỉ restart service và dùng docker, không cho sudo su
```

**Ai thực hiện:**
- **Cấp quyền**: IT Team / SysAdmin
- **Phê duyệt**: PM/PDM (Level 1.0-2.0), Ban CLGSP (Level 3.0+)
- **Ghi log**: Hệ thống tự động ghi log qua auditd/syslog
- **Rà soát**: IT Manager, Security Team (hàng tháng)

**Xem chi tiết**: Phần 5.3 - Quy định tài khoản máy chủ

#### B. Hệ thống Database

**Cách thức:**
- **MySQL/MariaDB**: Sử dụng GRANT statement với role-based privileges
- **PostgreSQL**: Sử dụng roles và role membership
- **SQL Server**: Sử dụng database roles và server roles
- **MongoDB**: Sử dụng built-in roles và custom roles

**Ví dụ cấp quyền (MySQL):**
```sql
-- Tạo role ReadOnly
CREATE ROLE 'readonly_role';
GRANT SELECT ON database_name.* TO 'readonly_role';

-- Gán role cho user
GRANT 'readonly_role' TO 'developer01'@'%';
SET DEFAULT ROLE 'readonly_role' FOR 'developer01'@'%';
```

**Ai thực hiện:**
- **Cấp quyền**: DBA hoặc DevOps (theo quy trình)
- **Phê duyệt**: PM/PDM (Level 1.0-2.0), Ban CLGSP (Level 3.0+)
- **Ghi log**: Database audit log, query log
- **Rà soát**: DBA, IT Manager (hàng quý)

**Xem chi tiết**: Phần 6.3 - Quyền truy cập DB

#### C. Hệ thống Cloud (AWS/Azure/GCP)

**Cách thức:**
- **AWS**: Sử dụng IAM roles, policies, và permission boundaries
- **Azure**: Sử dụng Azure RBAC, Azure AD roles
- **GCP**: Sử dụng Cloud IAM, custom roles

**Ví dụ IAM policy (AWS):**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::dev-bucket/*",
        "arn:aws:s3:::dev-bucket"
      ]
    }
  ]
}
```

**Ai thực hiện:**
- **Cấp quyền**: DevOps / Cloud Admin
- **Phê duyệt**: PM/PDM (Level 1.0-2.0), Ban CLGSP (Level 3.0+)
- **Ghi log**: CloudTrail (AWS), Activity Log (Azure), Audit Log (GCP)
- **Rà soát**: DevOps Manager, Security Team (hàng quý)

**Xem chi tiết**: Phần 13.3 - Cloud IAM

#### D. Hệ thống Container (Kubernetes)

**Cách thức:**
- Sử dụng RBAC với Role/ClusterRole và RoleBinding/ClusterRoleBinding
- Sử dụng ServiceAccount cho applications
- Sử dụng NetworkPolicy để giới hạn network access

**Ví dụ Role (Kubernetes):**
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: production
  name: developer-role
rules:
- apiGroups: [""]
  resources: ["pods", "services"]
  verbs: ["get", "list", "watch"]
```

**Ai thực hiện:**
- **Cấp quyền**: DevOps / Kubernetes Admin
- **Phê duyệt**: PM/PDM (Level 1.0-2.0), Ban CLGSP (Level 3.0+)
- **Ghi log**: Kubernetes audit log
- **Rà soát**: DevOps Manager (hàng quý)

**Xem chi tiết**: Phần 13.1 - Kubernetes RBAC

#### E. Hệ thống API/Application

**Cách thức:**
- Sử dụng API keys với rate limiting
- Sử dụng OAuth 2.0 / JWT tokens với scope-based permissions
- Sử dụng feature flags với permission matrix

**Ai thực hiện:**
- **Cấp quyền**: DevOps / Application Admin
- **Phê duyệt**: PM/PDM (Level 1.0-2.0), Ban CLGSP (Level 3.0+)
- **Ghi log**: Application log, API gateway log
- **Rà soát**: DevOps Manager (hàng quý)

**Xem chi tiết**: Phần 14 - Quyền truy cập API và Ứng dụng

#### F. Hệ thống Secret Management

**Cách thức:**
- Sử dụng HashiCorp Vault với policies
- Sử dụng AWS Secrets Manager với IAM policies
- Sử dụng Azure Key Vault với RBAC
- Sử dụng GCP Secret Manager với IAM

**Ai thực hiện:**
- **Cấp quyền**: DevOps / Security Team
- **Phê duyệt**: PM/PDM (Level 1.0-2.0), Ban CLGSP (Level 3.0+)
- **Ghi log**: Vault audit log, Cloud audit log
- **Rà soát**: Security Team (hàng tháng)

**Xem chi tiết**: Phần 15 - Quản lý Secret

### 3.9.2. Tổng hợp: Ai thực hiện từng bước

| Bước | Người thực hiện | Trách nhiệm |
|------|----------------|-------------|
| **1. Yêu cầu quyền** | Người dùng (Developer, DevOps, QA, etc.) | Tạo yêu cầu, mô tả lý do, xác định quyền cần |
| **2. Phê duyệt** | PM/PDM (Level 1.0-2.0)<br>Ban CLGSP (Level 3.0)<br>Lãnh đạo (Level 4.0) | Đánh giá tính hợp lý, phê duyệt hoặc từ chối |
| **3. Cấp quyền** | IT Team / SysAdmin<br>DBA (cho DB)<br>DevOps (cho Cloud/Container)<br>Security Team (cho Secret) | Cấp quyền theo role, cấu hình hệ thống, thiết lập thời gian hết hạn |
| **4. Ghi log** | Hệ thống tự động | Ghi log mọi hành động, thay đổi quyền |
| **5. Giám sát** | Security Team<br>IT Team | Giám sát hoạt động bất thường, cảnh báo |
| **6. Rà soát** | IT Manager<br>Security Team<br>DBA (cho DB)<br>DevOps Manager (cho Cloud/Container) | Rà soát định kỳ, thu hồi quyền không cần thiết |
| **7. Thu hồi quyền** | IT Team / SysAdmin<br>DBA (cho DB)<br>DevOps (cho Cloud/Container) | Thu hồi quyền khi không cần, nghỉ việc, vi phạm |

**Xem chi tiết quy trình**: Phần 7.1 - Quy trình cấp quyền

---

# 3.10. CƠ CHẾ KIỂM SOÁT TOÀN DIỆN

## 3.10.1. Tổng quan về cơ chế kiểm soát

Cơ chế kiểm soát là các biện pháp, quy trình, công nghệ và chính sách được thiết lập để đảm bảo việc thực thi và tuân thủ chính sách Quyền Truy Cập Tối Thiểu. Cơ chế kiểm soát được phân loại theo nhiều cách khác nhau để đảm bảo bao phủ toàn diện.

---

## 3.10.2. Phân loại theo mục đích (Preventive, Detective, Corrective, Compensating)

### A. Kiểm soát phòng ngừa (Preventive Controls)

**Mục đích**: Ngăn chặn các hành động vi phạm hoặc không mong muốn xảy ra.

**Các cơ chế kiểm soát phòng ngừa:**

#### 1. Kiểm soát truy cập (Access Controls)
- **RBAC (Role-Based Access Control)**: Phân quyền theo vai trò, tự động áp dụng quyền phù hợp
- **ABAC (Attribute-Based Access Control)**: Phân quyền dựa trên thuộc tính (thời gian, địa điểm, thiết bị)
- **MFA (Multi-Factor Authentication)**: Yêu cầu xác thực đa yếu tố cho quyền cao
- **IP Whitelisting**: Chỉ cho phép truy cập từ IP đã được phê duyệt
- **VPN bắt buộc**: Yêu cầu kết nối VPN để truy cập hệ thống nhạy cảm

#### 2. Kiểm soát quy trình (Process Controls)
- **Phê duyệt bắt buộc**: Mọi yêu cầu quyền đều phải được phê duyệt
- **Separation of Duties (SoD)**: Không một người có toàn quyền trong một quy trình
- **Quy trình chuẩn hóa**: Tất cả thao tác phải theo quy trình đã định nghĩa
- **Template bắt buộc**: Sử dụng template để đảm bảo thông tin đầy đủ

#### 3. Kiểm soát kỹ thuật (Technical Controls)
- **Deny-by-default**: Từ chối tất cả, chỉ cho phép khi được phê duyệt
- **Least Privilege enforcement**: Hệ thống tự động áp dụng nguyên tắc least privilege
- **Permission boundaries**: Giới hạn quyền tối đa có thể được cấp
- **Time-bound permissions**: Quyền tự động hết hạn sau thời gian quy định
- **JIT (Just-In-Time) access**: Quyền chỉ được cấp khi cần và tự động thu hồi

#### 4. Kiểm soát cấu hình (Configuration Controls)
- **Infrastructure as Code (IaC)**: Quản lý cấu hình qua code, có version control
- **Configuration management**: Quản lý tập trung, không cho phép thay đổi trực tiếp
- **Change management**: Mọi thay đổi cấu hình đều phải qua quy trình change management
- **Immutable infrastructure**: Hạ tầng không thể thay đổi trực tiếp, phải rebuild

**Ví dụ:**
- Hệ thống tự động từ chối yêu cầu quyền admin mà không có phê duyệt
- MFA bắt buộc ngăn chặn truy cập trái phép ngay cả khi password bị lộ
- JIT access tự động thu hồi quyền sau 2 giờ, ngăn chặn quyền bị lạm dụng

---

### B. Kiểm soát phát hiện (Detective Controls)

**Mục đích**: Phát hiện các hành động vi phạm hoặc bất thường sau khi chúng xảy ra.

**Các cơ chế kiểm soát phát hiện:**

#### 1. Giám sát và ghi log (Monitoring & Logging)
- **Audit logging**: Ghi log tất cả hành động với quyền cao
- **Real-time monitoring**: Giám sát thời gian thực các hoạt động truy cập
- **SIEM (Security Information and Event Management)**: Tập trung và phân tích log
- **User activity monitoring**: Giám sát hoạt động của người dùng
- **Privileged access monitoring**: Giám sát đặc biệt các quyền cao

#### 2. Phát hiện bất thường (Anomaly Detection)
- **Behavioral analytics**: Phân tích hành vi để phát hiện bất thường
- **Machine learning detection**: Sử dụng ML để phát hiện pattern bất thường
- **Baseline comparison**: So sánh với baseline để phát hiện thay đổi
- **Risk scoring**: Đánh giá điểm rủi ro dựa trên hoạt động

#### 3. Cảnh báo tự động (Automated Alerts)
- **Real-time alerts**: Cảnh báo ngay khi phát hiện bất thường
- **Threshold-based alerts**: Cảnh báo khi vượt ngưỡng (ví dụ: nhiều lần đăng nhập thất bại)
- **Pattern-based alerts**: Cảnh báo khi phát hiện pattern đáng ngờ
- **Escalation alerts**: Tự động nâng cấp cảnh báo nếu không được xử lý

#### 4. Báo cáo định kỳ (Periodic Reports)
- **Access review reports**: Báo cáo rà soát quyền định kỳ
- **Compliance reports**: Báo cáo tuân thủ
- **Security reports**: Báo cáo bảo mật
- **Usage reports**: Báo cáo sử dụng quyền

**Ví dụ:**
- Hệ thống phát hiện đăng nhập từ IP lạ vào tài khoản admin
- Cảnh báo khi có nhiều lần thử truy cập bị từ chối
- Báo cáo hàng tuần về quyền tạm thời đã hết hạn nhưng chưa được thu hồi

---

### C. Kiểm soát khắc phục (Corrective Controls)

**Mục đích**: Khắc phục các vấn đề đã phát hiện và ngăn chặn tái diễn.

**Các cơ chế kiểm soát khắc phục:**

#### 1. Phản ứng tự động (Automated Response)
- **Auto-revoke**: Tự động thu hồi quyền khi phát hiện vi phạm
- **Auto-disable**: Tự động vô hiệu hóa tài khoản khi phát hiện bất thường
- **Auto-lock**: Tự động khóa tài khoản sau nhiều lần đăng nhập thất bại
- **Auto-rollback**: Tự động rollback thay đổi khi phát hiện lỗi

#### 2. Quy trình xử lý sự cố (Incident Response)
- **Incident response plan**: Kế hoạch xử lý sự cố rõ ràng
- **Escalation procedures**: Quy trình nâng cấp xử lý
- **Remediation steps**: Các bước khắc phục cụ thể
- **Post-incident review**: Rà soát sau sự cố để cải thiện

#### 3. Khôi phục (Recovery)
- **Backup and restore**: Sao lưu và khôi phục dữ liệu
- **Disaster recovery**: Kế hoạch phục hồi thảm họa
- **Business continuity**: Đảm bảo tính liên tục kinh doanh

#### 4. Cải thiện (Improvement)
- **Root cause analysis**: Phân tích nguyên nhân gốc rễ
- **Process improvement**: Cải thiện quy trình
- **Control enhancement**: Tăng cường kiểm soát
- **Training and awareness**: Đào tạo và nâng cao nhận thức

**Ví dụ:**
- Tự động thu hồi quyền khi phát hiện truy cập từ IP đen
- Khóa tài khoản tự động sau 5 lần đăng nhập thất bại
- Rollback tự động khi phát hiện thay đổi cấu hình gây lỗi

---

### D. Kiểm soát bù đắp (Compensating Controls)

**Mục đích**: Bù đắp cho các kiểm soát chính khi không thể áp dụng hoặc không đủ hiệu quả.

**Các cơ chế kiểm soát bù đắp:**

#### 1. Giám sát tăng cường (Enhanced Monitoring)
- **Continuous monitoring**: Giám sát liên tục khi không thể ngăn chặn
- **Manual review**: Rà soát thủ công khi không thể tự động hóa
- **Dual approval**: Yêu cầu phê duyệt kép cho các trường hợp đặc biệt

#### 2. Hạn chế bổ sung (Additional Restrictions)
- **Time restrictions**: Hạn chế thời gian truy cập
- **Location restrictions**: Hạn chế địa điểm truy cập
- **Device restrictions**: Hạn chế thiết bị truy cập
- **Session restrictions**: Hạn chế thời gian phiên làm việc

#### 3. Báo cáo và rà soát (Reporting & Review)
- **Frequent reviews**: Rà soát thường xuyên hơn
- **Detailed reporting**: Báo cáo chi tiết hơn
- **Management oversight**: Giám sát của quản lý

**Ví dụ:**
- Khi không thể áp dụng MFA, tăng cường giám sát và rà soát hàng tuần
- Khi không thể tự động hóa, yêu cầu phê duyệt thủ công và báo cáo chi tiết

---

## 3.10.3. Phân loại theo loại (Administrative, Technical, Physical)

### A. Kiểm soát quản trị (Administrative Controls)

**Định nghĩa**: Các chính sách, quy trình, hướng dẫn và thực hành quản lý.

**Các cơ chế:**

#### 1. Chính sách và quy trình (Policies & Procedures)
- **Chính sách quyền truy cập**: Chính sách rõ ràng về quyền truy cập
- **Quy trình cấp quyền**: Quy trình chuẩn hóa cấp quyền
- **Quy trình rà soát**: Quy trình rà soát quyền định kỳ
- **Quy trình thu hồi**: Quy trình thu hồi quyền

#### 2. Phân công trách nhiệm (Segregation of Duties)
- **SoD matrix**: Ma trận phân công trách nhiệm
- **Approval hierarchy**: Hệ thống phê duyệt phân cấp
- **Dual control**: Kiểm soát kép cho các thao tác quan trọng

#### 3. Đào tạo và nhận thức (Training & Awareness)
- **Security training**: Đào tạo bảo mật định kỳ
- **Policy awareness**: Nâng cao nhận thức về chính sách
- **Best practices sharing**: Chia sẻ best practices

#### 4. Quản lý thay đổi (Change Management)
- **Change control board**: Ban quản lý thay đổi
- **Change approval process**: Quy trình phê duyệt thay đổi
- **Change documentation**: Tài liệu hóa thay đổi

---

### B. Kiểm soát kỹ thuật (Technical Controls)

**Định nghĩa**: Các công nghệ, hệ thống và công cụ kỹ thuật.

**Các cơ chế:**

#### 1. Xác thực và ủy quyền (Authentication & Authorization)
- **Single Sign-On (SSO)**: Đăng nhập một lần
- **Multi-Factor Authentication (MFA)**: Xác thực đa yếu tố
- **OAuth 2.0 / SAML**: Chuẩn xác thực
- **Certificate-based authentication**: Xác thực dựa trên chứng chỉ

#### 2. Mã hóa (Encryption)
- **Encryption at rest**: Mã hóa dữ liệu khi lưu trữ
- **Encryption in transit**: Mã hóa dữ liệu khi truyền
- **Key management**: Quản lý khóa mã hóa
- **Certificate management**: Quản lý chứng chỉ

#### 3. Firewall và Network Security
- **Network segmentation**: Phân đoạn mạng
- **Firewall rules**: Quy tắc firewall
- **Intrusion Detection/Prevention (IDS/IPS)**: Phát hiện/ngăn chặn xâm nhập
- **VPN**: Mạng riêng ảo

#### 4. Hệ thống giám sát (Monitoring Systems)
- **SIEM**: Hệ thống quản lý thông tin và sự kiện bảo mật
- **Log aggregation**: Tập trung log
- **Real-time monitoring**: Giám sát thời gian thực
- **Alerting systems**: Hệ thống cảnh báo

#### 5. Tự động hóa (Automation)
- **Automated provisioning**: Tự động cấp phát
- **Automated deprovisioning**: Tự động thu hồi
- **Automated compliance checks**: Tự động kiểm tra tuân thủ
- **Automated reporting**: Tự động báo cáo

---

### C. Kiểm soát vật lý (Physical Controls)

**Định nghĩa**: Các biện pháp bảo vệ vật lý cho tài sản và hệ thống.

**Các cơ chế:**

#### 1. Kiểm soát truy cập vật lý (Physical Access Control)
- **Badge access**: Kiểm soát bằng thẻ từ
- **Biometric access**: Kiểm soát bằng sinh trắc học
- **Visitor management**: Quản lý khách thăm
- **Secure areas**: Khu vực an toàn

#### 2. Giám sát vật lý (Physical Monitoring)
- **CCTV**: Camera giám sát
- **Security guards**: Bảo vệ
- **Alarm systems**: Hệ thống báo động
- **Motion sensors**: Cảm biến chuyển động

#### 3. Bảo vệ môi trường (Environmental Protection)
- **Fire suppression**: Hệ thống chữa cháy
- **Climate control**: Điều khiển khí hậu
- **Power backup**: Nguồn điện dự phòng
- **Disaster protection**: Bảo vệ khỏi thảm họa

---

## 3.10.4. Tự động hóa kiểm soát

### A. Tự động hóa cấp và thu hồi quyền

**Cơ chế:**
- **Automated provisioning**: Tự động cấp quyền dựa trên role và approval
- **Automated deprovisioning**: Tự động thu hồi quyền khi:
  - Quyền tạm thời hết hạn
  - Người dùng nghỉ việc
  - Phát hiện vi phạm
  - Không sử dụng trong thời gian dài

**Ví dụ:**
```yaml
# Ví dụ tự động thu hồi quyền JIT sau 2 giờ
JIT_Access:
  AutoRevoke: true
  Timeout: 2h
  Notification: true
  LogAction: true
```

### B. Tự động hóa giám sát và cảnh báo

**Cơ chế:**
- **Real-time monitoring**: Giám sát thời gian thực
- **Automated alerts**: Cảnh báo tự động khi phát hiện bất thường
- **Automated escalation**: Tự động nâng cấp cảnh báo
- **Automated response**: Tự động phản ứng (ví dụ: khóa tài khoản)

**Ví dụ cảnh báo:**
- Cảnh báo khi có đăng nhập từ IP lạ
- Cảnh báo khi có nhiều lần truy cập bị từ chối
- Cảnh báo khi quyền admin được sử dụng ngoài giờ hành chính
- Cảnh báo khi phát hiện quyền không được sử dụng trong 90 ngày

### C. Tự động hóa rà soát và báo cáo

**Cơ chế:**
- **Automated access reviews**: Tự động tạo báo cáo rà soát quyền
- **Automated compliance checks**: Tự động kiểm tra tuân thủ
- **Automated reporting**: Tự động tạo báo cáo định kỳ
- **Automated remediation**: Tự động khắc phục các vấn đề phát hiện

**Ví dụ báo cáo tự động:**
- Báo cáo hàng tuần về quyền tạm thời đã hết hạn
- Báo cáo hàng tháng về quyền admin
- Báo cáo hàng quý về tuân thủ chính sách
- Báo cáo ngay khi phát hiện vi phạm

---

## 3.10.5. Ma trận kiểm soát theo hệ thống

| Hệ thống | Preventive | Detective | Corrective | Compensating |
|----------|------------|-----------|------------|--------------|
| **Server** | RBAC, MFA, sudo policy | Audit logging, monitoring | Auto-revoke, incident response | Enhanced monitoring, manual review |
| **Database** | Role-based access, IP whitelist | Query logging, audit trail | Auto-disable, rollback | Frequent reviews, detailed reporting |
| **Cloud** | IAM policies, MFA | CloudTrail, monitoring | Auto-revoke, auto-lock | Time restrictions, location restrictions |
| **Container** | RBAC, network policies | Audit logging, monitoring | Auto-scaling, auto-rollback | Enhanced monitoring, manual approval |
| **API** | API keys, rate limiting | API logging, monitoring | Auto-block, auto-revoke | IP whitelisting, enhanced monitoring |
| **Secret** | Vault policies, encryption | Access logging, monitoring | Auto-rotate, auto-revoke | Manual review, dual approval |

---

## 3.10.6. Đánh giá hiệu quả kiểm soát

### A. Chỉ số đánh giá (KPIs)

**Chỉ số hiệu quả:**
- **Tỷ lệ vi phạm**: Số lượng vi phạm / Tổng số hoạt động
- **Thời gian phát hiện**: Thời gian từ khi vi phạm đến khi phát hiện
- **Thời gian khắc phục**: Thời gian từ khi phát hiện đến khi khắc phục
- **Tỷ lệ tuân thủ**: Số lượng tuân thủ / Tổng số yêu cầu
- **Tỷ lệ tự động hóa**: Số lượng kiểm soát tự động / Tổng số kiểm soát

**Mục tiêu:**
- Tỷ lệ vi phạm < 1%
- Thời gian phát hiện < 15 phút
- Thời gian khắc phục < 1 giờ
- Tỷ lệ tuân thủ > 95%
- Tỷ lệ tự động hóa > 80%

### B. Đánh giá định kỳ

**Tần suất:**
- **Hàng tuần**: Đánh giá cảnh báo và sự cố
- **Hàng tháng**: Đánh giá hiệu quả kiểm soát
- **Hàng quý**: Đánh giá toàn diện và cải thiện
- **Hàng năm**: Đánh giá và cập nhật chính sách

**Nội dung đánh giá:**
- Hiệu quả của các kiểm soát hiện tại
- Phát hiện các gap và rủi ro mới
- Đề xuất cải thiện
- Cập nhật kiểm soát

---

## 3.10.7. Quy trình triển khai kiểm soát

```
1. Xác định yêu cầu kiểm soát
   ↓
2. Thiết kế kiểm soát
   ↓
3. Phê duyệt kiểm soát
   ↓
4. Triển khai kiểm soát
   ↓
5. Kiểm thử kiểm soát
   ↓
6. Giám sát và đánh giá
   ↓
7. Cải thiện liên tục
```

---

**Xem chi tiết**: 
- Phần 7.1 - Quy trình cấp quyền
- Phần 9 - Giám sát và cảnh báo
- Phần 16 - Audit và Compliance
- Phần 17 - Incident Response

---

# 4. QUY TRÌNH QUẢN TRỊ HỆ THỐNG MẠNG

## 4.1 Kiến trúc mạng (Network Architecture)
- Sơ đồ mạng bao gồm VLAN, DMZ, WAN, VPN, WiFi.
- Danh mục thiết bị mạng: Router, Switch, Firewall, AP…

## 4.2 Quy trình vận hành mạng
- Kiểm tra băng thông, Ping, Latency, Packet Loss mỗi ngày.
- Giám sát thiết bị mạng qua SNMP/Zabbix/PRTG.
- Rà soát ACL/Firewall rule định kỳ 30 ngày.

## 4.3 Firewall & VPN
- Firewall áp dụng mô hình **deny-all, allow-by-rule**.
- Kết nối VPN yêu cầu MFA.
- Cấu hình firewall phải được sao lưu mỗi tuần.

---

# 5. QUY TRÌNH QUẢN TRỊ MÁY CHỦ

## 5.1 Danh mục máy chủ
| Server | IP | OS | Chức năng | Ghi chú |
|-------|----|----|-----------|---------|

## 5.2 Vận hành máy chủ
- Kiểm tra CPU, RAM, Disk, IOPS.
- Kiểm tra log hệ thống.
- Cập nhật bản vá bảo mật (patching).
- Kiểm tra tình trạng dịch vụ (service status).

## 5.3 Quy định tài khoản máy chủ

### 5.3.1. Nguyên tắc

- **Không sử dụng root cho tác vụ hàng ngày**: Chỉ sử dụng tài khoản root khi thực sự cần thiết
- **Chỉ dùng sudo theo policy**: Sử dụng sudo với quyền hạn cụ thể, không dùng sudo su
- **Mỗi tài khoản phải gắn với cá nhân**: Không dùng chung tài khoản, mỗi người có tài khoản riêng

### 5.3.2. Quy trình cấp quyền sudo

```
1. Người dùng yêu cầu quyền sudo
2. Quản lý phê duyệt
3. IT cấu hình sudo theo policy
4. Ghi log đầy đủ
5. Thông báo cho người dùng
```

### 5.3.3. Policy sudo

- **Sudo với quyền cụ thể**: Chỉ cho phép thực hiện các lệnh cụ thể, không cho phép sudo su
- **Ghi log đầy đủ**: Mọi lệnh sudo đều được ghi log
- **Timeout**: Sudo session tự động hết hạn sau 15 phút không sử dụng
- **MFA**: Yêu cầu MFA khi sử dụng sudo (nếu có thể)

### 5.3.4. Quy định tài khoản service

- Tài khoản service không được sử dụng để đăng nhập
- Tài khoản service chỉ được sử dụng để chạy service
- Tài khoản service phải có quyền tối thiểu

---

# 6. QUẢN TRỊ CƠ SỞ DỮ LIỆU (DATABASE)

## 6.1 Danh mục DB
- MySQL / MariaDB
- PostgreSQL
- SQL Server
- MongoDB / Redis

## 6.2 Quy trình vận hành DB
- Theo dõi slow queries, lock, deadlock.
- Kiểm tra replication.
- Theo dõi dung lượng DB/log.

## 6.3 Quyền truy cập DB

### 6.3.1. Role-based access

| Role | Quyền | Đối tượng | Mục đích |
|------|-------|-----------|----------|
| **ReadOnly** | SELECT | Developer, QA | Xem dữ liệu, không được thay đổi |
| **ReadWrite** | SELECT, INSERT, UPDATE, DELETE | Application, Service Account | Ứng dụng truy cập database |
| **DBAdmin** | Tất cả quyền | DBA, DevOps (theo quy trình) | Quản trị database |

### 6.3.2. Quy định truy cập

- **Cấm truy cập trực tiếp từ Internet**: Database không được expose ra Internet
- **Chỉ mở cổng cho IP whitelist**: Chỉ cho phép truy cập từ IP đã được whitelist
- **Sử dụng VPN**: Truy cập từ xa phải qua VPN
- **Encryption**: Kết nối database phải được mã hóa (SSL/TLS)

### 6.3.3. Quy trình cấp quyền database

```
1. Người dùng yêu cầu quyền database
2. Quản lý phê duyệt
3. DBA cấp quyền theo role
4. Cấu hình IP whitelist (nếu cần)
5. Ghi log đầy đủ
6. Thông báo cho người dùng
```

### 6.3.4. Quy định cho Production

- **Developer**: Chỉ có quyền ReadOnly trên Production
- **DevOps**: Có quyền ReadWrite/DBAdmin trên Production (theo quy trình, có log)
- **QA**: Chỉ có quyền ReadOnly trên Staging/UAT
- **DBA**: Có quyền DBAdmin trên tất cả môi trường (theo quy trình)

## 6.4 Backup & Restore
- Full backup: hằng ngày.
- Incremental backup: 1–6 giờ.
- Kiểm thử phục hồi dữ liệu mỗi 3 tháng.

---

# 7. IAM – QUẢN LÝ TÀI KHOẢN & PHÂN QUYỀN

## 7.1 Quy trình cấp quyền

### 7.1.1. Quy trình chi tiết

```
1. Người dùng gửi yêu cầu
   → Tạo yêu cầu trong hệ thống quản lý quyền
   → Mô tả lý do cần quyền
   → Xác định thời gian cần quyền (nếu tạm thời)
   → Xác định role/quyền cần

2. Quản lý phê duyệt
   → PM/PDM phê duyệt cho quyền Level 1.0-2.0
   → Ban CLGSP phê duyệt cho quyền Level 3.0
   → Lãnh đạo phê duyệt cho quyền Level 4.0
   → Đánh giá tính hợp lý của yêu cầu

3. IT cấp quyền theo role
   → Cấp quyền theo role đã được định nghĩa
   → Không cấp quyền dư thừa
   → Thiết lập thời gian hết hạn (nếu tạm thời)

4. Lưu log & thông báo
   → Ghi log đầy đủ: người yêu cầu, người phê duyệt, quyền được cấp, thời gian
   → Thông báo cho người dùng
   → Thông báo cho quản lý
```

### 7.1.2. Template yêu cầu cấp quyền

| Thông tin | Mô tả |
|-----------|-------|
| **Người yêu cầu** | Tên, email, phòng ban |
| **Lý do** | Mô tả lý do cần quyền |
| **Quyền cần** | Role/quyền cụ thể |
| **Hệ thống** | Hệ thống cần quyền |
| **Thời gian** | Vĩnh viễn/Tạm thời (nếu tạm thời, ghi rõ thời hạn) |
| **Người phê duyệt** | Tên, chức vụ |
| **Ngày phê duyệt** | Ngày phê duyệt |
| **Ngày cấp quyền** | Ngày IT cấp quyền |
| **Ngày hết hạn** | Ngày quyền hết hạn (nếu tạm thời) |  

## 7.2 Rà soát quyền

### 7.2.1. Rà soát định kỳ

| Loại rà soát | Tần suất | Nội dung | Người thực hiện |
|--------------|----------|----------|-----------------|
| **Rà soát quyền admin** | Hàng tháng | Xem xét tất cả tài khoản có quyền admin | IT Manager, Security Team |
| **Rà soát toàn bộ tài khoản** | Hàng quý | Rà soát tất cả tài khoản và quyền | IT Team |
| **Rà soát quyền tạm thời** | Hàng tuần | Kiểm tra quyền tạm thời đã hết hạn chưa | IT Team |
| **Rà soát quyền theo role** | Hàng quý | Kiểm tra quyền theo từng role | IT Manager |

### 7.2.2. Quy trình rà soát

```
1. Thu thập dữ liệu
   → Danh sách tài khoản
   → Danh sách quyền của từng tài khoản
   → Lịch sử sử dụng quyền
   → Log truy cập

2. Phân tích
   → Xác định quyền không cần thiết
   → Xác định quyền chưa sử dụng
   → Xác định quyền tạm thời đã hết hạn
   → Xác định tài khoản không hoạt động

3. Đề xuất
   → Đề xuất thu hồi quyền không cần thiết
   → Đề xuất khóa tài khoản không hoạt động
   → Đề xuất điều chỉnh quyền

4. Phê duyệt và thực hiện
   → Quản lý phê duyệt
   → IT thực hiện thu hồi/điều chỉnh
   → Ghi log đầy đủ
   → Thông báo cho người dùng
```

### 7.2.3. Tự động khóa tài khoản

- **Tài khoản không dùng trong 60 ngày**: Tự động khóa
- **Tài khoản không đăng nhập trong 90 ngày**: Tự động vô hiệu hóa
- **Tài khoản admin không dùng trong 30 ngày**: Cảnh báo và rà soát
- **Thông báo trước khi khóa**: 7 ngày trước khi khóa

## 7.3 MFA (Multi-Factor Authentication)

### 7.3.1. Yêu cầu MFA

| Loại tài khoản | MFA | Phương thức |
|----------------|-----|-------------|
| **Tài khoản admin** | Bắt buộc | TOTP (Google Authenticator, Authy) hoặc SMS |
| **Tài khoản có quyền cao** | Bắt buộc | TOTP hoặc SMS |
| **Tài khoản người dùng thông thường** | Khuyến khích | TOTP hoặc SMS |
| **Tài khoản service** | Không áp dụng | Sử dụng API key/Token |

### 7.3.2. Quy trình thiết lập MFA

```
1. Người dùng yêu cầu thiết lập MFA
2. IT hướng dẫn thiết lập
3. Người dùng cài đặt ứng dụng MFA (Google Authenticator, Authy, ...)
4. Quét QR code hoặc nhập secret key
5. Xác nhận bằng mã MFA
6. Lưu backup codes
7. Hoàn tất thiết lập
```

### 7.3.3. Quy định

- MFA phải được kích hoạt trong vòng 7 ngày sau khi được cấp quyền admin
- Backup codes phải được lưu trữ an toàn
- Nếu mất thiết bị MFA, phải báo ngay cho IT để reset

---

# 8. SAO LƯU – DỰ PHÒNG – PHỤC HỒI

## 8.1 Chính sách Backup
- Lưu tại **on-site + off-site**.
- Duy trì lịch sử 30 ngày trở lên.

## 8.2 Quy trình DRP (Disaster Recovery Plan)
- Phân loại hệ thống theo mức ưu tiên.
- Mục tiêu:
  - RTO < 4 giờ
  - RPO < 1 giờ

## 8.3 Kiểm thử DRP
- 6 tháng/lần.
- Lập báo cáo kết quả.

---

# 9. GIÁM SÁT VÀ CẢNH BÁO

## 9.1 Hệ thống giám sát
- Zabbix, Prometheus, Grafana, ELK, Splunk.

## 9.2 Nội dung giám sát
- CPU/RAM/Disk/IOPS.
- Trạng thái dịch vụ.
- Mạng (ping, băng thông).
- DB performance.

## 9.3 Cảnh báo (Alert)

### 9.3.1. Kênh cảnh báo

- **Email**: Cảnh báo qua email cho Security Team, IT Manager
- **Telegram/Slack**: Cảnh báo real-time qua chat
- **Dashboard**: Hiển thị cảnh báo trên dashboard
- **SMS**: Cảnh báo khẩn cấp qua SMS (cho sự cố Critical)

### 9.3.2. Phân loại cảnh báo

| Mức độ | Mô tả | Kênh | Thời gian phản ứng |
|--------|-------|------|-------------------|
| **Critical** | Sự cố nghiêm trọng, cần xử lý ngay | Email + SMS + Slack | Ngay lập tức |
| **High** | Sự cố quan trọng | Email + Slack | 15 phút |
| **Medium** | Sự cố trung bình | Email + Slack | 1 giờ |
| **Low** | Cảnh báo thông tin | Email | 24 giờ |

### 9.3.3. Các loại cảnh báo

**Cảnh báo bảo mật:**
- Đăng nhập từ IP lạ
- Nhiều lần đăng nhập thất bại
- Sử dụng quyền admin ngoài giờ hành chính
- Truy cập tài nguyên nhạy cảm
- Phát hiện quyền bị lạm dụng

**Cảnh báo tuân thủ:**
- Quyền tạm thời đã hết hạn nhưng chưa được thu hồi
- Quyền không được sử dụng trong 90 ngày
- Vi phạm chính sách quyền truy cập
- Thiếu MFA cho tài khoản admin

**Cảnh báo hệ thống:**
- Hệ thống giám sát không hoạt động
- Log không được ghi
- Backup thất bại
- Hệ thống kiểm soát lỗi

---

## 9.4 Dashboard và Báo cáo

### 9.4.1. Security Dashboard

**Mục đích**: Cung cấp cái nhìn tổng quan về tình trạng bảo mật và tuân thủ.

**Nội dung dashboard:**

#### A. Tổng quan (Overview)
- **Tổng số tài khoản**: Số lượng tài khoản đang hoạt động
- **Tổng số quyền**: Số lượng quyền đã được cấp
- **Quyền tạm thời**: Số lượng quyền JIT đang hoạt động
- **Tỷ lệ tuân thủ**: Phần trăm tuân thủ chính sách
- **Sự cố trong 24h**: Số lượng sự cố trong 24 giờ qua

#### B. Cảnh báo (Alerts)
- **Cảnh báo chưa xử lý**: Danh sách cảnh báo đang chờ xử lý
- **Cảnh báo theo mức độ**: Phân loại theo Critical, High, Medium, Low
- **Xu hướng cảnh báo**: Biểu đồ xu hướng cảnh báo theo thời gian

#### C. Quyền truy cập (Access)
- **Quyền mới được cấp**: Danh sách quyền được cấp trong 24h/7 ngày/30 ngày
- **Quyền đã hết hạn**: Danh sách quyền đã hết hạn cần thu hồi
- **Quyền không sử dụng**: Danh sách quyền không được sử dụng
- **Top users**: Người dùng có nhiều quyền nhất

#### D. Tuân thủ (Compliance)
- **Tỷ lệ tuân thủ**: Phần trăm tuân thủ theo từng tiêu chuẩn
- **Vi phạm**: Danh sách vi phạm chính sách
- **Rà soát sắp tới**: Lịch rà soát quyền sắp tới

#### E. Hoạt động (Activity)
- **Hoạt động truy cập**: Biểu đồ hoạt động truy cập theo thời gian
- **Hoạt động quyền cao**: Danh sách hoạt động với quyền cao
- **Đăng nhập**: Thống kê đăng nhập theo thời gian, địa điểm

### 9.4.2. Báo cáo định kỳ

#### A. Báo cáo hàng ngày

**Nội dung:**
- Tổng hợp cảnh báo trong ngày
- Số lượng quyền được cấp/thu hồi
- Sự cố và xử lý
- Vi phạm chính sách

**Người nhận**: Security Team, IT Manager

#### B. Báo cáo hàng tuần

**Nội dung:**
- Tổng hợp tuần
- Quyền tạm thời đã hết hạn
- Quyền không được sử dụng
- Xu hướng và phân tích
- Đề xuất cải thiện

**Người nhận**: Security Team, IT Manager, PM/PDM

#### C. Báo cáo hàng tháng

**Nội dung:**
- Tổng hợp tháng
- Rà soát quyền admin
- Phân tích tuân thủ
- Đánh giá hiệu quả kiểm soát
- KPI và metrics
- Đề xuất cải thiện

**Người nhận**: Security Team, IT Manager, Ban CLGSP, Lãnh đạo

#### D. Báo cáo hàng quý

**Nội dung:**
- Tổng hợp quý
- Rà soát toàn bộ tài khoản
- Đánh giá toàn diện
- Gap analysis
- Roadmap cải thiện
- Compliance report

**Người nhận**: Security Team, IT Manager, Ban CLGSP, Ban KTHT, Lãnh đạo

### 9.4.3. Báo cáo theo yêu cầu

**Các loại báo cáo:**
- **Access review report**: Báo cáo rà soát quyền
- **Compliance report**: Báo cáo tuân thủ
- **Security incident report**: Báo cáo sự cố bảo mật
- **User activity report**: Báo cáo hoạt động người dùng
- **Privileged access report**: Báo cáo quyền cao
- **Audit trail report**: Báo cáo audit trail

**Quy trình:**
```
1. Yêu cầu báo cáo
2. Xác định loại báo cáo và thời gian
3. Tạo báo cáo
4. Phê duyệt (nếu cần)
5. Cung cấp báo cáo
```

---

# 10. QUẢN LÝ THAY ĐỔI (CHANGE MANAGEMENT)

## 10.1 Quy trình thay đổi
1. Gửi Change Request (CR).  
2. Đánh giá rủi ro & phê duyệt.  
3. Thực hiện thay đổi.  
4. Kiểm tra hậu triển khai.  

## 10.2 Tài liệu cần có
- Change log.
- Checklist triển khai.
- Kế hoạch rollback (nếu lỗi).

---

# 11. NHẬT KÝ VẬN HÀNH (OPERATION LOG)

Ghi lại:
- Sự cố phát sinh.
- Bảo trì định kỳ.
- Các thay đổi cấu hình.
- Cảnh báo quan trọng.

---

# 12. QUY ĐỊNH VỀ QUYỀN TRUY CẬP TRONG QUY TRÌNH UPCODE

## 12.1. Quyền truy cập môi trường

| Môi trường | Developer | DevOps | QA | PM/PDM | DBA |
|------------|-----------|--------|----|----|-----|
| **Development** | Read/Write | Read/Write | Read | Read | Read/Write |
| **Staging/UAT** | Read | Read/Write | Read/Write | Read | Read/Write |
| **Production** | Read (chỉ xem log) | Read/Write (theo quy trình) | Read | Read | Read/Write (theo quy trình) |
| **DR** | Read (chỉ xem log) | Read/Write (theo quy trình) | Read | Read | Read/Write (theo quy trình) |

## 12.2. Quyền deploy

- **Developer**: Không được deploy trực tiếp lên Production/DR
- **DevOps**: Được deploy lên Production/DR sau khi có phê duyệt (theo QT-003)
- **QA**: Không được deploy, chỉ được test
- **DBA**: Được deploy database changes sau khi có phê duyệt

## 12.3. Quyền database trong quy trình upcode

- **Developer**: Read-only trên Production/DR
- **DevOps**: Read/Write trên Production/DR (theo quy trình, có log)
- **QA**: Read-only trên Staging/UAT
- **DBA**: Read/Write trên tất cả môi trường (theo quy trình)

## 12.4. Quyền cấu hình

- **Developer**: Không được thay đổi cấu hình Production/DR
- **DevOps**: Được thay đổi cấu hình Production/DR sau khi có phê duyệt
- **QA**: Không được thay đổi cấu hình
- **DBA**: Được thay đổi cấu hình database sau khi có phê duyệt

## 12.5. Quy trình cấp quyền tạm thời cho upcode

1. **Yêu cầu quyền**
   - Tạo yêu cầu trong hệ thống quản lý quyền
   - Mô tả lý do cần quyền (ví dụ: deploy lên Production)
   - Xác định thời gian cần quyền (thường là 1-2 giờ)

2. **Phê duyệt**
   - PM/PDM phê duyệt cho quyền Level 1.0-2.0
   - Ban CLGSP phê duyệt cho quyền Level 3.0
   - Lãnh đạo phê duyệt cho quyền Level 4.0

3. **Cấp quyền**
   - IT cấp quyền theo role
   - Tự động hết hạn sau thời gian quy định
   - Ghi log đầy đủ

4. **Thu hồi quyền**
   - Tự động thu hồi sau khi hết hạn
   - Thu hồi ngay sau khi hoàn thành deploy
   - Ghi log thu hồi

**Tham chiếu**: `QT-003-UPCODE.md` - Phần 9

---

# 13. QUYỀN TRUY CẬP CLOUD VÀ CONTAINER

## 13.1. Kubernetes RBAC

### 13.1.1. Role và RoleBinding

**Role**: Quyền trong một namespace cụ thể

**Quy định**:
- Mỗi namespace có role riêng
- Role chỉ áp dụng trong namespace đó
- Không được cấp quyền cluster-wide nếu không cần thiết

**Ví dụ Role**:
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: production
  name: developer-role
rules:
- apiGroups: [""]
  resources: ["pods", "services"]
  verbs: ["get", "list", "watch"]
```

### 13.1.2. ClusterRole và ClusterRoleBinding

**ClusterRole**: Quyền cluster-wide

**Quy định**:
- Chỉ cấp cho DevOps, Admin
- Phải có phê duyệt đặc biệt
- Ghi log đầy đủ

### 13.1.3. Service Account

**Quy định**:
- Mỗi application có Service Account riêng
- Service Account chỉ có quyền tối thiểu cần thiết
- Không dùng default Service Account
- Service Account không được dùng để đăng nhập

### 13.1.4. Quyền theo namespace

| Namespace | Developer | DevOps | QA | DBA |
|-----------|-----------|--------|----|-----|
| **development** | Read/Write | Read/Write | Read | Read |
| **staging** | Read | Read/Write | Read/Write | Read |
| **production** | Read (log only) | Read/Write* | Read | Read |
| **kube-system** | No access | Read* | No access | No access |

*Theo quy trình, có phê duyệt

### 13.1.5. Quy trình cấp quyền Kubernetes

```
1. Xác định namespace và quyền cần
2. Tạo Role/ClusterRole (nếu chưa có)
3. Tạo RoleBinding/ClusterRoleBinding
4. Gán cho Service Account hoặc User
5. Test quyền
6. Ghi log đầy đủ
```

## 13.2. Docker Registry

### 13.2.1. Quyền pull/push image

| Vai trò | Pull | Push | Delete | Quản lý repository |
|---------|------|------|--------|-------------------|
| **Developer** | ✅ (dev/staging) | ✅ (dev/staging) | ❌ | ❌ |
| **DevOps** | ✅ (all) | ✅ (all) | ✅ (staging/dev) | ✅ (staging/dev) |
| **QA** | ✅ (dev/staging) | ❌ | ❌ | ❌ |
| **DBA** | ✅ (all) | ❌ | ❌ | ❌ |

### 13.2.2. Quy định

- **Production images**: Chỉ DevOps được push
- **Image tags**: Sử dụng semantic versioning
- **Image scanning**: Tất cả images phải được scan trước khi push
- **Image signing**: Production images phải được sign

### 13.2.3. Quy trình cấp quyền registry

```
1. Xác định registry và quyền cần
2. Tạo user/robot account trong registry
3. Cấp quyền theo role
4. Cấu hình IP whitelist (nếu cần)
5. Test quyền
6. Ghi log đầy đủ
```

## 13.3. Cloud IAM

### 13.3.1. AWS IAM

**Quy định**:
- Sử dụng IAM roles thay vì access keys khi có thể
- Access keys phải được rotate định kỳ (90 ngày)
- Sử dụng least privilege policies
- Enable MFA cho root account và admin users

**Quyền theo vai trò**:
- **Developer**: Read-only trên dev/staging resources
- **DevOps**: Full access trên dev/staging, limited access trên production
- **DBA**: RDS, ElastiCache access
- **Admin**: Full access (theo quy trình)

### 13.3.2. Azure RBAC

**Quy định**:
- Sử dụng Azure AD roles
- Sử dụng managed identities thay vì service principals khi có thể
- Enable MFA cho admin accounts

**Quyền theo vai trò**:
- **Developer**: Reader trên dev/staging
- **DevOps**: Contributor trên dev/staging, limited trên production
- **DBA**: SQL DB Contributor
- **Admin**: Owner (theo quy trình)

### 13.3.3. GCP IAM

**Quy định**:
- Sử dụng service accounts thay vì user accounts khi có thể
- Sử dụng custom roles với least privilege
- Enable MFA cho admin accounts

**Quyền theo vai trò**:
- **Developer**: Viewer trên dev/staging
- **DevOps**: Editor trên dev/staging, limited trên production
- **DBA**: Cloud SQL Client
- **Admin**: Owner (theo quy trình)

### 13.3.4. Quy trình cấp quyền Cloud

```
1. Xác định cloud provider và quyền cần
2. Tạo IAM role/policy (nếu chưa có)
3. Gán role cho user/service account
4. Test quyền
5. Ghi log đầy đủ
6. Thiết lập rotation (nếu access keys)
```

---

# 14. QUYỀN TRUY CẬP API VÀ ỨNG DỤNG

## 14.1. API Access Control

### 14.1.1. API Key Management

**Quy định**:
- Mỗi application có API key riêng
- API key phải được rotate định kỳ (90 ngày)
- API key không được commit vào code
- API key phải được lưu trong secret management

**Quy trình tạo API key**:
```
1. Yêu cầu API key
2. Phê duyệt
3. Tạo API key trong hệ thống
4. Cấu hình rate limiting
5. Cấu hình IP whitelist (nếu cần)
6. Ghi log đầy đủ
7. Cung cấp API key cho người dùng (qua secure channel)
```

### 14.1.2. OAuth 2.0 / JWT Tokens

**Quy định**:
- Sử dụng OAuth 2.0 cho user authentication
- JWT tokens có thời gian hết hạn ngắn (15-60 phút)
- Refresh tokens có thời gian hết hạn dài hơn (7-30 ngày)
- Tokens phải được revoke khi không cần thiết

**Quy trình**:
```
1. User đăng nhập
2. Nhận access token và refresh token
3. Sử dụng access token để gọi API
4. Refresh token khi access token hết hạn
5. Revoke token khi logout hoặc không dùng
```

### 14.1.3. API Rate Limiting

**Quy định**:
- Mỗi API key có rate limit riêng
- Rate limit theo role:
  - **Developer**: 100 requests/minute
  - **Application**: 1000 requests/minute
  - **Admin**: 5000 requests/minute
- Vượt quá rate limit sẽ bị block tạm thời

### 14.1.4. API Versioning và Permissions

**Quy định**:
- API versioning: `/api/v1/`, `/api/v2/`
- Mỗi version có permissions riêng
- Deprecated API phải có thông báo trước khi remove

## 14.2. Application-level Permissions

### 14.2.1. Feature Flags

**Quy định**:
- Feature flags được quản lý tập trung
- Chỉ admin được enable/disable feature flags trên production
- Feature flags phải có documentation

**Quy trình**:
```
1. Tạo feature flag
2. Cấu hình permissions (ai được enable/disable)
3. Test feature flag
4. Deploy với feature flag disabled
5. Enable feature flag theo quy trình
```

### 14.2.2. Permission Matrix

**Quy định**:
- Mỗi feature có permission matrix
- Permission được kiểm tra ở application level
- Permission được cache để tăng performance

**Ví dụ**:
| Feature | Developer | DevOps | QA | Admin |
|---------|-----------|--------|----|----|
| View users | ✅ | ✅ | ✅ | ✅ |
| Create users | ✅ (dev) | ✅ | ✅ (staging) | ✅ |
| Delete users | ❌ | ❌ | ❌ | ✅ |
| Export data | ❌ | ✅ | ✅ | ✅ |

### 14.2.3. Role-based Feature Access

**Quy định**:
- Features được gán theo role
- Role được quản lý trong database hoặc IAM
- Changes phải được phê duyệt

---

# 15. QUẢN LÝ SECRET

## 15.1. Secret Management Tools

### 15.1.1. HashiCorp Vault

**Quy định**:
- Tất cả secrets phải được lưu trong Vault
- Secrets không được lưu trong code, config files, hoặc environment variables
- Vault access phải được authenticate và authorize

**Quyền truy cập Vault**:
| Vai trò | Read | Write | Delete | Admin |
|---------|------|-------|--------|-------|
| **Developer** | ✅ (dev secrets) | ❌ | ❌ | ❌ |
| **DevOps** | ✅ (all) | ✅ (dev/staging) | ❌ | ❌ |
| **DBA** | ✅ (DB secrets) | ❌ | ❌ | ❌ |
| **Admin** | ✅ (all) | ✅ (all) | ✅ (all) | ✅ |

### 15.1.2. AWS Secrets Manager

**Quy định**:
- Sử dụng AWS Secrets Manager cho AWS resources
- Secrets được encrypt bằng KMS
- Access được quản lý qua IAM

### 15.1.3. Azure Key Vault

**Quy định**:
- Sử dụng Azure Key Vault cho Azure resources
- Secrets được encrypt
- Access được quản lý qua Azure RBAC

### 15.1.4. GCP Secret Manager

**Quy định**:
- Sử dụng GCP Secret Manager cho GCP resources
- Secrets được encrypt
- Access được quản lý qua GCP IAM

## 15.2. Quy trình Quản lý Secret

### 15.2.1. Tạo Secret

```
1. Yêu cầu tạo secret
2. Phê duyệt
3. Tạo secret trong secret management tool
4. Cấu hình access permissions
5. Ghi log đầy đủ
6. Thông báo cho người cần
```

### 15.2.2. Truy cập Secret

**Quy định**:
- Truy cập secret phải được authenticate
- Mọi truy cập secret đều được ghi log
- Secrets không được expose trong logs hoặc error messages

**Quy trình**:
```
1. Authenticate với secret management tool
2. Request secret với proper permissions
3. Secret được decrypt và cung cấp
4. Ghi log truy cập
5. Secret không được lưu local (trừ khi cần thiết và được phê duyệt)
```

### 15.2.3. Rotation Secret

**Quy định**:
- Secrets phải được rotate định kỳ:
  - **API keys**: 90 ngày
  - **Database passwords**: 180 ngày
  - **SSL certificates**: Trước khi hết hạn
  - **SSH keys**: 365 ngày
- Rotation phải được tự động hóa khi có thể

**Quy trình**:
```
1. Tạo secret mới
2. Update application với secret mới
3. Verify application hoạt động với secret mới
4. Revoke secret cũ
5. Ghi log rotation
```

### 15.2.4. Revoke Secret

**Quy trình**:
```
1. Xác định secret cần revoke
2. Phê duyệt revoke
3. Revoke secret trong secret management tool
4. Update applications sử dụng secret
5. Ghi log revoke
6. Thông báo cho người liên quan
```

## 15.3. Best Practices

- **Không commit secrets**: Sử dụng .gitignore, pre-commit hooks
- **Sử dụng environment variables**: Chỉ cho non-sensitive config
- **Encrypt secrets at rest**: Tất cả secrets phải được encrypt
- **Encrypt secrets in transit**: Sử dụng TLS khi truy cập secrets
- **Audit log**: Ghi log tất cả operations trên secrets
- **Backup secrets**: Backup secrets an toàn (encrypted)

---

# 16. AUDIT VÀ COMPLIANCE

## 16.1. Audit Log

### 16.1.1. Yêu cầu Audit Log

**Quy định**:
- Tất cả hành động với quyền cao đều phải được ghi log
- Log phải bao gồm:
  - Timestamp
  - User/Service account
  - Action (create, read, update, delete)
  - Resource
  - IP address
  - Result (success/failure)
- Log không được chỉnh sửa hoặc xóa

### 16.1.2. Retention Policy

| Loại log | Retention | Lý do |
|----------|-----------|-------|
| **Access log** | 90 ngày | Compliance, troubleshooting |
| **Admin actions** | 1 năm | Security audit |
| **Authentication log** | 90 ngày | Security monitoring |
| **Secret access log** | 1 năm | Compliance |
| **Compliance log** | 7 năm | Legal requirements |

### 16.1.3. Access to Audit Log

**Quy định**:
- Chỉ Security Team và IT Manager được truy cập audit log
- Access to audit log phải được ghi log
- Audit log phải được backup định kỳ

## 16.2. Compliance

### 16.2.1. GDPR Requirements

**Quy định**:
- Quyền truy cập dữ liệu cá nhân phải được kiểm soát
- Ghi log tất cả truy cập dữ liệu cá nhân
- Có thể xóa dữ liệu cá nhân khi được yêu cầu (Right to be forgotten)
- Báo cáo data breach trong 72 giờ

### 16.2.2. ISO 27001

**Quy định**:
- Access control policy phải được document
- Access rights phải được review định kỳ
- User access rights phải được removed khi không cần thiết
- Privileged access phải được kiểm soát

### 16.2.3. SOC 2

**Quy định**:
- Access controls phải được implement và monitor
- Changes to access controls phải được authorized
- Access reviews phải được thực hiện định kỳ
- Audit logs phải được maintain

### 16.2.4. Quy trình Compliance Review

```
1. Xác định compliance requirements
2. Review current access controls
3. Identify gaps
4. Implement controls
5. Document controls
6. Regular audit và review
```

---

# 17. INCIDENT RESPONSE

## 17.1. Quy trình xử lý khi phát hiện quyền bị lạm dụng

### 17.1.1. Phát hiện

**Nguồn phát hiện**:
- Audit log analysis
- Security monitoring alerts
- User reports
- Automated detection

### 17.1.2. Quy trình xử lý

```
1. Phát hiện lạm dụng quyền
   ↓
2. Đánh giá mức độ nghiêm trọng
   - Critical: Thu hồi ngay lập tức
   - High: Thu hồi trong 1 giờ
   - Medium: Thu hồi trong 24 giờ
   ↓
3. Thu hồi quyền ngay lập tức
   ↓
4. Khóa tài khoản (nếu cần)
   ↓
5. Thu thập evidence
   ↓
6. Phân tích và báo cáo
   ↓
7. Khắc phục và cải thiện
```

### 17.1.3. Escalation

| Mức độ | Thời gian xử lý | Người xử lý | Escalation |
|--------|-----------------|------------|------------|
| **Critical** | Ngay lập tức | Security Team | CTO, IT Manager |
| **High** | 1 giờ | IT Team | Security Team |
| **Medium** | 24 giờ | IT Team | IT Manager |
| **Low** | 3 ngày | IT Team | - |

## 17.2. Quy trình thu hồi quyền khẩn cấp

### 17.2.1. Khi nào cần thu hồi khẩn cấp

- Phát hiện quyền bị lạm dụng
- Tài khoản bị compromise
- Nhân viên nghỉ việc đột ngột
- Vi phạm chính sách nghiêm trọng

### 17.2.2. Quy trình

```
1. Xác định tài khoản/quyền cần thu hồi
   ↓
2. Thu hồi quyền ngay lập tức (không cần phê duyệt)
   ↓
3. Khóa tài khoản (nếu cần)
   ↓
4. Thông báo cho Security Team và IT Manager
   ↓
5. Ghi log đầy đủ
   ↓
6. Báo cáo sau (trong 24 giờ)
```

### 17.2.3. Quyền thu hồi khẩn cấp

- **Security Team**: Có quyền thu hồi bất kỳ quyền nào
- **IT Manager**: Có quyền thu hồi quyền trong phạm vi quản lý
- **On-call Engineer**: Có quyền thu hồi quyền trong giờ ngoài hành chính (với approval sau)

## 17.3. Quy trình khôi phục quyền

### 17.3.1. Khi nào cần khôi phục

- Quyền bị thu hồi nhầm
- Sau khi xử lý xong incident
- Sau khi xác minh tài khoản an toàn

### 17.3.2. Quy trình

```
1. Yêu cầu khôi phục quyền
   ↓
2. Phê duyệt (Security Team hoặc IT Manager)
   ↓
3. Xác minh tài khoản an toàn
   ↓
4. Khôi phục quyền
   ↓
5. Ghi log đầy đủ
   ↓
6. Monitor tài khoản trong 7 ngày
```

---

# 18. TRAINING VÀ AWARENESS

## 18.1. Training về Quyền Truy Cập Tối Thiểu

### 18.1.1. Đối tượng training

- **Tất cả nhân viên**: Training cơ bản về quyền truy cập
- **IT Team**: Training chi tiết về quản lý quyền
- **Developers**: Training về quyền trong development
- **Managers**: Training về phê duyệt quyền

### 18.1.2. Nội dung training

**Training cơ bản (1 giờ)**:
- Nguyên tắc quyền truy cập tối thiểu
- Quy trình yêu cầu quyền
- Trách nhiệm của người dùng
- Best practices

**Training nâng cao (2 giờ)**:
- Quản lý quyền chi tiết
- RBAC, JIT, SoD
- Security best practices
- Incident response

### 18.1.3. Tần suất training

- **Training mới**: Khi nhân viên mới vào
- **Training định kỳ**: Mỗi năm 1 lần
- **Training cập nhật**: Khi có thay đổi chính sách

## 18.2. Awareness Program

### 18.2.1. Nội dung

- **Newsletter**: Gửi hàng tháng về security awareness
- **Security alerts**: Cảnh báo về các vấn đề bảo mật
- **Best practices**: Chia sẻ best practices
- **Security alerts**: Cảnh báo về các vấn đề bảo mật

### 18.2.2. Kênh truyền thông

- Email
- Slack/Teams channel
- Wiki/Intranet
- Training sessions

## 18.3. Best Practices

### 18.3.1. Cho người dùng

- **Không chia sẻ tài khoản**: Mỗi người có tài khoản riêng
- **Không chia sẻ password**: Password là bí mật cá nhân
- **Báo cáo ngay**: Báo cáo ngay khi phát hiện vấn đề
- **Đổi password định kỳ**: Đổi password mỗi 90 ngày
- **Sử dụng MFA**: Kích hoạt MFA cho tài khoản

### 18.3.2. Cho IT Team

- **Review quyền định kỳ**: Rà soát quyền hàng quý
- **Thu hồi quyền không dùng**: Thu hồi quyền không được sử dụng
- **Ghi log đầy đủ**: Ghi log tất cả operations
- **Monitor bất thường**: Monitor các hoạt động bất thường
- **Cập nhật chính sách**: Cập nhật chính sách khi cần

### 18.3.3. Cho Managers

- **Phê duyệt cẩn thận**: Xem xét kỹ trước khi phê duyệt
- **Đánh giá rủi ro**: Đánh giá rủi ro trước khi cấp quyền
- **Review định kỳ**: Review quyền của team định kỳ
- **Training team**: Đảm bảo team được training đầy đủ

---

# 19. TỔNG HỢP CƠ CHẾ KIỂM SOÁT

## 19.1. Ma trận kiểm soát toàn diện

### 19.1.1. Kiểm soát theo quy trình

| Quy trình | Preventive | Detective | Corrective | Compensating |
|-----------|------------|-----------|------------|--------------|
| **Cấp quyền** | Phê duyệt bắt buộc, RBAC, MFA | Audit log, Monitoring | Auto-revoke, Incident response | Enhanced review, Dual approval |
| **Sử dụng quyền** | Time-bound, Scope-limited, JIT | Activity monitoring, Anomaly detection | Auto-disable, Auto-lock | Manual review, Frequent audits |
| **Rà soát quyền** | Automated reviews, Scheduled audits | Usage analysis, Compliance checks | Auto-revoke unused, Remediation | Manual review, Management oversight |
| **Thu hồi quyền** | Auto-expiry, Scheduled revocation | Monitoring, Alerts | Immediate revocation, Account lock | Manual verification, Backup access |

### 19.1.2. Kiểm soát theo hệ thống

| Hệ thống | Administrative | Technical | Physical |
|----------|----------------|-----------|----------|
| **Server** | Policy, Procedures, Training | RBAC, MFA, Encryption, Monitoring | Data center access, CCTV |
| **Database** | Access policy, DBA procedures | Role-based access, Audit logging, Encryption | Server room access, Backup storage |
| **Cloud** | Cloud policy, IAM procedures | IAM roles, CloudTrail, Encryption | Cloud provider security, Data residency |
| **Container** | Container policy, RBAC procedures | Kubernetes RBAC, Network policies, Monitoring | Infrastructure access, Container registry |
| **API** | API policy, Key management | API keys, Rate limiting, OAuth, Monitoring | API gateway security, Network security |
| **Secret** | Secret policy, Rotation procedures | Vault, Encryption, Access logging | Vault server security, Backup storage |

### 19.1.3. Kiểm soát theo vai trò

| Vai trò | Preventive | Detective | Corrective |
|---------|------------|-----------|------------|
| **Developer** | Read-only on prod, Limited access | Activity monitoring, Code review | Auto-revoke, Training |
| **DevOps** | JIT access, MFA required | Privileged access monitoring, Audit log | Auto-revoke, Incident response |
| **DBA** | Separate admin account, MFA | Database audit log, Query monitoring | Auto-disable, Rollback |
| **Admin** | Dual approval, Time-bound access | Continuous monitoring, Behavioral analytics | Immediate revocation, Account lock |

---

## 19.2. KPI và Metrics kiểm soát

### 19.2.1. Chỉ số hiệu quả kiểm soát

| Chỉ số | Mục tiêu | Cách đo lường |
|--------|----------|---------------|
| **Tỷ lệ vi phạm** | < 1% | Số vi phạm / Tổng hoạt động |
| **Thời gian phát hiện** | < 15 phút | Thời gian từ vi phạm đến phát hiện |
| **Thời gian khắc phục** | < 1 giờ | Thời gian từ phát hiện đến khắc phục |
| **Tỷ lệ tuân thủ** | > 95% | Số tuân thủ / Tổng yêu cầu |
| **Tỷ lệ tự động hóa** | > 80% | Số kiểm soát tự động / Tổng kiểm soát |
| **Tỷ lệ quyền không sử dụng** | < 5% | Số quyền không dùng / Tổng quyền |
| **Tỷ lệ quyền hết hạn chưa thu hồi** | < 1% | Số quyền hết hạn / Tổng quyền tạm thời |

### 19.2.2. Dashboard Metrics

**Real-time metrics:**
- Số lượng cảnh báo đang chờ xử lý
- Số lượng quyền JIT đang hoạt động
- Số lượng đăng nhập trong giờ
- Tỷ lệ tuân thủ hiện tại

**Historical metrics:**
- Xu hướng vi phạm theo thời gian
- Xu hướng cảnh báo theo thời gian
- Xu hướng sử dụng quyền theo thời gian
- Xu hướng tuân thủ theo thời gian

---

## 19.3. Quy trình đánh giá và cải thiện kiểm soát

### 19.3.1. Đánh giá định kỳ

**Tần suất:**
- **Hàng tuần**: Đánh giá cảnh báo và sự cố
- **Hàng tháng**: Đánh giá hiệu quả kiểm soát
- **Hàng quý**: Đánh giá toàn diện và cải thiện
- **Hàng năm**: Đánh giá và cập nhật chính sách

**Nội dung đánh giá:**
1. **Hiệu quả kiểm soát hiện tại**
   - Kiểm soát có hoạt động đúng không?
   - Kiểm soát có phát hiện được vi phạm không?
   - Kiểm soát có ngăn chặn được vi phạm không?

2. **Phát hiện gap và rủi ro mới**
   - Có gap nào trong kiểm soát không?
   - Có rủi ro mới nào xuất hiện không?
   - Kiểm soát có đủ để bảo vệ khỏi rủi ro mới không?

3. **Đề xuất cải thiện**
   - Kiểm soát nào cần được tăng cường?
   - Kiểm soát nào cần được tự động hóa?
   - Kiểm soát nào cần được thêm mới?

4. **Cập nhật kiểm soát**
   - Triển khai cải thiện
   - Kiểm thử kiểm soát mới
   - Giám sát hiệu quả

### 19.3.2. Quy trình cải thiện liên tục

```
1. Thu thập dữ liệu
   ↓
2. Phân tích và đánh giá
   ↓
3. Xác định gap và cơ hội cải thiện
   ↓
4. Thiết kế giải pháp
   ↓
5. Phê duyệt giải pháp
   ↓
6. Triển khai giải pháp
   ↓
7. Kiểm thử và xác nhận
   ↓
8. Giám sát và đánh giá
   ↓
9. Lặp lại quy trình
```

---

## 19.4. Tổng hợp công cụ và công nghệ

### 19.4.1. Công cụ kiểm soát

**Identity and Access Management (IAM):**
- Active Directory / LDAP
- Azure AD / Okta / OneLogin
- AWS IAM / GCP IAM / Azure RBAC

**Privileged Access Management (PAM):**
- CyberArk
- BeyondTrust
- HashiCorp Vault

**Security Information and Event Management (SIEM):**
- Splunk
- QRadar
- ArcSight
- ELK Stack

**Monitoring và Alerting:**
- Zabbix / Nagios
- Prometheus / Grafana
- Datadog / New Relic

**Compliance và Audit:**
- Varonis
- Netwrix
- ManageEngine ADAudit

### 19.4.2. Tự động hóa

**Infrastructure as Code (IaC):**
- Terraform
- Ansible
- CloudFormation

**CI/CD Integration:**
- Jenkins
- GitLab CI
- GitHub Actions

**Policy as Code:**
- Open Policy Agent (OPA)
- HashiCorp Sentinel
- AWS Config Rules

---

## 19.5. Checklist kiểm soát

### 19.5.1. Checklist hàng ngày

- [ ] Kiểm tra cảnh báo chưa xử lý
- [ ] Kiểm tra quyền JIT đã hết hạn
- [ ] Kiểm tra sự cố trong 24h
- [ ] Kiểm tra hệ thống giám sát hoạt động
- [ ] Kiểm tra log được ghi đầy đủ

### 19.5.2. Checklist hàng tuần

- [ ] Rà soát quyền tạm thời đã hết hạn
- [ ] Rà soát quyền không được sử dụng
- [ ] Phân tích cảnh báo và sự cố
- [ ] Kiểm tra tuân thủ chính sách
- [ ] Cập nhật dashboard và báo cáo

### 19.5.3. Checklist hàng tháng

- [ ] Rà soát quyền admin
- [ ] Đánh giá hiệu quả kiểm soát
- [ ] Phân tích KPI và metrics
- [ ] Đề xuất cải thiện
- [ ] Báo cáo cho quản lý

### 19.5.4. Checklist hàng quý

- [ ] Rà soát toàn bộ tài khoản
- [ ] Đánh giá toàn diện kiểm soát
- [ ] Gap analysis
- [ ] Cập nhật chính sách (nếu cần)
- [ ] Training và awareness
- [ ] Compliance review

---

**Xem chi tiết**:
- Phần 3.10 - Cơ chế kiểm soát toàn diện
- Phần 9.4 - Dashboard và Báo cáo
- Phần 16 - Audit và Compliance
- Phần 17 - Incident Response

---

# 20. PHỤ LỤC

## 20.1. Mẫu biểu

### 20.1.1. Biểu mẫu cấp quyền

| Thông tin | Mô tả |
|-----------|-------|
| **Người yêu cầu** | Tên, email, phòng ban |
| **Lý do** | Mô tả lý do cần quyền |
| **Quyền cần** | Role/quyền cụ thể |
| **Hệ thống** | Hệ thống cần quyền |
| **Thời gian** | Vĩnh viễn/Tạm thời (nếu tạm thời, ghi rõ thời hạn) |
| **Người phê duyệt** | Tên, chức vụ |
| **Ngày phê duyệt** | Ngày phê duyệt |
| **Ngày cấp quyền** | Ngày IT cấp quyền |
| **Ngày hết hạn** | Ngày quyền hết hạn (nếu tạm thời) |

### 20.1.2. Biểu mẫu thay đổi cấu hình

| Thông tin | Mô tả |
|-----------|-------|
| **Người yêu cầu** | Tên, email, phòng ban |
| **Hệ thống** | Hệ thống cần thay đổi |
| **Cấu hình hiện tại** | Mô tả cấu hình hiện tại |
| **Cấu hình mới** | Mô tả cấu hình mới |
| **Lý do** | Mô tả lý do thay đổi |
| **Rủi ro** | Đánh giá rủi ro |
| **Kế hoạch rollback** | Kế hoạch rollback nếu có vấn đề |
| **Người phê duyệt** | Tên, chức vụ |
| **Ngày thực hiện** | Ngày thực hiện thay đổi |

### 20.1.3. Biểu mẫu yêu cầu truy cập

| Thông tin | Mô tả |
|-----------|-------|
| **Người yêu cầu** | Tên, email, phòng ban |
| **Hệ thống** | Hệ thống cần truy cập |
| **Loại truy cập** | SSH, Database, API, Web, ... |
| **Lý do** | Mô tả lý do cần truy cập |
| **Thời gian** | Vĩnh viễn/Tạm thời (nếu tạm thời, ghi rõ thời hạn) |
| **IP whitelist** | IP cần whitelist (nếu cần) |
| **Người phê duyệt** | Tên, chức vụ |
| **Ngày phê duyệt** | Ngày phê duyệt |
| **Ngày cấp quyền** | Ngày IT cấp quyền |

## 20.2. Checklist rà soát quyền

- [ ] Danh sách tài khoản đã được thu thập
- [ ] Danh sách quyền của từng tài khoản đã được thu thập
- [ ] Lịch sử sử dụng quyền đã được phân tích
- [ ] Log truy cập đã được xem xét
- [ ] Quyền không cần thiết đã được xác định
- [ ] Quyền chưa sử dụng đã được xác định
- [ ] Quyền tạm thời đã hết hạn đã được xác định
- [ ] Tài khoản không hoạt động đã được xác định
- [ ] Đề xuất thu hồi/điều chỉnh đã được tạo
- [ ] Quản lý đã phê duyệt
- [ ] IT đã thực hiện thu hồi/điều chỉnh
- [ ] Log đã được ghi đầy đủ
- [ ] Người dùng đã được thông báo

## 20.3. Sơ đồ hạ tầng

(Sẽ được bổ sung khi hoàn chỉnh)

---

## 21. CHECKLIST VÀ QUICK REFERENCE (Đã bổ sung)

### 21.1. Checklist

**Tham chiếu**: `CL-011-CHECKLIST_QUYEN_TRUY_CAP.md`

Checklist chi tiết cho:
- Cấp quyền
- Rà soát quyền
- Cấp quyền tạm thời (JIT)
- Thiết lập MFA
- Quyền máy chủ (SSH/sudo)
- Quyền database
- Quyền deploy
- Rà soát định kỳ
- Xử lý tài khoản nghỉ việc
- Kiểm tra bảo mật
- Quyền Cloud/Container (Kubernetes, Docker, Cloud IAM) ⭐
- Quyền API/Application (API key, OAuth, Feature flags) ⭐
- Quản lý Secret (Vault, Secrets Manager) ⭐
- Audit và Compliance ⭐
- Incident Response ⭐

### 21.2. Quick Reference

**Tham chiếu**: `QUICK_REFERENCE_QUYEN_TRUY_CAP.md`

Bảng tra cứu nhanh:
- Nguyên tắc cơ bản
- Quyền theo vai trò
- Quyền database (Role)
- Cấp độ phê duyệt
- Thời gian quyền tạm thời
- Rà soát định kỳ
- MFA
- Tự động khóa tài khoản
- Quy trình tóm tắt
- Quyền Cloud/Container ⭐
- Quyền API/Application ⭐
- Quản lý Secret ⭐
- Audit Log Retention ⭐
- Incident Response ⭐

### 21.3. Template

**Tham chiếu**: `TP-006-TEMPLATE_YEU_CAU_CAP_QUYEN.md`

Template để tạo yêu cầu cấp quyền với đầy đủ thông tin cần thiết.

---

## 22. THAM CHIẾU

### Quy trình liên quan

- **QT-003**: Quy trình Upcode (Phần 9 - Quy định về quyền truy cập)
- **QT-002**: Quy trình Quản trị Vận hành
- **QT-004**: Quy trình Hotfix

### Checklist và Template

- **CL-011**: Checklist Quyền Truy Cập
- **TP-006**: Template Yêu Cầu Cấp Quyền
- **QUICK_REFERENCE_QUYEN_TRUY_CAP**: Bảng tra cứu nhanh
- **HUONG_DAN_SU_DUNG_QUYEN_TRUY_CAP**: Hướng dẫn sử dụng quyền truy cập (trong folder Hỗ trợ)

---

**Phiên bản**: 3.0
**Ngày ban hành**: [Ngày hiện tại]
**Người soạn**: 
**Trạng thái**: Chính thức
