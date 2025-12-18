# TP-008: EXAMPLE KẾ HOẠCH HÀNH ĐỘNG

**Mã template**: TP-008 
**Tham chiếu quy trình**: QT-010

> **Lưu ý**: Đây là file example, chỉ để tham khảo. Khi tạo kế hoạch hành động thực tế, sử dụng `TP-008-TEMPLATE_KE_HOACH_HANH_DONG.md`.

---

## THÔNG TIN CHUNG

- **Kế hoạch ID**: ACTION-2024-12-17-001
- **Ngày tạo**: 2024-12-17
- **Người tạo**: Phạm Văn D
- **Email**: phamvand@company.com
- **Điện thoại**: 0123456789
- **Phòng ban**: IT Manager
- **Báo cáo rà soát liên quan**: AUDIT-2024-12-17-001

---

## 1. TỔNG QUAN

### 1.1. Mục đích kế hoạch

Khắc phục các vấn đề phát hiện trong rà soát hệ thống CNTT quý 4/2024, đảm bảo hệ thống tuân thủ đầy đủ chính sách và quy trình, nâng cao mức độ tuân thủ từ 85% lên >95%.

### 1.2. Phạm vi

**Vấn đề cần khắc phục**: 12 vấn đề

**Phân loại**:
- **Critical**: 1 vấn đề
- **High**: 3 vấn đề
- **Medium**: 5 vấn đề
- **Low**: 3 vấn đề

**Hệ thống/Quy trình ảnh hưởng**: 
- Production servers
- Database servers
- Cloud IAM
- Quy trình Upcode (QT-003)
- Quy trình cấp quyền
- Quy trình Provisioning (QT-005)

### 1.3. Thời gian

- **Thời gian bắt đầu**: 2024-12-18
- **Thời gian kết thúc dự kiến**: 2025-01-17
- **Thời hạn**: 30 ngày

---

## 2. DANH SÁCH VẤN ĐỀ VÀ KẾ HOẠCH KHẮC PHỤC

### 2.1. Vấn đề Critical

#### Vấn đề #1: Tài khoản admin chưa có MFA

**Thông tin vấn đề**:
- **Mô tả**: 3 tài khoản admin (admin01, admin02, admin03) chưa kích hoạt MFA
- **Mức độ nghiêm trọng**: Critical
- **Nguyên nhân**: Tài khoản được tạo trước khi có yêu cầu MFA bắt buộc
- **Tác động**: Rủi ro bảo mật nghiêm trọng, nếu tài khoản bị xâm nhập có thể truy cập toàn bộ hệ thống
- **Hệ thống/Quy trình ảnh hưởng**: 
 - Production servers
 - Database servers
 - Cloud IAM

**Kế hoạch khắc phục**:
- **Mục tiêu**: Kích hoạt MFA cho 100% tài khoản admin trong 24 giờ
- **Giải pháp**: 
 1. Kích hoạt MFA cho 3 tài khoản admin ngay lập tức
 2. Rà soát tất cả tài khoản admin để đảm bảo 100% có MFA
 3. Cập nhật quy trình cấp quyền để bắt buộc MFA cho tài khoản admin
- **Các bước thực hiện**:
 1. Liên hệ với 3 người sở hữu tài khoản để kích hoạt MFA
 2. Hướng dẫn họ cách kích hoạt MFA
 3. Kiểm tra và xác nhận MFA đã được kích hoạt
 4. Rà soát tất cả tài khoản admin khác
 5. Cập nhật quy trình cấp quyền
- **Người chịu trách nhiệm**: Lê Văn C (Security Team)
- **Team hỗ trợ**: 
 - Nguyễn Văn A (IT/Security Team)
 - Trần Thị B (IT Team)
- **Thời hạn**: 24 giờ
- **Ngày bắt đầu**: 2024-12-18
- **Ngày hoàn thành dự kiến**: 2024-12-19
- **Trạng thái**: Chưa bắt đầu
- **Ghi chú**: Ưu tiên cao nhất, cần hoàn thành ngay lập tức

### 2.2. Vấn đề High

#### Vấn đề #2: Deployment không có rollback plan

**Thông tin vấn đề**:
- **Mô tả**: 5 deployment trong tháng 12 không có rollback plan được ghi nhận trong RFC
- **Mức độ nghiêm trọng**: High
- **Nguyên nhân**: Team quên điền phần rollback plan trong RFC
- **Tác động**: Nếu deployment thất bại, không có kế hoạch rollback rõ ràng, có thể gây downtime kéo dài
- **Hệ thống/Quy trình ảnh hưởng**: 
 - Production deployments
 - Quy trình Upcode (QT-003)

**Kế hoạch khắc phục**:
- **Mục tiêu**: Đảm bảo 100% deployment có rollback plan được ghi nhận
- **Giải pháp**: 
 1. Bổ sung rollback plan cho 5 deployment đã thực hiện (retrospective)
 2. Cập nhật checklist (CL-002) để bắt buộc rollback plan
 3. Training team về tầm quan trọng của rollback plan
- **Các bước thực hiện**:
 1. Review 5 deployment đã thực hiện và bổ sung rollback plan
 2. Cập nhật CL-002 để bắt buộc rollback plan
 3. Tổ chức training cho team về rollback plan
 4. Kiểm tra các deployment tiếp theo có rollback plan
- **Người chịu trách nhiệm**: Trần Thị B (IT Team)
- **Team hỗ trợ**: 
 - Nguyễn Văn A (IT/Security Team)
 - DevOps Team
- **Thời hạn**: 7 ngày
- **Ngày bắt đầu**: 2024-12-20
- **Ngày hoàn thành dự kiến**: 2024-12-27
- **Trạng thái**: Chưa bắt đầu
- **Ghi chú**: Cần hoàn thành trong tuần đầu tiên

#### Vấn đề #3: Quyền tạm thời đã hết hạn chưa được thu hồi

**Thông tin vấn đề**:
- **Mô tả**: 8 quyền tạm thời đã hết hạn từ 7-30 ngày nhưng chưa được thu hồi
- **Mức độ nghiêm trọng**: High
- **Nguyên nhân**: Hệ thống tự động thu hồi quyền chưa hoạt động đúng
- **Tác động**: Quyền dư thừa có thể bị lạm dụng, vi phạm nguyên tắc Least Privilege
- **Hệ thống/Quy trình ảnh hưởng**: 
 - IAM system
 - Quy trình cấp quyền

**Kế hoạch khắc phục**:
- **Mục tiêu**: Thu hồi tất cả quyền đã hết hạn và sửa hệ thống tự động thu hồi
- **Giải pháp**: 
 1. Thu hồi ngay 8 quyền đã hết hạn
 2. Kiểm tra và sửa hệ thống tự động thu hồi quyền
 3. Rà soát tất cả quyền tạm thời để đảm bảo auto-revoke hoạt động
- **Các bước thực hiện**:
 1. Thu hồi ngay 8 quyền đã hết hạn
 2. Kiểm tra hệ thống tự động thu hồi quyền
 3. Sửa lỗi hệ thống (nếu có)
 4. Test hệ thống tự động thu hồi
 5. Rà soát tất cả quyền tạm thời
- **Người chịu trách nhiệm**: Nguyễn Văn A (IT/Security Team)
- **Team hỗ trợ**: 
 - Lê Văn C (Security Team)
 - DevOps Team
- **Thời hạn**: 7 ngày
- **Ngày bắt đầu**: 2024-12-20
- **Ngày hoàn thành dự kiến**: 2024-12-27
- **Trạng thái**: Chưa bắt đầu
- **Ghi chú**: Cần hoàn thành trong tuần đầu tiên

#### Vấn đề #4: Thiếu ghi nhận deployment

**Thông tin vấn đề**:
- **Mô tả**: 3 deployment không có ghi nhận đầy đủ (thiếu timestamp, người thực hiện, hoặc kết quả)
- **Mức độ nghiêm trọng**: High
- **Nguyên nhân**: Team quên ghi nhận, hoặc hệ thống ghi log không hoạt động
- **Tác động**: Không thể truy vết deployment, khó khăn trong audit và troubleshooting
- **Hệ thống/Quy trình ảnh hưởng**: 
 - Production deployments
 - Audit trail

**Kế hoạch khắc phục**:
- **Mục tiêu**: Bổ sung ghi nhận cho 3 deployment và sửa hệ thống ghi log
- **Giải pháp**: 
 1. Bổ sung ghi nhận cho 3 deployment (nếu có thể)
 2. Kiểm tra và sửa hệ thống ghi log
 3. Training team về tầm quan trọng của ghi nhận
- **Các bước thực hiện**:
 1. Review 3 deployment và bổ sung ghi nhận
 2. Kiểm tra hệ thống ghi log
 3. Sửa lỗi hệ thống (nếu có)
 4. Test hệ thống ghi log
 5. Training team về ghi nhận
- **Người chịu trách nhiệm**: Trần Thị B (IT Team)
- **Team hỗ trợ**: 
 - Nguyễn Văn A (IT/Security Team)
 - DevOps Team
- **Thời hạn**: 7 ngày
- **Ngày bắt đầu**: 2024-12-20
- **Ngày hoàn thành dự kiến**: 2024-12-27
- **Trạng thái**: Chưa bắt đầu
- **Ghi chú**: Cần hoàn thành trong tuần đầu tiên

### 2.3. Vấn đề Medium

#### Vấn đề #5: Tài liệu quy trình chưa được cập nhật

**Thông tin vấn đề**:
- **Mô tả**: 2 quy trình (QT-003, QT-005) có thay đổi trong thực tế nhưng tài liệu chưa được cập nhật
- **Mức độ nghiêm trọng**: Medium
- **Nguyên nhân**: Thay đổi quy trình không được cập nhật vào tài liệu
- **Tác động**: Tài liệu không phản ánh đúng quy trình thực tế, gây nhầm lẫn cho người dùng
- **Hệ thống/Quy trình ảnh hưởng**: 
 - QT-003 (Upcode)
 - QT-005 (Provisioning)

**Kế hoạch khắc phục**:
- **Mục tiêu**: Cập nhật tài liệu QT-003 và QT-005 để phản ánh đúng quy trình thực tế
- **Giải pháp**: 
 1. Cập nhật tài liệu QT-003 và QT-005
 2. Thiết lập quy trình cập nhật tài liệu khi có thay đổi
 3. Rà soát định kỳ tài liệu để đảm bảo đồng bộ
- **Các bước thực hiện**:
 1. So sánh tài liệu với quy trình thực tế
 2. Cập nhật tài liệu QT-003
 3. Cập nhật tài liệu QT-005
 4. Thiết lập quy trình cập nhật tài liệu
 5. Rà soát định kỳ
- **Người chịu trách nhiệm**: Phạm Văn D (IT Manager)
- **Team hỗ trợ**: 
 - Nguyễn Văn A (IT/Security Team)
 - Trần Thị B (IT Team)
- **Thời hạn**: 14 ngày
- **Ngày bắt đầu**: 2024-12-28
- **Ngày hoàn thành dự kiến**: 2025-01-11
- **Trạng thái**: Chưa bắt đầu
- **Ghi chú**: Có thể thực hiện song song với các vấn đề High

[Lặp lại cho các vấn đề Medium khác...]

### 2.4. Vấn đề Low

#### Vấn đề #12: Checklist không được sử dụng đầy đủ

**Thông tin vấn đề**:
- **Mô tả**: Một số team không sử dụng checklist đầy đủ, bỏ qua một số bước
- **Mức độ nghiêm trọng**: Low
- **Nguyên nhân**: Team chưa hiểu rõ tầm quan trọng của checklist, hoặc checklist quá dài
- **Tác động**: Có thể bỏ sót các bước quan trọng, nhưng chưa gây ra sự cố nghiêm trọng
- **Hệ thống/Quy trình ảnh hưởng**: 
 - Tất cả quy trình

**Kế hoạch khắc phục**:
- **Mục tiêu**: Tăng tỷ lệ sử dụng checklist đầy đủ lên >95%
- **Giải pháp**: 
 1. Training team về tầm quan trọng của checklist
 2. Rà soát và tối ưu checklist để ngắn gọn hơn
 3. Tích hợp checklist vào hệ thống để bắt buộc sử dụng
- **Các bước thực hiện**:
 1. Tổ chức training cho team về checklist
 2. Rà soát tất cả checklist
 3. Tối ưu checklist (nếu cần)
 4. Tích hợp checklist vào hệ thống (nếu có thể)
 5. Monitor việc sử dụng checklist
- **Người chịu trách nhiệm**: Phạm Văn D (IT Manager)
- **Team hỗ trợ**: 
 - Tất cả team
- **Thời hạn**: 30 ngày
- **Ngày bắt đầu**: 2025-01-01
- **Ngày hoàn thành dự kiến**: 2025-01-31
- **Trạng thái**: Chưa bắt đầu
- **Ghi chú**: Có thể thực hiện trong tháng tiếp theo

---

## 3. THEO DÕI TIẾN ĐỘ

### 3.1. Tổng hợp tiến độ

**Tổng số vấn đề**: 12

**Trạng thái**:
- **Chưa bắt đầu**: 12 vấn đề
- **Đang thực hiện**: 0 vấn đề
- **Hoàn thành**: 0 vấn đề
- **Đã đóng**: 0 vấn đề

**Tiến độ**: 0%

### 3.2. Tiến độ theo mức độ nghiêm trọng

**Critical**:
- Tổng: 1 vấn đề
- Hoàn thành: 0 vấn đề
- Tiến độ: 0%

**High**:
- Tổng: 3 vấn đề
- Hoàn thành: 0 vấn đề
- Tiến độ: 0%

**Medium**:
- Tổng: 5 vấn đề
- Hoàn thành: 0 vấn đề
- Tiến độ: 0%

**Low**:
- Tổng: 3 vấn đề
- Hoàn thành: 0 vấn đề
- Tiến độ: 0%

### 3.3. Lịch trình

| Vấn đề | Mức độ | Người chịu trách nhiệm | Ngày bắt đầu | Ngày hoàn thành dự kiến | Trạng thái |
|--------|--------|------------------------|--------------|-------------------------|------------|
| #1 | Critical | Lê Văn C | 2024-12-18 | 2024-12-19 | Chưa bắt đầu |
| #2 | High | Trần Thị B | 2024-12-20 | 2024-12-27 | Chưa bắt đầu |
| #3 | High | Nguyễn Văn A | 2024-12-20 | 2024-12-27 | Chưa bắt đầu |
| #4 | High | Trần Thị B | 2024-12-20 | 2024-12-27 | Chưa bắt đầu |
| #5 | Medium | Phạm Văn D | 2024-12-28 | 2025-01-11 | Chưa bắt đầu |
| ... | ... | ... | ... | ... | ... |
| #12 | Low | Phạm Văn D | 2025-01-01 | 2025-01-31 | Chưa bắt đầu |

---

## 4. BÁO CÁO ĐỊNH KỲ

### 4.1. Tần suất báo cáo

- **Critical**: Hàng ngày
- **High**: Hàng tuần
- **Medium**: Hàng tháng
- **Low**: Hàng quý

### 4.2. Báo cáo tiến độ

**Ngày báo cáo**: [Sẽ cập nhật khi có tiến độ]

**Tiến độ**:
- Tổng số vấn đề: 12
- Đã hoàn thành: 0
- Đang thực hiện: 0
- Chưa bắt đầu: 12
- Tiến độ: 0%

---

## 5. KẾT QUẢ VÀ ĐÁNH GIÁ

### 5.1. Kết quả khắc phục

[Sẽ cập nhật sau khi hoàn thành]

### 5.2. Đánh giá hiệu quả

[Sẽ cập nhật sau khi hoàn thành]

### 5.3. Khuyến nghị

[Sẽ cập nhật sau khi hoàn thành]

---

## PHỤ LỤC

### A. Tài liệu tham khảo

- `AUDIT-2024-12-17-001` - Báo cáo rà soát hệ thống quý 4/2024
- `QT-010-RA_SOAT_HE_THONG_AUDIT.md`
- `CL-012-CHECKLIST_RA_SOAT_HE_THONG.md`

### B. Bằng chứng khắc phục

[Sẽ cập nhật khi có bằng chứng]

### C. Danh sách người tham gia

- Phạm Văn D - IT Manager (Người tạo kế hoạch)
- Lê Văn C - Security Team (Chịu trách nhiệm vấn đề Critical)
- Nguyễn Văn A - IT/Security Team (Chịu trách nhiệm vấn đề High)
- Trần Thị B - IT Team (Chịu trách nhiệm vấn đề High)
- Hoàng Thị E - Ban CLGSP (Người phê duyệt)

---

**Phiên bản**: 1.0 
**Ngày ban hành**: 2024-12-17 
**Người soạn**: Phạm Văn D 
**Trạng thái**: Example
