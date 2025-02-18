#!/bin/sh
# Docker entrypoint script.
  echo "Database $PGDATABASE does not exist. Creating..."
  # Create Db
  mix ecto.create

  # Create table
  mix ecto.migrate

  #add value in tables
  mix run priv/repo/seeds.exs

#Run the server
exec mix phx.server