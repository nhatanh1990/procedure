# QT-006: QUY TRÌNH VERSIONING

---

## 📋 THÔNG TIN TÀI LIỆU

- **Mã quy trình**: QT-006
- **Tên quy trình**: Quy trình Versioning
- **Phiên bản**: 1.0
- **Ngày ban hành**: [Ngày hiện tại]
- **Người soạn**: 
- **Trạng thái**: Chính thức

---

## 📚 MỤC LỤC

1. [Tổng quan](#1-tổng-quan)
2. [Semantic Versioning](#2-semantic-versioning)
3. [Quy trình versioning](#3-quy-trình-versioning)
4. [Quản lý version trong code](#4-quản-lý-version-trong-code)
5. [Git tagging](#5-git-tagging)
6. [Pre-release versions](#6-pre-release-versions)
7. [Best practices](#7-best-practices)

---

## 1. TỔNG QUAN

### 1.1. Mục đích

Quy trình versioning nhằm quản lý phiên bản code và sản phẩm một cách nhất quán, dễ hiểu và tuân thủ chuẩn Semantic Versioning.

### 1.2. Phạm vi

- Quản lý version cho code
- Quản lý version cho sản phẩm
- Quản lý version cho API
- Quản lý version cho dependencies

### 1.3. Đối tượng

- Development Team
- DevOps Team
- QA Team

---

## 2. SEMANTIC VERSIONING

### 2.1. Tổng quan

Semantic Versioning (SemVer) là chuẩn versioning được sử dụng rộng rãi trong ngành công nghiệp phần mềm.

**Format**: `MAJOR.MINOR.PATCH`

### 2.2. Cấu trúc version

#### 2.2.1. MAJOR (X.0.0)

**Tăng MAJOR khi**:
- Breaking changes trong API
- Thay đổi kiến trúc lớn
- Thay đổi database schema không backward compatible
- Thay đổi format dữ liệu không backward compatible

**Ví dụ**: `1.0.0` → `2.0.0`

#### 2.2.2. MINOR (0.X.0)

**Tăng MINOR khi**:
- Thêm tính năng mới (backward compatible)
- Cải tiến performance (backward compatible)
- Thay đổi nhỏ trong API (backward compatible)
- Thêm API mới

**Ví dụ**: `1.0.0` → `1.1.0`

#### 2.2.3. PATCH (0.0.X)

**Tăng PATCH khi**:
- Sửa bug
- Security patch
- Performance fix nhỏ
- Documentation update

**Ví dụ**: `1.0.0` → `1.0.1`

### 2.3. Ví dụ

| Version | Mô tả |
|---------|-------|
| `1.0.0` | Release đầu tiên |
| `1.0.1` | Sửa bug |
| `1.1.0` | Thêm tính năng mới |
| `1.1.1` | Sửa bug |
| `2.0.0` | Breaking changes |

---

## 3. QUY TRÌNH VERSIONING

### 3.1. Quy trình tổng quan

```
1. Xác định loại thay đổi
   → Breaking changes? → Tăng MAJOR
   → Tính năng mới? → Tăng MINOR
   → Bug fix? → Tăng PATCH

2. Update version
   → Update trong code (package.json, pom.xml, ...)
   → Update trong CHANGELOG.md
   → Update trong documentation

3. Tạo tag
   → Tạo git tag: vX.Y.Z
   → Push tag lên remote

4. Ghi nhận
   → Ghi nhận version trong release note
   → Ghi nhận trong changelog
```

### 3.2. Chi tiết từng bước

#### Bước 1: Xác định loại thay đổi

**Công việc**:
- [ ] Xác định có breaking changes không
- [ ] Xác định có tính năng mới không
- [ ] Xác định có bug fix không
- [ ] Xác định version mới

**Quy tắc**:
- Nếu có breaking changes → Tăng MAJOR
- Nếu có tính năng mới (không breaking) → Tăng MINOR
- Nếu chỉ có bug fix → Tăng PATCH

#### Bước 2: Update version trong code

**Công việc**:
- [ ] Update version trong file cấu hình (package.json, pom.xml, ...)
- [ ] Update version trong code (nếu có)
- [ ] Update CHANGELOG.md
- [ ] Update documentation (nếu cần)

**Tham chiếu**: Phần 4 - Quản lý version trong code

#### Bước 3: Tạo git tag

**Công việc**:
- [ ] Tạo git tag: `vX.Y.Z`
- [ ] Push tag lên remote
- [ ] Verify tag

**Tham chiếu**: Phần 5 - Git tagging

#### Bước 4: Ghi nhận

**Công việc**:
- [ ] Ghi nhận version trong release note
- [ ] Ghi nhận trong changelog
- [ ] Update documentation

---

## 4. QUẢN LÝ VERSION TRONG CODE

### 4.1. File cấu hình

#### 4.1.1. Node.js (package.json)

```json
{
  "name": "my-service",
  "version": "1.2.3",
  ...
}
```

#### 4.1.2. Java/Maven (pom.xml)

```xml
<project>
  <groupId>com.example</groupId>
  <artifactId>my-service</artifactId>
  <version>1.2.3</version>
  ...
</project>
```

#### 4.1.3. Java/Gradle (build.gradle)

```gradle
version = '1.2.3'
```

#### 4.1.4. Python (setup.py hoặc __version__.py)

```python
__version__ = "1.2.3"
```

#### 4.1.5. Go (version.go)

```go
package main

const Version = "1.2.3"
```

### 4.2. CHANGELOG.md

#### 4.2.1. Format

```markdown
# Changelog

## [1.2.3] - 2024-01-15

### Added
- Tính năng mới X
- Tính năng mới Y

### Changed
- Cải tiến Z

### Fixed
- Fix bug A
- Fix bug B

### Removed
- Deprecated feature C

## [1.2.2] - 2024-01-10
...
```

#### 4.2.2. Quy tắc

- Ghi nhận mọi thay đổi quan trọng
- Sử dụng format chuẩn
- Sắp xếp theo thời gian (mới nhất trước)
- Link đến issues/PRs (nếu có)

### 4.3. Update version

**Quy trình**:
1. Xác định version mới
2. Update trong file cấu hình
3. Update CHANGELOG.md
4. Commit changes
5. Tạo tag

---

## 5. GIT TAGGING

### 5.1. Quy tắc đặt tên tag

**Format**: `vX.Y.Z`

**Ví dụ**:
- `v1.0.0`
- `v1.2.3`
- `v2.0.0-beta.1`

### 5.2. Tạo tag

#### 5.2.1. Lightweight tag

```bash
git tag v1.2.3
git push origin v1.2.3
```

#### 5.2.2. Annotated tag (khuyến nghị)

```bash
git tag -a v1.2.3 -m "Release v1.2.3"
git push origin v1.2.3
```

### 5.3. Quản lý tag

#### 5.3.1. Xem danh sách tag

```bash
git tag
git tag -l "v1.*"
```

#### 5.3.2. Xem thông tin tag

```bash
git show v1.2.3
```

#### 5.3.3. Xóa tag

```bash
# Xóa local tag
git tag -d v1.2.3

# Xóa remote tag
git push origin --delete v1.2.3
```

### 5.4. Best practices

- Sử dụng annotated tag
- Tag message rõ ràng
- Tag sau khi commit
- Push tag cùng lúc với code
- Không xóa tag đã publish

---

## 6. PRE-RELEASE VERSIONS

### 6.1. Alpha

**Format**: `X.Y.Z-alpha.N`

**Mục đích**: Development, chưa stable

**Ví dụ**: `1.0.0-alpha.1`, `1.0.0-alpha.2`

### 6.2. Beta

**Format**: `X.Y.Z-beta.N`

**Mục đích**: Testing, gần stable

**Ví dụ**: `1.0.0-beta.1`, `1.0.0-beta.2`

### 6.3. Release Candidate (RC)

**Format**: `X.Y.Z-rc.N`

**Mục đích**: Release candidate, sẵn sàng release

**Ví dụ**: `1.0.0-rc.1`, `1.0.0-rc.2`

### 6.4. Quy trình

```
1.0.0-alpha.1 → 1.0.0-alpha.2 → ... → 1.0.0-beta.1 → 1.0.0-beta.2 → ... → 1.0.0-rc.1 → 1.0.0-rc.2 → ... → 1.0.0
```

### 6.5. Khi nào sử dụng

- **Alpha**: Development, internal testing
- **Beta**: Public testing, gần release
- **RC**: Final testing trước release chính thức

---

## 7. BEST PRACTICES

### 7.1. Nguyên tắc chung

- **Nhất quán**: Sử dụng Semantic Versioning cho tất cả
- **Rõ ràng**: Version phải dễ hiểu
- **Tuân thủ**: Tuân thủ quy tắc SemVer
- **Ghi nhận**: Ghi nhận mọi thay đổi version

### 7.2. Quy tắc tăng version

- **MAJOR**: Chỉ khi có breaking changes
- **MINOR**: Khi có tính năng mới (backward compatible)
- **PATCH**: Khi có bug fix

### 7.3. Quản lý version

- Version trong code phải khớp với git tag
- CHANGELOG.md phải được update
- Release note phải ghi nhận version

### 7.4. Tránh

- Không tăng version tùy tiện
- Không bỏ qua PATCH version
- Không tăng MAJOR khi không có breaking changes
- Không xóa tag đã publish

---

**Phiên bản**: 1.0
**Ngày ban hành**: [Ngày hiện tại]
**Người soạn**:
**Trạng thái**: Chính thức

