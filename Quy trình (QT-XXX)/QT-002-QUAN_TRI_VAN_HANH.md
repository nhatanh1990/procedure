# QT-002: QUY TRÌNH QUẢN TRỊ VẬN HÀNH

---

## 📋 THÔNG TIN TÀI LIỆU

- **Mã quy trình**: QT-002
- **Tên quy trình**: Quy trình Quản trị Vận hành
- **Phiên bản**: 1.0
- **Ngày ban hành**: [Ngày hiện tại]
- **Người soạn**: 
- **Trạng thái**: Chính thức

---

## 📚 MỤC LỤC

1. [Tổng quan](#1-tổng-quan)
2. [Quy trình giám sát hệ thống](#2-quy-trình-giám-sát-hệ-thống)
3. [Quy trình quản lý log](#3-quy-trình-quản-lý-log)
4. [Quy trình quản lý backup](#4-quy-trình-quản-lý-backup)
5. [Quy trình quản lý cấu hình](#5-quy-trình-quản-lý-cấu-hình)
6. [Quy trình quản lý tài nguyên](#6-quy-trình-quản-lý-tài-nguyên)
7. [Quy trình xử lý sự cố vận hành](#7-quy-trình-xử-lý-sự-cố-vận-hành)
8. [Quy định và tiêu chuẩn](#8-quy-định-và-tiêu-chuẩn)
9. [Quy định về Quyền Truy Cập Tối Thiểu](#9-quy-định-về-quyền-truy-cập-tối-thiểu) ⭐
10. [Checklist](#10-checklist)

---

## 1. TỔNG QUAN

### 1.1. Mục đích

Quy trình quản trị vận hành nhằm đảm bảo hệ thống hoạt động ổn định, liên tục, an toàn và hiệu quả.

### 1.2. Phạm vi

- Giám sát hệ thống (Monitoring)
- Quản lý log
- Quản lý backup
- Quản lý cấu hình
- Quản lý tài nguyên
- Xử lý sự cố vận hành

### 1.3. Đối tượng

- DevOps Team
- Development Team
- QA Team
- Ban CLGSP

---

## 2. QUY TRÌNH GIÁM SÁT HỆ THỐNG

### 2.1. Tổng quan

Giám sát hệ thống là hoạt động theo dõi liên tục các chỉ số và trạng thái của hệ thống để phát hiện sớm các vấn đề.

### 2.2. Các chỉ số cần giám sát

#### 2.2.1. Chỉ số hạ tầng

- **CPU usage**: Sử dụng CPU (%)
- **Memory usage**: Sử dụng bộ nhớ (%)
- **Disk usage**: Sử dụng disk (%)
- **Network traffic**: Lưu lượng mạng (Mbps)
- **Response time**: Thời gian phản hồi (ms)

#### 2.2.2. Chỉ số ứng dụng

- **Request rate**: Số lượng request/giây
- **Error rate**: Tỷ lệ lỗi (%)
- **Response time**: Thời gian phản hồi (ms)
- **Throughput**: Thông lượng (req/s)
- **Active connections**: Số kết nối đang hoạt động

#### 2.2.3. Chỉ số database

- **Connection pool**: Số kết nối trong pool
- **Query performance**: Thời gian thực thi query (ms)
- **Lock wait time**: Thời gian chờ lock (ms)
- **Replication lag**: Độ trễ replication (nếu có) (s)

#### 2.2.4. Chỉ số business

- **Số người dùng online**: Số lượng người dùng đang online
- **Số giao dịch**: Số lượng giao dịch/giờ
- **Tỷ lệ thành công**: Tỷ lệ giao dịch thành công (%)

### 2.3. Quy trình giám sát

```
1. Thiết lập monitoring
   → Cấu hình monitoring tools (Prometheus, Grafana, ...)
   → Thiết lập alerting rules
   → Thiết lập dashboard
   → Thiết lập notification channels

2. Giám sát liên tục
   → Monitoring 24/7
   → Kiểm tra dashboard định kỳ
   → Xử lý cảnh báo
   → Ghi nhận sự kiện

3. Phân tích và báo cáo
   → Phân tích xu hướng
   → Phân tích hiệu năng
   → Báo cáo định kỳ (hàng ngày, hàng tuần, hàng tháng)
   → Đề xuất cải tiến
```

### 2.4. Alerting rules

#### 2.4.1. Mức độ cảnh báo

| Mức độ | Mô tả | Thời gian xử lý | Người xử lý |
|--------|-------|-----------------|-------------|
| **Critical** | Hệ thống down, mất dữ liệu | ≤ 15 phút | DevOps + Development |
| **High** | Ảnh hưởng nghiêm trọng đến dịch vụ | ≤ 1 giờ | DevOps |
| **Medium** | Ảnh hưởng một phần dịch vụ | ≤ 4 giờ | DevOps |
| **Low** | Ảnh hưởng nhỏ, có thể chấp nhận | ≤ 24 giờ | DevOps |

#### 2.4.2. Ngưỡng cảnh báo

- **CPU usage**: > 80% (High), > 90% (Critical)
- **Memory usage**: > 80% (High), > 90% (Critical)
- **Disk usage**: > 80% (High), > 90% (Critical)
- **Error rate**: > 1% (Medium), > 5% (High), > 10% (Critical)
- **Response time**: > 1s (Medium), > 3s (High), > 5s (Critical)

### 2.5. Dashboard

#### 2.5.1. Dashboard real-time

- Trạng thái hệ thống hiện tại
- Các chỉ số quan trọng
- Cảnh báo đang hoạt động
- Sự kiện gần đây

#### 2.5.2. Dashboard báo cáo

- Báo cáo hàng ngày: Tổng quan 24h qua
- Báo cáo hàng tuần: Xu hướng tuần
- Báo cáo hàng tháng: Phân tích tháng

---

## 3. QUY TRÌNH QUẢN LÝ LOG

### 3.1. Tổng quan

Quản lý log bao gồm việc ghi, thu thập, phân tích và lưu trữ log.

### 3.2. Yêu cầu log

#### 3.2.1. Các loại log cần ghi

- **Application log**: Log từ ứng dụng (INFO, WARN, ERROR)
- **Access log**: Log truy cập (HTTP requests)
- **Security log**: Log bảo mật (authentication, authorization)
- **Audit log**: Log kiểm toán (thay đổi quan trọng)
- **System log**: Log hệ thống (OS, middleware)

#### 3.2.2. Nội dung log

- **Timestamp**: Thời gian (ISO 8601 format)
- **Level**: Mức độ (INFO, WARN, ERROR, DEBUG)
- **Service/Module name**: Tên service/module
- **Request ID/Trace ID**: ID để trace request
- **User ID**: ID người dùng (nếu có)
- **Message**: Nội dung log
- **Stack trace**: Stack trace (nếu error)
- **Context**: Thông tin bổ sung (JSON format)

### 3.3. Quy trình quản lý log

```
1. Ghi log
   → Ghi log đầy đủ, có cấu trúc
   → Không ghi thông tin nhạy cảm (password, token, ...)
   → Sử dụng log level phù hợp
   → Sử dụng structured logging (JSON)

2. Thu thập log
   → Centralized logging (ELK, Loki, ...)
   → Log rotation (theo size/time)
   → Log retention policy
   → Log aggregation

3. Phân tích log
   → Tìm kiếm log
   → Phân tích lỗi
   → Phân tích xu hướng
   → Phân tích bảo mật

4. Lưu trữ log
   → Lưu trữ theo chính sách
   → Backup log quan trọng
   → Xóa log cũ theo chính sách
   → Archive log (nếu cần)
```

### 3.4. Log retention policy

- **Application log**: 30 ngày
- **Access log**: 90 ngày
- **Security log**: 1 năm
- **Audit log**: 2 năm
- **System log**: 30 ngày

### 3.5. Thông tin không được ghi trong log

- Password
- Token/API key
- Credit card number
- Personal identification number (PIN)
- SSH private key
- Certificate private key

---

## 4. QUY TRÌNH QUẢN LÝ BACKUP

### 4.1. Tổng quan

Quản lý backup bao gồm việc lập lịch, thực hiện, kiểm tra và quản lý backup.

### 4.2. Yêu cầu backup

#### 4.2.1. Các loại backup cần thực hiện

- **Database backup**: Backup database (hàng ngày)
- **Code backup**: Backup code (mỗi khi deploy - tag/commit)
- **Configuration backup**: Backup cấu hình (mỗi khi thay đổi)
- **Data backup**: Backup dữ liệu (theo yêu cầu nghiệp vụ)

#### 4.2.2. Chính sách backup

- **Full backup**: Hàng ngày (11:00 PM - 05:00 AM)
- **Incremental backup**: Hàng giờ (nếu cần)
- **Retention**: 30 ngày
- **Backup location**: Off-site và on-site
- **Encryption**: Encrypt backup (nếu chứa dữ liệu nhạy cảm)

### 4.3. Quy trình quản lý backup

```
1. Lập lịch backup
   → Thiết lập schedule backup
   → Tự động hóa backup
   → Kiểm tra backup thành công
   → Cảnh báo nếu backup thất bại

2. Thực hiện backup
   → Thực hiện backup theo schedule
   → Verify backup file
   → Kiểm tra tính toàn vẹn
   → Ghi nhận kết quả

3. Lưu trữ backup
   → Lưu trữ tại nhiều location
   → Encrypt backup (nếu cần)
   → Kiểm tra tính toàn vẹn
   → Quản lý dung lượng

4. Test restore
   → Test restore định kỳ (hàng tháng)
   → Test restore sau mỗi thay đổi lớn
   → Đảm bảo backup có thể restore được
   → Ghi nhận kết quả test

5. Quản lý backup
   → Xóa backup cũ theo chính sách
   → Giám sát dung lượng backup
   → Báo cáo định kỳ
   → Đề xuất cải tiến
```

### 4.4. Test restore

#### 4.4.1. Tần suất test restore

- **Định kỳ**: Hàng tháng
- **Sau thay đổi lớn**: Sau mỗi thay đổi lớn (migration, upgrade, ...)
- **Trước restore thực tế**: Luôn test trước khi restore thực tế

#### 4.4.2. Quy trình test restore

1. Chọn backup để test
2. Restore vào môi trường test
3. Verify dữ liệu
4. Test chức năng
5. Ghi nhận kết quả

---

## 5. QUY TRÌNH QUẢN LÝ CẤU HÌNH

### 5.1. Tổng quan

Quản lý cấu hình bao gồm việc tạo, lưu trữ, triển khai và quản lý thay đổi cấu hình.

### 5.2. Yêu cầu quản lý cấu hình

#### 5.2.1. Các loại cấu hình

- **Application configuration**: Cấu hình ứng dụng
- **Environment variables**: Biến môi trường
- **Database connection strings**: Chuỗi kết nối database
- **API keys và secrets**: API keys và secrets
- **Feature flags**: Feature flags

#### 5.2.2. Nguyên tắc

- Cấu hình không hardcode trong code
- Sử dụng configuration management (ConfigMap, Consul, Vault, ...)
- Version control cho cấu hình
- Encrypt sensitive configuration
- Tách biệt cấu hình theo môi trường

### 5.3. Quy trình quản lý cấu hình

```
1. Tạo cấu hình
   → Tạo cấu hình theo môi trường
   → Sử dụng template
   → Validate cấu hình
   → Review cấu hình

2. Lưu trữ cấu hình
   → Lưu trữ trong version control
   → Sử dụng configuration management tool
   → Encrypt sensitive data
   → Tổ chức theo môi trường

3. Triển khai cấu hình
   → Deploy cấu hình cùng với code
   → Validate cấu hình sau khi deploy
   → Rollback nếu cấu hình sai
   → Ghi nhận thay đổi

4. Quản lý thay đổi
   → Ghi nhận mọi thay đổi cấu hình
   → Review thay đổi cấu hình
   → Test cấu hình mới
   → Phê duyệt thay đổi (nếu cần)
```

### 5.4. Quản lý secrets

#### 5.4.1. Yêu cầu

- Secrets phải được encrypt
- Sử dụng secret management tool (Vault, AWS Secrets Manager, ...)
- Không commit secrets vào version control
- Rotate secrets định kỳ

#### 5.4.2. Quy trình quản lý secrets

1. Tạo secret trong secret management tool
2. Encrypt secret
3. Cấp quyền truy cập
4. Sử dụng secret trong ứng dụng
5. Rotate secret định kỳ

---

## 6. QUY TRÌNH QUẢN LÝ TÀI NGUYÊN

### 6.1. Tổng quan

Quản lý tài nguyên bao gồm việc giám sát, phân tích, tối ưu và mở rộng tài nguyên hệ thống.

### 6.2. Yêu cầu quản lý tài nguyên

#### 6.2.1. Các tài nguyên cần quản lý

- **CPU**: Bộ xử lý
- **Memory**: Bộ nhớ
- **Disk**: Ổ đĩa
- **Network bandwidth**: Băng thông mạng
- **Database connections**: Kết nối database

#### 6.2.2. Nguyên tắc

- Giám sát sử dụng tài nguyên
- Dự báo nhu cầu tài nguyên
- Tối ưu sử dụng tài nguyên
- Auto-scaling (nếu có thể)
- Cảnh báo khi tài nguyên gần hết

### 6.3. Quy trình quản lý tài nguyên

```
1. Giám sát tài nguyên
   → Giám sát sử dụng tài nguyên
   → Phát hiện tài nguyên thiếu
   → Cảnh báo khi tài nguyên > 80%
   → Ghi nhận sử dụng

2. Phân tích và dự báo
   → Phân tích xu hướng sử dụng
   → Dự báo nhu cầu tài nguyên
   → Lập kế hoạch mở rộng
   → Đề xuất tối ưu

3. Tối ưu tài nguyên
   → Tối ưu code
   → Tối ưu database
   → Tối ưu infrastructure
   → Đánh giá hiệu quả

4. Mở rộng tài nguyên
   → Lập kế hoạch mở rộng
   → Phê duyệt mở rộng
   → Thực hiện mở rộng
   → Kiểm tra sau mở rộng
```

### 6.4. Auto-scaling

#### 6.4.1. Yêu cầu

- Thiết lập auto-scaling rules
- Giám sát auto-scaling events
- Đánh giá hiệu quả auto-scaling
- Điều chỉnh auto-scaling rules

#### 6.4.2. Ngưỡng auto-scaling

- **Scale up**: Khi CPU > 70% hoặc Memory > 70%
- **Scale down**: Khi CPU < 30% và Memory < 30% trong 10 phút

---

## 7. QUY TRÌNH XỬ LÝ SỰ CỐ VẬN HÀNH

### 7.1. Tổng quan

Xử lý sự cố vận hành là quy trình phát hiện, phân loại, xử lý và đánh giá sau sự cố.

### 7.2. Phân loại sự cố vận hành

#### 7.2.1. Sự cố hạ tầng

- Server down
- Network issue
- Disk full
- Memory leak
- CPU overload

#### 7.2.2. Sự cố ứng dụng

- Application crash
- High error rate
- Performance degradation
- Memory leak
- Database connection issue

#### 7.2.3. Sự cố database

- Database connection issue
- Slow query
- Deadlock
- Data corruption
- Replication lag

### 7.3. Quy trình xử lý sự cố

```
1. Phát hiện sự cố
   → Từ monitoring/alerting
   → Từ người dùng
   → Từ log
   → Từ team khác

2. Phân loại sự cố
   → Đánh giá mức độ nghiêm trọng
   → Phân loại loại sự cố
   → Xác định nguyên nhân
   → Ưu tiên xử lý

3. Xử lý sự cố
   → Thực hiện khắc phục
   → Giám sát quá trình khắc phục
   → Xác nhận đã khắc phục
   → Ghi nhận

4. Đánh giá sau
   → Phân tích nguyên nhân
   → Đề xuất cải tiến
   → Cập nhật runbook
   → Báo cáo
```

### 7.4. Runbook

#### 7.4.1. Yêu cầu

- Mỗi loại sự cố phải có runbook
- Runbook phải được cập nhật thường xuyên
- Runbook phải được test định kỳ

#### 7.4.2. Nội dung runbook

- Mô tả sự cố
- Nguyên nhân thường gặp
- Các bước xử lý
- Cách verify đã khắc phục
- Liên hệ khi cần hỗ trợ

---

## 8. QUY ĐỊNH VÀ TIÊU CHUẨN

### 8.1. Quy định về giám sát

- Giám sát 24/7
- Cảnh báo phải được xử lý trong thời gian quy định
- Dashboard phải được cập nhật real-time
- Báo cáo định kỳ (hàng ngày, hàng tuần, hàng tháng)

### 8.2. Quy định về backup

- Database: Backup hàng ngày, retention 30 ngày
- Code: Backup mỗi khi deploy (tag/commit)
- Configuration: Backup mỗi khi thay đổi
- Test restore: Hàng tháng

### 8.3. Quy định về log

- Log phải đầy đủ, có cấu trúc
- Không ghi thông tin nhạy cảm
- Log phải được lưu trữ tập trung
- Log retention: Theo chính sách

### 8.4. Quy định về cấu hình

- Cấu hình không hardcode
- Sử dụng configuration management
- Sensitive data phải encrypt
- Mọi thay đổi cấu hình phải được review

### 8.5. Quy định về tài nguyên

- Giám sát sử dụng tài nguyên liên tục
- Cảnh báo khi tài nguyên > 80%
- Lập kế hoạch mở rộng khi tài nguyên > 70%

---

## 9. QUY ĐỊNH VỀ QUYỀN TRUY CẬP TỐI THIỂU

### 9.1. Nguyên tắc

- **Cấp đúng quyền – đủ quyền – chỉ quyền cần thiết**: Mỗi người dùng chỉ được cấp quyền đủ để thực hiện nhiệm vụ vận hành
- **Phân quyền theo vai trò (RBAC)**: Tất cả quyền được cấp thông qua Role
- **Cấp quyền tạm thời (JIT)**: Quyền cao chỉ được cấp khi có yêu cầu chính đáng, tự động hết hạn sau khi hoàn thành công việc

### 9.2. Quyền truy cập trong quản trị vận hành

#### 9.2.1. Quyền truy cập server

| Vai trò | SSH | Sudo | Config | Service |
|---------|-----|------|--------|---------|
| **Developer** | ❌ | ❌ | ❌ | ❌ |
| **DevOps** | ✅* | ✅* | ✅* | ✅* |
| **SysAdmin** | ✅* | ✅* | ✅* | ✅* |
| **DBA** | ✅* (DB server only) | ❌ | ❌ | ❌ |

*Sau khi có phê duyệt, có log

#### 9.2.2. Quyền truy cập log

| Vai trò | Read Log | Search Log | Export Log | Delete Log |
|---------|----------|------------|------------|------------|
| **Developer** | ✅ (dev/staging) | ✅ (dev/staging) | ❌ | ❌ |
| **DevOps** | ✅ (all) | ✅ (all) | ✅* | ❌ |
| **SysAdmin** | ✅ (all) | ✅ (all) | ✅* | ✅* |
| **QA** | ✅ (dev/staging) | ✅ (dev/staging) | ❌ | ❌ |

*Sau khi có phê duyệt

#### 9.2.3. Quyền truy cập backup

| Vai trò | View Backup | Create Backup | Restore Backup | Delete Backup |
|---------|-------------|---------------|----------------|---------------|
| **Developer** | ❌ | ❌ | ❌ | ❌ |
| **DevOps** | ✅ | ✅* | ✅* | ❌ |
| **SysAdmin** | ✅ | ✅* | ✅* | ✅* |
| **DBA** | ✅ (DB backup) | ✅* (DB backup) | ✅* (DB backup) | ❌ |

*Sau khi có phê duyệt

#### 9.2.4. Quyền truy cập cấu hình

| Vai trò | View Config | Modify Config | Deploy Config | Rollback Config |
|---------|-------------|---------------|---------------|-----------------|
| **Developer** | ✅ (dev/staging) | ❌ | ❌ | ❌ |
| **DevOps** | ✅ (all) | ✅* | ✅* | ✅* |
| **SysAdmin** | ✅ (all) | ✅* | ✅* | ✅* |

*Sau khi có phê duyệt

#### 9.2.5. Quyền truy cập monitoring tools

| Vai trò | View Metrics | View Alerts | Configure Alerts | Acknowledge Alerts |
|---------|--------------|-------------|------------------|-------------------|
| **Developer** | ✅ (dev/staging) | ✅ (dev/staging) | ❌ | ❌ |
| **DevOps** | ✅ (all) | ✅ (all) | ✅* | ✅ |
| **SysAdmin** | ✅ (all) | ✅ (all) | ✅* | ✅ |
| **On-call** | ✅ (all) | ✅ (all) | ❌ | ✅ |

*Sau khi có phê duyệt

### 9.3. Quy trình cấp quyền cho vận hành

1. **Yêu cầu quyền**
   - Tạo yêu cầu trong hệ thống quản lý quyền
   - Mô tả lý do cần quyền (ví dụ: Giám sát hệ thống, Xử lý sự cố)
   - Xác định loại quyền và tài nguyên
   - Xác định thời gian: Vĩnh viễn hoặc tạm thời

2. **Phê duyệt**
   - PM/PDM phê duyệt cho quyền Level 1.0-2.0
   - Ban CLGSP phê duyệt cho quyền Level 3.0
   - Lãnh đạo phê duyệt cho quyền Level 4.0

3. **Cấp quyền**
   - IT cấp quyền theo role
   - Cấp quyền cho tài nguyên cụ thể
   - Ghi log đầy đủ

4. **Thu hồi quyền**
   - Thu hồi quyền khi không còn cần
   - Thu hồi quyền khi nhân viên nghỉ việc
   - Ghi log thu hồi

### 9.4. Giám sát và ghi log

- Mọi hành động với quyền cao đều được ghi log
- Log được lưu tối thiểu 90 ngày
- Rà soát log định kỳ (hàng tháng)
- Cảnh báo khi có hành động bất thường

**Tham chiếu**: 
- `CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU.md` - Phần 4, 5, 6, 7, 9
- `QUICK_REFERENCE_QUYEN_TRUY_CAP.md` - Tra cứu nhanh
- `TP-006-TEMPLATE_YEU_CAU_CAP_QUYEN.md` - Template yêu cầu cấp quyền

---

## 10. CHECKLIST

**Tham chiếu chi tiết**: `CL-001-CHECKLIST_VAN_HANH.md`

### 10.1. Checklist giám sát

- [ ] Monitoring tools đã được cấu hình
- [ ] Alerting rules đã được thiết lập
- [ ] Dashboard đã được tạo
- [ ] Có người giám sát 24/7
- [ ] Có quy trình xử lý cảnh báo
- [ ] Có báo cáo định kỳ

### 10.2. Checklist quản lý log

- [ ] Log đã được cấu hình đầy đủ
- [ ] Centralized logging đã được thiết lập
- [ ] Log rotation đã được cấu hình
- [ ] Log retention policy đã được định nghĩa
- [ ] Có công cụ tìm kiếm và phân tích log
- [ ] Log không chứa thông tin nhạy cảm

### 10.3. Checklist quản lý backup

- [ ] Backup schedule đã được thiết lập
- [ ] Backup tự động hóa
- [ ] Backup được lưu trữ tại nhiều location
- [ ] Backup được encrypt (nếu cần)
- [ ] Test restore đã được thực hiện định kỳ
- [ ] Backup retention policy đã được áp dụng

### 10.4. Checklist quản lý cấu hình

- [ ] Cấu hình không hardcode trong code
- [ ] Sử dụng configuration management tool
- [ ] Cấu hình được version control
- [ ] Sensitive data được encrypt
- [ ] Có quy trình review thay đổi cấu hình
- [ ] Có quy trình rollback cấu hình

### 10.5. Checklist quản lý tài nguyên

- [ ] Giám sát tài nguyên đã được thiết lập
- [ ] Có cảnh báo khi tài nguyên gần hết
- [ ] Có phân tích xu hướng sử dụng
- [ ] Có kế hoạch mở rộng tài nguyên
- [ ] Auto-scaling đã được cấu hình (nếu có)

---

**Phiên bản**: 1.0
**Ngày ban hành**: [Ngày hiện tại]
**Người soạn**: 
**Trạng thái**: Chính thức

