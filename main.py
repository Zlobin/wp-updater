# python3 main.py

import urllib.request
import zipfile
import os
import shutil

# @TODO change it
# eg.: /var/www/blog
OLD_WP_PATH = ''
NEW_WP_PATH_TMP = ''

if not (os.path.exists(OLD_WP_PATH)) or not (os.path.exists(NEW_WP_PATH_TMP)):
  os._exit(0)

WP_URL = 'http://wordpress.org/latest.zip'
EXTRACTED_NAME = 'wordpress'

NEW_WP_PATH = os.path.join(NEW_WP_PATH_TMP, EXTRACTED_NAME)

# Download the file from url, save it in a temporary directory and get the
# path to it (e.g. '/tmp/tmpb43hma') in the `wp_archve` variable:
wp_archive, headers = urllib.request.urlretrieve(WP_URL)

with zipfile.ZipFile(wp_archive, 'r') as zf:
  zf.extractall(NEW_WP_PATH_TMP)

os.remove(wp_archive)

# Remove new files
shutil.rmtree(os.path.join(NEW_WP_PATH, 'wp-content'))
os.remove(os.path.join(NEW_WP_PATH, 'readme.html'))

# Copy content to the new WP
shutil.copy2(os.path.join(OLD_WP_PATH, 'wp-config.php'), NEW_WP_PATH)
shutil.copytree(os.path.join(OLD_WP_PATH, 'wp-content'), os.path.join(NEW_WP_PATH, 'wp-content'))

shutil.rmtree(OLD_WP_PATH)
shutil.copytree(NEW_WP_PATH, OLD_WP_PATH)
shutil.rmtree(NEW_WP_PATH)
