# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|

    config.vm.box = "ubuntu/trusty64"
    config.vm.provider "virtualbox" do |vb, override|
    
        vb.cpus = 1
        vb.gui = false
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
        override.vm.network "forwarded_port", guest: 5432, host: 5432 # postgres
        override.vm.network "forwarded_port", guest: 27017, host: 27017 # mongo
        override.vm.network "forwarded_port", guest: 80, host: 8080 # nginx
        override.vm.network "forwarded_port", guest: 80, host: 8000 # uwsgi
        override.vm.network "forwarded_port", guest: 9999, host: 9999 # Flask
    end
    
    # Configure Vagrant Cachier
    if Vagrant.has_plugin?("vagrant-cachier")
        config.cache.scope = :box
    end
    
    # default provisioning script
    config.vm.provision :shell, path: "./provision/bootstrap.sh"

end
