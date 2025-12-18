# QT-008: DANH SÁCH THAY ĐỔI CHUẨN

---

## THÔNG TIN TÀI LIỆU

- **Mã quy trình**: QT-008
- **Tên quy trình**: Danh sách Thay đổi Chuẩn
- **Phiên bản**: 1.0
- **Ngày ban hành**: [Ngày hiện tại]
- **Người soạn**: 
- **Trạng thái**: Chính thức

---

## MỤC LỤC

1. [Tổng quan](#1-tổng-quan)
2. [Nhóm A: Thay đổi Hạ tầng](#2-nhóm-a-thay-đổi-hạ-tầng-infrastructure)
3. [Nhóm B: Thay đổi Ứng dụng](#3-nhóm-b-thay-đổi-ứng-dụng-application)
4. [Nhóm C: Thay đổi Dữ liệu và Cấu hình](#4-nhóm-c-thay-đổi-dữ-liệu-và-cấu-hình-data--configuration)
5. [Nhóm D: Xử lý Sự cố](#5-nhóm-d-xử-lý-sự-cố-incident-management)
6. [Hướng dẫn sử dụng](#6-hướng-dẫn-sử-dụng)
7. [Thống kê](#7-thống-kê)

---

## 1. TỔNG QUAN

### 1.1. Mục đích

Danh sách này quy định 58 loại thay đổi chuẩn được phân loại theo 4 nhóm chính, giúp:
- Xác định nhanh loại thay đổi và quy trình áp dụng
- Đánh giá rủi ro và xác định cấp độ phê duyệt
- Áp dụng quy trình phù hợp cho từng loại thay đổi

### 1.2. Phạm vi

- Áp dụng cho tất cả các thay đổi trên hệ thống Production, DR, UAT
- Áp dụng cho hệ thống Cốt lõi và Vệ tinh
- Tham chiếu trong quy trình Upcode (QT-003) và Hotfix (QT-004)

### 1.3. Cấu trúc thông tin

Mỗi loại thay đổi bao gồm:
- **Mã**: Mã định danh duy nhất
- **Tên thay đổi**: Mô tả ngắn gọn
- **Mức độ rủi ro**: Thấp / Trung bình / Cao / Nghiêm trọng
- **Loại**: Chuẩn / Thông thường / Khẩn
- **Cấp độ duyệt**: Người/cấp có thẩm quyền phê duyệt
- **Điểm**: Điểm đánh giá rủi ro (Likelihood × Impact)

---

## 2. NHÓM A: THAY ĐỔI HẠ TẦNG (INFRASTRUCTURE)

**Tổng: 19 loại thay đổi**

### A1. Cập nhật và nâng cấp hệ thống

| Mã | Tên thay đổi | Mức độ rủi ro | Loại | Cấp độ duyệt | Điểm |
|----|--------------|---------------|------|--------------|------|
| A1.1 | Update windows (UAT/DR) | Thấp | Chuẩn | PM/PDM dự án | 2 |
| A1.2 | Update windows PROD, Linux | Thấp | Chuẩn | PM/PDM dự án/ Team lead DevOps | 2 |
| A1.3 | Nâng cấp hệ điều hành máy chủ | Trung bình | Chuẩn | PM/PDM dự án/ Team lead DevOps | 6 |
| A1.4 | Nâng cấp version phần mềm nền tảng | Nghiêm trọng | Thông thường | Lãnh đạo Công ty | 16 |

### A2. Dịch chuyển và tách cụm

| Mã | Tên thay đổi | Mức độ rủi ro | Loại | Cấp độ duyệt | Điểm |
|----|--------------|---------------|------|--------------|------|
| A2.1 | Dịch chuyển/Chuyển đổi hạ tầng | Nghiêm trọng | Thông thường | Lãnh đạo Công ty | 16 |
| A2.2 | Tách cụm (Cluster Splitting) | Nghiêm trọng | Thông thường | Lãnh đạo Công ty | 16 |
| A2.3 | Tách cụm để giảm tải DB và APP | Nghiêm trọng | Khẩn | Lãnh đạo Công ty | 16 |

### A3. Cấu hình mạng và bảo mật

| Mã | Tên thay đổi | Mức độ rủi ro | Loại | Cấp độ duyệt | Điểm |
|----|--------------|---------------|------|--------------|------|
| A3.1 | Thay đổi cấu hình mạng (firewall, load balancer, DNS, routing) | Cao | Chuẩn | Lãnh đạo Công ty | 12 |
| A3.2 | Thay đổi hoặc thêm hệ thống CDN/load balancer | Trung bình | Chuẩn | Lãnh đạo Công ty | 6 |
| A3.3 | Block IP theo yêu cầu | Thấp | Chuẩn | PM/PDM dự án | 2 |
| A3.4 | Cập nhật các phần mềm ATBM (KAS, SIEM, EDR) | Thấp | Chuẩn | PM/PDM dự án/ Team lead DevOps | 2 |

### A4. Quản lý tài nguyên và giám sát

| Mã | Tên thay đổi | Mức độ rủi ro | Loại | Cấp độ duyệt | Điểm |
|----|--------------|---------------|------|--------------|------|
| A4.1 | Thay đổi trên hệ thống giám sát | Thấp | Chuẩn | DevOps/ Team lead DevOps | 2 |
| A4.2 | Tăng dung lượng ổ cứng cho máy chủ Windows | Thấp | Chuẩn | PM/PDM dự án/ Team lead DevOps | 3 |
| A4.3 | Thay đổi tài nguyên của hệ thống (RAM, CPU) | Thấp | Chuẩn | PM/PDM dự án/ Team lead DevOps | 2 |
| A4.4 | Restart VM | Thấp | Chuẩn | PM/PDM dự án/ Team lead DevOps | 2 |
| A4.5 | Cài đặt/nâng cấp công cụ quản trị hạ tầng | Trung bình | Chuẩn | Lãnh đạo Công ty | 8 |

### A5. Cấu hình hệ thống

| Mã | Tên thay đổi | Mức độ rủi ro | Loại | Cấp độ duyệt | Điểm |
|----|--------------|---------------|------|--------------|------|
| A5.1 | Thay đổi cấu hình Domain | Thấp | Chuẩn | PM/PDM dự án/ Team lead DevOps | 2 |
| A5.2 | Thay đổi tham số cấu hình hệ thống | Thấp | Chuẩn | PM/PDM dự án/ Team lead DevOps | 2 |
| A5.3 | Thay đổi cấu hình sao lưu/backup | Trung bình | Chuẩn | PM/PDM dự án/ Team lead DevOps | 8 |

---

## 3. NHÓM B: THAY ĐỔI ỨNG DỤNG (APPLICATION)

**Tổng: 28 loại thay đổi**

### B1. Giao diện và nội dung

| Mã | Tên thay đổi | Mức độ rủi ro | Loại | Cấp độ duyệt | Điểm |
|----|--------------|---------------|------|--------------|------|
| B1.1 | Sửa lỗi giao diện (UI/UX) | Thấp | Chuẩn | PM/PDM dự án | 1 |
| B1.2 | Cập nhật pop-up, FAQ | Thấp | Chuẩn | Lãnh đạo TT/ PDM duyệt | 1 |
| B1.3 | Cập nhật hướng dẫn sử dụng | Thấp | Chuẩn | Lãnh đạo TT/ PDM duyệt | 1 |
| B1.4 | Chỉnh sửa phiếu in, báo cáo cho phần mềm | Thấp | Chuẩn | PM/PDM dự án | 1 |
| B1.5 | Tạo báo cáo/phiếu in đơn giản | Thấp | Chuẩn | PM/PDM dự án | 1 |
| B1.6 | Deploy báo cáo đặc thù | Trung bình | Chuẩn | Lãnh đạo TT/ PDM duyệt | 2 |

### B2. Chức năng nghiệp vụ

| Mã | Tên thay đổi | Mức độ rủi ro | Loại | Cấp độ duyệt | Điểm |
|----|--------------|---------------|------|--------------|------|
| B2.1 | Thêm chức năng nhỏ (rủi ro thấp) | Thấp | Chuẩn | PM/PDM dự án | 1 |
| B2.2 | Thêm chức năng nhỏ (rủi ro trung bình) | Trung bình | Thông thường | Ban CLGSP | 4 |
| B2.3 | Thêm module/chức năng mới | Thấp | Chuẩn | Lãnh đạo TT/ PDM duyệt | 1 |
| B2.4 | Tắt hoặc ẩn đi 1 số nút chức năng | Trung bình | Thông thường | Ban CLGSP | 4 |
| B2.5 | Chỉnh sửa chức năng phần mềm, chỉnh sửa báo cáo, phiếu in | Trung bình | Chuẩn | Lãnh đạo TT/ PDM duyệt | 2 |
| B2.6 | Thêm, sửa chức năng chung cho nhiều khách hàng | Trung bình | Thông thường | Ban CLGSP | 6 |
| B2.7 | Thêm giá trị vào danh mục | Thấp | Chuẩn | Lãnh đạo TT/ PDM duyệt | 1 |
| B2.8 | Chỉnh sửa rules hoặc validation | Trung bình | Thông thường | Ban CLGSP | 6 |
| B2.9 | Thay đổi quy trình xác thực người dùng | Thấp | Thông thường | PM/PDM dự án | 3 |

### B3. Kỹ thuật và tích hợp

| Mã | Tên thay đổi | Mức độ rủi ro | Loại | Cấp độ duyệt | Điểm |
|----|--------------|---------------|------|--------------|------|
| B3.1 | Thay đổi thư viện (Lib) - Level 1.5 | Trung bình | Thông thường | Ban CLGSP | 6 |
| B3.2 | Thay đổi thư viện (Lib) - Level 2 | Trung bình | Thông thường | Ban CLGSP | 6 |
| B3.3 | Thay đổi phiên bản runtime (Node, Python, Java, v.v.) | Trung bình | Thông thường | PM/PDM dự án | 8 |
| B3.4 | Tái cấu trúc code (Refactor) | Trung bình | Thông thường | Ban CLGSP, Ban KTHT | 6 |
| B3.5 | Thay đổi hệ thống logging/exception handling | Thấp | Thông thường | PM/PDM dự án | 3 |
| B3.6 | Cập nhật license phần mềm hoặc plugin thương mại | Trung bình | Thông thường | PM/PDM dự án | 4 |
| B3.7 | Thêm module mới hoặc plugin | Cao | Chuẩn | PM/PDM dự án | 9 |
| B3.8 | Thay đổi pipeline CI/CD | Cao | Chuẩn | Ban CLGSP | 9 |
| B3.9 | Tích hợp thêm hệ thống ngoài (API, SSO, thanh toán, Ký số, ...) | Cao | Thông thường | PM/PDM dự án | 9 |
| B3.10 | Tối ưu câu lệnh chậm (DB) | Trung bình | Chuẩn | Lãnh đạo TT/ PDM duyệt | 2 |

### B4. Sửa lỗi và bảo mật

| Mã | Tên thay đổi | Mức độ rủi ro | Loại | Cấp độ duyệt | Điểm |
|----|--------------|---------------|------|--------------|------|
| B4.1 | Sửa lỗi (bug fixing) | Trung bình | Chuẩn | PM/PDM dự án | 8 |
| B4.2 | Phát sinh trường hợp code lỗi cần hotfix luôn | Trung bình | Chuẩn | Lãnh đạo TT/ PDM duyệt | 2 |
| B4.3 | Xử lý lỗi ATBM (Rủi ro Thấp) | Thấp | Chuẩn | Lãnh đạo TT/ PDM duyệt | 2 |
| B4.4 | Xử lý lỗ hổng bảo mật nghiêm trọng | Cao | Thông thường | Tùy thuộc quy mô triển khai của SPDV | 12 |

### B5. Nâng cấp sản phẩm

| Mã | Tên thay đổi | Mức độ rủi ro | Loại | Cấp độ duyệt | Điểm |
|----|--------------|---------------|------|--------------|------|
| B5.1 | Nâng cấp phiên bản sản phẩm (Release Upgrade) | Cao | Thông thường | Lãnh đạo Công ty | 9 |

---

## 4. NHÓM C: THAY ĐỔI DỮ LIỆU VÀ CẤU HÌNH (DATA & CONFIGURATION)

**Tổng: 7 loại thay đổi**

### C1. Cấu trúc dữ liệu

| Mã | Tên thay đổi | Mức độ rủi ro | Loại | Cấp độ duyệt | Điểm |
|----|--------------|---------------|------|--------------|------|
| C1.1 | Thay đổi cấu trúc CSDL (schema/index/migration) | Trung bình | Chuẩn | Ban CLGSP | 8 |

### C2. Cấu hình nghiệp vụ

| Mã | Tên thay đổi | Mức độ rủi ro | Loại | Cấp độ duyệt | Điểm |
|----|--------------|---------------|------|--------------|------|
| C2.1 | Thực hiện cấu hình hệ thống chuẩn | Trung bình | Thông thường | Ban CLGSP | 4 |
| C2.2 | Thực hiện config cấu hình tự động | Trung bình | Thông thường | Ban CLGSP | 4 |
| C2.3 | Thêm giá trị vào danh mục | Thấp | Chuẩn | Lãnh đạo TT/ PDM duyệt | 1 |

### C3. Quản lý người dùng và quyền

| Mã | Tên thay đổi | Mức độ rủi ro | Loại | Cấp độ duyệt | Điểm |
|----|--------------|---------------|------|--------------|------|
| C3.1 | Change liên quan tới tài khoản | Thấp | Chuẩn | PM/PDM dự án/ Team lead DevOps | 1 |
| C3.2 | Mở khóa tài khoản (sai MK) | Thấp | Chuẩn | Lãnh đạo TT/ PDM duyệt | 1 |
| C3.3 | Gán/Thu Hồi Quyền Truy Cập | Thấp | Chuẩn | Lãnh đạo TT/ PDM duyệt | 2 |

---

## 5. NHÓM D: XỬ LÝ SỰ CỐ (INCIDENT MANAGEMENT)

**Tổng: 4 loại thay đổi**

### D1. Sự cố thông thường

| Mã | Tên thay đổi | Mức độ rủi ro | Loại | Cấp độ duyệt | Điểm |
|----|--------------|---------------|------|--------------|------|
| D1.1 | Xử lý sự cố thông thường | Thấp | Chuẩn | Lãnh đạo TT/ PDM duyệt | 4 |

### D2. Sự cố lớn

| Mã | Tên thay đổi | Mức độ rủi ro | Loại | Cấp độ duyệt | Điểm |
|----|--------------|---------------|------|--------------|------|
| D2.1 | Xử lý Sự cố Lớn (Major Incident) | Cao | Khẩn | Ban CLGSP, Ban KTHT | 9 |
| D2.2 | Xử lý sự cố lớn (trong phần APP) | Trung bình | Thông thường | Ban CLGSP | 6 |

### D3. Sự cố nghiêm trọng

| Mã | Tên thay đổi | Mức độ rủi ro | Loại | Cấp độ duyệt | Điểm |
|----|--------------|---------------|------|--------------|------|
| D3.1 | Xử lý Sự cố Nghiêm trọng (Serious Incident) | Nghiêm trọng | Khẩn | Lãnh đạo Công ty | 16 |

---

## 6. HƯỚNG DẪN SỬ DỤNG

### 6.1. Cách tra cứu

1. **Xác định loại thay đổi**: Dựa vào mô tả thay đổi, xác định thuộc nhóm nào (A/B/C/D)
2. **Tìm mã tương ứng**: Tra cứu trong bảng nhóm tương ứng
3. **Xác định quy trình**: Dựa vào "Loại" (Chuẩn/Thông thường/Khẩn) để xác định quy trình
4. **Xác định cấp phê duyệt**: Dựa vào "Cấp độ duyệt" trong bảng

### 6.2. Quy trình áp dụng

#### 6.2.1. Thay đổi Chuẩn (Standard Change)

- Tra cứu trong danh sách này
- Xác định cấp phê duyệt
- Thực hiện theo quy trình đã định nghĩa
- **Tham chiếu**: QT-003 - Phần 3.1

#### 6.2.2. Thay đổi Thông thường (Normal Change)

- Tra cứu trong danh sách này
- Đánh giá rủi ro (sử dụng điểm trong bảng)
- Xác định Level và cấp phê duyệt
- Tạo RFC và phê duyệt
- **Tham chiếu**: QT-003 - Phần 3.2

#### 6.2.3. Thay đổi Khẩn (Emergency Change)

- Tra cứu trong danh sách này
- Phê duyệt nhanh (ECAB hoặc Lãnh đạo)
- Thực hiện ngay
- Bổ sung hồ sơ sau
- **Tham chiếu**: QT-004 - Hotfix

### 6.3. Xử lý ngoại lệ

Nếu thay đổi không có trong danh sách này:
- Xem QT-003 - Phần 8: Quy trình xử lý ngoại lệ
- Đánh giá rủi ro và phân loại tạm thời
- Đề xuất bổ sung vào danh sách chuẩn (nếu phù hợp)

---

## 7. THỐNG KÊ

### 7.1. Phân bố theo nhóm

| Nhóm | Số lượng | Tỷ lệ |
|------|----------|-------|
| A. Hạ tầng | 19 | 32.8% |
| B. Ứng dụng | 28 | 48.3% |
| C. Dữ liệu & Cấu hình | 7 | 12.1% |
| D. Xử lý sự cố | 4 | 6.9% |
| **Tổng** | **58** | **100%** |

### 7.2. Phân bố theo mức độ rủi ro

| Mức độ rủi ro | Số lượng | Tỷ lệ |
|---------------|----------|-------|
| Thấp | 25 | 43.1% |
| Trung bình | 22 | 37.9% |
| Cao | 7 | 12.1% |
| Nghiêm trọng | 4 | 6.9% |
| **Tổng** | **58** | **100%** |

### 7.3. Phân bố theo loại thay đổi

| Loại thay đổi | Số lượng | Tỷ lệ |
|---------------|----------|-------|
| Chuẩn | 34 | 58.6% |
| Thông thường | 20 | 34.5% |
| Khẩn | 4 | 6.9% |
| **Tổng** | **58** | **100%** |

### 7.4. Phân bố theo cấp độ duyệt

| Cấp độ duyệt | Số lượng | Tỷ lệ |
|---------------|----------|-------|
| PM/PDM dự án | 20 | 34.5% |
| Lãnh đạo TT/PDM | 15 | 25.9% |
| Ban CLGSP | 12 | 20.7% |
| Lãnh đạo Công ty | 7 | 12.1% |
| Khác | 4 | 6.9% |
| **Tổng** | **58** | **100%** |

---

## PHỤ LỤC

### A. Tham chiếu

- **README.md**: File chính, tổng quan hệ thống
- **QT-003**: Quy trình Upcode
- **QT-004**: Quy trình Hotfix
- **QT-002**: Quy trình Quản trị Vận hành

### B. Bảng tra cứu nhanh theo mã

| Mã | Nhóm | Mức độ rủi ro | Loại |
|----|------|---------------|------|
| A1.1 - A5.3 | A. Hạ tầng | Thấp - Nghiêm trọng | Chuẩn/Thông thường/Khẩn |
| B1.1 - B5.1 | B. Ứng dụng | Thấp - Cao | Chuẩn/Thông thường |
| C1.1 - C3.3 | C. Dữ liệu & Cấu hình | Thấp - Trung bình | Chuẩn/Thông thường |
| D1.1 - D3.1 | D. Xử lý sự cố | Thấp - Nghiêm trọng | Chuẩn/Thông thường/Khẩn |

---

**Phiên bản**: 1.0
**Ngày ban hành**: [Ngày hiện tại]
**Người soạn**: 
**Trạng thái**: Chính thức

