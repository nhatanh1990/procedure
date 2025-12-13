# TROUBLESHOOTING GUIDE
## Hướng dẫn xử lý vấn đề thường gặp

**Phiên bản**: 1.0

---

## 📋 TỔNG QUAN

Tài liệu này cung cấp hướng dẫn xử lý các vấn đề thường gặp khi sử dụng hệ thống quy trình.

---

## ❓ FAQ - CÂU HỎI THƯỜNG GẶP

### 1. Tôi không biết thay đổi của mình thuộc loại nào?

**Giải pháp**:
1. Sử dụng [`QUICK_REFERENCE_THAY_DOI.md`](../QUICK_REFERENCE_THAY_DOI.md) để tra cứu nhanh
2. Sử dụng [`TP-005-TEMPLATE_TRA_CUU_THAY_DOI.md`](../Template%20(TP-XXX)/TP-005-TEMPLATE_TRA_CUU_THAY_DOI.md) để tra cứu chi tiết
3. Xem ví dụ: [`TP-005-EXAMPLE_TRA_CUU_THAY_DOI.md`](../Template%20(TP-XXX)/TP-005-EXAMPLE_TRA_CUU_THAY_DOI.md)

**Nếu không tìm thấy**:
- Xem quy trình xử lý ngoại lệ trong [`QT-003-UPCODE.md`](../Quy%20trình%20(QT-XXX)/QT-003-UPCODE.md) - Phần 8
- Hoặc sử dụng quy trình bổ sung thay đổi: [`QT-009-QUY_TRINH_BO_SUNG_THAY_DOI.md`](../Quy%20trình%20(QT-XXX)/QT-009-QUY_TRINH_BO_SUNG_THAY_DOI.md)

---

### 2. Tôi không biết cấp độ phê duyệt là gì?

**Giải pháp**:
- Xem trong [`QT-008-DANH_SACH_THAY_DOI_CHUAN.md`](../Quy%20trình%20(QT-XXX)/QT-008-DANH_SACH_THAY_DOI_CHUAN.md)
- Mỗi mã thay đổi đều có "Cấp độ duyệt"
- Hoặc xem bảng RACI trong [`QT-003-UPCODE.md`](../Quy%20trình%20(QT-XXX)/QT-003-UPCODE.md)

**Các cấp độ**:
- **Level 1.0**: PM/PDM
- **Level 2.0**: Ban CLGSP hoặc Lãnh đạo TT
- **Level 3.0**: Ban CLGSP + Ban KTHT
- **Level 4.0**: Lãnh đạo Công ty

---

### 3. Tôi cần hotfix nhưng không biết quy trình?

**Giải pháp**:
1. Đọc [`QT-004-HOTFIX.md`](../Quy%20trình%20(QT-XXX)/QT-004-HOTFIX.md)
2. Sử dụng [`TP-002-TEMPLATE_HOTFIX.md`](../Template%20(TP-XXX)/TP-002-TEMPLATE_HOTFIX.md)
3. Xem ví dụ: [`TP-002-EXAMPLE_HOTFIX.md`](../Template%20(TP-XXX)/TP-002-EXAMPLE_HOTFIX.md)
4. Sử dụng checklist: [`CL-003-CHECKLIST_HOTFIX.md`](../Checklist%20(CL-XXX)/CL-003-CHECKLIST_HOTFIX.md)

---

### 4. Tôi không biết cách điền template?

**Giải pháp**:
- Mỗi template đều có file example tương ứng
- Xem file example để hiểu cách điền
- Danh sách example:
  - [`TP-001-EXAMPLE_RFC.md`](../Template%20(TP-XXX)/TP-001-EXAMPLE_RFC.md)
  - [`TP-002-EXAMPLE_HOTFIX.md`](../Template%20(TP-XXX)/TP-002-EXAMPLE_HOTFIX.md)
  - [`TP-003-EXAMPLE_RELEASE_NOTE.md`](../Template%20(TP-XXX)/TP-003-EXAMPLE_RELEASE_NOTE.md)
  - [`TP-004-EXAMPLE_PROVISIONING.md`](../Template%20(TP-XXX)/TP-004-EXAMPLE_PROVISIONING.md)
  - [`TP-005-EXAMPLE_TRA_CUU_THAY_DOI.md`](../Template%20(TP-XXX)/TP-005-EXAMPLE_TRA_CUU_THAY_DOI.md)

---

### 5. Tôi cần rollback nhưng không biết cách?

**Giải pháp**:
- Xem quy trình rollback trong [`QT-003-UPCODE.md`](../Quy%20trình%20(QT-XXX)/QT-003-UPCODE.md) - Phần 7
- Sử dụng checklist rollback trong [`CL-002-CHECKLIST_UPCODE.md`](../Checklist%20(CL-XXX)/CL-002-CHECKLIST_UPCODE.md)
- Đảm bảo đã có rollback plan trước khi triển khai

---

### 6. Tôi không biết checklist nào cần sử dụng?

**Giải pháp**:
- Xem danh sách checklist trong [`README.md`](../README.md)
- Checklist tổng quát: CL-001 đến CL-005
- Checklist theo nhóm: CL-007 đến CL-010 (cho QT-008)
- Checklist tra cứu: CL-006

---

## 🔧 VẤN ĐỀ KỸ THUẬT

### Vấn đề 1: Không tìm thấy file

**Triệu chứng**: Link đến file không hoạt động

**Giải pháp**:
1. Kiểm tra đường dẫn file có đúng không
2. Kiểm tra file có tồn tại trong folder không
3. Xem cấu trúc folder trong [`README.md`](../README.md)

---

### Vấn đề 2: Thông tin trong file không khớp

**Triệu chứng**: Thông tin trong file A không khớp với file B

**Giải pháp**:
1. Kiểm tra version của file (xem phần "Phiên bản")
2. Xem [`CHANGELOG.md`](CHANGELOG.md) để biết thay đổi gần đây
3. Báo cáo vấn đề cho người quản lý

---

### Vấn đề 3: Không hiểu thuật ngữ

**Triệu chứng**: Gặp thuật ngữ không hiểu

**Giải pháp**:
1. Xem phần "Định nghĩa" trong mỗi quy trình
2. Tìm kiếm trong file để xem giải thích
3. Hỏi team lead hoặc người có kinh nghiệm

**Các thuật ngữ thường gặp**:
- **Standard Change**: Thay đổi chuẩn, đã được ủy quyền trước
- **Normal Change**: Thay đổi thông thường, cần CAB phê duyệt
- **Emergency Change**: Thay đổi khẩn, cần ECAB hoặc Lãnh đạo
- **CAB**: Change Advisory Board
- **ECAB**: Emergency Change Advisory Board
- **RACI**: Responsible, Accountable, Consulted, Informed

---

## 🚨 VẤN ĐỀ QUY TRÌNH

### Vấn đề 1: RFC bị từ chối

**Triệu chứng**: RFC bị từ chối phê duyệt

**Giải pháp**:
1. Xem lý do từ chối trong RFC
2. Bổ sung thông tin còn thiếu
3. Đánh giá lại rủi ro nếu cần
4. Gửi lại RFC sau khi đã bổ sung

---

### Vấn đề 2: Không biết ai phê duyệt

**Triệu chứng**: Không biết gửi RFC cho ai

**Giải pháp**:
1. Xác định cấp độ phê duyệt từ mã thay đổi
2. Xem bảng RACI trong [`QT-003-UPCODE.md`](../Quy%20trình%20(QT-XXX)/QT-003-UPCODE.md)
3. Hỏi PM/PDM hoặc team lead

---

### Vấn đề 3: Cần thay đổi ngoài giờ làm việc

**Triệu chứng**: Cần triển khai ngoài giờ làm việc

**Giải pháp**:
1. Xem quy định về thời gian triển khai trong [`QT-003-UPCODE.md`](../Quy%20trình%20(QT-XXX)/QT-003-UPCODE.md)
2. Nếu là hotfix, có thể triển khai ngoài giờ
3. Nếu là thay đổi thông thường, cần phê duyệt đặc biệt
4. Đảm bảo có người hỗ trợ và rollback plan

---

## 📞 LIÊN HỆ HỖ TRỢ

### Khi cần hỗ trợ

1. **Xem tài liệu trước**: Đọc kỹ quy trình và checklist
2. **Xem FAQ**: Kiểm tra phần FAQ ở trên
3. **Hỏi team**: Hỏi team lead hoặc người có kinh nghiệm
4. **Liên hệ quản lý**: Nếu vấn đề nghiêm trọng

### Thông tin liên hệ

- **Email hỗ trợ**: [support@company.com] (xem METADATA_CONFIG.md)
- **Slack/Teams**: [Channel] (xem METADATA_CONFIG.md)
- **JIRA**: Tạo ticket hỗ trợ

---

## 📝 BÁO CÁO VẤN ĐỀ

### Khi phát hiện vấn đề trong tài liệu

1. Ghi lại vấn đề cụ thể
2. Ghi lại file và phần có vấn đề
3. Báo cáo cho người quản lý
4. Đề xuất giải pháp nếu có

### Format báo cáo

```
**File**: [Tên file]
**Phần**: [Phần có vấn đề]
**Vấn đề**: [Mô tả vấn đề]
**Ảnh hưởng**: [Ảnh hưởng như thế nào]
**Đề xuất**: [Đề xuất giải pháp]
```

---

## ✅ CHECKLIST TROUBLESHOOTING

Khi gặp vấn đề, làm theo các bước:

- [ ] Đã đọc kỹ quy trình liên quan
- [ ] Đã xem FAQ ở trên
- [ ] Đã kiểm tra file example
- [ ] Đã hỏi team lead
- [ ] Đã xem TROUBLESHOOTING.md này
- [ ] Đã liên hệ hỗ trợ nếu cần

---

**Phiên bản**: 1.0  
**Ngày cập nhật**: 2024-12-17

