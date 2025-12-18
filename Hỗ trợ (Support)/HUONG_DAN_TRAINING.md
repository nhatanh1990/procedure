# HƯỚNG DẪN TRAINING
## Quy trình Quản trị Vận hành, Upcode, Hotfix và Thay đổi Hệ thống

---

## TỔNG QUAN

Tài liệu này hướng dẫn cách training nhân viên mới về hệ thống quy trình quản trị vận hành, upcode, hotfix và thay đổi hệ thống.

---

## MỤC TIÊU TRAINING

Sau khi hoàn thành training, nhân viên mới có thể:
- Hiểu rõ hệ thống quy trình
- Biết cách tra cứu loại thay đổi
- Biết cách tạo RFC và thực hiện upcode
- Biết cách xử lý hotfix
- Biết cách sử dụng checklist và template

---

## TÀI LIỆU TRAINING

### Tài liệu bắt buộc

1. **README.md**: File chính, tổng quan hệ thống
2. **QT-003**: Quy trình Upcode
3. **QT-004**: Quy trình Hotfix
4. **QT-008**: Danh sách Thay đổi Chuẩn
5. **QUICK_REFERENCE_THAY_DOI**: Bảng tra cứu nhanh

### Tài liệu tham khảo

- QT-002: Quản trị Vận hành
- QT-005: Provisioning
- QT-006: Versioning
- QT-007: Release Sản phẩm
- CL-001 đến CL-010: Checklist
- TP-001 đến TP-005: Template

---

## CHƯƠNG TRÌNH TRAINING

### Module 1: Tổng quan

#### Nội dung

1. **Giới thiệu hệ thống quy trình**
 - Mục đích và phạm vi
 - Cấu trúc tài liệu
 - Mối quan hệ giữa các quy trình

2. **Các khái niệm cơ bản**
 - Standard Change, Normal Change, Emergency Change
 - Production, DR, UAT, Staging
 - RFC, CAB, ECAB
 - Rollback, Hotfix

3. **Hướng dẫn sử dụng tài liệu**
 - Cách đọc quy trình
 - Cách sử dụng checklist
 - Cách sử dụng template

#### Bài tập

- [ ] Đọc README.md và tóm tắt
- [ ] Liệt kê các quy trình chính
- [ ] Giải thích sự khác biệt giữa Standard/Normal/Emergency Change

---

### Module 2: Tra cứu Loại Thay Đổi

#### Nội dung

1. **Danh sách thay đổi chuẩn (QT-008)**
 - 4 nhóm thay đổi (A/B/C/D)
 - 58 loại thay đổi
 - Cách tra cứu

2. **Quick Reference**
 - Bảng tra cứu nhanh
 - Tra cứu theo mã, nhóm, rủi ro

3. **Xử lý ngoại lệ**
 - Khi nào là ngoại lệ
 - Quy trình xử lý ngoại lệ

#### Bài tập

- [ ] Tra cứu 5 loại thay đổi thường gặp
- [ ] Xác định nhóm, rủi ro, loại, cấp duyệt
- [ ] Xử lý tình huống ngoại lệ

---

### Module 3: Quy trình Upcode

#### Nội dung

1. **Tổng quan quy trình upcode**
 - Các bước chính
 - Flowchart

2. **Phân loại thay đổi**
 - Standard Change
 - Normal Change
 - Emergency Change

3. **Đánh giá rủi ro**
 - Ma trận đánh giá rủi ro
 - Xác định Level
 - Bảng RACI

4. **Quy trình kiểm thử**
 - Mức độ kiểm thử theo Level
 - Các loại kiểm thử

5. **Quy trình triển khai**
 - Chuẩn bị
 - Triển khai
 - Kiểm tra
 - Giám sát

6. **Quy trình rollback**
 - Khi nào cần rollback
 - Quy trình rollback

#### Bài tập

- [ ] Tạo RFC cho một thay đổi cụ thể
- [ ] Đánh giá rủi ro và xác định Level
- [ ] Lập kế hoạch triển khai và rollback

---

### Module 4: Quy trình Hotfix

#### Nội dung

1. **Tổng quan quy trình hotfix**
 - Khi nào cần hotfix
 - Sự khác biệt với upcode thông thường

2. **Quy trình hotfix**
 - Phát hiện sự cố
 - Phê duyệt khẩn
 - Phát triển hotfix
 - Triển khai hotfix
 - Hoàn thiện

3. **Phân loại sự cố**
 - Critical, High, Medium, Low
 - Major Incident, Serious Incident

#### Bài tập

- [ ] Tạo Hotfix Request cho một sự cố
- [ ] Thực hành quy trình hotfix

---

### Module 5: Checklist và Template

#### Nội dung

1. **Checklist**
 - CL-001 đến CL-010
 - Cách sử dụng checklist

2. **Template**
 - TP-001: Template RFC
 - TP-002: Template Hotfix
 - TP-003: Template Release Note
 - TP-004: Template Provisioning
 - TP-005: Template Tra Cứu

3. **Thực hành**
 - Điền template RFC
 - Sử dụng checklist

#### Bài tập

- [ ] Điền đầy đủ một template RFC
- [ ] Sử dụng checklist cho một thay đổi

---

### Module 6: Case Study

#### Case Study 1: Standard Change

**Tình huống**: Cần sửa lỗi giao diện (UI/UX) trên Production

**Yêu cầu**:
1. Tra cứu loại thay đổi
2. Xác định quy trình
3. Tạo RFC
4. Thực hiện upcode

**Giải pháp**:
- Mã thay đổi: B1.1
- Loại: Chuẩn
- Cấp duyệt: PM/PDM
- Quy trình: QT-003 - Standard Change

#### Case Study 2: Normal Change

**Tình huống**: Cần thêm chức năng mới với rủi ro trung bình

**Yêu cầu**:
1. Tra cứu loại thay đổi
2. Đánh giá rủi ro
3. Xác định Level
4. Tạo RFC và phê duyệt
5. Thực hiện upcode

**Giải pháp**:
- Mã thay đổi: B2.2
- Loại: Thông thường
- Rủi ro: Trung bình
- Cấp duyệt: Ban CLGSP
- Quy trình: QT-003 - Normal Change

#### Case Study 3: Emergency Change (Hotfix)

**Tình huống**: Phát hiện lỗ hổng bảo mật nghiêm trọng trên Production

**Yêu cầu**:
1. Đánh giá sự cố
2. Tạo Hotfix Request
3. Phê duyệt khẩn
4. Thực hiện hotfix
5. Hoàn thiện

**Giải pháp**:
- Mã thay đổi: B4.4 hoặc D3.1
- Loại: Khẩn
- Cấp duyệt: Lãnh đạo Công ty
- Quy trình: QT-004 - Hotfix

#### Case Study 4: Ngoại lệ

**Tình huống**: Cần thực hiện thay đổi không có trong danh sách chuẩn

**Yêu cầu**:
1. Xác định ngoại lệ
2. Đánh giá rủi ro
3. Phân loại tạm thời
4. Lập kế hoạch chi tiết
5. Phê duyệt
6. Thực hiện

**Giải pháp**:
- Xử lý theo QT-003 - Phần 8: Quy trình xử lý ngoại lệ
- Đánh giá rủi ro và phân loại tạm thời
- Có thể cần phê duyệt từ cấp cao hơn 1 bậc

---

## ĐÁNH GIÁ SAU TRAINING

### Kiểm tra lý thuyết

1. **Câu hỏi trắc nghiệm** (20 câu)
 - Khái niệm cơ bản
 - Quy trình
 - Tra cứu loại thay đổi

2. **Câu hỏi tự luận** (5 câu)
 - Giải thích quy trình
 - Phân tích tình huống
 - Đề xuất giải pháp

### Kiểm tra thực hành

1. **Thực hành tra cứu**
 - Tra cứu 10 loại thay đổi
 - Xác định quy trình

2. **Thực hành tạo RFC**
 - Tạo RFC cho một thay đổi
 - Đánh giá rủi ro
 - Xác định Level

3. **Thực hành case study**
 - Xử lý 2 case study
 - Giải thích quy trình

### Tiêu chí đạt

- **Lý thuyết**: ≥ 80% điểm
- **Thực hành**: Hoàn thành 100% bài tập
- **Case study**: Xử lý đúng ít nhất 80%

---

## FAQ (FREQUENTLY ASKED QUESTIONS)

### Q1: Làm thế nào để tra cứu loại thay đổi?

**A**: 
1. Mở file `QT-008-DANH_SACH_THAY_DOI_CHUAN.md` hoặc `QUICK_REFERENCE_THAY_DOI.md`
2. Xác định nhóm (A/B/C/D) dựa vào mô tả
3. Tìm mã tương ứng trong nhóm
4. Xem thông tin: Rủi ro, Loại, Cấp duyệt

### Q2: Khi nào cần tạo RFC?

**A**: 
- Normal Change: Bắt buộc
- Standard Change: Không cần (đã ủy quyền trước)
- Emergency Change: Có thể tạo sau

### Q3: Làm thế nào để đánh giá rủi ro?

**A**: 
1. Xác định Likelihood (1-4)
2. Xác định Impact (1-4)
3. Tính điểm: Likelihood × Impact
4. Xác định mức độ rủi ro và Level

### Q4: Khi nào cần rollback?

**A**: 
- Sự cố nghiêm trọng ảnh hưởng đến dịch vụ
- Mất dữ liệu hoặc dữ liệu sai
- Hệ thống không thể hoạt động
- Performance suy giảm nghiêm trọng
- Lỗi bảo mật nghiêm trọng

### Q5: Sự khác biệt giữa Hotfix và Upcode thông thường?

**A**: 
- **Hotfix**: Khẩn cấp, xử lý sự cố, có thể phê duyệt sau
- **Upcode thông thường**: Có kế hoạch, phê duyệt trước, đầy đủ hồ sơ

### Q6: Làm thế nào để xử lý ngoại lệ?

**A**: 
1. Tra cứu trong danh sách chuẩn
2. Xác định là ngoại lệ
3. Đánh giá rủi ro
4. Phân loại tạm thời
5. Lập kế hoạch chi tiết
6. Phê duyệt (có thể cao hơn 1 bậc)
7. Thực hiện và đánh giá sau

### Q7: Checklist nào cần sử dụng?

**A**: 
- **CL-002**: Cho upcode thông thường
- **CL-003**: Cho hotfix
- **CL-006**: Cho tra cứu thay đổi
- **CL-007-010**: Cho từng nhóm cụ thể

---

## KẾ HOẠCH TRAINING

### Training cơ bản (1 ngày)

- **Sáng**: Module 1, 2, 3
- **Chiều**: Module 4, 5, 6

### Training nâng cao (1 ngày)

- **Sáng**: Review và case study nâng cao
- **Chiều**: Thực hành và đánh giá

### Training chuyên sâu (2 ngày)

- **Ngày 1**: Training cơ bản
- **Ngày 2**: Training nâng cao + Thực hành thực tế

---

## CHECKLIST TRAINING

### Trước training

- [ ] Đã chuẩn bị tài liệu
- [ ] Đã chuẩn bị case study
- [ ] Đã chuẩn bị bài tập
- [ ] Đã chuẩn bị môi trường thực hành

### Trong training

- [ ] Đã giới thiệu tổng quan
- [ ] Đã giải thích các khái niệm
- [ ] Đã thực hành tra cứu
- [ ] Đã thực hành tạo RFC
- [ ] Đã làm case study
- [ ] Đã trả lời câu hỏi

### Sau training

- [ ] Đã kiểm tra lý thuyết
- [ ] Đã kiểm tra thực hành
- [ ] Đã đánh giá kết quả
- [ ] Đã cấp chứng chỉ (nếu đạt)

---

## TÀI LIỆU THAM KHẢO

- **README.md**: File chính, tổng quan hệ thống
- **QT-003**: Quy trình Upcode
- **QT-004**: Quy trình Hotfix
- **QT-008**: Danh sách Thay đổi Chuẩn
- **QUICK_REFERENCE_THAY_DOI**: Bảng tra cứu nhanh

---

**Phiên bản**: 1.0
**Ngày cập nhật**: 2024-12-17

