import Gallery
import Picture
import Client

class Photographer:
	def __init__(self, name, photos=[], clients=[]):
		self.name = name
		self.photos = photos
		self.clients = clients
		print(f"new photographer: {self.name}. ")

	def create_client(self, client_name):
		new_client = Client.Client(client_name)
		self.clients.append(new_client)
		return self.clients

	# create a photo and assign filename and client_name
	def create_photo(self, filename, client_name):
		new_photo = Picture.Picture(filename,client_name)
		self.photos.append(new_photo)
		return self.photos       

	# if client.pyayment_status=True, then make client.is_atuhorized = True and add photos to gallery with same client_name
	def authorize_client(self, client_name):
		client_photos = []
		authorized_client = ""
		client_gallery = ""
		for photo in self.photos:
			if photo.client_name == client_name:
				client_photos.append(photo)
		for client in self.clients:
			if (client.name == client_name) and client.payment_status:
				client.is_authorized = True
				authorized_client = client
				# adding photos to the gallery and return the Gallery()
				client_gallery = Gallery.Gallery(client_name, client_photos)
				return client_gallery

# STEP 1: create a photographer
ahmed = Photographer("Ahmed")

# STEP 2: create a client
clients = ahmed.create_client("client-1")
print("\nprinting all clients of Ahmed")
for client in clients:
	print(client.name)

# STEP 3: create multiple photos for one client
print("\ncreating photos for one client")
ahmed.create_photo("picture-1", "client-1")
print("created one photo: picture-1, client name: client-1 ")
ahmed.create_photo("picture-2", "client-1")
print("created one photo: picture-2, client name: client-1 ")
photo_list = ahmed.create_photo("picture-3", "client-1")
print("created one photo: picture-3, client name: client-1 ")
print("\nprinting all photos captured by our photographer: ahmed")
for photo in photo_list:
	print(f"filename:{photo.filename} client: {photo.client_name}")

# STEP 4: if client-1 made payment, authorize clien-1 to acces their photos (assuming client.payment_status = True)
print("\nDisplaying client-1 gallery:\n")
gallery = ahmed.authorize_client("client-1")
gallery.display()