# CHANGELOG
## Lịch sử thay đổi của Hệ thống Quy trình và Quy định

Tất cả các thay đổi quan trọng của hệ thống quy trình sẽ được ghi lại trong file này.

Format dựa trên [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
và tuân thủ [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- File example cho tất cả template (TP-001 đến TP-006)
- Folder "Hỗ trợ (Support)" với các file hỗ trợ
- METADATA_CONFIG.md để quản lý metadata tập trung
- CHANGELOG.md để theo dõi thay đổi
- QUICK_START.md hướng dẫn nhanh cho người mới
- TROUBLESHOOTING.md hướng dẫn xử lý vấn đề
- HUONG_DAN_SU_DUNG_QUYEN_TRUY_CAP.md (tổng hợp từ PHUONG_PHAP_THUC_HIEN_NHANH và HUONG_DAN_SU_DUNG_QUYEN_TRUY_CAP_TRONG_QUY_TRINH)
- TP-006-EXAMPLE_YEU_CAU_CAP_QUYEN.md - Example cho template yêu cầu cấp quyền
- Phần 3.10 - Cơ chế kiểm soát toàn diện trong CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU.md
- Phần 9.4 - Dashboard và Báo cáo trong CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU.md
- Phần 19 - Tổng hợp cơ chế kiểm soát trong CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU.md

### Changed
- Cập nhật README.md với section về file Example
- Cải thiện template TP-003 (Release Note) cho Agile (v2.0)
  - Thêm Git version information
  - Thêm Docker image information
  - Thêm Testing Results và Performance Metrics (kiến nghị)
  - Tối ưu cho quy trình Agile
- Tổ chức lại folder QT: Gộp README_QUY_TRINH.md và QT-001 vào README.md
- Loại bỏ thông tin thời gian không cần thiết trong tất cả file
- Rút gọn và tối ưu folder "Hỗ trợ (Support)"
- Cập nhật CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU.md lên phiên bản 3.0
  - Bổ sung phần 1.1-1.4: Tại sao quan trọng, Rủi ro, Số liệu, FAQ
  - Bổ sung phần 3.1.1: Định nghĩa "đủ quyền" chi tiết
  - Bổ sung phần 3.7.1: Ghi nhận (Logging) ra sao
  - Bổ sung phần 3.9: Cách thức thực hiện và Ai thực hiện
  - Bổ sung phần 3.10: Cơ chế kiểm soát toàn diện
  - Bổ sung phần 9.4: Dashboard và Báo cáo
  - Bổ sung phần 19: Tổng hợp cơ chế kiểm soát
  - Loại bỏ phần 1.3: CASE STUDIES VÀ BÀI HỌC
- Cập nhật CL-011-CHECKLIST_QUYEN_TRUY_CAP.md lên phiên bản 2.0
- Cập nhật HUONG_DAN_SU_DUNG_QUYEN_TRUY_CAP.md lên phiên bản 2.0
- Cập nhật QT-003-UPCODE.md lên phiên bản 2.0

### Removed
- README_QUY_TRINH.md (gộp vào README.md)
- QT-001-QUY_TRINH_TONG_HOP.md (gộp vào README.md)
- DASHBOARD_THAY_DOI.md (không cần thiết)
- PHUONG_PHAP_THUC_HIEN_NHANH_QUYEN_TRUY_CAP.md (gộp vào HUONG_DAN_SU_DUNG_QUYEN_TRUY_CAP.md)
- HUONG_DAN_SU_DUNG_QUYEN_TRUY_CAP_TRONG_QUY_TRINH.md (gộp vào HUONG_DAN_SU_DUNG_QUYEN_TRUY_CAP.md)
- BAO_CAO_DANH_GIA_TONG_THE.md (gộp vào DANH_GIA_VA_BAO_CAO.md)
- DANH_GIA_CHINH_SACH_QUYEN_TRUY_CAP.md (gộp vào DANH_GIA_VA_BAO_CAO.md)
- DANH_GIA_MOI_TUONG_QUAN_QUYEN_TRUY_CAP.md (gộp vào DANH_GIA_VA_BAO_CAO.md)
- REVIEW_TONG_THE_VA_HUONG_DAN.md (gộp vào DANH_GIA_VA_BAO_CAO.md)
- Phần 1.3 - CASE STUDIES VÀ BÀI HỌC trong CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU.md
- BAO_CAO_RA_SOAT_CHAT_LUONG.md (file báo cáo tạm thời, đã xóa)
- REVIEW_TONG_THE.md (file báo cáo tạm thời, đã xóa)
- RA_SOAT_TONG_THE_TOAN_BO.md (file báo cáo tạm thời, đã xóa)

### Fixed
- Sửa sơ đồ mối quan hệ file trong README.md
- Cập nhật tất cả tham chiếu đến file đã xóa/gộp
- Sửa tham chiếu đến file không tồn tại (DANH_GIA_VA_BAO_CAO.md) trong README.md và Hỗ trợ (Support)/README.md
- Sửa số thứ tự phần trong CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU.md (phần 20.1, 22)

---

## [1.0.0] - 2024-12-17

### Added

#### Quy trình (QT-XXX)
- README.md (thay thế QT-001): Quy trình Tổng hợp
- QT-002: Quy trình Quản trị Vận hành
- QT-003: Quy trình Upcode
  - Phân loại hệ thống (Cốt lõi/Vệ tinh)
  - Bảng RACI chi tiết
  - Quy trình xử lý ngoại lệ
  - Quy định về quyền truy cập tối thiểu
- QT-004: Quy trình Hotfix
- QT-005: Quy trình Provisioning
- QT-006: Quy trình Versioning
- QT-007: Quy trình Release Sản phẩm
- QT-008: Danh sách Thay đổi Chuẩn (58 loại)
- QT-009: Quy trình Bổ sung Thay đổi

#### Checklist (CL-XXX)
- CL-001: Checklist Vận hành
- CL-002: Checklist Upcode
- CL-003: Checklist Hotfix
- CL-004: Checklist Provisioning
- CL-005: Checklist Release
- CL-006: Checklist Tra Cứu Thay Đổi
- CL-007: Checklist Nhóm A (Hạ tầng)
- CL-008: Checklist Nhóm B (Ứng dụng)
- CL-009: Checklist Nhóm C (Dữ liệu)
- CL-010: Checklist Nhóm D (Sự cố)
- CL-011: Checklist Quyền Truy Cập

#### Template (TP-XXX)
- TP-001: Template RFC (Request for Change)
- TP-002: Template Hotfix Request
- TP-003: Template Release Note (v1.0, sau nâng cấp lên v2.0)
- TP-004: Template Provisioning Request
- TP-005: Template Tra Cứu Thay Đổi
- TP-006: Template Yêu Cầu Cấp Quyền

#### Tài liệu hỗ trợ
- README.md: Hướng dẫn sử dụng tổng quan
- QUICK_REFERENCE_THAY_DOI.md: Bảng tra cứu nhanh
- HUONG_DAN_TRAINING.md: Hướng dẫn training
- CHÍNH SÁCH QUYỀN TRUY CẬP TỐI THIỂU.md: Chính sách quyền truy cập

### Features
- Hệ thống phân loại thay đổi với 58 loại chuẩn
- Đánh giá rủi ro với ma trận rủi ro
- Quy trình phê duyệt theo cấp độ (Level 1.0 - 4.0)
- Quy trình xử lý ngoại lệ
- Quy trình bổ sung thay đổi mới
- Tích hợp quyền truy cập tối thiểu
- Hỗ trợ quy trình Agile với Release Note tối ưu

---

## Ghi chú về Versioning

- **MAJOR** (X.0.0): Thay đổi lớn, breaking changes
- **MINOR** (0.X.0): Thêm tính năng mới, không breaking
- **PATCH** (0.0.X): Sửa lỗi, cải thiện nhỏ

---

**Phiên bản hiện tại**: 1.0.0  
**Ngày cập nhật gần nhất**: 2024-12-17
