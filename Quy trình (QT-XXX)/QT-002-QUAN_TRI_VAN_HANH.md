# QT-002: QUY TRÌNH QUẢN TRỊ VẬN HÀNH

---

## THÔNG TIN TÀI LIỆU

- **Mã quy trình**: QT-002
- **Tên quy trình**: Quy trình Quản trị Vận hành
- **Phiên bản**: 1.2
- **Ngày ban hành**: [Ngày hiện tại]
- **Người soạn**: 
- **Trạng thái**: Chính thức

---

## MỤC LỤC

1. [Tổng quan](#1-tổng-quan)
2. [Quy trình giám sát hệ thống](#2-quy-trình-giám-sát-hệ-thống)
3. [Quy trình quản lý log](#3-quy-trình-quản-lý-log)
4. [Quy trình quản lý backup](#4-quy-trình-quản-lý-backup)
5. [Quy trình quản lý cấu hình](#5-quy-trình-quản-lý-cấu-hình)
6. [Quy trình quản lý tài nguyên](#6-quy-trình-quản-lý-tài-nguyên)
7. [Quy trình xử lý sự cố vận hành](#7-quy-trình-xử-lý-sự-cố-vận-hành)
8. [Quy định và tiêu chuẩn](#8-quy-định-và-tiêu-chuẩn)
9. [Quy định về Quyền Truy Cập Tối Thiểu](#9-quy-định-về-quyền-truy-cập-tối-thiểu) 
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
- **Revenue/Doanh thu**: Doanh thu theo thời gian (nếu áp dụng)
- **Conversion rate**: Tỷ lệ chuyển đổi (%)
- **User session duration**: Thời gian phiên làm việc trung bình (phút)

#### 2.2.5. Chỉ số bảo mật (Security Metrics)

- **Failed login attempts**: Số lần đăng nhập thất bại/giờ
- **Security events**: Số sự kiện bảo mật (phát hiện tấn công, vi phạm)
- **SSL/TLS certificate expiry**: Thời gian còn lại của certificate (ngày)
- **Vulnerability scan results**: Kết quả quét lỗ hổng bảo mật
- **Unauthorized access attempts**: Số lần truy cập trái phép
- **MFA adoption rate**: Tỷ lệ tài khoản đã kích hoạt MFA (%)
- **Privileged access events**: Số sự kiện truy cập với quyền cao
- **Data breach indicators**: Các chỉ số cảnh báo rò rỉ dữ liệu

#### 2.2.6. Chỉ số container/Kubernetes (nếu áp dụng)

- **Pod status**: Trạng thái pod (Running, Pending, Failed)
- **Container restart count**: Số lần container restart
- **Resource requests/limits**: CPU và Memory requests/limits
- **Node status**: Trạng thái node (Ready, NotReady)
- **Deployment status**: Trạng thái deployment (Available, Progressing)
- **HPA (Horizontal Pod Autoscaler)**: Số replica hiện tại vs mong muốn
- **PVC (Persistent Volume Claim) usage**: Sử dụng storage (%)
- **Network policy violations**: Số vi phạm network policy

#### 2.2.7. Chỉ số cache

- **Cache hit rate**: Tỷ lệ cache hit (%)
- **Cache miss rate**: Tỷ lệ cache miss (%)
- **Cache eviction rate**: Tỷ lệ cache bị đẩy ra (eviction/s)
- **Cache memory usage**: Sử dụng bộ nhớ cache (%)
- **Cache response time**: Thời gian phản hồi từ cache (ms)
- **Cache connection pool**: Số kết nối đến cache server

#### 2.2.8. Chỉ số message queue (nếu áp dụng)

- **Queue depth**: Độ sâu hàng đợi (số message đang chờ)
- **Message processing rate**: Tỷ lệ xử lý message (msg/s)
- **Message age**: Tuổi của message cũ nhất trong queue (giây)
- **Consumer lag**: Độ trễ của consumer (số message chưa xử lý)
- **Dead letter queue size**: Số message trong dead letter queue
- **Queue throughput**: Thông lượng queue (msg/s)

#### 2.2.9. Chỉ số API/Service health

- **API availability**: Tỷ lệ sẵn sàng của API (%)
- **API response time (p50, p95, p99)**: Thời gian phản hồi phân vị (ms)
- **API error rate by endpoint**: Tỷ lệ lỗi theo từng endpoint (%)
- **API rate limiting**: Số request bị rate limit/giờ
- **Service health check**: Trạng thái health check (Healthy/Unhealthy)
- **Circuit breaker status**: Trạng thái circuit breaker (Open/Closed/Half-Open)
- **Dependency health**: Trạng thái các service phụ thuộc
- **API version usage**: Sử dụng các phiên bản API

#### 2.2.10. Chỉ số SLA/SLO

- **Uptime/Availability**: Tỷ lệ uptime (%)
- **SLA compliance**: Tuân thủ SLA (%)
- **SLO target achievement**: Đạt mục tiêu SLO (%)
- **MTTR (Mean Time To Repair)**: Thời gian sửa chữa trung bình (phút)
- **MTBF (Mean Time Between Failures)**: Thời gian giữa các lỗi trung bình (giờ)
- **Incident count**: Số sự cố trong kỳ
- **Service level compliance**: Tuân thủ mức dịch vụ (%)

#### 2.2.11. Chỉ số chi phí (Cost Metrics)

- **Infrastructure cost**: Chi phí hạ tầng (VNĐ/tháng)
- **Cloud resource cost**: Chi phí tài nguyên cloud (VNĐ/tháng)
- **Storage cost**: Chi phí lưu trữ (VNĐ/tháng)
- **Network cost**: Chi phí mạng (VNĐ/tháng)
- **Cost per transaction**: Chi phí mỗi giao dịch (VNĐ)
- **Cost trend**: Xu hướng chi phí (tăng/giảm %)
- **Resource utilization vs cost**: Tỷ lệ sử dụng tài nguyên vs chi phí

#### 2.2.12. Chỉ số compliance và audit

- **Compliance score**: Điểm tuân thủ (%)
- **Audit findings**: Số phát hiện từ audit
- **Policy violations**: Số vi phạm chính sách
- **Access review completion**: Tỷ lệ hoàn thành rà soát quyền (%)
- **Log retention compliance**: Tuân thủ chính sách lưu trữ log (%)
- **Backup compliance**: Tuân thủ chính sách backup (%)
- **Change management compliance**: Tuân thủ quy trình quản lý thay đổi (%)

#### 2.2.13. Chỉ số hiệu năng nâng cao

- **Latency percentiles**: p50, p95, p99 latency (ms)
- **Throughput per resource**: Thông lượng trên mỗi đơn vị tài nguyên
- **Resource efficiency**: Hiệu quả sử dụng tài nguyên (%)
- **Bottleneck identification**: Xác định điểm nghẽn
- **Performance degradation**: Mức độ suy giảm hiệu năng (%)
- **Cache effectiveness**: Hiệu quả cache (%)
- **Database query optimization**: Số query được tối ưu

#### 2.2.14. Chỉ số mạng (Network Metrics)

- **Bandwidth utilization**: Sử dụng băng thông (%)
- **Packet loss**: Tỷ lệ mất gói (%)
- **Network latency**: Độ trễ mạng (ms)
- **DNS resolution time**: Thời gian phân giải DNS (ms)
- **Connection errors**: Số lỗi kết nối
- **Firewall rule hits**: Số lần rule firewall được kích hoạt
- **VPN connection status**: Trạng thái kết nối VPN

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

**Hạ tầng:**
- **CPU usage**: > 80% (High), > 90% (Critical)
- **Memory usage**: > 80% (High), > 90% (Critical)
- **Disk usage**: > 80% (High), > 90% (Critical)
- **Disk I/O wait**: > 50% (High), > 80% (Critical)
- **Network bandwidth**: > 80% (High), > 90% (Critical)
- **Network packet loss**: > 1% (High), > 5% (Critical)

**Ứng dụng:**
- **Error rate**: > 1% (Medium), > 5% (High), > 10% (Critical)
- **Response time (p95)**: > 1s (Medium), > 3s (High), > 5s (Critical)
- **Response time (p99)**: > 2s (Medium), > 5s (High), > 10s (Critical)
- **Request rate**: Giảm > 20% so với bình thường (High)
- **Active connections**: > 80% capacity (High), > 95% (Critical)

**Database:**
- **Query performance (p95)**: > 1s (Medium), > 3s (High), > 5s (Critical)
- **Connection pool usage**: > 80% (High), > 95% (Critical)
- **Lock wait time**: > 1s (High), > 5s (Critical)
- **Replication lag**: > 10s (High), > 60s (Critical)
- **Database size growth**: > 20% trong 24h (High)

**Bảo mật:**
- **Failed login attempts**: > 10/giờ từ cùng IP (High), > 50/giờ (Critical)
- **Security events**: Bất kỳ sự kiện Critical (Critical)
- **SSL/TLS certificate expiry**: < 30 ngày (High), < 7 ngày (Critical)
- **Unauthorized access attempts**: Bất kỳ (High)
- **Vulnerability scan**: Phát hiện Critical vulnerability (Critical)

**Availability:**
- **Uptime**: < 99.5% (High), < 99% (Critical)
- **Service health check**: Unhealthy > 1 phút (High), > 5 phút (Critical)
- **Circuit breaker**: Open > 1 phút (High), > 5 phút (Critical)

**Cache:**
- **Cache hit rate**: < 80% (Medium), < 60% (High)
- **Cache memory usage**: > 90% (High), > 95% (Critical)

**Message Queue:**
- **Queue depth**: > 1000 messages (High), > 10000 (Critical)
- **Message age**: > 5 phút (High), > 30 phút (Critical)
- **Consumer lag**: > 1000 messages (High), > 10000 (Critical)

**Container/Kubernetes:**
- **Pod restart count**: > 5 lần/giờ (High), > 20 lần/giờ (Critical)
- **Node NotReady**: Bất kỳ node (High)
- **PVC usage**: > 80% (High), > 90% (Critical)

### 2.5. Dashboard

#### 2.5.1. Dashboard real-time

**Nội dung hiển thị:**
- Trạng thái hệ thống hiện tại (tất cả services)
- Các chỉ số quan trọng (CPU, Memory, Disk, Network, Error rate, Response time)
- Cảnh báo đang hoạt động (theo mức độ Critical, High, Medium, Low)
- Sự kiện gần đây (deployment, sự cố, thay đổi)
- Service health status (Healthy/Unhealthy)
- Active incidents và status
- Uptime hiện tại

**Yêu cầu:**
- Update real-time (mỗi 5-10 giây)
- Có thể filter theo service, môi trường
- Có thể drill-down vào chi tiết
- Mobile-friendly (responsive)

#### 2.5.2. Dashboard báo cáo

**Báo cáo hàng ngày:**
- Tổng quan 24h qua
- Số lượng cảnh báo theo mức độ
- Số sự cố và thời gian xử lý
- Uptime trong 24h
- Top 10 endpoint có response time cao nhất
- Top 10 endpoint có error rate cao nhất
- Tài nguyên sử dụng (CPU, Memory, Disk)
- Chi phí ước tính

**Báo cáo hàng tuần:**
- Xu hướng tuần (so sánh với tuần trước)
- Tổng hợp sự cố và MTTR
- Phân tích hiệu năng
- Phân tích chi phí
- Compliance score
- Security events summary

**Báo cáo hàng tháng:**
- Phân tích tháng toàn diện
- Xu hướng dài hạn
- So sánh với tháng trước
- Đánh giá SLA/SLO
- Phân tích chi phí và tối ưu
- Đề xuất cải tiến
- Compliance và audit summary

#### 2.5.3. Dashboard theo nhóm chỉ số

**Infrastructure Dashboard:**
- CPU, Memory, Disk, Network của tất cả servers
- Container/Kubernetes metrics (nếu có)
- Resource utilization trends

**Application Dashboard:**
- Request rate, Error rate, Response time
- API health và performance
- Service dependencies map
- Cache performance

**Database Dashboard:**
- Query performance
- Connection pool
- Replication status
- Database size và growth

**Security Dashboard:**
- Security events
- Failed login attempts
- Certificate expiry
- Vulnerability status
- Access patterns

**Business Dashboard:**
- User metrics
- Transaction metrics
- Revenue metrics (nếu áp dụng)
- Business KPIs

**Cost Dashboard:**
- Infrastructure cost
- Cost per service
- Cost trends
- Cost optimization opportunities

### 2.6. Tổng hợp các chỉ số giám sát

#### 2.6.1. Bảng tổng hợp theo nhóm

| Nhóm chỉ số | Số lượng | Mục đích | Tần suất giám sát |
|------------|---------|----------|-------------------|
| **Hạ tầng** | 5 chỉ số | Đảm bảo hạ tầng hoạt động ổn định | Real-time (mỗi 1-5 phút) |
| **Ứng dụng** | 5 chỉ số | Đảm bảo ứng dụng hoạt động tốt | Real-time (mỗi 1-5 phút) |
| **Database** | 4 chỉ số | Đảm bảo database hiệu quả | Real-time (mỗi 1-5 phút) |
| **Business** | 6 chỉ số | Theo dõi nghiệp vụ | Real-time (mỗi 5-15 phút) |
| **Bảo mật** | 8 chỉ số | Phát hiện và ngăn chặn mối đe dọa | Real-time (mỗi 1-5 phút) |
| **Container/K8s** | 8 chỉ số | Quản lý container (nếu áp dụng) | Real-time (mỗi 1-5 phút) |
| **Cache** | 6 chỉ số | Tối ưu hiệu năng cache | Real-time (mỗi 5-15 phút) |
| **Message Queue** | 6 chỉ số | Quản lý queue (nếu áp dụng) | Real-time (mỗi 1-5 phút) |
| **API/Service** | 8 chỉ số | Đảm bảo API hoạt động tốt | Real-time (mỗi 1-5 phút) |
| **SLA/SLO** | 7 chỉ số | Đảm bảo tuân thủ SLA/SLO | Theo kỳ (hàng ngày/tuần) |
| **Chi phí** | 7 chỉ số | Quản lý và tối ưu chi phí | Hàng ngày/tuần |
| **Compliance** | 7 chỉ số | Đảm bảo tuân thủ | Hàng tuần/tháng |
| **Hiệu năng nâng cao** | 7 chỉ số | Phân tích sâu hiệu năng | Real-time + phân tích định kỳ |
| **Mạng** | 7 chỉ số | Đảm bảo mạng hoạt động tốt | Real-time (mỗi 1-5 phút) |

**Tổng cộng**: 93 chỉ số giám sát

#### 2.6.2. Ưu tiên giám sát

##### 2.6.2.1. Bảng phân loại ưu tiên theo chỉ số

| Nhóm chỉ số | Chỉ số cụ thể | Ưu tiên | Tần suất giám sát | Thời gian phản ứng | Người phụ trách |
|------------|---------------|---------|-------------------|-------------------|-----------------|
| **Hạ tầng** | CPU usage | **Cao** | Real-time (1 phút) | ≤ 15 phút | DevOps |
| | Memory usage | **Cao** | Real-time (1 phút) | ≤ 15 phút | DevOps |
| | Disk usage | **Cao** | Real-time (1 phút) | ≤ 15 phút | DevOps |
| | Disk I/O wait | **Cao** | Real-time (1 phút) | ≤ 15 phút | DevOps |
| | Network traffic | **Cao** | Real-time (1 phút) | ≤ 15 phút | DevOps |
| | Network packet loss | **Cao** | Real-time (1 phút) | ≤ 15 phút | DevOps |
| **Ứng dụng** | Error rate | **Cao** | Real-time (1 phút) | ≤ 15 phút | DevOps + Dev |
| | Response time (p95, p99) | **Cao** | Real-time (1 phút) | ≤ 15 phút | DevOps + Dev |
| | Request rate | **Cao** | Real-time (1 phút) | ≤ 30 phút | DevOps |
| | Throughput | **Trung bình** | Real-time (5 phút) | ≤ 1 giờ | DevOps |
| | Active connections | **Cao** | Real-time (1 phút) | ≤ 30 phút | DevOps |
| **Database** | Connection pool | **Cao** | Real-time (1 phút) | ≤ 15 phút | DBA + DevOps |
| | Query performance | **Cao** | Real-time (1 phút) | ≤ 30 phút | DBA + Dev |
| | Lock wait time | **Cao** | Real-time (1 phút) | ≤ 30 phút | DBA |
| | Replication lag | **Cao** | Real-time (1 phút) | ≤ 1 giờ | DBA |
| **Business** | Số người dùng online | **Trung bình** | Real-time (5 phút) | ≤ 2 giờ | Business Team |
| | Số giao dịch | **Trung bình** | Real-time (5 phút) | ≤ 2 giờ | Business Team |
| | Tỷ lệ thành công | **Cao** | Real-time (1 phút) | ≤ 30 phút | DevOps + Business |
| | Revenue/Doanh thu | **Thấp** | Hàng ngày | ≤ 24 giờ | Business Team |
| | Conversion rate | **Thấp** | Hàng ngày | ≤ 24 giờ | Business Team |
| | User session duration | **Thấp** | Hàng ngày | ≤ 24 giờ | Business Team |
| **Bảo mật** | Failed login attempts | **Cao** | Real-time (1 phút) | ≤ 15 phút | Security Team |
| | Security events (Critical) | **Cao** | Real-time (1 phút) | ≤ 15 phút | Security Team |
| | Security events (High) | **Trung bình** | Real-time (5 phút) | ≤ 1 giờ | Security Team |
| | SSL/TLS certificate expiry | **Cao** | Hàng ngày | ≤ 7 ngày | DevOps |
| | Vulnerability scan (Critical) | **Cao** | Sau mỗi scan | ≤ 24 giờ | Security Team |
| | Unauthorized access attempts | **Cao** | Real-time (1 phút) | ≤ 15 phút | Security Team |
| | MFA adoption rate | **Trung bình** | Hàng tuần | ≤ 1 tuần | Security Team |
| | Privileged access events | **Cao** | Real-time (1 phút) | ≤ 15 phút | Security Team |
| | Data breach indicators | **Cao** | Real-time (1 phút) | ≤ 15 phút | Security Team |
| **Container/K8s** | Pod status (Failed) | **Cao** | Real-time (1 phút) | ≤ 15 phút | DevOps |
| | Pod status (Running) | **Trung bình** | Real-time (5 phút) | ≤ 1 giờ | DevOps |
| | Container restart count | **Cao** | Real-time (1 phút) | ≤ 30 phút | DevOps |
| | Node status (NotReady) | **Cao** | Real-time (1 phút) | ≤ 15 phút | DevOps |
| | Deployment status | **Trung bình** | Real-time (5 phút) | ≤ 1 giờ | DevOps |
| | HPA status | **Trung bình** | Real-time (5 phút) | ≤ 1 giờ | DevOps |
| | PVC usage | **Cao** | Real-time (1 phút) | ≤ 30 phút | DevOps |
| | Network policy violations | **Cao** | Real-time (1 phút) | ≤ 15 phút | Security Team |
| **Cache** | Cache hit rate | **Trung bình** | Real-time (5 phút) | ≤ 2 giờ | DevOps |
| | Cache miss rate | **Trung bình** | Real-time (5 phút) | ≤ 2 giờ | DevOps |
| | Cache eviction rate | **Thấp** | Hàng ngày | ≤ 24 giờ | DevOps |
| | Cache memory usage | **Cao** | Real-time (1 phút) | ≤ 30 phút | DevOps |
| | Cache response time | **Trung bình** | Real-time (5 phút) | ≤ 2 giờ | DevOps |
| | Cache connection pool | **Trung bình** | Real-time (5 phút) | ≤ 1 giờ | DevOps |
| **Message Queue** | Queue depth | **Cao** | Real-time (1 phút) | ≤ 30 phút | DevOps |
| | Message processing rate | **Trung bình** | Real-time (5 phút) | ≤ 1 giờ | DevOps |
| | Message age | **Cao** | Real-time (1 phút) | ≤ 30 phút | DevOps |
| | Consumer lag | **Cao** | Real-time (1 phút) | ≤ 30 phút | DevOps |
| | Dead letter queue size | **Cao** | Real-time (1 phút) | ≤ 1 giờ | DevOps |
| | Queue throughput | **Trung bình** | Real-time (5 phút) | ≤ 2 giờ | DevOps |
| **API/Service** | API availability | **Cao** | Real-time (1 phút) | ≤ 15 phút | DevOps |
| | API response time (p95, p99) | **Cao** | Real-time (1 phút) | ≤ 30 phút | DevOps |
| | API error rate by endpoint | **Cao** | Real-time (1 phút) | ≤ 30 phút | DevOps |
| | API rate limiting | **Trung bình** | Real-time (5 phút) | ≤ 1 giờ | DevOps |
| | Service health check | **Cao** | Real-time (1 phút) | ≤ 15 phút | DevOps |
| | Circuit breaker status | **Cao** | Real-time (1 phút) | ≤ 15 phút | DevOps |
| | Dependency health | **Cao** | Real-time (1 phút) | ≤ 30 phút | DevOps |
| | API version usage | **Thấp** | Hàng tuần | ≤ 1 tuần | DevOps |
| **SLA/SLO** | Uptime/Availability | **Cao** | Real-time (1 phút) | ≤ 15 phút | DevOps |
| | SLA compliance | **Cao** | Hàng ngày | ≤ 24 giờ | DevOps Manager |
| | SLO target achievement | **Cao** | Hàng ngày | ≤ 24 giờ | DevOps Manager |
| | MTTR | **Cao** | Sau mỗi sự cố | ≤ 24 giờ | DevOps Manager |
| | MTBF | **Trung bình** | Hàng tuần | ≤ 1 tuần | DevOps Manager |
| | Incident count | **Cao** | Hàng ngày | ≤ 24 giờ | DevOps Manager |
| | Service level compliance | **Cao** | Hàng ngày | ≤ 24 giờ | DevOps Manager |
| **Chi phí** | Infrastructure cost | **Trung bình** | Hàng ngày | ≤ 24 giờ | Finance + DevOps |
| | Cloud resource cost | **Trung bình** | Hàng ngày | ≤ 24 giờ | Finance + DevOps |
| | Storage cost | **Thấp** | Hàng tuần | ≤ 1 tuần | Finance + DevOps |
| | Network cost | **Thấp** | Hàng tuần | ≤ 1 tuần | Finance + DevOps |
| | Cost per transaction | **Thấp** | Hàng tuần | ≤ 1 tuần | Finance + DevOps |
| | Cost trend | **Trung bình** | Hàng tuần | ≤ 1 tuần | Finance + DevOps |
| | Resource utilization vs cost | **Thấp** | Hàng tháng | ≤ 1 tháng | Finance + DevOps |
| **Compliance** | Compliance score | **Trung bình** | Hàng tuần | ≤ 1 tuần | Compliance Team |
| | Audit findings | **Cao** | Sau mỗi audit | ≤ 24 giờ | Compliance Team |
| | Policy violations | **Cao** | Real-time (1 phút) | ≤ 1 giờ | Compliance Team |
| | Access review completion | **Trung bình** | Hàng tuần | ≤ 1 tuần | Security Team |
| | Log retention compliance | **Trung bình** | Hàng tuần | ≤ 1 tuần | DevOps |
| | Backup compliance | **Cao** | Hàng ngày | ≤ 24 giờ | DevOps |
| | Change management compliance | **Trung bình** | Hàng tuần | ≤ 1 tuần | DevOps |
| **Hiệu năng nâng cao** | Latency percentiles (p50, p95, p99) | **Trung bình** | Real-time (5 phút) | ≤ 2 giờ | DevOps |
| | Throughput per resource | **Thấp** | Hàng tuần | ≤ 1 tuần | DevOps |
| | Resource efficiency | **Thấp** | Hàng tuần | ≤ 1 tuần | DevOps |
| | Bottleneck identification | **Trung bình** | Hàng tuần | ≤ 1 tuần | DevOps |
| | Performance degradation | **Cao** | Real-time (1 phút) | ≤ 30 phút | DevOps |
| | Cache effectiveness | **Thấp** | Hàng tuần | ≤ 1 tuần | DevOps |
| | Database query optimization | **Trung bình** | Hàng tuần | ≤ 1 tuần | DBA |
| **Mạng** | Bandwidth utilization | **Cao** | Real-time (1 phút) | ≤ 30 phút | Network Team |
| | Packet loss | **Cao** | Real-time (1 phút) | ≤ 15 phút | Network Team |
| | Network latency | **Cao** | Real-time (1 phút) | ≤ 30 phút | Network Team |
| | DNS resolution time | **Trung bình** | Real-time (5 phút) | ≤ 1 giờ | Network Team |
| | Connection errors | **Cao** | Real-time (1 phút) | ≤ 15 phút | Network Team |
| | Firewall rule hits | **Trung bình** | Hàng ngày | ≤ 24 giờ | Security Team |
| | VPN connection status | **Trung bình** | Real-time (5 phút) | ≤ 1 giờ | Network Team |

##### 2.6.2.2. Định nghĩa mức ưu tiên

**Ưu tiên Cao:**
- **Đặc điểm**: Chỉ số quan trọng, ảnh hưởng trực tiếp đến hoạt động của hệ thống
- **Tần suất giám sát**: Real-time (mỗi 1 phút) hoặc liên tục
- **Thời gian phản ứng**: ≤ 15 phút đến ≤ 1 giờ
- **Hậu quả nếu bỏ qua**: Có thể dẫn đến sự cố nghiêm trọng, downtime, mất dữ liệu
- **Ví dụ**: CPU usage, Memory usage, Error rate, Service availability, Security events

**Ưu tiên Trung bình:**
- **Đặc điểm**: Chỉ số quan trọng nhưng không ảnh hưởng ngay lập tức
- **Tần suất giám sát**: Real-time (mỗi 5 phút) hoặc định kỳ (hàng ngày/tuần)
- **Thời gian phản ứng**: ≤ 1 giờ đến ≤ 24 giờ
- **Hậu quả nếu bỏ qua**: Có thể ảnh hưởng hiệu năng, trải nghiệm người dùng
- **Ví dụ**: Throughput, Cache hit rate, Cost trends, Compliance score

**Ưu tiên Thấp:**
- **Đặc điểm**: Chỉ số hỗ trợ, phân tích xu hướng, tối ưu hóa
- **Tần suất giám sát**: Định kỳ (hàng ngày/tuần/tháng)
- **Thời gian phản ứng**: ≤ 24 giờ đến ≤ 1 tuần
- **Hậu quả nếu bỏ qua**: Không ảnh hưởng ngay, nhưng có thể mất cơ hội tối ưu
- **Ví dụ**: Revenue trends, Conversion rate, Cost optimization opportunities

##### 2.6.2.3. Hướng dẫn sử dụng bảng ưu tiên

**1. Thiết lập monitoring:**
- Ưu tiên **Cao**: Thiết lập alerting tự động, notification real-time (Email, SMS, Slack)
- Ưu tiên **Trung bình**: Thiết lập alerting định kỳ, notification qua Email/Slack
- Ưu tiên **Thấp**: Thiết lập báo cáo định kỳ, không cần alerting tự động

**2. Phân bổ nguồn lực:**
- **Ưu tiên Cao**: Phân bổ 60-70% thời gian giám sát
- **Ưu tiên Trung bình**: Phân bổ 20-30% thời gian giám sát
- **Ưu tiên Thấp**: Phân bổ 10% thời gian giám sát

**3. Dashboard organization:**
- **Dashboard chính (Main)**: Chỉ hiển thị chỉ số ưu tiên **Cao**
- **Dashboard phụ (Secondary)**: Hiển thị chỉ số ưu tiên **Trung bình**
- **Dashboard phân tích (Analytics)**: Hiển thị chỉ số ưu tiên **Thấp** và xu hướng

**4. On-call rotation:**
- Chỉ số ưu tiên **Cao** được gán cho on-call engineer
- Chỉ số ưu tiên **Trung bình** được xử lý trong giờ làm việc
- Chỉ số ưu tiên **Thấp** được xử lý theo lịch định kỳ

##### 2.6.2.4. Tổng hợp theo ưu tiên

**Ưu tiên Cao (47 chỉ số):**
- Tất cả chỉ số hạ tầng (6)
- Error rate, Response time, Request rate, Active connections (4)
- Tất cả chỉ số database (4)
- Tỷ lệ thành công giao dịch (1)
- Failed login, Security events Critical, SSL/TLS expiry, Unauthorized access, Vulnerability Critical, Privileged access, Data breach (7)
- Pod Failed, Container restart, Node NotReady, PVC usage, Network policy violations (5)
- Cache memory usage (1)
- Queue depth, Message age, Consumer lag, Dead letter queue (4)
- API availability, Response time, Error rate, Health check, Circuit breaker, Dependency health (6)
- Uptime, SLA/SLO compliance, MTTR, Incident count, Service level compliance (5)
- Backup compliance, Audit findings, Policy violations (3)
- Performance degradation (1)
- Bandwidth, Packet loss, Network latency, Connection errors (4)

**Ưu tiên Trung bình (32 chỉ số):**
- Throughput, API rate limiting, API version usage (3)
- Số người dùng online, Số giao dịch (2)
- Security events High, MFA adoption (2)
- Pod Running, Deployment status, HPA (3)
- Cache hit/miss rate, Response time, Connection pool (5)
- Message processing rate, Queue throughput (2)
- MTBF (1)
- Infrastructure cost, Cloud cost, Cost trend (3)
- Compliance score, Access review, Log retention, Change management (4)
- Latency percentiles, Bottleneck identification, Query optimization (3)
- DNS resolution, Firewall hits, VPN status (3)

**Ưu tiên Thấp (12 chỉ số):**
- Revenue, Conversion rate, User session duration (3)
- Cache eviction rate (1)
- Storage cost, Network cost, Cost per transaction, Resource utilization vs cost (4)
- Throughput per resource, Resource efficiency, Cache effectiveness (3)
- API version usage (1)

#### 2.6.3. Công cụ giám sát khuyến nghị

**Infrastructure Monitoring:**
- Prometheus + Grafana
- Zabbix
- Datadog
- New Relic

**Application Performance Monitoring (APM):**
- New Relic
- Datadog APM
- Elastic APM
- Dynatrace

**Log Management:**
- ELK Stack (Elasticsearch, Logstash, Kibana)
- Loki + Grafana
- Splunk
- CloudWatch Logs

**Security Monitoring:**
- SIEM (Security Information and Event Management)
- WAF (Web Application Firewall) logs
- IDS/IPS (Intrusion Detection/Prevention System)
- Vulnerability scanners

**Cost Management:**
- AWS Cost Explorer
- Azure Cost Management
- GCP Billing
- CloudHealth

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
| **Developer** | | | | |
| **DevOps** | * | * | * | * |
| **SysAdmin** | * | * | * | * |
| **DBA** | * (DB server only) | | | |

*Sau khi có phê duyệt, có log

#### 9.2.2. Quyền truy cập log

| Vai trò | Read Log | Search Log | Export Log | Delete Log |
|---------|----------|------------|------------|------------|
| **Developer** | (dev/staging) | (dev/staging) | | |
| **DevOps** | (all) | (all) | * | |
| **SysAdmin** | (all) | (all) | * | * |
| **QA** | (dev/staging) | (dev/staging) | | |

*Sau khi có phê duyệt

#### 9.2.3. Quyền truy cập backup

| Vai trò | View Backup | Create Backup | Restore Backup | Delete Backup |
|---------|-------------|---------------|----------------|---------------|
| **Developer** | | | | |
| **DevOps** | | * | * | |
| **SysAdmin** | | * | * | * |
| **DBA** | (DB backup) | * (DB backup) | * (DB backup) | |

*Sau khi có phê duyệt

#### 9.2.4. Quyền truy cập cấu hình

| Vai trò | View Config | Modify Config | Deploy Config | Rollback Config |
|---------|-------------|---------------|---------------|-----------------|
| **Developer** | (dev/staging) | | | |
| **DevOps** | (all) | * | * | * |
| **SysAdmin** | (all) | * | * | * |

*Sau khi có phê duyệt

#### 9.2.5. Quyền truy cập monitoring tools

| Vai trò | View Metrics | View Alerts | Configure Alerts | Acknowledge Alerts |
|---------|--------------|-------------|------------------|-------------------|
| **Developer** | (dev/staging) | (dev/staging) | | |
| **DevOps** | (all) | (all) | * | |
| **SysAdmin** | (all) | (all) | * | |
| **On-call** | (all) | (all) | | |

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

**Phiên bản**: 1.2
**Ngày ban hành**: [Ngày hiện tại]
**Người soạn**: 
**Trạng thái**: Chính thức

**Changelog:**
- **v1.2** (2024-12-17): Bổ sung bảng phân loại ưu tiên chi tiết cho tất cả 91 chỉ số giám sát (Cao/Trung bình/Thấp), định nghĩa mức ưu tiên, hướng dẫn sử dụng, và tổng hợp theo ưu tiên
- **v1.1** (2024-12-17): Bổ sung 10 nhóm chỉ số giám sát mới (Bảo mật, Container/K8s, Cache, Message Queue, API/Service, SLA/SLO, Chi phí, Compliance, Hiệu năng nâng cao, Mạng), mở rộng ngưỡng cảnh báo, chi tiết hóa dashboard
- **v1.0**: Phiên bản ban đầu

