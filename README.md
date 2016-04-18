# Shadowsocks commandline local client setup (Tested on Ubuntu)
1. Checkout the code
2. You need to install the shadowsocks by running `pip install shadowsocks`
3. Download your shadowsock server config json files to configs folder if you're using vpnso service
4. Running the script: `python vpnsso_config_converter.py` to convert the vpnso config files to the sslocal format
and save to the root folder
If you're not using vpnso service, keep your config file format like following under the project root folder
with file name like config_xx.json:
    {
        "server":"my ip",
        "server_port":8388,
        "local_port":1080,
        "password":"my password",
        "timeout":600,
        "method":"aes-256-cfb"
    }

5. Set the alias like:
`alias sso='/home/kelvin/DevTools/sso.sh'`
6. Run the commands: ssp xx to start or switch among the ss servers.
if you have config_xx.json, you can run `ssp xx`
and when you're ready to switch to config_yy.json, just run `ssp yy`,
it will automatically help you kill the exising process and recreate new one.
