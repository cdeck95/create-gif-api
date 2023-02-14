from PIL import Image, ImageSequence

gif1 = Image.open("./gifphy-api/Golden.gif")
gif2 = Image.open("./gifphy-api/Rose.png")
gif3 = Image.open("./gifphy-api/AcidTab.png")
gif4 = Image.open("./gifphy-api/Turban.png")
gif5 = Image.open("./gifphy-api/Golden.png")
gif6 = Image.open("./gifphy-api/Sash.png")
background = Image.open("./gifphy-api/Transparent3.png")
frames = []
for gif1_frame in ImageSequence.Iterator(gif1):
	for gif2_frame in ImageSequence.Iterator(gif2):
		for gif3_frame in ImageSequence.Iterator(gif3):
			for gif4_frame in ImageSequence.Iterator(gif4):
				for gif5_frame in ImageSequence.Iterator(gif5):
					for gif6_frame in ImageSequence.Iterator(gif6):
						frame = background.copy()
						frame.paste(gif1_frame, mask=gif1_frame.convert("LA"))
						frame.paste(gif2_frame, mask=gif2_frame.convert("LA"))
						frame.paste(gif3_frame, mask=gif3_frame.convert("LA"))
						frame.paste(gif4_frame, mask=gif4_frame.convert("LA"))
						frame.paste(gif5_frame, mask=gif5_frame.convert("LA"))
						frame.paste(gif6_frame, mask=gif6_frame.convert("LA"))
						frames.append(frame)
frames[0].save("out2.gif", save_all=True, append_images=frames[1:], loop=0)
