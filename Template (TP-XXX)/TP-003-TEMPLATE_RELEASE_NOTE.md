# TP-003: TEMPLATE RELEASE NOTE

**Mã template**: TP-003 
**Tham chiếu quy trình**: QT-007 
**Phiên bản**: 2.0 (Agile Release Note)

---

# Release Note - [Service Name] v[Version]

## Thông tin Release

| Thông tin | Giá trị |
|-----------|---------|
| **Service Name** | [Tên service] |
| **Version** | [X.Y.Z] |
| **Release Date** | [YYYY-MM-DD HH:mm] |
| **Release Type** | [Major/Minor/Patch] |
| **Previous Version** | [X.Y.Z] |

## Version Information

### Git Version
- **Git Tag**: `v[X.Y.Z]` hoặc `[tag-name]`
- **Git Commit**: `[commit-hash]` (ví dụ: `a1b2c3d`)
- **Git Branch**: `[branch-name]` (ví dụ: `main`, `release/v1.2.3`)
- **Compare**: [View changes](https://github.com/org/service/compare/v[X.Y.Z-1]...v[X.Y.Z])

### Docker Image
- **Image Name**: `[registry]/[namespace]/[service-name]`
- **Image Tag**: `v[X.Y.Z]` hoặc `[tag]`
- **Image Digest**: `sha256:[digest]` (ví dụ: `sha256:abc123...`)
- **Full Image**: `[registry]/[namespace]/[service-name]:v[X.Y.Z]@sha256:[digest]`

**Ví dụ**:
```bash
# Pull image
docker pull registry.example.com/myorg/user-service:v1.2.3

# Hoặc với digest (khuyến nghị cho production)
docker pull registry.example.com/myorg/user-service:v1.2.3@sha256:abc123def456...
```

---

## Tóm tắt

[Mô tả ngắn gọn 1-2 câu về release này]

**Highlights**:
- [Tính năng chính 1]
- [Bug fix quan trọng 1]
- [Cải tiến chính 1]

---

## Breaking Changes

> ** QUAN TRỌNG**: Nếu có breaking changes, đọc kỹ phần này trước khi upgrade.

- **[Tên breaking change]**: [Mô tả ngắn gọn]
 - **Impact**: [Ảnh hưởng đến gì]
 - **Migration**: [Hướng dẫn ngắn gọn hoặc link]

---

## Tính năng mới

- **[Tên tính năng]**: [Mô tả ngắn gọn]
 - Issue: [#123](link) | PR: [#456](link)

---

## Sửa lỗi

- **[Tên lỗi]**: [Mô tả ngắn gọn]
 - Issue: [#123](link) | PR: [#456](link)

---

## Cải tiến

- **[Cải tiến]**: [Mô tả ngắn gọn]

---

## Bảo mật

- **[Vấn đề bảo mật]**: [Mô tả ngắn gọn]
 - CVE: [CVE-YYYY-NNNN] | Severity: [Critical/High/Medium/Low]

---

## Dependencies

**Updated**:
- `[package]`: `[old-version]` → `[new-version]`

**Added**:
- `[package]`: `[version]`

**Removed**:
- `[package]`: `[version]`

---

## Upgrade Instructions

### Docker/Kubernetes

```bash
# Update image tag trong deployment
kubectl set image deployment/[deployment-name] [container-name]=[registry]/[namespace]/[service-name]:v[X.Y.Z]

# Hoặc update trong values.yaml (Helm)
image:
 repository: [registry]/[namespace]/[service-name]
 tag: v[X.Y.Z]
 digest: sha256:[digest] # Khuyến nghị
```

### Docker Compose

```yaml
services:
 service-name:
 image: [registry]/[namespace]/[service-name]:v[X.Y.Z]
 # Hoặc với digest
 # image: [registry]/[namespace]/[service-name]:v[X.Y.Z]@sha256:[digest]
```

---

## Testing Results (Kiến nghị)

> ** Lưu ý**: Phần này là kiến nghị, điền nếu có thông tin test quan trọng hoặc cần thiết.

- **Unit Tests**: [Coverage %] - [Pass/Fail]
- **Integration Tests**: [Pass/Fail]
- **E2E Tests**: [Pass/Fail]
- **Load Tests**: [Pass/Fail] (nếu có)
- **Security Tests**: [Pass/Fail] (nếu có)
- **Performance Tests**: [Pass/Fail] (nếu có)

**Ghi chú**: [Bất kỳ ghi chú nào về testing, ví dụ: "Tất cả tests đã pass, không có regression"]

---

## Performance Metrics (Kiến nghị)

> ** Lưu ý**: Phần này là kiến nghị, điền nếu có cải thiện performance đáng kể hoặc cần lưu ý.

### Metrics cải thiện

- **Response Time**: [Giảm/Tăng X%] - [Trước: Xms, Sau: Yms]
- **Throughput**: [Tăng X%] - [Trước: X req/s, Sau: Y req/s]
- **Memory Usage**: [Giảm/Tăng X%] - [Trước: X MB, Sau: Y MB]
- **CPU Usage**: [Giảm/Tăng X%] - [Trước: X%, Sau: Y%]
- **Database Query Time**: [Giảm/Tăng X%] (nếu có)

**Ghi chú**: [Bất kỳ ghi chú nào về performance, ví dụ: "Cải thiện đáng kể nhờ tối ưu database query"]

---

## Links

- **Full Changelog**: [Link](https://github.com/org/service/compare/v[X.Y.Z-1]...v[X.Y.Z])
- **Documentation**: [Link]
- **API Docs**: [Link]
- **Migration Guide**: [Link] (nếu có breaking changes)

---

## Contributors

- [@username1](link) - [Role]
- [@username2](link) - [Role]

---

**Release Manager**: [@username](link) 
**Reviewed By**: [@username](link) 
**Approved By**: [@username](link)

---

**Template Version**: 2.0 (Agile)

