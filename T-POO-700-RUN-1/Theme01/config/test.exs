import Config

# Configure your database
#
# The MIX_TEST_PARTITION environment variable can be used
# to provide built-in test partitioning in CI environment.
# Run `mix help test` for more information.
config :timeManager, Todolist.Repo,
  username: "postgres",
  password: "postgres",
  database: "timemanager_test#{System.get_env("MIX_TEST_PARTITION")}",
  hostname: "localhost",
  pool: Ecto.Adapters.SQL.Sandbox,
  pool_size: 10

# We don't run a server during test. If one is required,
# you can enable the server option below.
config :timeManager, TodolistWeb.Endpoint,
  http: [ip: {127, 0, 0, 1}, port: 4002],
  secret_key_base: "U2+OnCyu8p0BZ3HixUaTS67CMpiMg3rpyeV1w3MfgQJeDif9pRVePs7N5vfhwIgu",
  server: false

# In test we don't send emails.
config :timeManager, Todolist.Mailer, adapter: Swoosh.Adapters.Test

# Print only warnings and errors during test
config :logger, level: :warn

# Initialize plugs at runtime for faster test compilation
config :phoenix, :plug_init_mode, :runtime
