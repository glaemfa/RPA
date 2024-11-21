import qrcode

student_id = input("학번을 입력하세요: ")
name = input("이름을 입력하세요: ")
major = input("전공을 입력하세요: ")

qr_data = f"학번: {student_id}\n이름: {name}\n전공: {major}"

qr_img = qrcode.make(qr_data)

save_path = 'my_info_data.png'
qr_img.save(save_path)

print(f"QR 코드가 성공적으로 생성되어 {save_path}에 저장되었습니다.")
