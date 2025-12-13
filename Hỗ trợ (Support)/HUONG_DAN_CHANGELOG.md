# HƯỚNG DẪN CHANGELOG.md
## Changelog cho Sản phẩm/Service

**Phiên bản**: 1.0

---

## 📋 TỔNG QUAN

**CHANGELOG.md** là file ghi lại lịch sử thay đổi của sản phẩm/service theo thời gian. File này giúp:
- Người dùng biết được các thay đổi trong mỗi phiên bản
- Developer theo dõi lịch sử phát triển
- Dễ dàng tạo Release Note từ changelog

---

## 🎯 CHANGELOG.md LÀ GÌ?

### Định nghĩa

**CHANGELOG.md** là file markdown trong repository của sản phẩm/service, ghi lại tất cả các thay đổi quan trọng theo từng phiên bản, được sắp xếp theo thứ tự thời gian (mới nhất ở trên).

### Vị trí

- **Trong repository**: `CHANGELOG.md` ở root folder của project
- **Ví dụ**: `my-service/CHANGELOG.md`

### Mục đích

1. **Cho người dùng**: Biết được tính năng mới, bug fixes, breaking changes
2. **Cho developer**: Theo dõi lịch sử phát triển, dễ dàng tạo Release Note
3. **Cho quản lý**: Theo dõi tiến độ và thay đổi

---

## 📝 CẤU TRÚC CHANGELOG.md

### Format chuẩn

Format dựa trên [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) và [Semantic Versioning](https://semver.org/).

```markdown
# Changelog

Tất cả các thay đổi quan trọng của project này sẽ được ghi lại trong file này.

Format dựa trên [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
và tuân thủ [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Tính năng mới đang phát triển

### Changed
- Thay đổi đang phát triển

### Deprecated
- Tính năng sẽ bị loại bỏ

### Removed
- Tính năng đã bị loại bỏ

### Fixed
- Bug đã sửa

### Security
- Lỗ hổng bảo mật đã sửa

## [1.2.3] - 2024-12-17

### Added
- Tính năng Two-Factor Authentication (2FA)
- User Activity Logging

### Changed
- Cải thiện performance query user list (giảm 40% response time)

### Fixed
- Sửa lỗi session timeout không hoạt động đúng
- Sửa lỗi email reset password không được gửi

### Security
- Update dependency `express` từ 4.18.1 lên 4.18.2 (CVE-2024-12345)

## [1.2.2] - 2024-12-10

### Added
- Tính năng export user data

### Fixed
- Sửa lỗi memory leak trong user service
```

---

## 📋 CÁC LOẠI THAY ĐỔI

### Added
**Khi nào sử dụng**: Thêm tính năng mới

**Ví dụ**:
- `- Thêm tính năng Two-Factor Authentication (2FA)`
- `- Thêm API endpoint mới: POST /api/v2/users`

### Changed
**Khi nào sử dụng**: Thay đổi tính năng hiện có (backward compatible)

**Ví dụ**:
- `- Cải thiện performance query user list (giảm 40% response time)`
- `- Thay đổi format response của API /api/users`

### Deprecated
**Khi nào sử dụng**: Tính năng sẽ bị loại bỏ trong tương lai

**Ví dụ**:
- `- API /api/v1/users sẽ bị deprecated trong v2.0.0, sử dụng /api/v2/users thay thế`

### Removed
**Khi nào sử dụng**: Đã loại bỏ tính năng

**Ví dụ**:
- `- Loại bỏ API /api/v1/users (đã deprecated từ v1.5.0)`

### Fixed
**Khi nào sử dụng**: Sửa lỗi/bug

**Ví dụ**:
- `- Sửa lỗi session timeout không hoạt động đúng`
- `- Sửa lỗi memory leak trong user service`

### Security
**Khi nào sử dụng**: Sửa lỗ hổng bảo mật

**Ví dụ**:
- `- Update dependency express từ 4.18.1 lên 4.18.2 (CVE-2024-12345)`
- `- Sửa lỗ hổng SQL injection trong user query`

---

## 🔄 QUY TRÌNH CẬP NHẬT CHANGELOG

### Khi phát triển tính năng mới

1. **Trong quá trình phát triển**: Thêm vào section `[Unreleased]`
2. **Khi release**: Di chuyển từ `[Unreleased]` sang version mới

### Khi chuẩn bị release

1. **Tạo release branch**: `release/v1.2.3`
2. **Update CHANGELOG.md**:
   - Di chuyển các thay đổi từ `[Unreleased]` sang version mới
   - Thêm ngày release: `## [1.2.3] - 2024-12-17`
   - Sắp xếp theo loại: Added, Changed, Fixed, Security, etc.
3. **Commit**: `git commit -m "chore: update CHANGELOG.md for v1.2.3"`
4. **Merge vào main**

### Khi tạo Release Note

1. **Copy từ CHANGELOG.md**: Lấy nội dung của version mới
2. **Format lại**: Theo format của Release Note template
3. **Bổ sung thông tin**: Git version, Docker image, testing results, etc.

---

## ✅ BEST PRACTICES

### 1. Viết rõ ràng

**Tốt**:
- `- Sửa lỗi session timeout không hoạt động đúng (Issue #125)`

**Không tốt**:
- `- Fix bug`
- `- Sửa lỗi`

### 2. Liên kết với Issue/PR

**Tốt**:
- `- Thêm tính năng 2FA (Issue #123, PR #456)`

**Không tốt**:
- `- Thêm tính năng 2FA`

### 3. Nhóm theo loại

**Tốt**:
```markdown
### Added
- Tính năng A
- Tính năng B

### Fixed
- Bug 1
- Bug 2
```

**Không tốt**:
```markdown
- Tính năng A
- Bug 1
- Tính năng B
- Bug 2
```

### 4. Sử dụng ngôn ngữ nhất quán

- Sử dụng tiếng Việt hoặc tiếng Anh nhất quán
- Nếu dùng tiếng Việt, viết đầy đủ, rõ ràng

### 5. Breaking Changes

**Luôn làm nổi bật breaking changes**:

```markdown
## [2.0.0] - 2024-12-17

### ⚠️ Breaking Changes
- API /api/v1/users đã bị loại bỏ, sử dụng /api/v2/users
- Thay đổi format response của API /api/users

### Added
- API /api/v2/users với format mới
```

---

## 📝 TEMPLATE CHANGELOG.md

```markdown
# Changelog

Tất cả các thay đổi quan trọng của [Tên Service] sẽ được ghi lại trong file này.

Format dựa trên [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
và tuân thủ [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- 

### Changed
- 

### Deprecated
- 

### Removed
- 

### Fixed
- 

### Security
- 

## [X.Y.Z] - YYYY-MM-DD

### Added
- Tính năng mới 1 (Issue #123, PR #456)
- Tính năng mới 2

### Changed
- Cải thiện performance (giảm X% response time)
- Thay đổi format response API

### Fixed
- Sửa lỗi [mô tả lỗi] (Issue #789)
- Sửa lỗi [mô tả lỗi]

### Security
- Update dependency [package] từ [old] lên [new] (CVE-YYYY-NNNN)

## [X.Y.Z-1] - YYYY-MM-DD

### Added
- 

### Fixed
- 

---

## Links

- [Release Notes](link-to-release-notes)
- [Documentation](link-to-docs)
```

---

## 🔗 LIÊN KẾT VỚI RELEASE NOTE

### Mối quan hệ

- **CHANGELOG.md**: Ghi lại tất cả thay đổi theo thời gian (trong repository)
- **Release Note**: Tài liệu cho một release cụ thể (có thể publish riêng)

### Sử dụng CHANGELOG để tạo Release Note

1. **Copy nội dung** từ CHANGELOG.md cho version mới
2. **Bổ sung thông tin**:
   - Git version (tag, commit)
   - Docker image (tag, digest)
   - Testing results
   - Performance metrics
   - Upgrade instructions
3. **Format lại** theo template Release Note

---

## 📌 LƯU Ý

1. **Luôn cập nhật CHANGELOG.md** khi có thay đổi
2. **Commit riêng** cho CHANGELOG.md: `chore: update CHANGELOG.md`
3. **Review CHANGELOG** trước khi release
4. **Giữ CHANGELOG.md** trong repository, không xóa
5. **Sử dụng format nhất quán** cho tất cả entries

---

## 🔗 THAM KHẢO

- **Quy trình Release**: [`../Quy trình (QT-XXX)/QT-007-RELEASE_SAN_PHAM.md`](../Quy%20trình%20(QT-XXX)/QT-007-RELEASE_SAN_PHAM.md)
- **Template Release Note**: [`../Template (TP-XXX)/TP-003-TEMPLATE_RELEASE_NOTE.md`](../Template%20(TP-XXX)/TP-003-TEMPLATE_RELEASE_NOTE.md)
- **Keep a Changelog**: https://keepachangelog.com/
- **Semantic Versioning**: https://semver.org/

---

**Phiên bản**: 1.0  
**Ngày cập nhật**: 2024-12-17

