# TP-004: TEMPLATE PROVISIONING REQUEST

**Mã template**: TP-004 
**Tham chiếu quy trình**: QT-005

---

## THÔNG TIN CHUNG

- **Request ID**: [PROV-YYYYMMDD-XXX]
- **Ngày tạo**: [YYYY-MM-DD]
- **Người tạo**: [Tên]
- **Email**: [Email]
- **Điện thoại**: [SĐT]
- **Dự án**: [Tên dự án]

---

## YÊU CẦU

### Mô tả yêu cầu
[Mô tả chi tiết yêu cầu provisioning]

### Mục đích
[Mục đích sử dụng tài nguyên]

### Môi trường
- [ ] Production
- [ ] DR
- [ ] UAT
- [ ] Staging

### Thời gian cần
- **Ngày bắt đầu**: [YYYY-MM-DD]
- **Ngày kết thúc**: [YYYY-MM-DD] (nếu có)
- **Thời gian sử dụng**: [Vĩnh viễn/Tạm thời]

---

## TÀI NGUYÊN CẦN

### Server

#### Application Server
- **Số lượng**: [X]
- **OS**: [Ubuntu/CentOS/...]
- **CPU**: [X cores]
- **Memory**: [X GB]
- **Disk**: [X GB] ([SSD/HDD])
- **Network**: [X Mbps]

#### Database Server
- **Số lượng**: [X]
- **Database type**: [MySQL/PostgreSQL/MongoDB/...]
- **Version**: [X.Y.Z]
- **Storage**: [X GB]
- **Backup**: [Có/Không]
- **Replication**: [Có/Không]
- **High Availability**: [Có/Không]

#### Cache Server
- **Số lượng**: [X]
- **Cache type**: [Redis/Memcached/...]
- **Memory**: [X GB]

### Network

#### VPC/VLAN
- **Tên**: [Tên VPC/VLAN]
- **CIDR**: [X.X.X.X/XX]

#### Subnet
- **Số lượng**: [X]
- **CIDR**: [X.X.X.X/XX]

#### Security Group/Firewall
- **Rules**: [Mô tả rules]

#### Load Balancer
- **Type**: [Application/Network]
- **Protocol**: [HTTP/HTTPS/TCP]

#### DNS
- **Domain**: [domain.com]
- **Subdomain**: [subdomain]

### Storage

#### Block Storage
- **Capacity**: [X GB]
- **Type**: [SSD/HDD]
- **IOPS**: [X]

#### Object Storage
- **Capacity**: [X GB]
- **Type**: [S3/MinIO/...]

### Monitoring và Logging

#### Monitoring
- **Tools**: [Prometheus/Grafana/Zabbix/...]
- **Metrics**: [List metrics cần giám sát]

#### Logging
- **Tools**: [ELK/Loki/...]
- **Retention**: [X ngày]

---

## THIẾT KẾ

### Kiến trúc
[Mô tả hoặc link đến sơ đồ kiến trúc]

### Cấu hình
[Mô tả cấu hình cần thiết]

### Bảo mật
[Mô tả yêu cầu bảo mật]

### Network
[Mô tả cấu hình mạng]

---

## PHÊ DUYỆT

### Phê duyệt bởi
- **Người phê duyệt**: [Tên]
- **Chức vụ**: [Chức vụ]
- **Ngày phê duyệt**: [YYYY-MM-DD]
- [ ] Đã phê duyệt
- [ ] Từ chối
- [ ] Cần bổ sung thông tin

**Ghi chú**: [Ghi chú nếu có]

---

## THỰC HIỆN

### Người thực hiện
- **Infrastructure Team**: [Tên]
- **DevOps Team**: [Tên]

### Thời gian thực hiện
- **Bắt đầu**: [YYYY-MM-DD HH:MM]
- **Kết thúc**: [YYYY-MM-DD HH:MM]

### Trạng thái
- [ ] Đã hoàn thành
- [ ] Đang thực hiện
- [ ] Đã hủy

### Kết quả
[Mô tả kết quả provisioning]

### Thông tin tài nguyên
[Thông tin tài nguyên đã được tạo: IP, hostname, credentials (lưu trong secret management), ...]

---

## BÀN GIAO

### Tài liệu
- [ ] Tài liệu kiến trúc đã được tạo
- [ ] Tài liệu cấu hình đã được tạo
- [ ] Runbook đã được tạo

### Bàn giao
- [ ] Đã bàn giao cho Development Team
- [ ] Đã bàn giao cho DevOps Team
- [ ] Training đã được thực hiện (nếu cần)

### Ngày bàn giao
[YYYY-MM-DD]

---

**Phiên bản**: 1.0

