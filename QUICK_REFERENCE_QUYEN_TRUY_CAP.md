# QUICK REFERENCE - QUYỀN TRUY CẬP TỐI THIỂU
## Bảng tra cứu nhanh

**Tham chiếu**: `CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU.md`

---

## TẠI SAO QUAN TRỌNG? (TÓM TẮT)

### Lợi ích chính
- **Giảm 80-90% rủi ro bảo mật**: Bảo vệ khỏi tấn công, vi phạm dữ liệu
- **Tuân thủ pháp luật**: ISO 27001, GDPR, SOC 2, PCI DSS
- **Giảm 60-70% lỗi vô ý**: Tránh xóa nhầm, cấu hình sai
- **Truy vết dễ dàng**: Biết rõ ai làm gì, khi nào
- **Tiết kiệm chi phí**: Tránh thiệt hại hàng triệu USD từ sự cố bảo mật

### Rủi ro nếu không tuân thủ
- **Thiệt hại tài chính**: Trung bình $4.45 triệu USD/vụ vi phạm
- **Mất danh tiếng**: 66% khách hàng mất niềm tin sau sự cố
- **Vi phạm pháp luật**: Phạt GDPR lên đến 4% doanh thu
- **Rủi ro bảo mật cao**: 74% vụ vi phạm liên quan đến quyền quá cao

** Xem chi tiết**: Phần 1.1-1.5 trong `CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU.md`

---

## NGUYÊN TẮC CƠ BẢN

| Nguyên tắc | Mô tả |
|------------|-------|
| **Least Privilege** | Cấp đúng quyền – đủ quyền – chỉ quyền cần thiết |
| **RBAC** | Phân quyền theo vai trò (Role-Based Access Control) |
| **JIT** | Cấp quyền tạm thời (Just-In-Time) |
| **SoD** | Separation of Duties - Không một người có toàn quyền |
| **Deny-by-default** | Từ chối tất cả, chỉ cho phép khi được phê duyệt |

---

## QUYỀN THEO VAI TRÒ

### Quyền truy cập môi trường

| Môi trường | Developer | DevOps | QA | PM/PDM | DBA |
|------------|-----------|--------|----|----|-----|
| **Development** | Read/Write | Read/Write | Read | Read | Read/Write |
| **Staging/UAT** | Read | Read/Write | Read/Write | Read | Read/Write |
| **Production** | Read (log only) | Read/Write* | Read | Read | Read/Write* |
| **DR** | Read (log only) | Read/Write* | Read | Read | Read/Write* |

*Theo quy trình, có phê duyệt, có log

### Quyền deploy

| Vai trò | Development | Staging/UAT | Production/DR |
|---------|-------------|-------------|---------------|
| **Developer** | Deploy | Không deploy | Không deploy |
| **DevOps** | Deploy | Deploy | Deploy* |
| **QA** | Không deploy | Không deploy | Không deploy |
| **DBA** | DB changes | DB changes | DB changes* |

*Sau khi có phê duyệt (theo QT-003)

### Quyền database

| Vai trò | Development | Staging/UAT | Production/DR |
|---------|-------------|-------------|---------------|
| **Developer** | Read/Write | ReadOnly | ReadOnly |
| **DevOps** | Read/Write | Read/Write | Read/Write* |
| **QA** | ReadOnly | ReadOnly | ReadOnly |
| **DBA** | DBAdmin | DBAdmin | DBAdmin* |

*Theo quy trình, có log

---

## QUYỀN DATABASE (ROLE)

| Role | Quyền | Đối tượng | Mục đích |
|------|-------|-----------|----------|
| **ReadOnly** | SELECT | Developer, QA | Xem dữ liệu, không được thay đổi |
| **ReadWrite** | SELECT, INSERT, UPDATE, DELETE | Application, Service Account | Ứng dụng truy cập database |
| **DBAdmin** | Tất cả quyền | DBA, DevOps (theo quy trình) | Quản trị database |

---

## CẤP ĐỘ PHÊ DUYỆT

| Level | Người phê duyệt | Quyền |
|-------|-----------------|-------|
| **1.0** | PM/PDM | Quyền cơ bản, môi trường Development/Staging |
| **2.0** | Ban CLGSP hoặc Lãnh đạo TT | Quyền trung bình, môi trường UAT |
| **3.0** | Ban CLGSP + Ban KTHT | Quyền cao, môi trường Production |
| **4.0** | Lãnh đạo Công ty | Quyền đặc biệt, hệ thống cốt lõi |

---

## ⏱ THỜI GIAN QUYỀN TẠM THỜI (JIT)

| Loại quyền | Thời gian tối đa | Ghi chú |
|------------|------------------|---------|
| **Deploy Production** | 1-2 giờ | Tự động hết hạn sau khi deploy |
| **Quyền admin tạm thời** | 4 giờ | Có thể gia hạn nếu cần |
| **Quyền database tạm thời** | 2 giờ | Tự động hết hạn |
| **Quyền cấu hình tạm thời** | 1 giờ | Tự động hết hạn |

---

## RÀ SOÁT ĐỊNH KỲ

| Loại rà soát | Tần suất | Người thực hiện |
|--------------|----------|-----------------|
| **Quyền admin** | Hàng tháng | IT Manager, Security Team |
| **Toàn bộ tài khoản** | Hàng quý | IT Team |
| **Quyền tạm thời** | Hàng tuần | IT Team |
| **Quyền theo role** | Hàng quý | IT Manager |

---

## MFA (MULTI-FACTOR AUTHENTICATION)

| Loại tài khoản | MFA | Phương thức |
|----------------|-----|-------------|
| **Tài khoản admin** | Bắt buộc | TOTP (Google Authenticator, Authy) hoặc SMS |
| **Tài khoản có quyền cao** | Bắt buộc | TOTP hoặc SMS |
| **Tài khoản người dùng thông thường** | Khuyến khích | TOTP hoặc SMS |
| **Tài khoản service** | Không áp dụng | API key/Token |

---

## TỰ ĐỘNG KHÓA TÀI KHOẢN

| Điều kiện | Hành động | Thời gian cảnh báo |
|-----------|-----------|-------------------|
| **Không dùng trong 60 ngày** | Tự động khóa | 7 ngày trước |
| **Không đăng nhập trong 90 ngày** | Tự động vô hiệu hóa | 7 ngày trước |
| **Admin không dùng trong 30 ngày** | Cảnh báo và rà soát | Ngay lập tức |
| **Nghỉ việc** | Thu hồi trong 24 giờ | Ngay lập tức |

---

## QUY TRÌNH CẤP QUYỀN (TÓM TẮT)

```
1. Yêu cầu quyền
 ↓
2. Phê duyệt (Level 1.0-4.0)
 ↓
3. Cấp quyền theo role
 ↓
4. Ghi log & thông báo
```

---

## QUY TRÌNH RÀ SOÁT (TÓM TẮT)

```
1. Thu thập dữ liệu
 ↓
2. Phân tích
 ↓
3. Đề xuất
 ↓
4. Phê duyệt và thực hiện
```

---

## QUY TRÌNH CẤP QUYỀN TẠM THỜI (JIT)

```
1. Yêu cầu quyền (mô tả lý do, thời gian)
 ↓
2. Phê duyệt nhanh
 ↓
3. Cấp quyền (tự động hết hạn)
 ↓
4. Thu hồi sau khi hoàn thành
```

---

## LIÊN HỆ

- **Yêu cầu quyền**: [Hệ thống quản lý quyền]
- **Hỗ trợ IT**: [Email/Phone]
- **Security Team**: [Email/Phone]

---

## THAM CHIẾU

- **Chính sách đầy đủ**: `CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU.md`
- **Checklist**: `CL-011-CHECKLIST_QUYEN_TRUY_CAP.md`
- **Quy trình Upcode**: `QT-003-UPCODE.md` - Phần 9

---

## QUYỀN CLOUD/CONTAINER

### Kubernetes RBAC

| Namespace | Developer | DevOps | QA | DBA |
|-----------|-----------|--------|----|-----|
| **development** | Read/Write | Read/Write | Read | Read |
| **staging** | Read | Read/Write | Read/Write | Read |
| **production** | Read (log only) | Read/Write* | Read | Read |
| **kube-system** | No access | Read* | No access | No access |

*Theo quy trình, có phê duyệt

### Docker Registry

| Vai trò | Pull | Push | Delete |
|---------|------|------|--------|
| **Developer** | (dev/staging) | (dev/staging) | |
| **DevOps** | (all) | (all) | (staging/dev) |
| **QA** | (dev/staging) | | |

### Cloud IAM

| Cloud | Developer | DevOps | DBA | Admin |
|-------|-----------|--------|-----|-------|
| **AWS** | Read-only (dev/staging) | Full (dev/staging), Limited (prod) | RDS access | Full* |
| **Azure** | Reader (dev/staging) | Contributor (dev/staging), Limited (prod) | SQL DB Contributor | Owner* |
| **GCP** | Viewer (dev/staging) | Editor (dev/staging), Limited (prod) | Cloud SQL Client | Owner* |

*Theo quy trình, có phê duyệt

---

## QUYỀN API/APPLICATION

### API Key Rate Limiting

| Vai trò | Rate Limit |
|---------|------------|
| **Developer** | 100 requests/minute |
| **Application** | 1000 requests/minute |
| **Admin** | 5000 requests/minute |

### Feature Flags

| Vai trò | Enable/Disable |
|---------|----------------|
| **Developer** | |
| **DevOps** | (dev/staging) |
| **Admin** | (all) |

---

## QUYỀN SECRET MANAGEMENT

### HashiCorp Vault

| Vai trò | Read | Write | Delete | Admin |
|---------|------|-------|--------|-------|
| **Developer** | (dev secrets) | | | |
| **DevOps** | (all) | (dev/staging) | | |
| **DBA** | (DB secrets) | | | |
| **Admin** | (all) | (all) | (all) | |

### Secret Rotation

| Loại secret | Rotation period |
|-------------|-----------------|
| **API keys** | 90 ngày |
| **Database passwords** | 180 ngày |
| **SSL certificates** | Trước khi hết hạn |
| **SSH keys** | 365 ngày |

---

## AUDIT LOG RETENTION

| Loại log | Retention |
|----------|-----------|
| **Access log** | 90 ngày |
| **Admin actions** | 1 năm |
| **Authentication log** | 90 ngày |
| **Secret access log** | 1 năm |
| **Compliance log** | 7 năm |

---

## INCIDENT RESPONSE

### Escalation

| Mức độ | Thời gian xử lý | Người xử lý |
|--------|-----------------|------------|
| **Critical** | Ngay lập tức | Security Team |
| **High** | 1 giờ | IT Team |
| **Medium** | 24 giờ | IT Team |
| **Low** | 3 ngày | IT Team |

---

**Phiên bản**: 2.0

