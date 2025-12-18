# BEST PRACTICES
## Chuẩn mực sử dụng Hệ thống Quy trình và Quy định

**Phiên bản**: 1.0

---

## NGUYÊN TẮC CHUNG

### 1. Tuân thủ quy trình

- **Luôn tuân thủ quy trình** - Không bỏ qua bước
- **Sử dụng checklist** - Đảm bảo không bỏ sót
- **Ghi log đầy đủ** - Để audit và troubleshooting

### 2. Tài liệu hóa

- **Điền template đầy đủ** - Không bỏ trống thông tin quan trọng
- **Lưu lại tài liệu** - Template, checklist đã hoàn thành
- **Cập nhật tài liệu** - Khi có thay đổi

### 3. An toàn và kiểm soát

- **Phê duyệt trước khi thực hiện** - Trừ trường hợp khẩn cấp
- **Test trước khi deploy** - Không deploy trực tiếp lên Production
- **Có kế hoạch rollback** - Luôn chuẩn bị sẵn

---

## CHUẨN MỰC THEO QUY TRÌNH

### 1. Upcode (QT-003)

#### Nên làm

- **Tra cứu mã thay đổi trước**: Sử dụng `TP-005` và `QT-008`
- **Tạo RFC đầy đủ**: Sử dụng `TP-001`, xem `TP-001-EXAMPLE_RFC.md`
- **Phê duyệt trước khi deploy**: Trừ trường hợp khẩn cấp
- **Test trên Staging trước**: Không deploy trực tiếp lên Production
- **Sử dụng checklist**: `CL-002` và checklist theo nhóm (CL-007 đến CL-010)
- **Ghi log đầy đủ**: Mọi thao tác đều được ghi log

#### Không nên làm

- Deploy mà không có RFC
- Bỏ qua phê duyệt
- Deploy trực tiếp lên Production mà không test
- Bỏ qua checklist
- Không ghi log

#### Tips

- **Sử dụng Quick Reference**: `QUICK_REFERENCE_THAY_DOI.md` để tra cứu nhanh
- **Xem example**: `TP-001-EXAMPLE_RFC.md` để hiểu cách điền template
- **In checklist**: In checklist ra và đánh dấu khi thực hiện

---

### 2. Hotfix (QT-004)

#### Nên làm

- **Tạo Hotfix Request ngay**: Sử dụng `TP-002`
- **Phê duyệt khẩn cấp**: Có thể phê duyệt nhanh qua chat/phone
- **Test nhanh nhưng đầy đủ**: Test critical path
- **Sử dụng checklist**: `CL-003`
- **Ghi log đầy đủ**: Đặc biệt quan trọng với hotfix
- **Tạo RFC sau**: Tạo RFC đầy đủ sau khi hotfix thành công

#### Không nên làm

- Hotfix mà không có Hotfix Request
- Bỏ qua test hoàn toàn
- Không ghi log
- Quên tạo RFC sau

#### Tips

- **Ưu tiên fix**: Fix lỗi trước, tài liệu sau (nhưng không bỏ qua)
- **Thông báo ngay**: Thông báo cho team ngay khi bắt đầu hotfix
- **Review sau**: Review hotfix sau khi hoàn thành để cải thiện

---

### 3. Release (QT-007)

#### Nên làm

- **Quản lý version trước**: Sử dụng `QT-006`
- **Tạo Release Note đầy đủ**: Sử dụng `TP-003`
- **Test kỹ lưỡng**: Test đầy đủ trên Staging
- **Sử dụng checklist**: `CL-005`
- **Thông báo trước**: Thông báo cho team và stakeholders
- **Monitor sau release**: Monitor hệ thống sau khi release

#### Không nên làm

- Release mà không có Release Note
- Release vào giờ cao điểm
- Release mà không test
- Không monitor sau release

#### Tips

- **Release vào giờ thấp điểm**: Tránh giờ cao điểm
- **Có rollback plan**: Luôn chuẩn bị sẵn kế hoạch rollback
- **Thông báo rõ ràng**: Thông báo rõ ràng về thay đổi và impact

---

### 4. Provisioning (QT-005)

#### Nên làm

- **Tạo Provisioning Request đầy đủ**: Sử dụng `TP-004`
- **Xác định rõ yêu cầu**: Resource, config, network, security
- **Phê duyệt trước**: Phê duyệt trước khi tạo resource
- **Sử dụng checklist**: `CL-004`
- **Ghi log đầy đủ**: Ghi log mọi resource được tạo
- **Tag resource**: Tag resource để quản lý

#### Không nên làm

- Tạo resource mà không có request
- Tạo resource mà không tag
- Không ghi log
- Không xác định rõ yêu cầu

#### Tips

- **Sử dụng template**: Sử dụng `TP-004` để đảm bảo đầy đủ thông tin
- **Xem example**: `TP-004-EXAMPLE_PROVISIONING.md` để tham khảo
- **Review định kỳ**: Review resource định kỳ để tối ưu

---

### 5. Quyền Truy Cập

#### Nên làm

- **Tra cứu quyền trước**: Sử dụng `QUICK_REFERENCE_QUYEN_TRUY_CAP.md`
- **Tạo yêu cầu đầy đủ**: Sử dụng `TP-006`
- **Phê duyệt đúng cấp**: Xem Quick Reference để biết cấp phê duyệt
- **Sử dụng checklist**: `CL-011`
- **Rà soát định kỳ**: Rà soát quyền định kỳ
- **Thu hồi khi không dùng**: Thu hồi quyền khi không còn cần

#### Không nên làm

- Cấp quyền mà không có yêu cầu
- Cấp quyền dư thừa
- Không rà soát định kỳ
- Không thu hồi quyền không dùng

#### Tips

- **Sử dụng JIT**: Sử dụng quyền tạm thời (JIT) khi có thể
- **Least Privilege**: Chỉ cấp quyền tối thiểu cần thiết
- **MFA**: Kích hoạt MFA cho tài khoản admin

---

## CHUẨN MỰC SỬ DỤNG TEMPLATE

### 1. Luôn xem Example trước

- Xem example file trước khi điền template
- Copy example và chỉnh sửa
- Giữ format và cấu trúc

### 2. Điền đầy đủ thông tin

- Không bỏ trống thông tin quan trọng
- Điền rõ ràng, dễ hiểu
- Sử dụng format chuẩn (date, version, etc.)

### 3. Lưu lại template đã điền

- Lưu lại template đã điền
- Đặt tên file rõ ràng (ví dụ: RFC-2024-12-17-Deploy-2FA.md)
- Lưu vào thư mục phù hợp

---

## CHUẨN MỰC SỬ DỤNG CHECKLIST

### 1. Sử dụng checklist trong mọi trường hợp

- Luôn sử dụng checklist khi thực hiện quy trình
- Không bỏ qua checklist
- Đánh dấu từng bước khi hoàn thành

### 2. Lưu lại checklist đã hoàn thành

- Lưu lại checklist đã hoàn thành
- Ghi ngày tháng và người thực hiện
- Lưu để audit

### 3. Cập nhật checklist nếu cần

- Nếu phát hiện thiếu bước, đề xuất cập nhật
- Không tự ý bỏ qua bước trong checklist

---

## CHUẨN MỰC GHI LOG

### 1. Ghi log đầy đủ

- Ghi log mọi thao tác quan trọng
- Ghi log với timestamp
- Ghi log với user/account thực hiện

### 2. Format log chuẩn

```
[YYYY-MM-DD HH:MM:SS] [USER] [ACTION] [RESOURCE] [RESULT]
```

**Ví dụ**:
```
[2024-12-17 10:30:00] [devops-user] [DEPLOY] [user-service:v1.2.3] [SUCCESS]
```

### 3. Lưu log

- Lưu log vào hệ thống log tập trung
- Backup log định kỳ
- Giữ log theo retention policy

---

## CHUẨN MỰC PHÊ DUYỆT

### 1. Phê duyệt đúng cấp

- Xác định đúng cấp phê duyệt
- Gửi phê duyệt đúng người
- Chờ phê duyệt trước khi thực hiện

### 2. Phê duyệt nhanh cho khẩn cấp

- Hotfix có thể phê duyệt nhanh qua chat/phone
- Ghi log phê duyệt sau
- Không lạm dụng phê duyệt nhanh

### 3. Ghi log phê duyệt

- Ghi log người phê duyệt
- Ghi log thời gian phê duyệt
- Ghi log lý do phê duyệt (nếu có)

---

## CHUẨN MỰC TEST

### 1. Test trước khi deploy

- Test trên Development trước
- Test trên Staging trước khi Production
- Test critical path

### 2. Test đầy đủ

- Test chức năng
- Test performance
- Test security (nếu cần)
- Test rollback

### 3. Ghi log test

- Ghi log kết quả test
- Ghi log người test
- Ghi log thời gian test

---

## CHUẨN MỰC ROLLBACK

### 1. Luôn có kế hoạch rollback

- Chuẩn bị kế hoạch rollback trước khi deploy
- Test rollback trên Staging
- Ghi log kế hoạch rollback

### 2. Thực hiện rollback khi cần

- Rollback ngay khi phát hiện vấn đề nghiêm trọng
- Không cố gắng fix trên Production
- Ghi log rollback

### 3. Review sau rollback

- Review nguyên nhân rollback
- Cải thiện quy trình
- Ghi log review

---

## CHUẨN MỰC MONITORING

### 1. Monitor sau deploy

- Monitor hệ thống sau deploy
- Monitor metrics quan trọng
- Monitor logs

### 2. Alert khi có vấn đề

- Cấu hình alert cho metrics quan trọng
- Phản ứng nhanh khi có alert
- Ghi log alert

### 3. Review định kỳ

- Review metrics định kỳ
- Tối ưu hệ thống
- Cải thiện monitoring

---

## CHECKLIST CHUẨN MỰC

### Trước khi thực hiện

- [ ] Đã xác định đúng quy trình
- [ ] Đã tìm đúng template
- [ ] Đã tìm đúng checklist
- [ ] Đã xem example (nếu có)
- [ ] Đã hiểu rõ quy trình

### Khi thực hiện

- [ ] Đã điền template đầy đủ
- [ ] Đã được phê duyệt (nếu cần)
- [ ] Đã test (nếu cần)
- [ ] Đã sử dụng checklist
- [ ] Đã ghi log đầy đủ

### Sau khi hoàn thành

- [ ] Đã lưu lại template
- [ ] Đã lưu lại checklist
- [ ] Đã thông báo cho người liên quan
- [ ] Đã monitor (nếu cần)
- [ ] Đã cập nhật tài liệu (nếu cần)

---

**Phiên bản**: 1.0 
**Ngày cập nhật**: 2024-12-17

