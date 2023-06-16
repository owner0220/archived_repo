require_relative "../../../base"

require "vagrant/util/template_renderer"

describe "templates/guests/redhat/network_dhcp" do
  let(:template) { "guests/redhat/network_dhcp" }

  it "renders the template" do
    result = Vagrant::Util::TemplateRenderer.render(template, options: {
      device: "en0",
    })
    expect(result).to eq <<-EOH.gsub(/^ {6}/, "")
      #VAGRANT-BEGIN
      # The contents below are automatically generated by Vagrant. Do not modify.
      BOOTPROTO=dhcp
      ONBOOT=yes
      DEVICE=en0
      NM_CONTROLLED=no
      #VAGRANT-END
    EOH
  end

  it "renders the template with NetworkManager enabled" do
    result = Vagrant::Util::TemplateRenderer.render(template, options: {
      device: "en0",
      nm_controlled: "yes"
    })
    expect(result).to eq <<-EOH.gsub(/^ {6}/, "")
      #VAGRANT-BEGIN
      # The contents below are automatically generated by Vagrant. Do not modify.
      BOOTPROTO=dhcp
      ONBOOT=yes
      DEVICE=en0
      NM_CONTROLLED=yes
      #VAGRANT-END
    EOH
  end

end
