import moviepy.editor as mp

clip = mp.VideoFileClip('/home/mowshon/Downloads/green3.mp4')
background = mp.ImageClip('https://www.worldatlas.com/r/w728-h425-c728x425/upload/66/14/d8/kangchenjunga.jpg')

masked_clip = clip.fx(mp.vfx.mask_color, color=[51, 224, 58], thr=100, s=15)
masked_clip = masked_clip.resize(0.4).set_pos(('left', 'bottom'))

final_clip = mp.CompositeVideoClip([
    background,
    masked_clip
]).set_duration(1)

final_clip.write_videofile('test.mp4')