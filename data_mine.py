import pylab
import imageio


def show_image(filename = None, list_frames = None):
    """Show a set of images from a video.

    Args:
        filename: String going to the directory
        list_frames: A list of frames to be investigated

    Returns:
        Individual dialog boxes with the desired image
    """
    if filename is None:
        return "Insert a correct filepath."
    if list_frames is None:
        return "Add a list to the function."
    else:
        vid = imageio.get_reader(filename, 'ffmpeg')
        for num in list_frames:
            image = vid.get_data(num)
            image_dim_length = image.shape[1]
            image_dim_height = image.shape[0]
            fig = pylab.figure()
            fig.suptitle('image #{} Height {} Length {}'.format(num, image_dim_height, image_dim_length), fontsize=20)
            pylab.imshow(image)
        pylab.show()
