Vagrant.configure('2') do |config|
  config.vm.box = 'centos/7'
  # rsync is uni-directional. Some files are created on the server like db migrations.
  config.vm.synced_folder('.',  '/vagrant', :owner => 1900, :group => 1900)
  excluded_folders = [
    '.git',
    '.idea',
  ]
  config.vm.synced_folder(
    '.',
    '/home/deploy/harmony-cloud-test/local/',
    owner: 1900,
    group: 1900,
    type: "rsync",
    rsync__chown: true,
    rsync__exclude: excluded_folders
  )

  config.vm.hostname = 'local-cgroup.harmonycloud.com'
  config.vm.network :private_network, ip: '172.16.29.234'

  config.vm.provider "virtualbox" do |v|
    v.name = "oonandbazul"
    v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    v.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
    v.cpus = 2
    v.memory = 2048
  end
end
