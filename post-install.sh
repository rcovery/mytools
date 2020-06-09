#Installing sublime text
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
sudo apt-get install apt-transport-https
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list

#Installing draw.io
wget https://github.com/jgraph/drawio-desktop/releases/download/v13.0.3/draw.io-amd64-13.0.3.deb
sudo dpkg -i draw.io-amd-13.0.3.deb

#Installing brave-browser
curl -s https://brave-browser-apt-release.s3.brave.com/brave-core.asc | sudo apt-key --keyring /etc/apt/trusted.gpg.d/brave-browser-release.gpg add -
echo "deb [arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list

#Installing WPS Office
wget http://wdl1.pcfg.cache.wpscdn.com/wpsdl/wpsoffice/download/linux/9522/wps-office_11.1.0.9522.XA_amd64.deb -O wps.deb
sudo dpkg -i wps.deb

#Installing spotify
curl -sS https://download.spotify.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list

#Downloading brModelo
wget http://www.sis4.com/brModelo/brModelo.jar
sudo mv brModelo.jar /opt/
sudo apt-get update
sudo apt-get install sublime-text kdenlive gimp brave-browser spotify-client
