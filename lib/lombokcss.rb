# frozen_string_literal: true

require "lombokcss/version"

# LombokCSS RubyGem — ships the compiled assets so Rails/Sprockets apps can
# include them. Example (config/initializers/assets.rb):
#
#   Rails.application.config.assets.paths << Lombokcss.assets_path
#
# then in your manifest:  *= require lombok.min
module Lombokcss
  # Repo root inside the installed gem.
  def self.root
    File.expand_path("..", __dir__)
  end

  # Path to the compiled CSS/JS (dist/).
  def self.assets_path
    File.join(root, "dist")
  end

  # Path to a specific asset, e.g. Lombokcss.asset("lombok.min.css").
  def self.asset(name)
    File.join(assets_path, name)
  end
end
