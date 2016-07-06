# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|

    config.vm.box = "ubuntu/trusty64"
    config.vm.provider "virtualbox" do |vb|
        # Display the VirtualBox GUI when booting the machine
        vb.gui = true
  
        # Customize the amount of memory on the VM:
        vb.memory = "1024"
        
        # Share a folder to the guest VM, types: docker, nfs, rsync, smb, virtualbox
        # Windows supports: smb
        # Mac supports: rsync, nfs
        # override.vm.synced_folder host_folder.to_s, guest_folder.to_s, type: "smb"
        override.vm.synced_folder "./provision", "/vagrant"
        override.vm.synced_folder "./data/website", "/var/www/sheparddb"
        
        # Create a forwarded port mapping which allows access to a specific port
        # within the machine from a port on the host machine. In the example below,
        # accessing "localhost:8080" will access port 80 on the guest machine.
        override.vm.network "forwarded_port", guest: 5432, host: 5432
        override.vm.network "forwarded_port", guest: 80, host: 8080
    end
    
    # default provisioning script
    config.vm.provision :shell, path: "./provision/bootstrap.sh"

end
