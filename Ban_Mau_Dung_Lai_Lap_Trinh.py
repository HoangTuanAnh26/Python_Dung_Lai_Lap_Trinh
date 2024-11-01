
# import datetime

# def ask_yes_no(prompt):
# 	while True:
# 		answer = input(prompt)
# 		if answer == "yes":
# 			return True
# 		elif answer == "no":
# 			return False
# 		else:
# 			continue

# def calculate_age(year_born):
# 	now = datetime.datetime.now()
# 	CURRENT_YEAR = now.year
# 	return CURRENT_YEAR - year_born

# def convert_meter_to_feet(meter):
# 	METER_TO_FEET = 3.281
# 	feet = meter * METER_TO_FEET
# 	feet = round(feet,1)
# 	return feet

# def print_height_info(height_feet, is_male):
# 	if is_male == True:
# 		if height_feet > 6.5:
# 			print("You are", end=" ")
# 			for i in range(10):
# 				print("very", end=" ")
# 			print("tall as a man")
# 		elif height_feet > 6.0:
# 			print("You are tall as a man")
# 		else:
# 			print("You are short as a man")
# 	else:
# 		if height_feet > 5.7:
# 			print("You are tall as a girl")
# 		elif height_feet < 5.0:
# 			print("You are", end=" ")
# 			i=0
# 			while i<10:
# 				print("very ", end = "")
# 				i+=1
# 			print("short as a girl")
# 		else:
# 			print("You are short as a girl")	

# def print_person_info(firstname, lastname, age, height_feet, is_vietnamese, is_male):
# 	now = datetime.datetime.now()
# 	CURRENT_YEAR = now.year
# 	print("\n---")
# 	print("Your name is " + firstname + " " + lastname)
# 	print("{2} is {0} years old in {1}".format(age,CURRENT_YEAR,firstname))
# 	print("You are " + str(height_feet) + " feet tall")
# 	if is_vietnamese:
# 		print("You are from Vietnam")
# 	else:
# 		print("You are not from Vietnam")
# 	print_height_info(height_feet, is_male)

# def ask_person_info():
# 	firstname = input("Your firstname: ")
# 	lastname = input("Your lastname: ")
# 	year_born = int(input("When you were born: "))
# 	height_meter = float(input("Your height (meter): "))
# 	is_male = ask_yes_no("Are you male (yes/no): ")
# 	is_vietnamese = ask_yes_no("Are you Vietnamese (yes/no): ")
# 	return firstname, lastname, year_born, height_meter, is_male, is_vietnamese

# def main():
# 	firstname, lastname, year_born, height_meter, is_male, is_vietnamese = ask_person_info()
# 	age = calculate_age(year_born)
# 	height_feet = convert_meter_to_feet(height_meter)
# 	print_person_info(firstname, lastname, age, height_feet, is_vietnamese, is_male)

# main()





# def calc_total_price(apple_weight, APPLE_PRICE):
# 	return apple_weight * APPLE_PRICE

# def calc_return(total_price, money_given):
# 	if money_given < total_price:
# 		return -1
	
# 	return money_given - total_price

# def print_return_info(total):
# 	# 500 200 100 50 20 10 1 
# 	count_500 = int(total/500)
# 	total = total - 500*count_500
# 	if count_500 != 0:
# 		print("500k : " + str(count_500))

# 	count_200 = int(total/200)
# 	total = total - 200*count_200
# 	if count_200 != 0:
# 		print("200k : " + str(count_200))

# 	count_100 = int(total/100)
# 	total = total - 100*count_100
# 	if count_100 != 0:
# 		print("100k : " + str(count_100))

# 	count_50 = int(total/50)
# 	total = total - 50*count_50
# 	if count_50 != 0:
# 		print("50k : " + str(count_50))

# 	count_20 = int(total/20)
# 	total = total - 20*count_20
# 	if count_20 != 0:
# 		print("20k : " + str(count_20))

# 	count_10 = int(total/10)
# 	total = total - 10*count_10
# 	if count_10 != 0:
# 		print("10k : " + str(count_10))

# 	count_1 = int(total)
# 	if count_1 != 0:
# 		print("1k : " + str(count_1))

# def main():
# 	APPLE_PRICE = 21 # k VND
# 	apple_weight = input("Enter weight of apples: ")
# 	money_given = input("Total money customer give you: ")

# 	apple_weight = float(apple_weight)
# 	money_given = float(money_given)

# 	total_price = calc_total_price(apple_weight, APPLE_PRICE)
# 	money_return = calc_return(total_price, money_given)
	
# 	print("Total price: " + str(int(total_price)))

# 	if money_return == -1:
# 		print("Not enough cash")
# 	else:
# 		print("You need to return to customer: " + str(round(money_return,2)))
# 		print_return_info(money_return)

# main()





# import webbrowser

# class Video:
# 	def __init__(self, title, link):
# 		self.title = title
# 		self.link = link
# 		self.seen = False

# 	def open(self):
# 		webbrowser.open(self.link)
# 		self.seen = True

# class Playlist:
# 	def __init__(self, name, description, rating, videos):
# 		self.name = name
# 		self.description = description
# 		self.rating = rating
# 		self.videos = videos

# def read_video():
# 	title = input("Enter title: ") + "\n"
# 	link = input("Enter link: ") + "\n"
# 	video = Video(title, link)
# 	return video

# def print_video(video):
# 	print("Video title: ", video.title, end="")
# 	print("Video link: ", video.link, end="")

# def read_videos():
# 	videos = []
# 	total_video = int(input("Enter how many videos: "))
# 	for i in range(total_video):
# 		print("Enter video ", i+1)
# 		vid = read_video()
# 		videos.append(vid)
# 	return videos

# def print_videos(videos):
# 	for i in range(len(videos)):
# 		print("Video " + str(i+1) + ":")
# 		print_video(videos[i])

# def write_video_txt(video, file):
# 	file.write(video.title)
# 	file.write(video.link)

# def write_videos_txt(videos, file):
# 	total = len(videos)
# 	file.write(str(total) + "\n")
# 	for i in range(total):
# 		write_video_txt(videos[i], file)

# def read_video_from_txt(file):
# 	title = file.readline()
# 	link = file.readline()
# 	video = Video(title, link)
# 	return video

# def read_videos_from_txt(file):
# 	videos = []
# 	total = file.readline()		
# 	for i in range(int(total)):
# 		video = read_video_from_txt(file)
# 		videos.append(video)
# 	return videos

# def read_playlist():
# 	playlist_name = input("Enter playlist name: ") + "\n"
# 	playlist_description = input("Enter playlist description: ") + "\n"
# 	playlist_rating = input("Enter rating (1-5): ") + "\n"
# 	playlist_videos = read_videos()
# 	playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
# 	return playlist

# def write_playlist_txt(playlist):
# 	with open("data.txt", "w") as file:
# 		file.write(playlist.name)
# 		file.write(playlist.description)
# 		file.write(playlist.rating)
# 		write_videos_txt(playlist.videos, file)
# 	print("Successfully write playlist to txt")

# def read_playlist_from_txt():
# 	with open("data.txt", "r") as file:
# 		playlist_name = file.readline()
# 		playlist_description = file.readline()
# 		playlist_rating = file.readline()
# 		playlist_videos = read_videos_from_txt(file)
# 	playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
# 	return playlist

# def print_playlist(playlist):
# 	print("-------")
# 	print("Playlist name: " +  playlist.name, end="")
# 	print("Playlist description: " +  playlist.description, end="")
# 	print("Playlist rating: " +  playlist.rating, end="")
# 	print_videos(playlist.videos)

# def show_menu():
# 	print("Main Menu:")
# 	print("-----------------------------")
# 	print("| Option 1: Create playlist |")
# 	print("| Option 2: Show playlist   |")
# 	print("| Option 3: Play a video    |")
# 	print("| Option 4: Add a video     |")
# 	print("| Option 5: Update playlist |")
# 	print("| Option 6: Remove video    |")
# 	print("| Option 7: Save and Exit   |")
# 	print("-----------------------------")

# def select_in_range(prompt, min, max):
# 	choice = input(prompt)
# 	while not choice.isdigit() or int(choice) < min or int(choice) > max:
# 		choice = input(prompt)

# 	choice = int(choice)
# 	return choice

# def play_video(playlist):
# 	print_videos(playlist.videos)
# 	total = len(playlist.videos)

# 	choice = select_in_range("Select a video (1," + str(total) + "): " , 1,total)
# 	print("Open video: " + playlist.videos[choice-1].title + " - " + playlist.videos[choice-1].link, end ="")
# 	playlist.videos[choice-1].open()

# def add_video(playlist):
# 	print("Enter new video information:")
# 	new_video_title = input("Enter new video title: ") + "\n"
# 	new_video_link =  input("Enter new video link: ") + "\n"
# 	new_video = Video(new_video_title, new_video_link)
# 	playlist.videos.append(new_video)
# 	return playlist

# def update_playlist(playlist):
# 	# Update name / description / rating
# 	print("Update playlist?")
# 	print("1. Name")	
# 	print("2. Description")	
# 	print("3. Rating")	

# 	choice = select_in_range("Enter what you want to update (1-3):", 1,3)
# 	if choice == 1:
# 		new_playlist_name = input("Enter new name for playlist: ") + "\n"
# 		playlist.name = new_playlist_name
# 		print("Updated Successfully !")
# 		return playlist
# 	if choice == 2:
# 		new_playlist_description = input("Enter new description for playlist: ") + "\n"
# 		playlist.description = new_playlist_description
# 		print("Updated Successfully !")
# 		return playlist
# 	if choice == 3:
# 		new_playlist_rating = str(select_in_range("Enter new rating (1-5): ",1,5)) + "\n"
# 		playlist.rating = new_playlist_rating
# 		print("Updated Successfully !")
# 		return playlist

# def remove_video(playlist):
# 	print_videos(playlist.videos)
# 	choice = select_in_range("Enter video you want to delete: ",1,len(playlist.videos))
# 	new_video_list = []
# 	# del playlist.videos[choice-1]
# 	for i in range(len(playlist.videos)):
# 		if i == choice-1:
# 			continue
# 		new_video_list.append(playlist.videos[i])

# 	playlist.videos = new_video_list

# 	print("Delete Successfully !!!")
# 	return playlist

# def main():
# 	try:
# 		playlist = read_playlist_from_txt()
# 		print("Loaded data Successfully !!!")
# 	except:
# 		print("Welcome first user !!!")		

# 	while True:
# 		show_menu()
# 		choice = select_in_range("Select an option (1-7):", 1, 7)
# 		if choice == 1:
# 			playlist = read_playlist()	
# 			input("\nPress Enter to continue.\n")	
# 		elif choice == 2:
# 			print_playlist(playlist)
# 			input("\nPress Enter to continue.\n")	
# 		elif choice == 3:
# 			play_video(playlist)	
# 			input("\nPress Enter to continue.\n")	
# 		elif choice == 4:
# 			playlist = add_video(playlist)	
# 			input("\nPress Enter to continue.\n")
# 		elif choice == 5:
# 			playlist = update_playlist(playlist)	
# 			input("\nPress Enter to continue.\n")
# 		elif choice == 6:
# 			playlist = remove_video(playlist)	
# 			input("\nPress Enter to continue.\n")
# 		elif choice == 7:
# 			write_playlist_txt(playlist)
# 			input("\nPress Enter to continue.\n")	
# 			break
# 		else:
# 			print("Wrong Input, Exist.")
# 			break
			
# main()






import pygame
import webbrowser

# Lớp Video đại diện cho mỗi video với tiêu đề và đường dẫn (link) kèm trạng thái đã xem
class Video:
	def __init__(self, title, link):
		self.title = title  # Tiêu đề video
		self.link = link  # Đường dẫn video
		self.seen = False  # Trạng thái đã xem video hay chưa

	# Phương thức mở video trong trình duyệt
	def open(self):
		webbrowser.open(self.link)  # Mở trình duyệt với đường dẫn của video
		print("Open " + self.title)  # In ra thông báo video đang mở
		self.seen = True  # Đánh dấu video đã được xem

# Lớp Playlist đại diện cho danh sách phát với thông tin và danh sách video
class Playlist:
	def __init__(self, name, description, rating, videos):
		self.name = name  # Tên danh sách phát
		self.description = description  # Mô tả danh sách phát
		self.rating = rating  # Đánh giá danh sách phát
		self.videos = videos  # Danh sách video trong playlist

# Lớp TextButton để vẽ các nút (button) có chứa văn bản
class TextButton:
	def __init__(self, text, position):
		self.text = text  # Nội dung văn bản của nút
		self.position = position  # Vị trí hiển thị của nút

	# Kiểm tra xem con chuột có đang nằm trên văn bản không
	def is_mouse_on_text(self):
		mouse_x, mouse_y = pygame.mouse.get_pos()  # Lấy vị trí của con trỏ chuột
		# Kiểm tra vị trí chuột có nằm trong vùng văn bản hay không
		if mouse_x > self.position[0] and mouse_x < self.position[0] + self.text_box[2] and mouse_y > self.position[1] and mouse_y < self.position[1] + self.text_box[3]:
			return True
		else:
			return False

	# Phương thức vẽ văn bản của nút trên màn hình
	def draw(self):
		font = pygame.font.SysFont('sans', 30)  # Khởi tạo font chữ
		text_render = font.render(self.text, True, (0, 0, 255))  # Vẽ văn bản
		self.text_box = text_render.get_rect()  # Lấy kích thước của hộp văn bản

		# Kiểm tra nếu chuột đang ở trên văn bản, tô màu xanh và kẻ đường kẻ dưới văn bản
		if self.is_mouse_on_text():
			text_render = font.render(self.text, True, (0, 0, 255))  # Tô màu xanh chữ
			pygame.draw.line(screen, (0, 0, 255), (self.position[0], self.position[1] + self.text_box[3]), (self.position[0] + self.text_box[2], self.position[1] + self.text_box[3]))  # Kẻ gạch dưới
		else:
			text_render = font.render(self.text, True, (0, 0, 0))  # Tô màu đen nếu chuột không ở trên văn bản

		screen.blit(text_render, self.position)  # Vẽ văn bản lên màn hình

# Đọc thông tin về một video từ file
def read_video_from_txt(file):
	title = file.readline()  # Đọc tiêu đề video
	link = file.readline()  # Đọc đường dẫn video
	video = Video(title, link)  # Tạo đối tượng video từ tiêu đề và link
	return video

# Đọc danh sách các video từ file
def read_videos_from_txt(file):
	videos = []
	total = file.readline()  # Đọc tổng số video trong file		
	for i in range(int(total)):  # Duyệt qua từng video và đọc thông tin
		video = read_video_from_txt(file)  # Đọc video từ file
		videos.append(video)  # Thêm video vào danh sách
	return videos

# Đọc một danh sách phát từ file
def read_playlist_from_txt(file):
	playlist_name = file.readline()  # Đọc tên danh sách phát
	playlist_description = file.readline()  # Đọc mô tả danh sách phát
	playlist_rating = file.readline()  # Đọc đánh giá danh sách phát
	playlist_videos = read_videos_from_txt(file)  # Đọc danh sách video trong danh sách phát
	playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)  # Tạo đối tượng playlist
	return playlist

# Đọc tất cả danh sách phát từ file
def read_playlists_from_txt():
	playlists = []
	with open("data.txt", "r") as file:
		total = file.readline()  # Đọc tổng số danh sách phát
		for i in range(int(total)):  # Duyệt qua từng danh sách phát
			playlist = read_playlist_from_txt(file)  # Đọc danh sách phát từ file
			playlists.append(playlist)  # Thêm danh sách phát vào danh sách
	return playlists


# Khởi tạo Pygame
pygame.init()
screen = pygame.display.set_mode((600, 400))  # Thiết lập kích thước màn hình
pygame.display.set_caption('Pygame App')  # Đặt tiêu đề cho cửa sổ Pygame
running = True  # Cờ điều khiển vòng lặp chính
clock = pygame.time.Clock()  # Khởi tạo đồng hồ để điều chỉnh tốc độ vòng lặp

# Tải dữ liệu danh sách phát
playlists = read_playlists_from_txt()  # Đọc danh sách phát từ file
videos_btn_list = []  # Danh sách các nút video
playlists_btn_list = []  # Danh sách các nút danh sách phát
margin = 50  # Khoảng cách giữa các nút
playlist_choice = None  # Lựa chọn hiện tại của người dùng

# Tạo nút cho mỗi danh sách phát
for i in range(len(playlists)):
	playlist_btn = TextButton(playlists[i].name.rstrip(), (50, 50 + margin * i))  # Tạo nút danh sách phát
	playlists_btn_list.append(playlist_btn)  # Thêm nút vào danh sách

# Vòng lặp chính của chương trình
while running:		
	clock.tick(60)  # Giới hạn FPS của vòng lặp là 60
	screen.fill((255,255,0))  # Tô màu vàng cho màn hình

	# Vẽ các nút danh sách phát lên màn hình
	for playlist_button in playlists_btn_list:
		playlist_button.draw()

	# Vẽ các nút video lên màn hình
	for video_button in videos_btn_list:
		video_button.draw()

	# Xử lý các sự kiện của Pygame
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:  # Kiểm tra nếu có sự kiện nhấn chuột
			if event.button == 1:  # Nếu nhấn chuột trái
				for i in range(len(playlists_btn_list)):  # Kiểm tra nếu người dùng nhấn vào nút danh sách phát
					if playlists_btn_list[i].is_mouse_on_text(): 	
						playlist_choice = i  # Ghi lại danh sách phát mà người dùng chọn
						videos_btn_list = []  # Xóa danh sách nút video cũ
						# Tạo các nút video tương ứng với danh sách phát đã chọn
						for j in range(len(playlists[i].videos)):
							video_btn = TextButton(str(j + 1) + ". " + playlists[i].videos[j].title.rstrip(), (250, 50 + margin * j))
							videos_btn_list.append(video_btn)

				# Nếu đã chọn danh sách phát, kiểm tra nếu người dùng nhấn vào một video
				if playlist_choice != None:
					for i in range(len(videos_btn_list)):
						if videos_btn_list[i].is_mouse_on_text():
							playlists[playlist_choice].videos[i].open()  # Mở video đã chọn

		if event.type == pygame.QUIT:  # Kiểm tra nếu người dùng thoát ứng dụng
			running = False  # Thoát khỏi vòng lặp

	pygame.display.flip()  # Cập nhật màn hình sau mỗi vòng lặp

pygame.quit()  # Kết thúc Pygame khi vòng lặp chính dừng lại
