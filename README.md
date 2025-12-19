# HỆ THỐNG QUY TRÌNH VÀ QUY ĐỊNH
## Quản trị vận hành, Upcode, Hotfix, Provisioning, Versioning và Release

**Phiên bản**: 2.0 
**Ngày cập nhật**: 2024-12-17

---

## GIỚI THIỆU

Hệ thống Quy trình và Quy định này là bộ tài liệu toàn diện quy định các quy trình quản trị, vận hành và phát triển hệ thống CNTT, được xây dựng dựa trên các chuẩn quốc tế (ITIL, ISO 27001) và thực tiễn tốt nhất trong ngành.

Hệ thống bao gồm:
- **9 quy trình chính**: Quản trị vận hành, Upcode, Hotfix, Provisioning, Versioning, Release, Danh sách Thay đổi Chuẩn, Bổ sung Thay đổi, Rà soát Hệ thống Audit
- **12 checklist**: Hỗ trợ thực hiện từng quy trình
- **16 template và example**: Chuẩn hóa tài liệu và yêu cầu
- **Chính sách Quyền Truy Cập Tối Thiểu**: Đảm bảo bảo mật và tuân thủ
- **Tài liệu hỗ trợ**: Hướng dẫn sử dụng, troubleshooting, training

---

## MỤC ĐÍCH TÀI LIỆU

Hệ thống quy trình này được xây dựng nhằm:

### 1. Đảm bảo chất lượng và an toàn
- **Giảm 70-80% lỗi deployment**: Quy trình kiểm thử đầy đủ, có rollback plan
- **Giảm 80-90% rủi ro bảo mật**: Đánh giá rủi ro, kiểm thử bảo mật, quyền truy cập tối thiểu
- **Tăng 99.9% uptime**: Giám sát proactive, quản lý sự cố hiệu quả
- **Đảm bảo tính nhất quán**: Mọi thay đổi đều tuân thủ quy trình chuẩn

### 2. Tăng hiệu quả và tốc độ
- **Giảm 60-70% thời gian thực hiện**: Quy trình chuẩn hóa, có template và checklist
- **Tăng 50% tốc độ phê duyệt**: Quy trình phê duyệt rõ ràng, phân cấp
- **Giảm 50% thời gian training**: Tài liệu đầy đủ, có ví dụ và hướng dẫn
- **Tăng 40% hiệu quả làm việc**: Mọi người biết rõ vai trò và quy trình

### 3. Tuân thủ và quản lý
- **Tuân thủ chuẩn quốc tế**: ITIL, ISO 27001, GDPR, SOC 2, PCI DSS
- **Tăng tính minh bạch**: Mọi thay đổi đều được ghi nhận và theo dõi
- **Dễ dàng audit**: Tài liệu đầy đủ, có thể kiểm tra và đánh giá
- **Quản lý rủi ro hiệu quả**: Đánh giá và phân loại rủi ro rõ ràng

### 4. Xây dựng văn hóa tổ chức
- **Tăng sự hợp tác**: Quy trình rõ ràng, mọi người biết vai trò
- **Giảm xung đột**: Trách nhiệm rõ ràng, quy trình công bằng
- **Tăng sự tự tin**: Nhân viên biết cách làm đúng, giảm lo lắng
- **Học hỏi liên tục**: Tài liệu được cập nhật dựa trên kinh nghiệm

---

## ĐỐI TƯỢNG ÁP DỤNG

Hệ thống quy trình này áp dụng cho tất cả các đối tượng sau:

### Đối tượng chính

| Đối tượng | Mô tả | Quy trình liên quan |
|-----------|-------|---------------------|
| **Development Team** | Phát triển code, tính năng mới, sửa lỗi | QT-003, QT-004, QT-006, QT-007, QT-008, QT-009 |
| **DevOps Team** | Triển khai, vận hành, tự động hóa, quản lý hạ tầng | QT-002, QT-003, QT-004, QT-005, QT-006, QT-007 |
| **QA Team** | Kiểm thử, đảm bảo chất lượng, test automation | QT-002, QT-003, QT-006, QT-007 |
| **PM/PDM** | Quản lý dự án, phê duyệt thay đổi, quản lý timeline | QT-003, QT-005, QT-007, QT-009 |
| **Ban CLGSP** | Quản lý chất lượng, phê duyệt thay đổi Level 2.0-3.0 | QT-003, QT-009 |
| **Ban KTHT** | Kiểm thử hệ thống, tư vấn kỹ thuật, phê duyệt | QT-003 |
| **Infrastructure Team** | Quản lý hạ tầng, network, server, storage | QT-005 |
| **ECAB** | Phê duyệt thay đổi khẩn cấp (Emergency Change Advisory Board) | QT-004 |
| **Lãnh đạo** | Phê duyệt cấp cao, quyết định chiến lược | QT-003, QT-004 |
| **Product Owner** | Quản lý sản phẩm, roadmap, quyết định tính năng | QT-007 |
| **IT/Security Team** | Quản lý bảo mật, quyền truy cập, audit | Tất cả quy trình (đặc biệt Chính sách Quyền Truy Cập, QT-010) |
| **DBA Team** | Quản lý database, backup, performance | QT-002, QT-003, QT-005 |

### Đối tượng tham khảo

- **Nhân viên mới**: Sử dụng `QUICK_START.md` và `HUONG_DAN_SU_DUNG_NHANH.md`
- **Quản lý cấp cao**: Xem tổng quan và báo cáo trong các quy trình
- **Auditor/Compliance**: Sử dụng tài liệu để đánh giá tuân thủ

---

## PHẠM VI ÁP DỤNG

### 1. Phạm vi hệ thống

Hệ thống quy trình áp dụng cho:

#### 1.1. Môi trường
- **Production**: Môi trường sản xuất chính
- **DR (Disaster Recovery)**: Môi trường dự phòng
- **UAT (User Acceptance Testing)**: Môi trường kiểm thử chấp nhận người dùng
- **Staging**: Môi trường staging/pre-production
- **Development**: Môi trường phát triển (một số quy trình)

#### 1.2. Loại hệ thống
- **Hệ thống Cốt lõi/Trọng điểm**: Hệ thống quan trọng, ảnh hưởng nhiều người dùng
- **Hệ thống Vệ tinh**: Hệ thống hỗ trợ, ảnh hưởng ít người dùng
- **Hệ thống mới**: Hệ thống mới được triển khai
- **Hệ thống legacy**: Hệ thống cũ đang vận hành

#### 1.3. Loại thay đổi
- **Standard Change**: Thay đổi chuẩn (58 loại trong QT-008)
- **Normal Change**: Thay đổi thông thường
- **Emergency Change**: Thay đổi khẩn cấp (Hotfix)

### 2. Phạm vi quy trình

#### 2.1. Quy trình quản trị và vận hành
- **Quản trị vận hành (QT-002)**: Giám sát, log, backup, config, tài nguyên, sự cố
- **Quản lý thay đổi**: Upcode, Hotfix, Release
- **Quản lý tài nguyên**: Provisioning, versioning
- **Quản lý quyền truy cập**: Cấp, thu hồi, rà soát quyền

#### 2.2. Quy trình phát triển
- **Triển khai code**: Upcode (QT-003)
- **Sửa lỗi khẩn cấp**: Hotfix (QT-004)
- **Phát hành sản phẩm**: Release (QT-007)
- **Quản lý phiên bản**: Versioning (QT-006)

#### 2.3. Quy trình hỗ trợ
- **Cung cấp tài nguyên**: Provisioning (QT-005)
- **Tra cứu thay đổi**: Danh sách Thay đổi Chuẩn (QT-008)
- **Bổ sung thay đổi**: Quy trình bổ sung (QT-009)

### 3. Phạm vi tài liệu

#### 3.1. Tài liệu quy trình
- **9 quy trình chính**: QT-002 đến QT-010
- **12 checklist**: CL-001 đến CL-012
- **16 template và example**: TP-001 đến TP-008 (mỗi loại có template và example)

#### 3.2. Tài liệu hỗ trợ
- **Hướng dẫn sử dụng**: QUICK_START, HUONG_DAN_SU_DUNG_NHANH
- **Best Practices**: Chuẩn mực sử dụng
- **Quick Reference**: Tra cứu nhanh thay đổi và quyền truy cập
- **Chính sách**: Chính sách Quyền Truy Cập Tối Thiểu
- **Troubleshooting**: Xử lý vấn đề thường gặp

#### 3.3. Tài liệu quản lý
- **CHANGELOG**: Lịch sử thay đổi hệ thống
- **METADATA_CONFIG**: Quản lý metadata
- **Training**: Hướng dẫn training nhân viên mới

### 4. Phạm vi không áp dụng

Các trường hợp sau **KHÔNG** áp dụng hệ thống quy trình này:
- Thay đổi trên môi trường Development cá nhân (local)
- Thay đổi không ảnh hưởng đến hệ thống (ví dụ: chỉnh sửa tài liệu nội bộ)
- Thay đổi khẩn cấp cực kỳ nghiêm trọng (cần xử lý ngay, tài liệu sau)
- Thay đổi trên hệ thống test/thử nghiệm tạm thời

**Lưu ý**: Ngay cả trong các trường hợp trên, vẫn nên tuân thủ các nguyên tắc cơ bản về bảo mật, ghi log, và quyền truy cập tối thiểu.

---

## BẮT ĐẦU TẠI ĐÂY

### Tôi cần làm gì? → Chọn đúng quy trình

```

 TÔI CẦN LÀM GÌ? 

 
 DEPLOY CODE?
 Lỗi khẩn cấp? → [Hotfix](#hotfix)
 Tính năng mới? → [Upcode](#upcode)
 Release? → [Release](#release)
 
 QUẢN TRỊ VẬN HÀNH? → [Vận hành](#vận-hành)
 
 TẠO TÀI NGUYÊN? → [Provisioning](#provisioning)
 
 CẤP QUYỀN? → [Quyền truy cập](#quyền-truy-cập)
 
 NGƯỜI MỚI? → [Hướng dẫn nhanh](#hướng-dẫn-nhanh)
```

---

## HƯỚNG DẪN NHANH

 **Xem ngay**: [`HUONG_DAN_SU_DUNG_NHANH.md`](HUONG_DAN_SU_DUNG_NHANH.md) - Decision tree, tình huống thường gặp, quy trình tóm tắt

 **Best Practices**: [`BEST_PRACTICES.md`](BEST_PRACTICES.md) - Chuẩn mực sử dụng và quy tắc vàng

---

## CÁC TÌNH HUỐNG THƯỜNG GẶP

### Upcode (Deploy thông thường)

**Đối tượng**: Development Team, DevOps Team, QA Team, PM/PDM, Ban CLGSP, Ban KTHT, Lãnh đạo

**Lợi ích**:
- Giảm 70% lỗi deployment
- Giảm 60% thời gian rollback
- Tăng 50% tốc độ phê duyệt
- Giảm 80% rủi ro bảo mật

**Quy trình nhanh**:
1. Tra cứu mã thay đổi → `QUICK_REFERENCE_THAY_DOI.md` hoặc `QT-008`
2. Tạo RFC → `TP-001-TEMPLATE_RFC.md` (xem `TP-001-EXAMPLE_RFC.md`)
3. Phê duyệt
4. Thực hiện → `QT-003-UPCODE.md` + `CL-002-CHECKLIST_UPCODE.md`

**File cần**:
- Quy trình: `Quy trình (QT-XXX)/QT-003-UPCODE.md`
- Checklist: `Checklist (CL-XXX)/CL-002-CHECKLIST_UPCODE.md`
- Template: `Template (TP-XXX)/TP-001-TEMPLATE_RFC.md`
- Tra cứu: `QUICK_REFERENCE_THAY_DOI.md` hoặc `Quy trình (QT-XXX)/QT-008-DANH_SACH_THAY_DOI_CHUAN.md`

---

### Hotfix (Sửa lỗi khẩn cấp)

**Đối tượng**: Development Team, DevOps Team, ECAB, Lãnh đạo

**Lợi ích**:
- Giảm 90% thời gian xử lý sự cố
- Giảm thiệt hại do downtime
- Bảo vệ danh tiếng
- Đảm bảo chất lượng dù khẩn cấp

**Quy trình nhanh**:
1. Tạo Hotfix Request → `TP-002-TEMPLATE_HOTFIX.md` (xem `TP-002-EXAMPLE_HOTFIX.md`)
2. Phê duyệt khẩn cấp (có thể qua chat/phone)
3. Thực hiện → `QT-004-HOTFIX.md` + `CL-003-CHECKLIST_HOTFIX.md`

**File cần**:
- Quy trình: `Quy trình (QT-XXX)/QT-004-HOTFIX.md`
- Checklist: `Checklist (CL-XXX)/CL-003-CHECKLIST_HOTFIX.md`
- Template: `Template (TP-XXX)/TP-002-TEMPLATE_HOTFIX.md`

---

### Release (Phát hành sản phẩm)

**Đối tượng**: Development Team, DevOps Team, QA Team, PM/PDM, Product Owner

**Lợi ích**:
- Tăng chất lượng release
- Giảm 80% lỗi production
- Tăng sự hài lòng khách hàng
- Tăng tốc độ release

**Quy trình nhanh**:
1. Quản lý version → `QT-006-VERSIONING.md`
2. Tạo Release Note → `TP-003-TEMPLATE_RELEASE_NOTE.md` (xem `TP-003-EXAMPLE_RELEASE_NOTE.md`)
3. Thực hiện release → `QT-007-RELEASE_SAN_PHAM.md` + `CL-005-CHECKLIST_RELEASE.md`
4. Deploy → `QT-003-UPCODE.md`

**File cần**:
- Quy trình: `Quy trình (QT-XXX)/QT-007-RELEASE_SAN_PHAM.md`
- Checklist: `Checklist (CL-XXX)/CL-005-CHECKLIST_RELEASE.md`
- Template: `Template (TP-XXX)/TP-003-TEMPLATE_RELEASE_NOTE.md`
- Versioning: `Quy trình (QT-XXX)/QT-006-VERSIONING.md`

---

### Vận hành (Quản trị vận hành)

**Đối tượng**: DevOps Team, Development Team, QA Team

**Lợi ích**:
- Tăng 99.9% uptime
- Giảm 80% thời gian phục hồi
- Tăng khả năng truy vết
- Tối ưu tài nguyên

**Quy trình nhanh**:
1. Đọc quy trình → `QT-002-QUAN_TRI_VAN_HANH.md`
2. Sử dụng checklist → `CL-001-CHECKLIST_VAN_HANH.md`

**File cần**:
- Quy trình: `Quy trình (QT-XXX)/QT-002-QUAN_TRI_VAN_HANH.md`
- Checklist: `Checklist (CL-XXX)/CL-001-CHECKLIST_VAN_HANH.md`

---

### Provisioning (Tạo tài nguyên)

**Đối tượng**: DevOps Team, Infrastructure Team, Development Team, PM/PDM

**Lợi ích**:
- Giảm 70% thời gian cung cấp
- Giảm 60% lỗi cấu hình
- Tối ưu chi phí
- Bảo mật từ đầu

**Quy trình nhanh**:
1. Tạo Provisioning Request → `TP-004-TEMPLATE_PROVISIONING.md` (xem `TP-004-EXAMPLE_PROVISIONING.md`)
2. Phê duyệt
3. Thực hiện → `QT-005-PROVISIONING.md` + `CL-004-CHECKLIST_PROVISIONING.md`

**File cần**:
- Quy trình: `Quy trình (QT-XXX)/QT-005-PROVISIONING.md`
- Checklist: `Checklist (CL-XXX)/CL-004-CHECKLIST_PROVISIONING.md`
- Template: `Template (TP-XXX)/TP-004-TEMPLATE_PROVISIONING.md`

---

### Quyền truy cập

**Quy trình nhanh**:
1. Tra cứu quyền → `QUICK_REFERENCE_QUYEN_TRUY_CAP.md`
2. Tạo yêu cầu → `Template (TP-XXX)/TP-006-TEMPLATE_YEU_CAU_CAP_QUYEN.md`
3. Phê duyệt và cấp quyền → `Checklist (CL-XXX)/CL-011-CHECKLIST_QUYEN_TRUY_CAP.md`

**File cần**:
- Quick Reference: `QUICK_REFERENCE_QUYEN_TRUY_CAP.md` 
- Template: `Template (TP-XXX)/TP-006-TEMPLATE_YEU_CAU_CAP_QUYEN.md`
- Checklist: `Checklist (CL-XXX)/CL-011-CHECKLIST_QUYEN_TRUY_CAP.md`
- Hướng dẫn: `Hỗ trợ (Support)/HUONG_DAN_SU_DUNG_QUYEN_TRUY_CAP.md`
- Chính sách: `CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU.md`

---

## CẤU TRÚC FOLDER

```
QT/
 README.md FILE NÀY - Bắt đầu tại đây

 HUONG_DAN_SU_DUNG_NHANH.md Hướng dẫn sử dụng nhanh
 BEST_PRACTICES.md Chuẩn mực sử dụng

 Quy trình (QT-XXX)/
 QT-002-QUAN_TRI_VAN_HANH.md
 QT-003-UPCODE.md
 QT-004-HOTFIX.md
 QT-005-PROVISIONING.md
 QT-006-VERSIONING.md
 QT-007-RELEASE_SAN_PHAM.md
 QT-008-DANH_SACH_THAY_DOI_CHUAN.md (58 loại)
 QT-009-QUY_TRINH_BO_SUNG_THAY_DOI.md
 QT-010-RA_SOAT_HE_THONG_AUDIT.md 

 Checklist (CL-XXX)/
 CL-001 đến CL-012 (12 checklist)

 Template (TP-XXX)/
 TP-001 đến TP-008 (8 template + 8 example)

 Hỗ trợ (Support)/
 QUICK_START.md
 HUONG_DAN_SU_DUNG_QUYEN_TRUY_CAP.md
 TROUBLESHOOTING.md
 CHANGELOG.md
 ...

 QUICK_REFERENCE_THAY_DOI.md Tra cứu nhanh
 QUICK_REFERENCE_QUYEN_TRUY_CAP.md Tra cứu nhanh
 CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU.md
```

---

## DANH SÁCH QUY TRÌNH

| Mã | Tên | File | Mô tả | Đối tượng chính |
|----|-----|------|-------|-----------------|
| **QT-002** | Quản trị Vận hành | `Quy trình (QT-XXX)/QT-002-QUAN_TRI_VAN_HANH.md` | Giám sát, log, backup, config | DevOps, Development, QA |
| **QT-003** | Upcode | `Quy trình (QT-XXX)/QT-003-UPCODE.md` | Triển khai code lên môi trường | Development, DevOps, QA, PM/PDM, Ban CLGSP, Ban KTHT |
| **QT-004** | Hotfix | `Quy trình (QT-XXX)/QT-004-HOTFIX.md` | Sửa lỗi khẩn cấp | Development, DevOps, ECAB, Lãnh đạo |
| **QT-005** | Provisioning | `Quy trình (QT-XXX)/QT-005-PROVISIONING.md` | Cung cấp tài nguyên | DevOps, Infrastructure, Development, PM/PDM |
| **QT-006** | Versioning | `Quy trình (QT-XXX)/QT-006-VERSIONING.md` | Quản lý phiên bản | Development, DevOps, QA |
| **QT-007** | Release | `Quy trình (QT-XXX)/QT-007-RELEASE_SAN_PHAM.md` | Phát hành sản phẩm | Development, DevOps, QA, PM/PDM, Product Owner |
| **QT-008** | Danh sách Thay đổi Chuẩn | `Quy trình (QT-XXX)/QT-008-DANH_SACH_THAY_DOI_CHUAN.md` | 58 loại thay đổi | Tất cả các team |
| **QT-009** | Bổ sung Thay đổi | `Quy trình (QT-XXX)/QT-009-QUY_TRINH_BO_SUNG_THAY_DOI.md` | Bổ sung thay đổi mới | Development, DevOps, PM/PDM, Ban CLGSP, Ban KTHT |
| **QT-010** | Rà soát Hệ thống Audit | `Quy trình (QT-XXX)/QT-010-RA_SOAT_HE_THONG_AUDIT.md` | Rà soát hệ thống khi cần audit | IT/Security Team, IT Manager, Ban CLGSP, Auditor |

---

## CHECKLIST VÀ TEMPLATE

### Checklist (12 file)

| Mã | Tên | File |
|----|-----|------|
| **CL-001** | Vận hành | `Checklist (CL-XXX)/CL-001-CHECKLIST_VAN_HANH.md` |
| **CL-002** | Upcode | `Checklist (CL-XXX)/CL-002-CHECKLIST_UPCODE.md` |
| **CL-003** | Hotfix | `Checklist (CL-XXX)/CL-003-CHECKLIST_HOTFIX.md` |
| **CL-004** | Provisioning | `Checklist (CL-XXX)/CL-004-CHECKLIST_PROVISIONING.md` |
| **CL-005** | Release | `Checklist (CL-XXX)/CL-005-CHECKLIST_RELEASE.md` |
| **CL-006** | Tra Cứu Thay Đổi | `Checklist (CL-XXX)/CL-006-TRA_CUU_THAY_DOI.md` |
| **CL-007-010** | Nhóm A/B/C/D | `Checklist (CL-XXX)/CL-007 đến CL-010` |
| **CL-011** | Quyền Truy Cập | `Checklist (CL-XXX)/CL-011-CHECKLIST_QUYEN_TRUY_CAP.md` |
| **CL-012** | Rà soát Hệ thống | `Checklist (CL-XXX)/CL-012-CHECKLIST_RA_SOAT_HE_THONG.md` |

### Template (8 template + 8 example)

| Mã | Tên | Template | Example |
|----|-----|----------|---------|
| **TP-001** | RFC | `Template (TP-XXX)/TP-001-TEMPLATE_RFC.md` | `TP-001-EXAMPLE_RFC.md` |
| **TP-002** | Hotfix | `Template (TP-XXX)/TP-002-TEMPLATE_HOTFIX.md` | `TP-002-EXAMPLE_HOTFIX.md` |
| **TP-003** | Release Note | `Template (TP-XXX)/TP-003-TEMPLATE_RELEASE_NOTE.md` | `TP-003-EXAMPLE_RELEASE_NOTE.md` |
| **TP-004** | Provisioning | `Template (TP-XXX)/TP-004-TEMPLATE_PROVISIONING.md` | `TP-004-EXAMPLE_PROVISIONING.md` |
| **TP-005** | Tra Cứu | `Template (TP-XXX)/TP-005-TEMPLATE_TRA_CUU_THAY_DOI.md` | `TP-005-EXAMPLE_TRA_CUU_THAY_DOI.md` |
| **TP-006** | Cấp Quyền | `Template (TP-XXX)/TP-006-TEMPLATE_YEU_CAU_CAP_QUYEN.md` | `TP-006-EXAMPLE_YEU_CAU_CAP_QUYEN.md` |
| **TP-007** | Báo cáo Rà soát | `Template (TP-XXX)/TP-007-TEMPLATE_BAO_CAO_RA_SOAT.md` | `TP-007-EXAMPLE_BAO_CAO_RA_SOAT.md` |
| **TP-008** | Kế hoạch Hành động | `Template (TP-XXX)/TP-008-TEMPLATE_KE_HOACH_HANH_DONG.md` | `TP-008-EXAMPLE_KE_HOACH_HANH_DONG.md` |

---

## QUICK REFERENCE

### Tra cứu nhanh

- **Thay đổi**: [`QUICK_REFERENCE_THAY_DOI.md`](QUICK_REFERENCE_THAY_DOI.md) - Bảng tra cứu 58 loại thay đổi
- **Quyền truy cập**: [`QUICK_REFERENCE_QUYEN_TRUY_CAP.md`](QUICK_REFERENCE_QUYEN_TRUY_CAP.md) - Bảng tra cứu quyền theo vai trò

---

## HỖ TRỢ

### Folder "Hỗ trợ (Support)"

| File | Mục đích |
|------|----------|
| **QUICK_START.md** | Hướng dẫn nhanh cho người mới |
| **HUONG_DAN_SU_DUNG_QUYEN_TRUY_CAP.md** | Hướng dẫn quyền truy cập |
| **TROUBLESHOOTING.md** | Xử lý vấn đề thường gặp |
| **CHANGELOG.md** | Lịch sử thay đổi hệ thống |
| **HUONG_DAN_CHANGELOG.md** | Hướng dẫn CHANGELOG cho sản phẩm |
| **METADATA_CONFIG.md** | Quản lý metadata |

 **Xem chi tiết**: [`Hỗ trợ (Support)/README.md`](Hỗ%20trợ%20(Support)/README.md)

---

## QUY TẮC VÀNG

1. **Luôn bắt đầu với Quick Reference** - Tra cứu nhanh trước
2. **Luôn sử dụng Template** - Không tự tạo format
3. **Luôn sử dụng Checklist** - Không bỏ sót bước
4. **Luôn đọc quy trình** - Hiểu rõ trước khi thực hiện
5. **Luôn ghi log** - Mọi thao tác đều được ghi log

 **Xem chi tiết**: [`BEST_PRACTICES.md`](BEST_PRACTICES.md)

---

## MỐI QUAN HỆ QUY TRÌNH

```
Release: QT-006 (Versioning) → QT-007 (Release) → QT-003 (Upcode) → QT-002 (Vận hành)
Hotfix: QT-002 (Phát hiện) → QT-004 (Hotfix) → QT-006 (Versioning) → QT-002 (Vận hành)
Provisioning: QT-005 → QT-002 (Vận hành)
```

---

## TÌM KIẾM NHANH

### Tôi cần...

- **Deploy code** → Xem [Upcode](#-upcode-deploy-thông-thường)
- **Sửa lỗi khẩn cấp** → Xem [Hotfix](#-hotfix-sửa-lỗi-khẩn-cấp)
- **Release sản phẩm** → Xem [Release](#-release-phát-hành-sản-phẩm)
- **Tra cứu thay đổi** → `QUICK_REFERENCE_THAY_DOI.md`
- **Cấp quyền** → Xem [Quyền truy cập](#-quyền-truy-cập)
- **Tạo tài nguyên** → Xem [Provisioning](#-provisioning-tạo-tài-nguyên)
- **Hướng dẫn chi tiết** → `HUONG_DAN_SU_DUNG_NHANH.md`
- **Best Practices** → `BEST_PRACTICES.md`
- **Gặp vấn đề** → `Hỗ trợ (Support)/TROUBLESHOOTING.md`

---

## TÀI LIỆU QUAN TRỌNG NHẤT

### Cho mọi người

1. **README.md** (File này) - Bắt đầu tại đây 
2. **HUONG_DAN_SU_DUNG_NHANH.md** - Hướng dẫn sử dụng nhanh 
3. **BEST_PRACTICES.md** - Chuẩn mực sử dụng 

### Cho Developer/DevOps

1. **QUICK_REFERENCE_THAY_DOI.md** - Tra cứu nhanh
2. **QUICK_REFERENCE_QUYEN_TRUY_CAP.md** - Tra cứu quyền
3. **Template và Example** - Trong folder `Template (TP-XXX)`

### Cho PM/PDM

1. **QT-007-RELEASE_SAN_PHAM.md** - Quy trình release
2. **QT-008-DANH_SACH_THAY_DOI_CHUAN.md** - Danh sách thay đổi
3. **TP-003-TEMPLATE_RELEASE_NOTE.md** - Template release note

### Cho IT/Security

1. **CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU.md** - Chính sách đầy đủ
2. **QUICK_REFERENCE_QUYEN_TRUY_CAP.md** - Tra cứu nhanh
3. **Hỗ trợ (Support)/HUONG_DAN_SU_DUNG_QUYEN_TRUY_CAP.md** - Hướng dẫn

---

**Phiên bản**: 2.0 
**Ngày cập nhật**: 2024-12-17

