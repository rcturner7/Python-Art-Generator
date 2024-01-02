import os
import itertools
import hashlib
from PIL import Image


def generate_image_hash(image):
    image_data = image.tobytes()
    return hashlib.sha256(image_data).hexdigest()


def get_image_paths(folder):
    return [os.path.join(folder, f) for f in sorted(os.listdir(folder)) if f.endswith(('.png', '.jpg', '.jpeg'))]


def main():
    base_path = "Layers"  # Replace with your actual path
    categories = ["backgrounds", "bodies", "eyes", "mouths", "hair"]
    image_paths = {category: get_image_paths(os.path.join(base_path, category)) for category in categories}
    existing_hashes = set()

    output_path = "Build"  # The directory where the images will be saved
    os.makedirs(output_path, exist_ok=True)  # Create the directory if it doesn't exist

    for combination in itertools.product(*[image_paths[category] for category in categories]):
        images = [Image.open(fp).convert("RGBA") for fp in combination]
        base_image = images[0]

        for overlay in images[1:]:
            base_image.paste(overlay, (0, 0), overlay)

        img_hash = generate_image_hash(base_image)
        if img_hash not in existing_hashes:
            existing_hashes.add(img_hash)
            base_image.save(os.path.join(output_path, f"{img_hash}.png"))


if __name__ == "__main__":
    main()
