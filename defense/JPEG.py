import torch
from torchvision import transforms
from PIL import Image
from io import BytesIO#BytesIO实现了在内存中读写bytes
_to_pil_image = transforms.ToPILImage()
_to_tensor = transforms.ToTensor()

def jpeg_compression(x):
    lst_img = []
    for img in x:
        img = _to_pil_image(img.detach().clone().cpu())
        virtualpath = BytesIO()
        img.save(virtualpath, 'JPEG', quality=75)#压缩成jpeg
        lst_img.append(_to_tensor(Image.open(virtualpath)))
    return x.new_tensor(torch.stack(lst_img)).to(x.device)