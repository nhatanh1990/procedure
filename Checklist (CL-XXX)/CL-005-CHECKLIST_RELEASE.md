# CL-005: CHECKLIST RELEASE

**Mã checklist**: CL-005  
**Tham chiếu quy trình**: QT-007

---

## 1. CHECKLIST CHUẨN BỊ RELEASE

### 1.1. Code sẵn sàng

- [ ] Code đã được review và merge
- [ ] Tất cả tests đã pass
- [ ] Code coverage: ≥ 80%
- [ ] Security scan: Pass
- [ ] Performance tests: Pass (nếu cần)

### 1.2. Documentation

- [ ] API documentation đã được update
- [ ] User guide đã được update (nếu cần)
- [ ] CHANGELOG.md đã được update

### 1.3. Version

- [ ] Version đã được xác định
- [ ] Version đã được update trong code

### 1.4. Release Note

- [ ] Release Note draft đã được tạo
- [ ] Release Note đã được review
- [ ] Release Note đã được phê duyệt

---

## 2. CHECKLIST TẠO RELEASE

### 2.1. Release branch

- [ ] Release branch đã được tạo
- [ ] Version đã được update
- [ ] CHANGELOG.md đã được update

### 2.2. Merge và tag

- [ ] Release branch đã được merge vào main
- [ ] Git tag đã được tạo
- [ ] Git tag đã được push

### 2.3. Build artifacts

- [ ] Docker image đã được build
- [ ] Binary đã được build (nếu có)
- [ ] Documentation đã được build (nếu có)
- [ ] Artifacts đã được test

### 2.4. Push artifacts

- [ ] Docker image đã được push
- [ ] Binary đã được push (nếu có)
- [ ] Documentation đã được push (nếu có)

---

## 3. CHECKLIST DEPLOY RELEASE

### 3.1. Deploy Staging

- [ ] Deploy lên Staging thành công
- [ ] Service đã start thành công
- [ ] Health check pass
- [ ] Smoke test pass

### 3.2. Test Staging

- [ ] Unit tests: Pass
- [ ] Integration tests: Pass
- [ ] E2E tests: Pass
- [ ] Performance tests: Pass (nếu cần)
- [ ] Không có regression

### 3.3. Deploy Production

- [ ] Deploy lên Production thành công
- [ ] Service đã start thành công
- [ ] Health check pass
- [ ] Smoke test pass

### 3.4. Test Production

- [ ] Smoke tests: Pass
- [ ] Không có lỗi trong log
- [ ] Metrics trong giới hạn cho phép
- [ ] Monitoring không có cảnh báo
- [ ] Đã giám sát hệ thống (ít nhất 1 giờ)

---

## 4. CHECKLIST PUBLISH RELEASE

### 4.1. Publish Release Note

- [ ] Release Note đã được publish trên documentation site
- [ ] Release Note đã được publish trên GitHub/GitLab
- [ ] Changelog đã được update

### 4.2. Thông báo

- [ ] Development Team đã được thông báo
- [ ] DevOps Team đã được thông báo
- [ ] QA Team đã được thông báo
- [ ] Product Owner đã được thông báo
- [ ] Người dùng đã được thông báo (nếu cần)

### 4.3. Update documentation

- [ ] API documentation đã được update
- [ ] User guide đã được update (nếu cần)
- [ ] Deployment guide đã được update (nếu cần)
- [ ] Runbook đã được update (nếu cần)

### 4.4. Ghi nhận

- [ ] Release đã được ghi nhận trong JIRA
- [ ] Release đã được ghi nhận trong changelog
- [ ] Release đã được ghi nhận trong release history

---

**Phiên bản**: 1.0

