# QT-003: QUY TRÌNH UPCODE

---

## THÔNG TIN TÀI LIỆU

- **Mã quy trình**: QT-003
- **Tên quy trình**: Quy trình Upcode
- **Phiên bản**: 2.0
- **Ngày ban hành**: [Ngày hiện tại]
- **Người soạn**: 
- **Trạng thái**: Chính thức

---

## MỤC LỤC

1. [Tổng quan](#1-tổng-quan)
2. [Quy trình upcode](#2-quy-trình-upcode)
3. [Quy trình Git và đánh mã Jira](#3-quy-trình-git-và-đánh-mã-jira)
4. [Phân loại thay đổi](#4-phân-loại-thay-đổi)
5. [Đánh giá rủi ro](#5-đánh-giá-rủi-ro)
6. [Quy trình kiểm thử](#6-quy-trình-kiểm-thử)
7. [Quy trình triển khai](#7-quy-trình-triển-khai)
8. [Quy trình rollback](#8-quy-trình-rollback)
9. [Quy trình xử lý ngoại lệ](#9-quy-trình-xử-lý-ngoại-lệ)
10. [Quy định về quyền truy cập tối thiểu](#10-quy-định-về-quyền-truy-cập-tối-thiểu)
11. [Checklist](#11-checklist)

---

## 1. TỔNG QUAN

### 1.1. Mục đích

Quy trình upcode nhằm đảm bảo code được triển khai an toàn, có kiểm soát và có thể rollback khi cần.

### 1.2. Phạm vi

- Triển khai code lên môi trường Production, DR, UAT, Staging
- Áp dụng cho tất cả loại thay đổi: Standard, Normal, Emergency
- Áp dụng cho các hệ thống:
 - Hệ thống Cốt lõi/Trọng điểm
 - Hệ thống Vệ tinh

### 1.3. Đối tượng

- Development Team
- DevOps Team
- QA Team
- PM/PDM
- Ban CLGSP
- Ban KTHT
- Lãnh đạo Trung tâm/Công ty

---

## 2. QUY TRÌNH UPCODE

### 2.1. Quy trình tổng quan

```mermaid
flowchart TD
 Start([Bắt đầu: Code đã sẵn sàng]) --> Identify[Xác định loại thay đổi]
 
 Identify --> AssessRisk[Đánh giá rủi ro]
 
 AssessRisk --> Plan[Lập kế hoạch triển khai]
 
 Plan --> Approve[Phê duyệt]
 
 Approve -->|Chưa phê duyệt| Wait[Chờ phê duyệt]
 Wait --> Approve
 
 Approve -->|Đã phê duyệt| Test[Kiểm thử]
 
 Test -->|Fail| Fix[Sửa lỗi]
 Fix --> Test
 
 Test -->|Pass| Backup[Backup]
 
 Backup --> Deploy[Triển khai]
 
 Deploy --> Verify[Kiểm tra deployment]
 
 Verify -->|Fail| Rollback[Rollback]
 Rollback --> End([Kết thúc])
 
 Verify -->|Pass| SmokeTest[Smoke test]
 
 SmokeTest -->|Fail| Rollback
 
 SmokeTest -->|Pass| Monitor[Giám sát]
 
 Monitor -->|Có vấn đề| Rollback
 
 Monitor -->|OK| Confirm[Xác nhận thành công]
 
 Confirm --> Record[Ghi nhận]
 
 Record --> End
 
 style Start fill:#90EE90
 style End fill:#FFB6C1
 style Rollback fill:#FFA500
 style Deploy fill:#87CEEB
```

### 2.2. Chi tiết từng bước

#### Bước 1: Chuẩn bị

**Công việc**:
- [ ] Code đã được review và merge
- [ ] Tất cả tests đã pass
- [ ] Documentation đã được update
- [ ] Xác định loại thay đổi (Standard/Normal/Emergency)
- [ ] Đánh giá rủi ro
- [ ] Xác định Level phê duyệt

**Checklist**:
- [ ] Unit tests: Pass
- [ ] Integration tests: Pass
- [ ] Code coverage: ≥ 80%
- [ ] Security scan: Pass
- [ ] Performance tests: Pass (nếu cần)

#### Bước 2: Lập kế hoạch triển khai

**Công việc**:
- [ ] Lập kế hoạch triển khai chi tiết
- [ ] Lập kế hoạch rollback
- [ ] Lập kế hoạch kiểm thử
- [ ] Xác định thời gian triển khai
- [ ] Xác định người thực hiện

**Nội dung kế hoạch**:
- Mô tả thay đổi
- Môi trường triển khai
- Thời gian triển khai
- Các bước triển khai
- Kế hoạch rollback
- Kế hoạch kiểm thử

#### Bước 3: Phê duyệt

**Công việc**:
- [ ] Tạo RFC (Request for Change) - Sử dụng template TP-001
- [ ] Gửi phê duyệt theo Level
- [ ] Chờ phê duyệt

**Tham chiếu**: `TP-001-TEMPLATE_RFC.md`

#### Bước 4: Kiểm thử

**Công việc**:
- [ ] Thực hiện kiểm thử theo Level (xem Phần 5)
- [ ] Test rollback
- [ ] Ghi nhận kết quả kiểm thử

**Tham chiếu**: Phần 5 - Quy trình kiểm thử

#### Bước 5: Triển khai

**Công việc**:
- [ ] Backup hệ thống
- [ ] Deploy code
- [ ] Kiểm tra deployment
- [ ] Smoke test
- [ ] Giám sát hệ thống

**Tham chiếu**: Phần 6 - Quy trình triển khai

#### Bước 6: Xác nhận

**Công việc**:
- [ ] Giám sát hệ thống (ít nhất 1 giờ)
- [ ] Kiểm tra log
- [ ] Kiểm tra metrics
- [ ] Xác nhận thành công
- [ ] Ghi nhận

---

## 3. QUY TRÌNH GIT VÀ ĐÁNH MÃ JIRA

### 3.1. Mục đích

Quy trình này quy định cách thức quản lý code trên Git và liên kết với Jira để:
- **Quản trị xuyên suốt**: Theo dõi code từ Jira task đến Git commit, từ Git commit đến deployment
- **Truy vết đầy đủ**: Biết được code nào thuộc task nào, ai thực hiện, khi nào
- **Audit dễ dàng**: Có thể truy vết toàn bộ lịch sử thay đổi
- **Tăng tính minh bạch**: Mọi thay đổi đều được ghi nhận và liên kết

### 3.2. Quy trình Git

#### 3.2.1. Quy trình tổng quan

```mermaid
flowchart TD
 Start([Bắt đầu: Task từ Jira]) --> CreateBranch[Tạo branch từ Jira task]
 CreateBranch --> Develop[Phát triển code]
 Develop --> Commit[Commit với mã Jira]
 Commit --> Push[Push lên Git]
 Push --> CreatePR[Tạo Pull Request]
 CreatePR --> Review[Code Review]
 Review -->|Cần sửa| Fix[Sửa code]
 Fix --> Commit
 Review -->|Approve| Merge[Merge vào main/develop]
 Merge --> Tag[Tạo tag nếu cần]
 Tag --> Deploy[Deploy]
 Deploy --> CloseJira[Đóng task Jira]
 CloseJira --> End([Kết thúc])
 
 style Start fill:#90EE90
 style End fill:#FFB6C1
 style Commit fill:#87CEEB
 style Merge fill:#FFD700
```

#### 3.2.2. Quy tắc đặt tên branch

**Format**: `{type}/{JIRA-TASK-ID}-{short-description}`

**Ví dụ**:
- `feature/PROJ-123-add-user-authentication`
- `bugfix/PROJ-456-fix-login-error`
- `hotfix/PROJ-789-critical-security-patch`
- `refactor/PROJ-101-optimize-database-query`

**Quy tắc**:
- **type**: `feature`, `bugfix`, `hotfix`, `refactor`, `docs`, `test`
- **JIRA-TASK-ID**: Mã task từ Jira (ví dụ: `PROJ-123`)
- **short-description**: Mô tả ngắn gọn, dùng ký tự thường, nối bằng dấu gạch ngang

**Ví dụ tạo branch**:
```bash
# Từ Jira task PROJ-123: "Add user authentication"
git checkout -b feature/PROJ-123-add-user-authentication

# Từ Jira task PROJ-456: "Fix login error"
git checkout -b bugfix/PROJ-456-fix-login-error
```

#### 3.2.3. Quy tắc commit message

**Format**: `{JIRA-TASK-ID}: {Mô tả ngắn gọn}`

**Ví dụ**:
```
PROJ-123: Add user authentication with JWT
PROJ-456: Fix login error when password contains special characters
PROJ-789: Hotfix - Critical security patch for SQL injection
```

**Quy tắc chi tiết**:
- **Bắt buộc có mã Jira**: Mọi commit phải có mã Jira task
- **Mô tả rõ ràng**: Mô tả ngắn gọn nhưng đủ thông tin
- **Sử dụng present tense**: "Add", "Fix", "Update" (không dùng "Added", "Fixed")
- **Giới hạn độ dài**: Dòng đầu tiên ≤ 72 ký tự
- **Body (tùy chọn)**: Có thể thêm mô tả chi tiết sau dòng đầu tiên

**Ví dụ commit message đầy đủ**:
```
PROJ-123: Add user authentication with JWT

- Implement JWT token generation
- Add login endpoint
- Add middleware for token validation
- Update user model to include refresh token
- Add unit tests for authentication

Closes PROJ-123
```

**Ví dụ commit với multiple tasks**:
```
PROJ-123, PROJ-124: Refactor authentication module

- Consolidate authentication logic
- Update both login and registration flows
- Improve error handling

Closes PROJ-123
Closes PROJ-124
```

#### 3.2.4. Quy trình commit và push

**Bước 1: Commit code**
```bash
# Stage files
git add .

# Commit với mã Jira
git commit -m "PROJ-123: Add user authentication with JWT"

# Hoặc commit với message đầy đủ
git commit -m "PROJ-123: Add user authentication with JWT

- Implement JWT token generation
- Add login endpoint
- Add middleware for token validation

Closes PROJ-123"
```

**Bước 2: Push lên remote**
```bash
# Push branch lên remote
git push origin feature/PROJ-123-add-user-authentication

# Nếu branch chưa tồn tại trên remote
git push -u origin feature/PROJ-123-add-user-authentication
```

**Bước 3: Tạo Pull Request**
- Tạo PR trên Git platform (GitHub, GitLab, Bitbucket)
- **Title**: `[PROJ-123] Add user authentication with JWT`
- **Description**: Mô tả chi tiết, link đến Jira task
- **Reviewers**: Assign reviewers theo quy trình

**Bước 4: Code Review**
- Reviewers review code
- Nếu cần sửa, sửa và commit tiếp (vẫn giữ mã Jira)
- Sau khi approve, merge vào main/develop

**Bước 5: Merge và đóng task**
- Merge PR vào main/develop
- Git tự động link commit với Jira (nếu có integration)
- Đóng task Jira hoặc chuyển sang trạng thái "Done"

### 3.3. Đánh mã task từ Jira sang Git

#### 3.3.1. Mục đích

Đánh mã task từ Jira sang Git nhằm:
- **Liên kết xuyên suốt**: Từ Jira → Git → Deployment → Production
- **Truy vết đầy đủ**: Biết được code nào thuộc task nào
- **Quản trị hiệu quả**: Dễ dàng quản lý và theo dõi
- **Audit dễ dàng**: Có thể audit toàn bộ quy trình

#### 3.3.2. Quy tắc đánh mã

**Format**: `{PROJECT-PREFIX}-{TASK-NUMBER}`

**Ví dụ**:
- `PROJ-123`
- `PROJ-456`
- `PROJ-789`

**Quy tắc**:
- **PROJECT-PREFIX**: Tiền tố dự án (ví dụ: `PROJ`, `APP`, `API`)
- **TASK-NUMBER**: Số thứ tự task (ví dụ: `123`, `456`)
- **Format nhất quán**: Tất cả task phải có format nhất quán

#### 3.3.3. Nơi đánh mã

**1. Git Branch Name**
```bash
# Format: {type}/{JIRA-TASK-ID}-{short-description}
feature/PROJ-123-add-user-authentication
bugfix/PROJ-456-fix-login-error
```

**2. Git Commit Message**
```bash
# Format: {JIRA-TASK-ID}: {Mô tả}
PROJ-123: Add user authentication with JWT
PROJ-456: Fix login error when password contains special characters
```

**3. Pull Request Title**
```
[PROJ-123] Add user authentication with JWT
[PROJ-456] Fix login error when password contains special characters
```

**4. Pull Request Description**
```markdown
## Mô tả
Thêm tính năng xác thực người dùng với JWT

## Jira Task
- [PROJ-123](https://jira.company.com/browse/PROJ-123)

## Thay đổi
- Implement JWT token generation
- Add login endpoint
- Add middleware for token validation

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

Closes PROJ-123
```

**5. Code Comments (tùy chọn)**
```python
# PROJ-123: Add user authentication with JWT
def generate_jwt_token(user_id):
 """
 Generate JWT token for user authentication.
 
 Related Jira task: PROJ-123
 """
 # Implementation
 pass
```

#### 3.3.4. Quy trình đánh mã

**Bước 1: Tạo task trong Jira**
- Tạo task trong Jira với mã task (ví dụ: `PROJ-123`)
- Ghi nhận mã task

**Bước 2: Tạo branch với mã Jira**
```bash
# Tạo branch với mã Jira
git checkout -b feature/PROJ-123-add-user-authentication
```

**Bước 3: Commit với mã Jira**
```bash
# Commit với mã Jira trong message
git commit -m "PROJ-123: Add user authentication with JWT"
```

**Bước 4: Push và tạo PR**
- Push branch lên remote
- Tạo PR với title có mã Jira: `[PROJ-123] Add user authentication with JWT`
- Link PR với Jira task (nếu có integration)

**Bước 5: Merge và đóng task**
- Merge PR vào main/develop
- Git tự động link commit với Jira (nếu có integration)
- Đóng task Jira hoặc chuyển sang trạng thái "Done"

#### 3.3.5. Tích hợp Jira-Git

**Cấu hình Git Integration trong Jira**:
1. Cài đặt Git Integration trong Jira
2. Cấu hình Git repository
3. Cấu hình branch pattern: `{type}/{JIRA-TASK-ID}-*`
4. Cấu hình commit message pattern: `{JIRA-TASK-ID}: *`

**Lợi ích**:
- Tự động link commit với Jira task
- Tự động cập nhật trạng thái task khi merge
- Hiển thị commit trong Jira task
- Hiển thị Jira task trong Git commit

**Ví dụ tích hợp**:
- **Jira**: Task `PROJ-123` hiển thị tất cả commit liên quan
- **Git**: Commit `PROJ-123: Add user authentication` hiển thị link đến Jira task

### 3.4. Best Practices

#### 3.4.1. Git Best Practices

** Nên làm**:
- Luôn tạo branch từ Jira task
- Luôn commit với mã Jira
- Commit thường xuyên, mỗi commit là một thay đổi logic
- Viết commit message rõ ràng
- Tạo PR sau mỗi feature/bugfix
- Review code trước khi merge
- Merge vào main/develop sau khi approve

** Không nên làm**:
- Commit mà không có mã Jira
- Commit nhiều thay đổi không liên quan trong một commit
- Push trực tiếp lên main/develop (trừ hotfix)
- Merge mà không có code review
- Xóa branch ngay sau khi merge (giữ ít nhất 30 ngày)

#### 3.4.2. Jira-Git Integration Best Practices

** Nên làm**:
- Tạo task Jira trước khi bắt đầu code
- Sử dụng mã Jira nhất quán trong branch, commit, PR
- Link PR với Jira task
- Đóng task Jira sau khi merge
- Sử dụng Jira để track progress

** Không nên làm**:
- Code mà không có task Jira
- Sử dụng mã Jira không nhất quán
- Quên đóng task Jira sau khi merge
- Tạo nhiều task Jira cho một feature nhỏ

### 3.5. Ví dụ quy trình hoàn chỉnh

**Scenario**: Thêm tính năng xác thực người dùng

**Bước 1: Tạo task Jira**
- Tạo task: `PROJ-123: Add user authentication with JWT`
- Mã task: `PROJ-123`

**Bước 2: Tạo branch**
```bash
git checkout main
git pull origin main
git checkout -b feature/PROJ-123-add-user-authentication
```

**Bước 3: Phát triển code**
```bash
# Develop code...
# Test code...
```

**Bước 4: Commit**
```bash
git add .
git commit -m "PROJ-123: Add user authentication with JWT

- Implement JWT token generation
- Add login endpoint
- Add middleware for token validation
- Update user model to include refresh token
- Add unit tests for authentication

Closes PROJ-123"
```

**Bước 5: Push và tạo PR**
```bash
git push origin feature/PROJ-123-add-user-authentication
```

**PR Title**: `[PROJ-123] Add user authentication with JWT`

**PR Description**:
```markdown
## Mô tả
Thêm tính năng xác thực người dùng với JWT

## Jira Task
- [PROJ-123](https://jira.company.com/browse/PROJ-123)

## Thay đổi
- Implement JWT token generation
- Add login endpoint
- Add middleware for token validation
- Update user model to include refresh token
- Add unit tests for authentication

## Testing
- [x] Unit tests pass
- [x] Integration tests pass
- [x] Manual testing completed

Closes PROJ-123
```

**Bước 6: Code Review và Merge**
- Reviewers review code
- Approve và merge vào main
- Git tự động link commit với Jira (nếu có integration)

**Bước 7: Đóng task Jira**
- Đóng task `PROJ-123` hoặc chuyển sang trạng thái "Done"

**Kết quả**:
- Code được quản lý trên Git với mã Jira
- Có thể truy vết từ Jira → Git → Deployment
- Audit dễ dàng với lịch sử đầy đủ

---

## 4. PHÂN LOẠI THAY ĐỔI

### 3.1. Standard Change (Thay đổi chuẩn)

**Đặc điểm**:
- Rủi ro thấp
- Lặp đi lặp lại
- Có trong danh sách chuẩn
- Đã được ủy quyền trước

**Phê duyệt**: Đã ủy quyền trước, không cần CAB mỗi lần

**Thời gian**: Nhanh (1-2 ngày)

**Danh sách thay đổi chuẩn**: 
- **Tham chiếu**: `QT-008-DANH_SACH_THAY_DOI_CHUAN.md`
- Danh sách bao gồm 58 loại thay đổi được phân thành 4 nhóm:
 - **Nhóm A**: Hạ tầng (19 loại)
 - **Nhóm B**: Ứng dụng (28 loại)
 - **Nhóm C**: Dữ liệu & Cấu hình (7 loại)
 - **Nhóm D**: Xử lý sự cố (4 loại)

### 3.2. Normal Change (Thay đổi thông thường)

**Đặc điểm**:
- Cần đánh giá
- Chưa có trong danh sách chuẩn
- Rủi ro trung bình đến cao

**Phê duyệt**: Cần CAB phê duyệt

**Thời gian**: Trung bình (3-7 ngày)

### 3.3. Emergency Change (Thay đổi khẩn)

**Đặc điểm**:
- Khẩn cấp để xử lý sự cố
- Rủi ro có thể cao
- Cần xử lý ngay

**Phê duyệt**: ECAB hoặc Lãnh đạo, có thể phê duyệt sau

**Thời gian**: Rất nhanh (< 1 ngày)

**Lưu ý**: Xem thêm QT-004 (Hotfix) cho trường hợp sự cố nghiêm trọng

---

## 5. ĐÁNH GIÁ RỦI RO

### 4.1. Ma trận đánh giá rủi ro

**Công thức**: `Rủi ro = Likelihood × Impact`

#### 4.1.1. Likelihood (Khả năng xảy ra)

| Điểm | Mô tả | Ví dụ |
|------|-------|-------|
| 4 | Rất cao | Thay đổi lớn, chưa test kỹ |
| 3 | Cao | Thay đổi trung bình, test cơ bản |
| 2 | Trung bình | Thay đổi nhỏ, test đầy đủ |
| 1 | Thấp | Thay đổi rất nhỏ, test kỹ |

#### 4.1.2. Impact (Tác động)

| Điểm | Mô tả | Ví dụ |
|------|-------|-------|
| 4 | Nghiêm trọng | Hệ thống down, mất dữ liệu |
| 3 | Cao | Ảnh hưởng nhiều người dùng |
| 2 | Trung bình | Ảnh hưởng một số người dùng |
| 1 | Thấp | Ảnh hưởng ít người dùng |

### 4.2. Phân loại mức độ rủi ro

| Điểm | Mức độ | Level | Cấp phê duyệt |
|------|--------|-------|---------------|
| 13-16 | Nghiêm trọng | 4.0 | Lãnh đạo Công ty |
| 9-12 | Cao | 3.0 | Ban CLGSP + Ban KTHT |
| 4-8 | Trung bình | 2.0 | Ban CLGSP hoặc Lãnh đạo TT |
| 1-3 | Thấp | 1.0 | PM/PDM |

### 4.3. Phân loại hệ thống

#### 4.3.1. Hệ thống Cốt lõi/Trọng điểm

**Đặc điểm**:
- Hệ thống quan trọng, ảnh hưởng đến nhiều người dùng
- Hệ thống xử lý dữ liệu quan trọng
- Hệ thống liên quan đến thanh toán, bảo mật

**Quy định**:
- Tuân thủ nghiêm ngặt đánh giá rủi ro
- Bắt buộc có kế hoạch triển khai chi tiết
- Bắt buộc có kịch bản rollback
- Cần phê duyệt từ cấp cao hơn

#### 4.3.2. Hệ thống Vệ tinh

**Đặc điểm**:
- Hệ thống hỗ trợ, ảnh hưởng ít người dùng
- Hệ thống độc lập, không ảnh hưởng đến hệ thống khác

**Quy định**:
- Tự đánh giá rủi ro dựa trên quy mô
- Linh hoạt hơn trong phê duyệt
- Vẫn tuân thủ quy trình cho sự cố lớn/nghiêm trọng

### 4.4. Bảng RACI - Cấp độ phê duyệt và trách nhiệm

| Level | Loại thay đổi | Rủi ro | Hệ thống | Accountable (Phê duyệt) | Responsible (Thực hiện) | Consulted (Tư vấn) | Informed (Thông báo) |
|-------|---------------|--------|----------|------------------------|------------------------|-------------------|---------------------|
| **1.0** | Chuẩn/Thông thường | Thấp | Cốt lõi & Vệ tinh | PM/PDM/Team Lead DevOps | DevOps/Dev Team | - | Ban CLGSP |
| **2.0** | Chuẩn | Trung bình | Cốt lõi | Lãnh đạo TT/PDM | DevOps/Dev Team | Ban CLGSP | Ban KTHT |
| **2.0** | Chuẩn | Trung bình | Vệ tinh | PM/PDM/Team Lead | DevOps/Dev Team | - | - |
| **2.0** | Thông thường | Trung bình | Cốt lõi | Ban CLGSP | DevOps/Dev Team | Ban KTHT | Lãnh đạo TT |
| **2.0** | Thông thường | Trung bình | Vệ tinh | PM/PDM/Team Lead | DevOps/Dev Team | - | - |
| **3.0** | Thông thường | Trung bình/Cao | Cốt lõi | Ban CLGSP (+ Ban KTHT) | DevOps/Dev Team | Ban KTHT | Lãnh đạo TT |
| **3.0** | Thông thường | Trung bình/Cao | Vệ tinh | Theo đề xuất đơn vị | DevOps/Dev Team | - | - |
| **4.0** | Khẩn/Thông thường | Cao/Nghiêm trọng | Cốt lõi | Lãnh đạo Công ty | DevOps/Dev Team | Ban CLGSP, Ban KTHT | Toàn bộ |
| **4.0** | Khẩn/Thông thường | Cao/Nghiêm trọng | Vệ tinh | Lãnh đạo Công ty (hoặc N/A) | DevOps/Dev Team | Ban CLGSP | - |

### 4.5. Quy trình đánh giá rủi ro

1. Xác định Likelihood
2. Xác định Impact
3. Tính điểm rủi ro
4. Xác định loại hệ thống (Cốt lõi/Vệ tinh)
5. Xác định Level
6. Xác định cấp phê duyệt (tra bảng RACI)

---

## 6. QUY TRÌNH KIỂM THỬ

### 6.1. Mức độ kiểm thử theo Level

| Level | Loại kiểm thử | Bắt buộc | Tùy chọn | Môi trường kiểm thử |
|-------|---------------|----------|----------|---------------------|
| **1.0** | Unit Test | | - | Development |
| **2.0** | Unit Test + Integration Test | | Regression Test | UAT/Staging |
| **3.0** | Unit + Integration + Regression | | Load Test, Security Test | UAT/Staging |
| **4.0** | Tất cả + Load Test + Security Test | | Performance Test, Stress Test | UAT/Staging + DR |

### 6.2. Các loại kiểm thử

#### 5.2.1. Unit Test

- Test từng function/module riêng lẻ
- Coverage: ≥ 80%
- Tự động hóa

#### 5.2.2. Integration Test

- Test tích hợp giữa các module
- Test API
- Test database

#### 5.2.3. Regression Test

- Test các chức năng cũ vẫn hoạt động
- Test các test case quan trọng
- Tự động hóa (nếu có thể)

#### 5.2.4. Load Test

- Test hiệu năng dưới tải
- Test khả năng mở rộng
- Test giới hạn hệ thống

#### 5.2.5. Security Test

- Test bảo mật
- Test authentication/authorization
- Test SQL injection, XSS, ...

#### 5.2.6. Smoke Test

- Test nhanh các chức năng cơ bản
- Sau khi deploy
- Xác nhận hệ thống hoạt động

### 6.3. Quy trình kiểm thử

```
1. Chuẩn bị môi trường test
2. Chạy unit tests
3. Chạy integration tests
4. Chạy regression tests (nếu cần)
5. Chạy load tests (nếu cần)
6. Chạy security tests (nếu cần)
7. Ghi nhận kết quả
8. Xác nhận pass/fail
```

---

## 7. QUY TRÌNH TRIỂN KHAI

### 6.1. Chuẩn bị triển khai

**Công việc**:
- [ ] Backup hệ thống
- [ ] Backup database
- [ ] Backup cấu hình
- [ ] Chuẩn bị rollback plan
- [ ] Thông báo team

### 6.2. Triển khai

**Công việc**:
- [ ] Deploy code
- [ ] Update cấu hình (nếu cần)
- [ ] Run migration (nếu cần)
- [ ] Restart service (nếu cần)
- [ ] Kiểm tra deployment

### 6.3. Kiểm tra sau triển khai

**Công việc**:
- [ ] Kiểm tra service đã start
- [ ] Kiểm tra health check
- [ ] Kiểm tra log
- [ ] Smoke test
- [ ] Kiểm tra metrics

### 6.4. Giám sát

**Công việc**:
- [ ] Giám sát hệ thống (ít nhất 1 giờ)
- [ ] Kiểm tra error rate
- [ ] Kiểm tra response time
- [ ] Kiểm tra resource usage
- [ ] Kiểm tra log

---

## 8. QUY TRÌNH ROLLBACK

### 7.1. Khi nào cần rollback

- Sự cố nghiêm trọng ảnh hưởng đến dịch vụ
- Mất dữ liệu hoặc dữ liệu sai
- Hệ thống không thể hoạt động
- Performance suy giảm nghiêm trọng
- Lỗi bảo mật nghiêm trọng

### 7.2. Quy trình rollback

#### 7.2.1. Quy trình tổng quan

```mermaid
flowchart TD
 Start([Bắt đầu: Lập kế hoạch thay đổi]) --> CheckRisk{Mức độ rủi ro<br/>Trung bình trở lên?}
 
 CheckRisk -->|Thấp| Optional[Rollback<br/>tùy chọn]
 CheckRisk -->|Trung bình/Cao/Nghiêm trọng| Required[Rollback<br/>bắt buộc]
 
 Optional --> PlanRollback
 Required --> PlanRollback
 
 PlanRollback[Lập kế hoạch rollback<br/>- Các bước rollback chi tiết<br/>- Thời gian rollback dự kiến<br/>- Điều kiện kích hoạt rollback<br/>- Script rollback]
 
 PlanRollback --> PrepareBackup[Chuẩn bị backup<br/>- Backup database<br/>- Backup code<br/>- Backup cấu hình]
 
 PrepareBackup --> TestRollback[Test rollback<br/>trên UAT/Staging]
 
 TestRollback --> ExecuteTestRollback[Thực hiện rollback<br/>trên môi trường test]
 
 ExecuteTestRollback --> VerifyTestRollback{Kiểm tra<br/>Rollback thành công?}
 
 VerifyTestRollback -->|Thất bại| FixPlan[Sửa kế hoạch<br/>rollback]
 FixPlan --> TestRollback
 
 VerifyTestRollback -->|Thành công| MeasureTime[Đo thời gian<br/>rollback thực tế]
 
 MeasureTime --> UpdatePlan[Cập nhật kế hoạch<br/>với thời gian thực tế]
 
 UpdatePlan --> Ready[Chuẩn bị sẵn sàng<br/>- Backup đầy đủ<br/>- Script rollback sẵn sàng<br/>- Người thực hiện sẵn sàng]
 
 Ready --> Deploy[Triển khai<br/>thay đổi lên Production]
 
 Deploy --> Monitor[Giám sát<br/>sau triển khai]
 
 Monitor --> CheckIssue{Có vấn đề?}
 
 CheckIssue -->|Không| Success[Thành công<br/>Không cần rollback]
 CheckIssue -->|Có| AssessIssue{Đánh giá<br/>mức độ vấn đề}
 
 AssessIssue -->|Nhỏ, có thể chấp nhận| MonitorMore[Giám sát thêm]
 AssessIssue -->|Nghiêm trọng| TriggerRollback[Kích hoạt rollback]
 
 MonitorMore --> CheckIssue
 
 TriggerRollback --> StopService[Dừng dịch vụ<br/>nếu cần]
 
 StopService --> ExecuteRollback[Thực hiện rollback<br/>Theo kế hoạch đã test]
 
 ExecuteRollback --> VerifyRollback{Kiểm tra<br/>Rollback thành công?}
 
 VerifyRollback -->|Thất bại| Escalate[Escalate<br/>Tăng cường xử lý]
 Escalate --> ExecuteRollback
 
 VerifyRollback -->|Thành công| RestartService[Khởi động lại<br/>dịch vụ]
 
 RestartService --> VerifySystem{Kiểm tra hệ thống<br/>Hoạt động bình thường?}
 
 VerifySystem -->|Đúng| Document[Ghi nhận<br/>- Thời điểm rollback<br/>- Nguyên nhân<br/>- Kết quả]
 VerifySystem -->|Sai| Escalate
 
 Document --> PostMortem[Đánh giá sau rollback<br/>- Phân tích nguyên nhân<br/>- Rút kinh nghiệm<br/>- Cải tiến quy trình]
 
 PostMortem --> UpdateJIRA[Cập nhật JIRA<br/>Đóng ticket]
 
 UpdateJIRA --> End([Kết thúc])
 Success --> End
 
 style Start fill:#90EE90
 style End fill:#FFB6C1
 style PlanRollback fill:#87CEEB
 style TestRollback fill:#FFE4B5
 style ExecuteRollback fill:#FFA500
 style VerifyRollback fill:#90EE90
 style Document fill:#DDA0DD
 style TriggerRollback fill:#FF6B6B
```

#### 7.2.2. Chi tiết các bước

**Bước 1: Lập kế hoạch rollback**
- Các bước rollback chi tiết
- Thời gian rollback dự kiến
- Điều kiện kích hoạt rollback
- Script rollback

**Bước 2: Test rollback trên UAT/Staging**
- Thực hiện rollback trên môi trường test
- Xác nhận rollback thành công
- Đo thời gian rollback thực tế

**Bước 3: Chuẩn bị sẵn sàng**
- Backup đầy đủ
- Script rollback sẵn sàng
- Người thực hiện rollback sẵn sàng

**Bước 4: Thực hiện rollback (nếu cần)**
- Theo kế hoạch đã test
- Ghi nhận kết quả
- Đánh giá sau rollback

### 7.3. Rollback plan

**Nội dung rollback plan**:
- Version cần rollback
- Các bước rollback
- Thời gian rollback
- Người thực hiện
- Cách verify rollback thành công

---

## 9. QUY TRÌNH XỬ LÝ NGOẠI LỆ

### 8.1. Định nghĩa ngoại lệ

Ngoại lệ là các trường hợp thay đổi không nằm trong danh sách thay đổi chuẩn (QT-008), bao gồm:

1. Thay đổi hoàn toàn mới, chưa từng thực hiện trước đó
2. Thay đổi có đặc điểm khác biệt so với các loại trong danh sách chuẩn
3. Thay đổi kết hợp nhiều loại trong danh sách chuẩn
4. Thay đổi trên hệ thống mới chưa được phân loại

### 8.2. Quy trình xử lý ngoại lệ

1. **Xác định loại thay đổi**
 - Tra cứu trong danh sách chuẩn (QT-008)
 - So sánh với danh sách chuẩn
 - Xác định có phải ngoại lệ không

2. **Đánh giá rủi ro**
 - Sử dụng ma trận rủi ro (Phần 4)
 - Tính điểm Likelihood × Impact
 - Xác định mức độ rủi ro

3. **Phân loại tạm thời**
 - Phân vào loại gần nhất trong danh sách chuẩn
 - Hoặc phân vào loại "Thay đổi thông thường" nếu không có loại tương ứng

4. **Lập kế hoạch chi tiết**
 - Mô tả chi tiết thay đổi
 - Kế hoạch triển khai
 - Kế hoạch rollback
 - Đánh giá rủi ro chi tiết

5. **Phê duyệt**
 - Theo cấp độ tương ứng với mức độ rủi ro
 - Có thể cần phê duyệt từ cấp cao hơn 1 bậc so với loại tương ứng

6. **Thực hiện**
 - Theo quy trình của loại tương ứng
 - Tăng cường giám sát và kiểm tra

7. **Đánh giá sau**
 - Đánh giá kết quả
 - Rút kinh nghiệm
 - Đề xuất bổ sung vào danh sách chuẩn (nếu phù hợp)

### 8.3. Lưu ý quan trọng

- Ngoại lệ không được sử dụng để tránh quy trình phê duyệt
- Mọi ngoại lệ đều phải được ghi nhận và theo dõi
- Ngoại lệ có mức độ rủi ro cao cần được xử lý đặc biệt cẩn trọng
- Định kỳ rà soát các ngoại lệ để xem xét bổ sung vào danh sách chuẩn

---

## 10. QUY ĐỊNH VỀ QUYỀN TRUY CẬP TỐI THIỂU

### 9.1. Nguyên tắc

- **Cấp đúng quyền – đủ quyền – chỉ quyền cần thiết**: Mỗi người dùng chỉ được cấp quyền đủ để hoàn thành nhiệm vụ
- **Phân quyền theo vai trò (RBAC)**: Tất cả quyền được cấp thông qua Role
- **Cấp quyền tạm thời (Just-In-Time – JIT)**: Quyền cao (root/admin) chỉ được cấp khi có yêu cầu chính đáng, tự động hết hạn sau khoảng thời gian xác định
- **Tài khoản quản trị tách biệt**: Tài khoản làm việc hằng ngày ≠ tài khoản admin
- **Separation of Duties (SoD)**: Không một cá nhân nào có toàn quyền trong một quy trình

### 9.2. Quy định quyền truy cập trong quy trình upcode

#### 9.2.1. Quyền truy cập môi trường

| Môi trường | Developer | DevOps | QA | PM/PDM |
|------------|-----------|--------|----|----|
| **Development** | Read/Write | Read/Write | Read | Read |
| **Staging/UAT** | Read | Read/Write | Read/Write | Read |
| **Production** | Read (chỉ xem log) | Read/Write (theo quy trình) | Read | Read |
| **DR** | Read (chỉ xem log) | Read/Write (theo quy trình) | Read | Read |

#### 9.2.2. Quyền deploy

- **Developer**: Không được deploy trực tiếp lên Production/DR
- **DevOps**: Được deploy lên Production/DR sau khi có phê duyệt
- **QA**: Không được deploy, chỉ được test

#### 9.2.3. Quyền database

- **Developer**: Read-only trên Production/DR
- **DevOps**: Read/Write trên Production/DR (theo quy trình, có log)
- **QA**: Read-only trên Staging/UAT

#### 9.2.4. Quyền cấu hình

- **Developer**: Không được thay đổi cấu hình Production/DR
- **DevOps**: Được thay đổi cấu hình Production/DR sau khi có phê duyệt
- **QA**: Không được thay đổi cấu hình

### 9.3. Quy trình cấp quyền tạm thời (JIT)

1. **Yêu cầu quyền**
 - Tạo yêu cầu trong hệ thống quản lý quyền
 - Mô tả lý do cần quyền
 - Xác định thời gian cần quyền

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
 - Thu hồi ngay sau khi hoàn thành công việc
 - Ghi log thu hồi

### 9.4. Giám sát và ghi log

- Mọi hành động với quyền cao đều được ghi log
- Log được lưu tối thiểu 90 ngày
- Rà soát log định kỳ (hàng tháng)
- Cảnh báo khi có hành động bất thường

**Tham chiếu**: `QT/CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU.md`

---

## 11. CHECKLIST

**Tham chiếu chi tiết**: `CL-002-CHECKLIST_UPCODE.md`

### 10.1. Checklist trước triển khai

- [ ] Code đã được review và merge
- [ ] Tất cả tests đã pass
- [ ] Documentation đã được update
- [ ] Đã xác định loại thay đổi
- [ ] Đã đánh giá rủi ro
- [ ] Đã lập kế hoạch triển khai
- [ ] Đã lập kế hoạch rollback
- [ ] Đã được phê duyệt

### 10.2. Checklist trong triển khai

- [ ] Đã backup hệ thống
- [ ] Đã backup database
- [ ] Đã backup cấu hình
- [ ] Đã deploy code
- [ ] Đã kiểm tra deployment
- [ ] Đã smoke test
- [ ] Đã giám sát hệ thống

### 10.3. Checklist sau triển khai

- [ ] Hệ thống hoạt động bình thường
- [ ] Không có lỗi trong log
- [ ] Metrics trong giới hạn cho phép
- [ ] Đã ghi nhận
- [ ] Đã thông báo team

---

**Phiên bản**: 2.0
**Ngày ban hành**: [Ngày hiện tại]
**Người soạn**: 
**Trạng thái**: Chính thức

**Cập nhật lần cuối**: 2024-12-17
- Bổ sung quy trình Git và đánh mã Jira (Phần 3)
- Cập nhật số thứ tự các phần (4-11)

---

## PHỤ LỤC

### A. Tham chiếu

- **README.md**: File chính, tổng quan hệ thống
- **QT-002**: Quy trình Quản trị Vận hành
- **QT-004**: Quy trình Hotfix
- **QT-006**: Quy trình Versioning
- **QT-008**: Danh sách Thay đổi Chuẩn
- **CL-002**: Checklist Upcode
- **TP-001**: Template RFC
- **CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU**: `QT/CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU.md`

### B. Thuật ngữ

- **Standard Change**: Thay đổi chuẩn - Thay đổi đã được phê duyệt trước, có quy trình rõ ràng, rủi ro thấp
- **Normal Change**: Thay đổi thông thường - Thay đổi cần đánh giá và phê duyệt trước khi thực hiện
- **Emergency Change**: Thay đổi khẩn - Thay đổi khẩn cấp để xử lý sự cố
- **RFC**: Request for Change - Yêu cầu thay đổi
- **CAB**: Change Advisory Board - Ban tư vấn thay đổi
- **ECAB**: Emergency CAB - Ban tư vấn thay đổi khẩn cấp
- **RBAC**: Role-Based Access Control - Phân quyền theo vai trò
- **JIT**: Just-In-Time - Cấp quyền tạm thời
- **SoD**: Separation of Duties - Tách biệt trách nhiệm

