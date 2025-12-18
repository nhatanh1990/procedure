# CL-010: CHECKLIST NHÓM D - XỬ LÝ SỰ CỐ

**Mã checklist**: CL-010 
**Tham chiếu**: `QT-008-DANH_SACH_THAY_DOI_CHUAN.md` - Nhóm D, `QT-004-HOTFIX.md`

---

## TỔNG QUAN

Nhóm D bao gồm 4 loại thay đổi liên quan đến xử lý sự cố:
- D1: Sự cố thông thường (1 loại)
- D2: Sự cố lớn (2 loại)
- D3: Sự cố nghiêm trọng (1 loại)

**Lưu ý**: Nhóm D thường liên quan đến quy trình Hotfix (QT-004)

---

## CHECKLIST CHUNG CHO NHÓM D

### Phát hiện sự cố

- [ ] Đã phát hiện sự cố
- [ ] Đã ghi nhận sự cố
- [ ] Đã đánh giá mức độ nghiêm trọng
- [ ] Đã xác định nguyên nhân sơ bộ
- [ ] Đã quyết định cần hotfix

### Chuẩn bị hotfix

- [ ] Đã tra cứu mã thay đổi trong QT-008
- [ ] Đã tạo Hotfix Request (TP-002)
- [ ] Đã phê duyệt khẩn
- [ ] Đã tạo hotfix branch
- [ ] Đã sửa lỗi
- [ ] Đã test nhanh

### Triển khai hotfix

- [ ] Đã backup hệ thống
- [ ] Đã deploy hotfix
- [ ] Đã kiểm tra deployment
- [ ] Đã xác nhận sửa lỗi
- [ ] Đã giám sát hệ thống

### Hoàn thiện

- [ ] Đã merge vào main branch
- [ ] Đã bổ sung hồ sơ
- [ ] Đã đánh giá sau
- [ ] Đã ghi nhận

---

## CHECKLIST THEO TỪNG LOẠI

### D1: Sự cố thông thường

#### D1.1 - Xử lý sự cố thông thường
- [ ] Đã phát hiện sự cố
- [ ] Đã đánh giá mức độ: Thấp
- [ ] Đã xác định nguyên nhân
- [ ] Đã lập kế hoạch xử lý
- [ ] Đã được Lãnh đạo TT/PDM duyệt
- [ ] Đã thực hiện xử lý
- [ ] Đã xác nhận đã khắc phục
- [ ] Đã ghi nhận

**Thời gian xử lý**: ≤ 24 giờ

### D2: Sự cố lớn

#### D2.1 - Xử lý Sự cố Lớn (Major Incident)
- [ ] Đã phát hiện sự cố lớn
- [ ] Đã đánh giá mức độ: Cao
- [ ] Đã xác định nguyên nhân
- [ ] Đã lập kế hoạch xử lý khẩn
- [ ] Đã được Ban CLGSP, Ban KTHT phê duyệt khẩn
- [ ] Đã thực hiện xử lý khẩn
- [ ] Đã xác nhận đã khắc phục
- [ ] Đã đánh giá sau
- [ ] Đã ghi nhận

**Thời gian xử lý**: ≤ 4 giờ

**Lưu ý**:
- Phải xử lý khẩn cấp
- Có thể phê duyệt sau
- Phải bổ sung hồ sơ trong 1 tuần

#### D2.2 - Xử lý sự cố lớn (trong phần APP)
- [ ] Đã phát hiện sự cố lớn trong APP
- [ ] Đã đánh giá mức độ: Trung bình
- [ ] Đã xác định nguyên nhân
- [ ] Đã lập kế hoạch xử lý
- [ ] Đã được Ban CLGSP phê duyệt
- [ ] Đã thực hiện xử lý
- [ ] Đã xác nhận đã khắc phục
- [ ] Đã ghi nhận

**Thời gian xử lý**: ≤ 24 giờ

### D3: Sự cố nghiêm trọng

#### D3.1 - Xử lý Sự cố Nghiêm trọng (Serious Incident)
- [ ] Đã phát hiện sự cố nghiêm trọng
- [ ] Đã đánh giá mức độ: Nghiêm trọng
- [ ] Đã xác định nguyên nhân
- [ ] Đã lập kế hoạch xử lý khẩn cấp
- [ ] Đã được Lãnh đạo Công ty phê duyệt khẩn
- [ ] Đã thực hiện xử lý khẩn cấp
- [ ] Đã xác nhận đã khắc phục
- [ ] Đã đánh giá sau
- [ ] Đã ghi nhận
- [ ] Đã báo cáo Lãnh đạo

**Thời gian xử lý**: ≤ 1 giờ

**Lưu ý**:
- Phải xử lý khẩn cấp ngay lập tức
- Có thể phê duyệt sau
- Phải bổ sung hồ sơ trong 1 tuần
- Phải báo cáo Lãnh đạo

---

## CHECKLIST XỬ LÝ SỰ CỐ CHI TIẾT

### Bước 1: Phát hiện và đánh giá

- [ ] Đã phát hiện sự cố (từ monitoring/người dùng/log)
- [ ] Đã ghi nhận sự cố
- [ ] Đã thu thập thông tin ban đầu
- [ ] Đã đánh giá mức độ nghiêm trọng
- [ ] Đã xác định nguyên nhân sơ bộ
- [ ] Đã quyết định cần hotfix

### Bước 2: Phê duyệt khẩn

- [ ] Đã tạo Hotfix Request (TP-002)
- [ ] Đã gửi phê duyệt khẩn
- [ ] Đã được phê duyệt (hoặc có thể phê duyệt sau)

**Cấp phê duyệt**:
- D1.1: Lãnh đạo TT/PDM
- D2.1: Ban CLGSP, Ban KTHT
- D2.2: Ban CLGSP
- D3.1: Lãnh đạo Công ty

### Bước 3: Phát triển hotfix

- [ ] Đã tạo hotfix branch
- [ ] Đã sửa lỗi
- [ ] Đã test nhanh
- [ ] Đã code review (nếu có thời gian)

### Bước 4: Triển khai hotfix

- [ ] Đã backup hệ thống
- [ ] Đã deploy hotfix
- [ ] Đã kiểm tra deployment
- [ ] Đã smoke test
- [ ] Đã xác nhận sửa lỗi
- [ ] Đã giám sát hệ thống (ít nhất 30 phút)

### Bước 5: Hoàn thiện

- [ ] Đã merge vào main branch
- [ ] Đã bổ sung hồ sơ (trong 1 tuần)
- [ ] Đã đánh giá sau
- [ ] Đã ghi nhận

---

## LƯU Ý ĐẶC BIỆT

### Cho sự cố thông thường (D1)

- Có thể xử lý theo quy trình bình thường
- Thời gian xử lý: ≤ 24 giờ
- Phải ghi nhận đầy đủ

### Cho sự cố lớn (D2)

- Phải xử lý khẩn cấp
- Có thể phê duyệt sau
- Phải bổ sung hồ sơ trong 1 tuần
- Thời gian xử lý: ≤ 4 giờ

### Cho sự cố nghiêm trọng (D3)

- Phải xử lý khẩn cấp ngay lập tức
- Có thể phê duyệt sau
- Phải bổ sung hồ sơ trong 1 tuần
- Phải báo cáo Lãnh đạo
- Thời gian xử lý: ≤ 1 giờ

### Nguyên tắc chung

- Ưu tiên khắc phục sự cố
- Có thể bỏ qua một số bước nếu khẩn cấp
- Phải bổ sung hồ sơ sau
- Phải đánh giá sau để rút kinh nghiệm

---

**Tham chiếu**:
- `QT-008-DANH_SACH_THAY_DOI_CHUAN.md`: Danh sách thay đổi chuẩn
- `QT-004-HOTFIX.md`: Quy trình Hotfix
- `TP-002-TEMPLATE_HOTFIX.md`: Template Hotfix Request

---

**Phiên bản**: 1.0

