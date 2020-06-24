Pod::Spec.new do |s|
  s.name             = 'Dependency'
  s.version          = '1.0.0'
  s.summary          = 'Summary of Dependency.'
  s.description      = 'Description of Dependency.'
  s.homepage         = 'https://github.com/postmates/ios-pod-template'
  s.author           = 'Postmates Inc'
  s.license          = 'Copyright'
  s.source           = { :git => 'git@github.com:postmates/ios-pod-template.git', :tag => "v#{s.version}" }
  s.ios.deployment_target = '10.0'
  s.swift_version = '5.0'
  s.source_files = 'Sources/*.swift'
end
