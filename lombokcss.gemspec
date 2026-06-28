# frozen_string_literal: true

require_relative "lib/lombokcss/version"

Gem::Specification.new do |spec|
  spec.name        = "lombokcss"
  spec.version     = Lombokcss::VERSION
  spec.authors     = ["LombokCSS contributors"]
  spec.summary     = "Token-first component CSS framework. One markup, five design styles, dark + RTL."
  spec.description = "LombokCSS compiled assets packaged as a RubyGem for Rails/Sprockets and Ruby projects."
  spec.homepage    = "https://github.com/codinglombok/lombokcss"
  spec.license     = "MIT"
  spec.required_ruby_version = ">= 2.7"

  spec.metadata = {
    "homepage_uri"    => spec.homepage,
    "source_code_uri" => "https://github.com/codinglombok/lombokcss",
    "changelog_uri"   => "https://github.com/codinglombok/lombokcss/blob/main/CHANGELOG.md",
    "bug_tracker_uri" => "https://github.com/codinglombok/lombokcss/issues"
  }

  spec.files = Dir["dist/**/*", "src/**/*", "lib/**/*", "README.md", "LICENSE", "CHANGELOG.md"]
  spec.require_paths = ["lib"]
end
